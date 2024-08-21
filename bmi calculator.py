def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
def main():
    try:
        weight = float(input("Please enter your weight in kilograms: "))
        height = float(input("Please enter your height in meters: "))
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"This is considered: {category}")
    except ValueError:
        print("Oops! Please enter correct numeric values for both weight and height.")
if __name__ == "__main__":
    main()
