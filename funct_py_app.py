
def get_first_last_three_chars(s):
    if len(s) < 6:
        return "Недостатньо символів"
    else:
        return s[:3] + s[-3:]


try:
    s = input("Enter a string: ")
    result = get_first_last_three_chars(s)
    print(result)
except ValueError:
    print("Error: input must be a valid string.")
