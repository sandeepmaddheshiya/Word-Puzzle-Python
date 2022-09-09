import random
print("___________________________________________________________")
print("|                        WELCOME                           |")
print("|                          TO                              |")
print("|                    WORD PUZZLE GAME                      |")
print("|              MADE BY SANDEEP MADDHESHIYA                 |")
print("------------------------------------------------------------")

l=["WATER","FRESH","FISH","CRICKET","LAPTOP","PUZZLE","BOTTLE","BEDROOM","ICECREAM","MOUSE","JERRY","KITCHEN","PIZZA"]
def lowerstr(str):
    return str.casefold()
life=3
score=0
while(True):
    start=int(input("SELECT THE FOLLOWING: \n"
                    "1: TO START THE GAME \n"
                    "2: TO EXIT \n"))
    if start == 1:
        print("YOU HAVE 3 LIFE")
        while(life>0):
            r = random.choice(l)
            s = []
            for i in range(0, len(r)):
                s.append(r[i])
            random.shuffle(s)
            a = "".join(s)
            print(a)

            b=input("ENTER HERE: \n")
            b=lowerstr(b)
            c=lowerstr(r)

            if b==c:
                score +=1
                print(f"CORRECT    SCORE{score}     LIFE={life}")
            else:
                life -= 1
                print(f"WRONG      SCORE{score}     LIFE={life}")
            if life==0:
                print("THANK YOU FOR PLAYING\n")
            else:
                continue

    elif start==2:
        break
