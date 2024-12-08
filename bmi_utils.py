# bmi_utils.py

def calculate_bmi(weight, height_cm):
    """Calculate BMI given weight (kg) and height (cm)."""
    height_m = height_cm / 100  # Convert cm to meters
    return weight / (height_m ** 2)
