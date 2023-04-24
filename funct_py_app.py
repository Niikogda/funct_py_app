def sounds():
    while True:
        try:
            list=input("enter your list pls: ")
            cons=0
            vow=0
            for i in list.lower():
                if i.isalpha():
                    if i in "aeiou":
                        vow +=1
                    else:
                        cons +=1
            print("consonats: ", cons)
            print("vowels", vow)
        except ValueError:
            print("MASTAKE")
sounds()