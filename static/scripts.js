// Function to toggle password visibility
function togglePassword() {
    const passwordField = document.getElementById("password");
    const toggleIcon = document.getElementById("togglePasswordIcon");
    
    if (passwordField.type === "password") {
        passwordField.type = "text";
        toggleIcon.textContent = "🙈"; // Hide password icon
    } else {
        passwordField.type = "password";
        toggleIcon.textContent = "👁️"; // Show password icon
    }
}

// Function to validate registration form
function validateRegistrationForm() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    
    if (!name || !email || !password) {
        alert("Please fill out all fields.");
        return false;
    }

    // Basic email validation
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailRegex.test(email)) {
        alert("Please enter a valid email address.");
        return false;
    }

    return true;
}

// Function to validate login form
function validateLoginForm() {
    const email = document.getElementById("loginEmail").value;
    const password = document.getElementById("loginPassword").value;
    
    if (!email || !password) {
        alert("Please fill out both fields.");
        return false;
    }
    
    return true;
}

// Handling form submission for login and registration
document.querySelector("#loginForm").addEventListener("submit", function(event) {
    if (!validateLoginForm()) {
        event.preventDefault();
    }
});

document.querySelector("#registerForm").addEventListener("submit", function(event) {
    if (!validateRegistrationForm()) {
        event.preventDefault();
    }
});
