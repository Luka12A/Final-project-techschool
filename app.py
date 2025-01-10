from flask import Flask
from flask_login import LoginManager
from config import Config
from routes import init_routes
from models import User, db, add_data

app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

db.init_app(app)  


login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

init_routes(app)

with app.app_context():
    db.create_all() 
    print("Tables created successfully.")
    add_data()

    admin_user = User.query.filter_by(username='admin').first()
    if not admin_user:
        admin_user = User(username='admin', email='admin@example.com', is_admin=True)
        admin_user.set_password('adminpassword')  
        db.session.add(admin_user)
        db.session.commit()
        print("Admin user created!")


if __name__ == "__main__":
    app.run(debug=True)
