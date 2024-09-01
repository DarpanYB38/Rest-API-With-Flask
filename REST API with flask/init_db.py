from app import app, db

# Create the application context
with app.app_context():
    try:
        db.create_all()
        print("Database initialized.")
    except Exception as e:
        print(f"An error occurred: {e}")
