from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    courses = db.relationship('Course', backref='category', lazy=True)

    def __repr__(self):
        return f"<Category {self.name}>"

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    file = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return f"<Course {self.name} ({self.price})>"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    def get_id(self):
        return str(self.id)  

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def is_active(self):
        return True 


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)  
    quantity = db.Column(db.Integer, default=1, nullable=False)
    user = db.relationship('User', backref=db.backref('cart', lazy=True))
    product = db.relationship('Course', backref=db.backref('cart', lazy=True))  

    def __repr__(self):
        return f'<Cart {self.user_id} {self.product_id} {self.quantity}>'



def add_data():
    if Category.query.count() == 0:
        web_dev = Category(name="Web Development")
        design = Category(name="Design")
        data_science = Category(name="Data Science")
        db.session.add_all([web_dev, design, data_science])
        db.session.commit()

    if Course.query.count() == 0:
        web_dev = Category.query.filter_by(name="Web Development").first()
        design = Category.query.filter_by(name="Design").first()
        data_science = Category.query.filter_by(name="Data Science").first()


        courses = [
            Course(name="JavaScript for Beginners", price=50, file="assets/main-image-1.png", category=web_dev),
            Course(name="Advanced React.js", price=100, file="assets/main-image-2.png", category=web_dev),
            Course(name="CSS Mastery", price=40, file="assets/main-image-3.png", category=web_dev),
            Course(name="UI/UX Design Principles", price=70, file="assets/main-image-4.png", category=design),
            Course(name="Photoshop for Beginners", price=60, file="assets/main-image-5.png", category=design),
            Course(name="Data Science with Python", price=120, file="assets/main-image-6.png", category=data_science),
            Course(name="Machine Learning Basics", price=150, file="assets/main-image-7.png", category=data_science),
            Course(name="Full Stack Web Development", price=200, file="assets/main-image-8.png", category=web_dev),
            Course(name="React Native for Mobile Development", price=120, file="assets/main-image-9.png", category=web_dev),
            Course(name="Advanced CSS and Flexbox", price=80, file="assets/main-image-10.png", category=web_dev),
            Course(name="WordPress for Beginners", price=40, file="assets/main-image-11.png", category=web_dev),
            Course(name="Introduction to Python", price=50, file="assets/main-image-12.png", category=data_science),
            Course(name="Data Visualization with Python", price=75, file="assets/main-image-13.png", category=data_science),
            Course(name="Building Web Applications with Flask", price=130, file="assets/main-image-14.png", category=web_dev),
            Course(name="Machine Learning with TensorFlow", price=150, file="assets/main-image-15.png", category=data_science),
            Course(name="Sketch for UI Design", price=60, file="assets/main-image-16.png", category=design),
            Course(name="Digital Illustration with Procreate", price=90, file="assets/main-image-17.png", category=design),
            Course(name="Creating E-Commerce Websites", price=150, file="assets/main-image-18.png", category=web_dev),
            Course(name="Advanced HTML5 & CSS3", price=100, file="assets/main-image-19.png", category=web_dev),
            Course(name="Cybersecurity Fundamentals", price=200, file="assets/main-image-20.png", category=data_science)
        ]

        db.session.add_all(courses)
        db.session.commit()  


