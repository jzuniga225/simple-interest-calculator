def calculate_simple_interest (p, r, t):
    principal = p
    rate = r
    time = t
    return (principal * rate * time) / 100

if __name__ == "__main__":
    try:
        p = float(input("Enter principal amount: "))
        r = float(input("Enter annual interest rate (in %): "))
        t = float(input("Enter time in years: "))

        interest = calculate_simple_interest(p, r, t)
        print(f"Simple Interest: {interest:.2f}")
    except ValueError:
        print("Please enter valid numeric values.")
