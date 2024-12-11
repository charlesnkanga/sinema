from app import db, create_app

app = create_app()
with app.app_context():
    print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])
    print("Registered tables before creating:", db.Model.metadata.tables.keys())
    db.drop_all()
    db.create_all()
    print("Registered tables after creating:", db.Model.metadata.tables.keys())
    print("Database tables created!")