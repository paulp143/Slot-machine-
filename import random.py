import random
wheels=int(input("3,4,5 "))
spins=int(input("How many spins?" ))-1
won_spins=0
lost_spins=0
total_spins=0
wheel_values=[1,2,3,4,5]
if wheels==3:
    while spins>=total_spins-1:
        total_spins=won_spins+lost_spins
        result = [random.choice(wheel_values) for _ in range(wheels)]
        print(f"\nAuto spin #{total_spins}: {result}")
        if result[0]==result[1]==result[2]:
            won_spins+=1
            
        else:
            lost_spins+=1
        print("hm")
    total_spins=won_spins+lost_spins
    print(f"Wins: {won_spins}")
    print(f"Lost: {lost_spins}")
    print(f"total spins: {total_spins}")
    print(f"Win rate: {(won_spins/total_spins)*100}%")
elif wheels==4:
    while spins<=total_spins:
            total_spins=won_spins+lost_spins
            result = [random.choice(wheel_values) for _ in range(wheels)]
            print(f"\nAuto spin #{total_spins}: {result}")
            if result[0]==result[1]==result[2]==result[3]:
                won_spins+=1
            else:
                lost_spins+=1
    total_spins=won_spins+lost_spins
    print(f"Wins: {won_spins}")
    print(f"Lost: {lost_spins}")
    print(f"total spins: {total_spins}")
    print(f"Win rate: {(won_spins/total_spins)*100}%")
elif wheels==5:
    while spins<=total_spins-1:
            total_spins=won_spins+lost_spins
            result = [random.choice(wheel_values) for _ in range(wheels)]
            print(f"\nAuto spin #{total_spins}: {result}")
            if result[0]==result[1]==result[2]==result[3]==result[4]:
                won_spins+=1
            else:
                lost_spins+=1
    total_spins=won_spins+lost_spins
    print(f"Wins: {won_spins}")
    print(f"Lost: {lost_spins}")
    print(f"total spins: {total_spins}")
    print(f"Win rate: {(won_spins/total_spins)*100}%")
else:
    print("invalid_input")

