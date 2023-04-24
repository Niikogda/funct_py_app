
def most_common_number(lst):
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    max_count = max(counts.values())
    most_common_nums = [k for k, v in counts.items() if v == max_count]
    return min(most_common_nums)


try:
    lst = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
    result = most_common_number(lst)
    print("The most common number is:", result)
except ValueError:
    print("Error: input must be a valid list of integers.")
