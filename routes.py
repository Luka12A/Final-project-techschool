from flask import render_template, redirect, url_for, flash, session, request
from flask_login import login_user, login_required, current_user, logout_user
from models import db, User, Course, Cart, Category
from forms import RegistrationForm, LoginForm,CourseForm


def init_routes(app):
    # Home Route
    @app.route('/')
    def home():
        popular_products = Course.query.limit(9).all()
        return render_template('index.html', popular_products=popular_products)

    # Register Route
    @app.route("/register", methods=['GET', 'POST'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            print(f"Username: {form.username.data}, Email: {form.email.data}, Password: {form.password.data}")
        
        try:
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)  
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            print(f"Error: {e}")
        flash('There was an error creating your account. Please try again later.', 'danger')

        return render_template('register.html', form=form)



    # Login Route
    
    @app.route("/login", methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
        
            if user and user.check_password(form.password.data):
                login_user(user)
                session['user_id'] = user.id
                session['username'] = user.username  
            
                if user.is_admin:
                    return redirect(url_for('admin_dashboard'))

                return redirect(url_for('home'))
            else:
                flash('Login failed. Check your username and password.', 'danger')
    
        return render_template('login.html', form=form)



    from flask_login import login_required, current_user

    @app.route('/admin', methods=['GET', 'POST'])
    def admin_dashboard():
        if request.method == 'POST':
            name = request.form.get('name')
            description = request.form.get('description')
            price = request.form.get('price')
            category_id = request.form.get('category_id') 
            file = request.files['file']
        
            file_path = f"static/{file.filename}"
            file.save(file_path)
        

            new_course = Course(
            name=name, 
            price=price, 
            file=file.filename,
            category_id=category_id 
        )
            db.session.add(new_course)
            print('course added')
            db.session.commit()
        
            flash("Course added successfully!", "success")
            return redirect(url_for('admin_dashboard'))
    
        categories = Category.query.all()
        return render_template('admin_dashboard.html', categories=categories)


    # Logout Route
    @app.route('/logout')
    def logout():
        session.pop('user_id', None)
        session.pop('username', None)
        flash('You have been logged out.', 'info')
        return redirect(url_for('home'))

    @app.route('/add_to_cart/<int:product_id>', methods=['POST'])
    def add_to_cart(product_id):
        if 'cart' not in session:
            session['cart'] = []
        session['cart'].append(product_id)
        session.modified = True  

        cart_items = Course.query.filter(Course.id.in_(session['cart'])).all()
    
        flash("Item added to cart!", "success")
    
        return render_template("cart.html", cart_items=cart_items)
    
    @app.route('/add_to_cart')
    def cart():
        return render_template("cart.html")


    @app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
    def remove_from_cart(product_id):
        if 'cart' in session:
            session['cart'] = [item for item in session['cart'] if item != product_id]
            session.modified = True 
    
    # Fetch the updated cart items
        cart_items = Course.query.filter(Course.id.in_(session['cart'])).all()
    
        flash('Item removed from cart', category='success')
    
        return render_template("cart.html", cart_items=cart_items)
  

    @app.route('/courses', methods=['GET'])
    def courses_page():
        query = request.args.get('query', '').strip()
        if query:
            courses = Course.query.filter(Course.name.ilike(f"%{query}%")).limit(20)
        else:
            courses = Course.query.distinct().all()
        return render_template('courses.html', courses=courses)

    @app.route('/course/<int:course_id>')
    def course_details(course_id):
        course = Course.query.get_or_404(course_id)
        return render_template('course_details.html', course=course)
    
    @app.route('/about')
    def about():
        return render_template('about.html')
    
    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']
        
            print(f"Name: {name}, Email: {email}, Message: {message}")
        
            return redirect(url_for('home'))
    
        return render_template('contact.html')
    

