filename = 'pi_million_digits.txt'

def generate_pi(decimal_places):
    with open(filename) as f:
        try:
            decimal_places = int(decimal_places) + 2
        except ValueError:
            print("Not an integer value.")
        else:
            if decimal_places > 1000:
                decimal_places = 1002
            if decimal_places == 2:
                print("You cannot generate 0 decimal places.")
                required_pi_digits = 3.14
            else:
                required_pi_digits = f.read(decimal_places)
            print(required_pi_digits)

decimal_places = input("Please enter the amount of pi decimal places you would like to"
" generate (cannot generate more than 1000): ")
generate_pi(decimal_places)
