# BMI Calculator - BalanceBuddy
## 📋 Project Overview
BalanceBuddy is a web-based BMI (Body Mass Index) Calculator that helps users track their health by calculating their BMI based on their height, weight, age, and gender. It offers user authentication, allowing users to register, log in, and log out securely.

## 🚀 Features
BMI Calculation: Calculate BMI based on height, weight, age, and gender.

User Authentication: Secure user registration and login system.

Password Hashing: Securely stores passwords using hashing algorithms.

Flash Messages: Display user-friendly messages for login, registration, and error notifications.

Responsive Design: Accessible on multiple devices (mobile, tablet, desktop).

## 🛠️ Technologies Used
### Languages

HTML: Structure of the web pages.

CSS: Styling and layout of the web interface.

Python: Backend logic using Flask.

SQL: Database for storing user data.

### Packages and Libraries

Flask: Lightweight web framework for Python.

Flask-Bcrypt: For secure password hashing.

SQLite: Lightweight database for storing user information.

bcrypt: Library for hashing passwords.

Jinja2: Templating engine for dynamic HTML rendering.

## 📦 Requirements
Before running the project, ensure you have the following installed:

Python 3.x: Download from Python's official site.

SQLite: Comes pre-installed with Python, but you can also download it here.

Visual Studio Code (VS Code): Optional, but recommended for coding and debugging. 

### Python Libraries

Install the required Python packages using the following command:

       pip install Flask Flask-Bcrypt bcrypt
## Run the Application
Start the Flask development server:

       python app.py
### Access the Application
Open your browser and visit:

#### http://127.0.0.1:5000
## 🔑 How to Use
Register a New Account:

Go to the Register page and create an account by entering your name, email, and password.
#### Log In:

After registration, log in using your credentials.
#### Calculate BMI:

Once logged in, access the BMI Calculator page, enter your height, weight, age, and gender, and calculate your BMI.
#### Log Out:

Securely log out using the Logout link in the navigation bar.
## 🗄️ Project Structure
## bmi-calculator/
│-- app.py	

│-- init_db.py

│-- database.db

│-- requirements.txt

│-- README.md

│-- LICENSE

│-- /static

│   ├── style.css

│   └── images/

│                   ─└──── logo0.jpg

│                   ─└────---------.jpg
         
│-- /templates

│   ├── index.html

│   ├── login.html

│   ├── register.html

│   └── bmi_calculator.html

app.py: Main Flask application.

create_database.py: Initializes the SQLite database.

database.db: SQLite database file.

requirements.txt: List of dependencies.

/static: Contains static files like CSS and images.

/templates: HTML templates for the web pages.

## 🛡️ Security
Password Hashing: All passwords are securely hashed using bcrypt.

User Authentication: Prevents unauthorized access to sensitive pages.
## 🐛 Troubleshooting
#### Issue: Database file not found
Solution: Ensure you have run create_database.py to create the database.db file.

#### Issue: Flask app not starting
Solution: Ensure your virtual environment is activated and dependencies are installed.

#### Issue: Port conflict
Solution: Use a different port when running Flask:

python app.py --port=5001
## 👨‍💻 Contributing
Contributions are welcome! If you have any improvements, please fork the repository, make your changes, and submit a pull request.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🌟 Acknowledgments

Flask documentation: Flask Official Docs
bcrypt documentation: bcrypt GitHub

## Recommendations🙌 
Run the create_database.py first to activate the database 

Or
It will run Properly after you run the program app.py

Thank you for using BalanceBuddy! Happy Coding! 🚀
