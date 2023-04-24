
def sort_by_age(lst):
    return sorted(lst, key=lambda x: x[1])


try:
    n = int(input("Enter the number of tuples in the list: "))
    lst = []
    for i in range(n):
        name = input("Enter the name of person #" + str(i+1) + ": ")
        age = int(input("Enter the age of person #" + str(i+1) + ": "))
        lst.append((name, age))
    sorted_lst = sort_by_age(lst)
    print("The sorted list is:")
    for person in sorted_lst:
        print(person[0], "-", person[1], "years old")
except ValueError:
    print("Error: input must be a valid integer or string.")
