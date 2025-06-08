package main

import (
	"fmt"
	"math/rand"
)

var totalBalance int = 5000
var timesWon int = 0
var timesLost int = 0
var totalMoneyWon int = 0
var totalMoneyLost int = 0
var multiplier int = 3
var randomNumberScope int = 10

var start string
var reset string = "default"
var chosenNumber int
var moneyUsed int

func main() {

	commands()

	var chanceOfWinning float64
	chanceOfWinning = 1 / float64(randomNumberScope)
	var chanceOfWinningInProsent float64
	chanceOfWinningInProsent = chanceOfWinning * 100.0

	fmt.Printf("Welcome to the casino! You have %d kroner with you, good luck.\n", totalBalance)
	fmt.Printf("The chance of winning is %.1f (of 1) or %.1f%%.\n", chanceOfWinning, chanceOfWinningInProsent)
	fmt.Println()

	for {
		playRound()

		if totalBalance < 1 {
			fmt.Println()
			fmt.Println("*You leave the casino feeling dejected.*")
			leaving()
			fmt.Println()
			fmt.Print("Want to reset? ")
			fmt.Scan(&reset)
		}
		fmt.Println()

		if reset == "default" {
			var continueCheck string

			fmt.Print("Do you want to continue playing? ")
			fmt.Scan(&continueCheck)

			if continueCheck == "yes" {
				fmt.Println("*You stay at the casino*")
				fmt.Println()
			} else if continueCheck == "no" {
				fmt.Println("*You leave the casino*")
				leaving()
				fmt.Println()
				fmt.Print("Want to reset?  ")
				fmt.Scan(&reset)
			} else {
				fmt.Println("*You stay at the casino*")
				fmt.Println()
			}
		}
		if reset == "no" {
			fmt.Println()
			fmt.Println()
			fmt.Println("Thank you for playing!")
			break
		} else if reset != "default" {
			fmt.Println()
			totalBalance = 5000
			timesWon = 0
			timesLost = 0
			totalMoneyWon = 0
			totalMoneyLost = 0
			reset = "default"

			commands()

			fmt.Printf("Welcome to the casino! You have %d kroner with you, good luck.\n", totalBalance)
			fmt.Printf("The chance of winning is %.1f of 1 or %.1f%%.\n", chanceOfWinning, chanceOfWinningInProsent)
			fmt.Println()
		}
	}
}

func winning(totalBalance, moneyUsed int) int {
	return totalBalance + (moneyUsed * multiplier)
}
func losing(totalBalance, moneyUsed int) int {
	return totalBalance - moneyUsed
}
func leaving() {
	fmt.Println("==========================")
	fmt.Println("Stats:")
	fmt.Println("Final balance =", totalBalance)
	fmt.Println("Times won =", timesWon)
	fmt.Println("Times lost =", timesLost)
	fmt.Println("Total money won =", totalMoneyWon)
	fmt.Println("Total money lost =", totalMoneyLost)
}
func playRound() int {

	var winningNumber int
	winningNumber = rand.Intn(randomNumberScope) + 1

	//User input
	for {
		fmt.Print("How many kroner are you betting? ")
		fmt.Scan(&moneyUsed)
		if moneyUsed > totalBalance {
			fmt.Println("You can't bet more than you have!")
		} else if moneyUsed < 1 {
			fmt.Println("You have to wager atleast 1 krone and you can't use text!")
		} else {
			break
		}
	}
	for {
		fmt.Printf("Choose a number from 1 to %d: ", randomNumberScope)
		fmt.Scan(&chosenNumber)
		if chosenNumber == 1981523142113518 {
			fmt.Println(winningNumber)
		} else if chosenNumber < 1 {
			fmt.Println("The number must be greater than 1.")
		} else if chosenNumber > randomNumberScope {
			fmt.Printf("The number must be under %d!\n", randomNumberScope+1)
		} else {
			break
		}
	}

	//Checking results:
	var win bool
	if chosenNumber == winningNumber {
		win = true
	} else {
		win = false
	}

	if win {
		totalBalance = winning(totalBalance, moneyUsed)
		timesWon++
		totalMoneyWon += moneyUsed
		fmt.Printf("You won this round and your new balance is %d kroner.\n", totalBalance)
		return totalBalance
	} else {
		totalBalance = losing(totalBalance, moneyUsed)
		timesLost++
		totalMoneyLost += moneyUsed
		fmt.Printf("You lost this round, your new balance is %d. The number was %d\n", totalBalance, winningNumber)
		return totalBalance
	}
}

func commands() (int, int, int) {

	for {
		fmt.Print("Type anything to start: ")
		fmt.Scan(&start)
		fmt.Println()

		if start == "setstartingmoney" {
			fmt.Print("How much do you want to start with? ")
			fmt.Scan(&totalBalance)
			fmt.Printf("Total balance = %d\n", totalBalance)
			fmt.Println()
		} else if start == "setmultiplier" {
			fmt.Print("How high should the multipler be? ")
			fmt.Scan(&multiplier)
			fmt.Printf("Payback multipler = %d\n", multiplier)
			fmt.Println()
		} else if start == "setscope" {
			fmt.Print("What do you want your chances to be? ")
			fmt.Scan(&randomNumberScope)
			fmt.Printf("The winning number is now between 1 and %d\n", randomNumberScope)
			fmt.Println()
		} else {
			return totalBalance, multiplier, randomNumberScope
		}
	}
}
