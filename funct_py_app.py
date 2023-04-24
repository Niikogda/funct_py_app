def average():
    while True:  
        try:
            lst = input("enter nums: ")
            lst=lst.split()
            lst = [float(x) for x in lst]  
            result = sum(lst) / len(lst)
            print(result)
            return result
        except ValueError:
            print(" mistake ")
average()
 