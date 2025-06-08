import random

def winning(total_balance, money_used):
    return(total_balance + (money_used * 3))

def losing(total_balance,money_used):
    return(total_balance - money_used)

total_balance = 5000
times_won = 0
times_lost = 0
total_money_won = 0
total_money_lost = 0

def leaving():
    print("==========================")
    print("Stats:") 
    print(f"Final balance = {total_balance}")
    print(f"Times won = {times_won}")
    print(f"Times lost = {times_lost}")
    print(f"Total money won = {total_money_won}")
    print(f"Total money lost = {total_money_lost}")
    print("Thank you for coming.")
    
    
def play_round():

    global total_balance, times_won, times_lost, total_money_won, total_money_lost
    winning_number = random.randint(1,10)

    if total_balance <= 0:
        print("")
        print(f"*You leave the casino feeling dejected.*")
        leaving()
        return total_balance
 
#User input:
    while True:
        try:
            money_used = int(input("How many kroner are you betting? "))
            if money_used > total_balance:
                print("You can't bet more than you have!")
            elif money_used < 1:
                print("You have to wager atleast 1 krone!")
            else: 
                break 

        except ValueError:
            print("Enter a valid number. No decimals or text.")

    while True:
        try:
            chosen_number = int(input("Which number from one to ten are you chosing? "))
            if not (1 <= chosen_number <= 10):
                print("The number has to be from one to ten!")
            else:
                break
                
        except ValueError:
            print("Enter a valid number. No decimals or text.")


#Checking results:  
    if chosen_number == winning_number:
        win = True
    else:
        win = False
    
#Winning:
    if win == True:
        total_balance = winning(total_balance, money_used)
        times_won += 1
        total_money_won = total_money_won + money_used
        print(f"You won this round and your new balance is {total_balance} kroner.")
#Losing:
    elif win == False:
        total_balance = losing(total_balance, money_used)
        times_lost += 1
        total_money_lost = total_money_lost + money_used
        print(f"You lost this round, your new balance is {total_balance}. The number was {winning_number}.")

#Returning the total balance
    return(total_balance)

#Casino itself:       
print(f"Welcome to the casino! You have {total_balance} kroner with you, good luck.")
print("The chance of winning is 1 in 10 or 10%.")
print("")

while True:
    total_balance = play_round()    

    if total_balance is None or total_balance <= 0:
        print("")
        print(f"*You leave the casino feeling dejected.*")
        leaving()
        break


    print("")

    continuation_confirmation = input("Do you want to continue playing (Yes, no) ").lower()
    if continuation_confirmation == "yes":
        print("*You stay at the casino*")
        print("")

    elif continuation_confirmation == "no":
        print(f"*You leave the casino*")
        leaving()
        break
    else:
        print("*You stay at the casino*")
        print("")