import random

starting_money = 5000
amount_won = 0
print(f"You have {starting_money} kroner with you")
print("")

def winning(amount, money_used):
    return(amount + money_used)

def losing(amount,money_used):
    return(amount - money_used)

#Don't touch these ⬆️

while starting_money > 0:
    gambling = int(input("How many kroner are you gambling? "))
    print("")

    winning_number = random.randint(1,10)

    chosen_number = int(input("Which number from one to ten are you choosing? "))
    print("")

    if gambling > starting_money:
        break

    elif chosen_number == winning_number:
        result = winning(starting_money, gambling)
        print(f"You won, your amount is now {result} kroner.")
        starting_money = result
        amount_won = amount_won + 1

    else:
        result = losing(starting_money,gambling)
        print(f"You lost, the number was {winning_number} your amount is now {result} kroner.")
        starting_money = result


print("============================================")
print(f"You lost after winning {amount_won} times")