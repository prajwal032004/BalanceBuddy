# BalanceBuddy BMI Calculator

## 📋 Project Overview

BalanceBuddy is a web-based BMI (Body Mass Index) Calculator built with Flask and Python. It helps users track their health by calculating their BMI based on height, weight, age, and gender, with secure user authentication and a responsive design.

## 🚀 Features

- **BMI Calculation**: Accurate BMI calculations with personalized recommendations
- **User Authentication**: Secure registration and login system
- **Data Persistence**: SQLite database for storing user data and BMI history
- **Password Security**: Secure password hashing using bcrypt
- **Flash Messages**: User-friendly notifications for actions and errors
- **Responsive Design**: Clean interface that works across all devices

## 🛠️ Technologies Used

- **Backend Framework**: Flask
- **Database**: SQLite
- **Password Hashing**: Flask-Bcrypt
- **Template Engine**: Jinja2
- **Frontend**: HTML, CSS, JavaScript
- **Form Handling**: Flask-WTF
- **Session Management**: Flask-Login

## 📦 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- SQLite3

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/balancebuddy.git
   cd balancebuddy
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   ```bash
   python init_db.py
   ```

5. **Start the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   Visit `http://127.0.0.1:5000` in your browser

## 🏗️ Project Structure

```
balancebuddy/
├── app/
│   ├── __init__.py      # Flask application initialization
│   ├── models/          # Database models
│   ├── routes/          # Route handlers
│   ├── forms/           # Form classes
│   ├── utils/           # Utility functions
│   └── templates/       # Jinja2 templates
├── static/
│   ├── css/            # Stylesheets
│   ├── js/             # JavaScript files
│   └── images/         # Image assets
├── instance/
│   └── database.db     # SQLite database
├── tests/              # Unit tests
├── app.py             # Application entry point
├── init_db.py         # Database initialization script
├── config.py          # Configuration settings
├── requirements.txt   # Project dependencies
└── README.md         # Project documentation
```

## 🔑 Key Features Usage

### Registration
1. Navigate to the registration page
2. Enter your email, password, and personal details
3. Submit the form to create your account

### BMI Calculation
1. Log in to your account
2. Go to the BMI Calculator page
3. Enter your height, weight, age, and select gender
4. View your BMI result and personalized recommendations

### View History
1. Access your dashboard
2. View your BMI calculation history
3. Track your progress over time

## 🛡️ Security Features

- Secure password hashing with bcrypt
- CSRF protection
- Session security
- Input validation and sanitization
- SQL injection prevention
- XSS protection

## 🐛 Troubleshooting

### Common Issues

1. **Database Initialization Error**
   ```bash
   # Remove existing database and reinitialize
   rm instance/database.db
   python init_db.py
   ```

2. **Dependencies Issues**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

3. **Server Issues**
   - Check if port 5000 is available
   - Ensure virtual environment is activated
   - Verify database file exists

## 📜 License

This project is licensed under the self License.

## 🌟 Acknowledgments

- Flask documentation
- SQLite documentation
- Python bcrypt library
- Bootstrap framework

---

Made with ❤️ by Prajwal
