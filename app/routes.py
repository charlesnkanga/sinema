from flask import render_template, Blueprint, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Movie, Review
from app.forms import RegistrationForm, LoginForm, MovieForm, ReviewForm
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)

# **1. Register**
@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.password_hash = generate_password_hash(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

# **2. Login**
@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('main.home'))
        flash('Invalid username or password.', 'danger')
    return render_template('login.html', form=form)

# **3. Logout**
@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.home'))

# **4. Home**
@main.route('/')
def home():
    return render_template('home.html')

# **5. Add Movies**
@main.route('/movies/add', methods=['GET', 'POST'])
@login_required
def add_movie():
    form = MovieForm()
    if form.validate_on_submit():
        movie = Movie(
            title=form.title.data,
            description=form.description.data,
            release_date=form.release_date.data  # No conversion needed
        )
        db.session.add(movie)
        db.session.commit()
        flash('Movie added successfully!', 'success')
        return redirect(url_for('main.list_movies'))
    return render_template('add_movie.html', form=form)

# **6. List Movies**
@main.route('/movies', methods=['GET'])
@login_required
def list_movies():
    movies = Movie.query.all()
    user_favorites = [movie.id for movie in current_user.favorites]

    # Ensure all dates are formatted properly for display
    formatted_movies = [
        {
            "id": movie.id,
            "title": movie.title,
            "description": movie.description,
            "release_date": movie.release_date.strftime('%d-%m-%Y') if movie.release_date else "Unknown",
            "is_favorited": movie.id in user_favorites
        }
        for movie in movies
    ]

    return render_template('list_movies.html', movies=formatted_movies)

# **7. Movie Details and Reviews**
@main.route('/movies/<int:movie_id>', methods=['GET', 'POST'])
@login_required
def movie_details(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    reviews = Review.query.filter_by(movie_id=movie_id).all()
    form = ReviewForm()

    if form.validate_on_submit():
        review = Review(
            rating=form.rating.data,
            content=form.content.data,
            movie_id=movie_id,
            user_id=current_user.id
        )
        db.session.add(review)
        db.session.commit()
        flash('Review added successfully!', 'success')
        return redirect(url_for('main.movie_details', movie_id=movie_id))

    # Fetch recommended movies based on shared favorites
    users_who_favorited = [user.id for user in movie.fans]
    recommended_movies = Movie.query.filter(
        Movie.id != movie_id,
        Movie.fans.any(User.id.in_(users_who_favorited))
    ).limit(5).all()

    return render_template(
        'movie_details.html',
        movie=movie,
        reviews=reviews,
        form=form,
        recommended_movies=recommended_movies
    )

# **8. Toggle Favorites (AJAX)**
@main.route('/movies/<int:movie_id>/toggle_favorite', methods=['POST'])
@login_required
def toggle_favorite(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if movie in current_user.favorites:
        current_user.favorites.remove(movie)
        db.session.commit()
        return jsonify({'status': 'removed'})
    else:
        current_user.favorites.append(movie)
        db.session.commit()
        return jsonify({'status': 'added'})

# **9. Favorites**
@main.route('/movies/favorites')
@login_required
def favorites():
    favorite_movies = current_user.favorites.all()
    return render_template('favorites.html', movies=favorite_movies)