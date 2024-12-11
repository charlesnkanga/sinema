# Sinema

## Overview

Sinema is a web application designed to allow users to discover and review movies, mark their favorites, and receive personalized recommendations based on their preferences. The project demonstrates fundamental web development concepts, including a login system, database relationships, and an advanced feature for recommending movies.

## Features
1. **Login System**
   - Users can register for an account, log in, and log out securely.
   - Passwords are hashed for security.

2. **Many-to-Many Relationship**
   - Users can mark movies as favorites using a many-to-many relationship between users and movies.

3. **Advanced Feature**
   - Recommendation system that suggests movies based on a user’s favorite genres.

4. **Styling and Accessibility**
   - Fully responsive design using Bootstrap and custom CSS.
   - Accessible features, including ARIA labels, semantic HTML, and color contrast compliance.

## Installation and Setup
1. **Clone or Download the Project**
   - Clone the repository or download the project zip file.

2. **Set Up a Virtual Environment**
   - Create and activate a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
     ```

3. **Install Dependencies**
   - Install required packages using the `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```

4. **Set Up the Database**
   - Run the database creation script:
     ```bash
     python create_db.py
     ```

5. **Run the Application Locally**
   - Start the Flask development server:
     ```bash
     python run.py
     ```
   - Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to access the application.

## File Structure

```
sinema/
├── app/
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       ├── scripts.js
│   │       └── favorites.js
│   ├── templates/
│   │   ├── add_movie.html
│   │   ├── base.html
│   │   ├── favorites.html
│   │   ├── home.html
│   │   ├── list_movies.html
│   │   └── movie_details.html
├── migrations/
│   ├── env.py
│   ├── README.md
│   ├── script.py.mako
│   ├── versions/
│   │   └── cbcee2decf22_reinitialize_database_schema.py
├── config.py
├── create_db.py
├── requirements.txt
├── run.py
```
## File Descriptions

### app/
- **`__init__.py`**: Initializes the Flask application and its extensions (e.g., SQLAlchemy, Flask-Login).
- **`forms.py`**: Contains Flask-WTF forms for user input, such as login, registration, and movie submission forms.
- **`models.py`**: Defines the database models (e.g., User, Movie, Review) and relationships.
- **`routes.py`**: Contains the application’s routes (views) to handle user interactions and database operations.

### static/
- **`styles.css`**: Custom CSS file for additional styling.
- **`scripts.js`**: General JavaScript functionality for the app.
- **`favorites.js`**: Handles AJAX functionality for marking movies as favorites.

### templates/
- **`add_movie.html`**: Template for the page where users can add a movie.
- **`base.html`**: Base layout template that includes common elements like navigation.
- **`favorites.html`**: Template to display the user’s favorite movies.
- **`home.html`**: Homepage of the application.
- **`list_movies.html`**: Template to list all movies.
- **`movie_details.html`**: Template for viewing movie details and adding/viewing reviews.

### migrations/
- **`env.py`**: Alembic environment configuration for database migrations.
- **`README.md`**: Details about the migrations.
- **`script.py.mako`**: Template used by Alembic for generating migration scripts.
- **`versions/`**: Contains generated migration scripts for database schema changes (e.g., **cbcee2decf22_reinitialize_database_schema.py**).

### Root Files
- **`config.py`**: Configuration file for the application, including database settings and secret keys.
- **`create_db.py`**: Script to initialize the database.
- **`requirements.txt`**: Specifies all required Python packages for the application.
- **`run.py`**: Entry point for running the Flask application.
  
## Usage
1. **Registration and Login**
   - Navigate to the registration page and create an account.
   - Log in to access all features.

2. **Add Movies**
   - Add movies to the database using the “Add Movie” page.

3. **Mark Favorites**
   - Mark movies as favorites by clicking the favorite/unfavorite button.

4. **Write and View Reviews**
   - Leave reviews for movies and view other users’ reviews.

5. **Recommendations**
   - Receive movie recommendations based on your favorite genres.

## Testing
- The application has been tested locally and deployed to ensure:
  - Login and registration work as intended.
  - Favorites and recommendations function correctly.
  - The design is responsive and accessible.
  - The database handles all user interactions effectively.

## Deployment
- The application is deployed using PythonAnywhere.

## Additional Information

If you encounter issues or have additional requirements to run the project, please refer to the `README.md` file in the project.