
def get_divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


try:
    num = int(input("Enter an integer number: "))
    print("The divisors of", num, "are:", get_divisors(num))
except ValueError:
    print("Error: input must be an integer.")
