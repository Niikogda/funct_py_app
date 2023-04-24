def average():
    while True:  
        try:
            lst = input("enter nums: ")
            lst=lst.split()
            lst = [int(x) for x in lst]  
            result = sum(lst) / len(lst)
            print(result)
            return result
        except ValueError:
            print(" mistake ")
average()
 