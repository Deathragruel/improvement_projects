import sys

def generate_fibonacci_sequence(n):
    try:
        n = int(n)
    except ValueError:
        print(f"{n} is not an integer value.")
    else:
        if n == 0:
            print("So you don't want to see one?")
            sys.exit()
        if n == 1:
            print(0)
        for i in range(1, n+1):
            first_number = 0
            second_number = 1
            total_number = first_number + second_number
            print(total_number)
            i += 1
            first_number = second_number 
            second_number = total_number

n = input("Please enter the amount of numbers of fibonacci sequence you would "
"like to see (Press CTRL-C to cancel): ")
generate_fibonacci_sequence(n)
