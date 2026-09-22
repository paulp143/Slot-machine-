import random
import time

wheel1=[1,2,3]
spins=1
bet="0"
money=input("How much money do you have: ")
if money=="dev":
    money=9999999999999999999999999999999999999999
else:
    money=int(money)
def All_in():
    if insane=="y":
        number=int(input("What number between 1 and 3. "))
        if number<1 or number>4:
            print("Invalid input.")
            number=int(input("What number between 1 and 3. "))

wheels=int(input("Whith how many wheels do you want to play (3=X2, 4=X4, 5=X10): "))
while True:
    if wheels >5 or wheels<3:
        print("Invalid input.")
        wheels=int(input("With how many wheels do you want to play (3=X2, 4=X4, 5=X10): "))
    else:
        break

while True :
    result1=random.choice(wheel1)
    result2=random.choice(wheel1)
    result3=random.choice(wheel1)
    result4=random.choice(wheel1)
    result5=random.choice(wheel1)
    results=[result1, result2, result3, result4, result5]
    print(f"You have {money}€.")
    betinput=input("How much do you want to bet ").lower()
    if betinput=="all in":
        bet=money
    else:
        bet=int(betinput)
    while True:
        if money<int(bet):
            print("Invalid input.")
            bet=int(input("How much do you want to bet "))
        else:
            break



    insane=input("Do you want to bet on a specific number? You get 50 times more but you also loose 10 times more. (Y for Yes) ").lower()
    while True:
        if bet==money:
            All_in()
            break

        if wheels==3:
            break
        elif wheels==4:
            if money<(bet*2):
                print("You dont have enough money." )
                bet=int(input("How much do you want to bet " ))
            else:
                break    
        elif wheels==5:
            if money<(bet*4):
                print("You dont have enough money." )
                bet=int(input("How much do you want to bet " ))
            elif insane=="y" :
                if money<(bet*50):  
                    print("You dont have enough money." )
                    bet=int(input("How much do you want to bet " ))
                else:
                    number=int(input("What number between 1 and 3."))
                    while number<1 or number>4:
                        print("The number has to be between 1 and 3")
                        number=int(input("What number between 1 and 3."))
                break  
        elif insane=="y":
            if money<(bet*10):
                print("You dont have enough money." )
                bet=int(input("How much do you want to bet " ))
            else:
                number=int(input("What number between 1 and 3. "))
                while number<1 or number>4:
                    print("Invalid input")
                    number=int(input("What number between 1 and 3. "))
                break
        elif insane=="":
            break



#animation
    for i in range(5):
        animation=[random.choice(wheel1),
                random.choice(wheel1),
                random.choice(wheel1),
                random.choice(wheel1),
                random.choice(wheel1),
           ]
        print(*animation[:wheels])
        time.sleep(0.2)
    print("? ? ?")
    time.sleep(1.5)
    print("--------result--------")
    if spins==1:
        if betinput=="all in":
            print(*results[:wheels])
            time.sleep(0.5)
            break
        else:
            print(*([results[0]]*wheels))
            
    else:
        print(*results[:wheels])
    time.sleep(0.5)

    
#wining 
    if spins==1:
        print("You Won!")
        if wheels==3:
            money+=bet
            if insane=="y":
                money+=bet*50
        elif wheels==4:
            money+=bet*2
            if insane=="y":
                money+=bet*50
        elif wheels==5:
            money+bet*10
            if insane=="y":
                money+=bet*50
        spins+=1
    else:
        if wheels ==3:
            
            if result1==result2 and result1==result3:

                print("You Won")
                money+=bet
                if insane=="y" and number==result1:
                    money=bet*50+money
                
            else:
                print("Better luck next time.")
                money-=bet
                if insane=="y":
                    money-=bet*50
        if wheels ==4:
            if result1==result2 and result1==result3 and result1==result4:

                print("You Won")
                money+=bet*2
                if insane=="y" and number==result1:
                    money+=bet*50
            else:
                print("Better luck next time.")
                money-=bet
                if insane=="y":
                    money-=bet*50
        if wheels ==5:
            if result1==result2 and result1==result3 and result1==result4 and result1==result5:

                print("You Won")
                money=bet*10+money
                if insane=="y" and number==result1:
                    money+=bet*50
            else:
                print("Better luck next time.")
                money-=bet*4
                if insane=="y":
                    money-=bet*50
    if money<=0:
        print("You have lost.")
        break
    breakout=input("To stop press Q ").lower()
    if breakout=="q":
        break
