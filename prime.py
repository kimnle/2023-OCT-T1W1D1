def is_prime(number):
    for i in range(2, number):
        if (number % i == 0):
            print("Not a prime")
            break
        else:
            print("A Prime")

is_prime(5)