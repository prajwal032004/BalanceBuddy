from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from bmi_utils import calculate_bmi  # Make sure this function is defined correctly

app = Flask(__name__)
app.secret_key = 'supersecretkey'
DATABASE = 'database.db'

# --- Database Functions ---
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

# Initialize the database when the app starts
init_db()  # Directly calling it here

def get_user(email, password):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        if user and check_password_hash(user[3], password):  # Check the hashed password
            return user
        return None

def register_user(name, email, password):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        hashed_password = generate_password_hash(password)
        try:
            cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, hashed_password))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

# --- Routes ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = get_user(email, password)
        if user:
            session['user'] = user[1]  # Store user's name in the session
            flash('Login successful!', 'success')
            return redirect(url_for('bmi_calculator'))  # Redirect to BMI calculator after login
        else:
            flash('Invalid email or password.', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        if register_user(name, email, password):
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Email already registered.', 'error')
            return redirect(url_for('register'))  # Correct redirection to the same route
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)  # Remove user from session
    flash('Logged out successfully.', 'success')
    return redirect(url_for('index'))

@app.route('/try_again')
def try_again():
    return render_template('try_again.html')

@app.route('/bmi_calculator', methods=['GET', 'POST'])
def bmi_calculator():
    if 'user' not in session:  # Check if the user is logged in
        flash('Please log in to access the BMI calculator.', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':  # Handle BMI calculation on POST
        try:
            age = request.form['age']
            height = float(request.form['height'])
            weight = float(request.form['weight'])
            gender = request.form['gender']
            
            # Call the BMI calculation function
            bmi = calculate_bmi(weight, height)
            
            # Return the result page
            return render_template('bmi_result.html', bmi=bmi, age=age, gender=gender)
        except ValueError:
            flash('Please enter valid numeric values for height and weight.', 'error')
            return redirect(url_for('bmi_calculator'))  # Redirect back to the calculator if error
    return render_template('bmi_calculator.html')

if __name__ == '__main__':
    app.run(debug=True)
