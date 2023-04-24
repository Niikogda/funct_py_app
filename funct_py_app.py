
def capitalize_words(s):
    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

while True:
    try:
        s = input("Enter a string: ")
        result = capitalize_words(s)
        print(f"The string with capitalized words is: {result}")
        break
    except ValueError:
        print("Invalid input")
