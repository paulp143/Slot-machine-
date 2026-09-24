import random
import time
start_time=time.perf_counter()
money_balance=0
wheel_values = [1, 2, 3]
succesful_spins = 0
unsuccesful_spins = 0
round_number = 0
spins=int(input("How many spins? "))-1
while True:
    if spins>1000:
        yes=input(f"Are you sure you want to make {spins} spins? ").lower()
        if  yes!="y":
            spins=int(input("How many spins "))-1
        else:
            break
    else:
        break
wheels=int(input("3, 4 or 5? "))
def print_stats(wheels, bet, result, picked_number, round_total, won):
    total = succesful_spins + unsuccesful_spins
    win_rate = 0 if total == 0 else round((succesful_spins / total) * 100, 2)
    print("\n===== Round Stats =====")
    print(f"Round: {round_total}")
    print(f"Wheels: {wheels}")
    print(f"Bet: {bet}€")
    print(f"Money Balance: {money_balance}€")
    print(f"Picked number: {picked_number if picked_number is not None else 'none'}")
    print(f"Result: {result}")
    print(f"Outcome: {'WIN' if won else 'LOSS'}")
    print(f"Wins: {succesful_spins}")
    print(f"Losses: {unsuccesful_spins}")
    print(f"Win rate: {win_rate}%")
    print("=======================")


while round_number<=spins:
    round_number += 1
    
    bet = random.randint(1, 1000)
    insane = random.random() < 0.5
    picked_number = random.randint(1, 3) if insane else None

    result = [random.choice(wheel_values) for _ in range(wheels)]
    print(f"\nAuto spin #{round_number}: {result}")


    win = False
    if wheels == 3:
        win = result[0] == result[1] == result[2]
    elif wheels == 4:
        win = result[0] == result[1] == result[2] == result[3]
    elif wheels == 5:
        win = result[0] == result[1] == result[2] == result[3] == result[4]

    if insane and picked_number is not None and result and result[0] == picked_number:
        win = True

    if win:
        succesful_spins += 1
        print("You Won!")
        money_balance+=bet
    else:
        unsuccesful_spins += 1
        print("Better luck next time.")
        money_balance-=bet
    print_stats(wheels, bet, result, picked_number, round_number, win)
end=time.perf_counter()
print(f"Runtime {round(end-start_time, 5)} miliseconds")
    
