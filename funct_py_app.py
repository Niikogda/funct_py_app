
def unique_list():
    while True:
        try:
            lst = input("enter list: ")
            lst = lst.split()
            unique_lst = []
            for elem in lst:
                if elem not in unique_lst:
                   unique_lst.append(elem)
            return unique_lst
        except ValueError:
            print("mistake")
print(unique_list())