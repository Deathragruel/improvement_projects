filename = 'e_thousand_digits.txt'

def generate_e(decimal_places):
    with open(filename) as f:
        try:
            decimal_places = 2 + int(decimal_places)
        except ValueError:
            print(f"{decimal_places} is not an integer.")
        else:
            if decimal_places > 102:
                print("Warned you! (not more than 100)")
                decimal_places = 102
            if decimal_places == 2:
                print("You cannot have 0 decimal places.")
            required_e_digits = f.read(decimal_places)
            print(required_e_digits)
        

decimal_places = input("Please enter the number of decimal places you would "
"like to generate for the value of e (It can't surpass 100): ")

if __name__ == '__main__':
    generate_e(decimal_places)
