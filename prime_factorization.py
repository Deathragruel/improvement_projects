number = int(input("Please write the number you would like to undergo prime "
        "factorisation: "))

number_list = []
n = 2

while number != 1:
    if number % n == 0:
        # Dividing with a normal division operator would always result
        # in a float value.
        number = number//n
        number_list.append(n)
    else:
        n += 1

for n in number_list:
    print(n)
