def calculate_bmi(weight, height_cm):
    """Calculate BMI given weight (kg) and height (cm)."""
    height_m = height_cm / 100
    return weight / (height_m ** 2)
