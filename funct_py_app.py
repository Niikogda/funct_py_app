
def dot_product(list1, list2):
    if len(list1) != len(list2):
        print("Error: the lists must have the same length.")
        return None
    else:
        result = 0
        for i in range(len(list1)):
            result += list1[i] * list2[i]
        return result

# Приклад виклику функції
try:
    list1 = list(map(int, input("Enter the first list of numbers separated by spaces: ").split()))
    list2 = list(map(int, input("Enter the second list of numbers separated by spaces: ").split()))
    print("The dot product of the two lists is:", dot_product(list1, list2))
except ValueError:
    print("Error: input must contain only integers separated by spaces.")
