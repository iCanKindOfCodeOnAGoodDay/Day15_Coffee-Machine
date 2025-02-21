# By Scott Quashen based on the London App Brewery Project from 100 Days of Code - Python
# Feb 20th 2025
# This is a basic program that works in the console which acts as a coffee ordering machine
# Inputs include order number, and amount of each coin entered.
# Outputs include user's coffee selection, change, and report of machines materials stock.

# Note, machine never runs out of resources because program can only serve once per run.

import validations
import menu

menuData = menu.menu

def main():
    print("Welcome to Vegan Coin Coffee!")
    orderNumber = validations.validateOrderNumber(input("Type 0 for Espresso, 1 for latte, and 2 for cappuccino."))
    itemName = lookupItemName(orderNumber)
    print("You ordered " + itemName + ".")
    orderCost = getPrice(orderNumber)
    currentMoney = addMoney()
    checkEnoughMoney(orderCost, currentMoney) # will prevent program from moving forward until enough money is in machine to cover costs
    serve(orderNumber)
    refund(orderCost, currentMoney)
    maintenanceReport(itemName) # never runs out of resources because program runs only once

def checkEnoughMoney(price, money):
    if price > money:
        print("You need to add more money, this much more: " + str(price - money))
        runningTotal = money + addMoney()
        checkEnoughMoney(price, runningTotal)

def addMoney():
    pennies = validations.validCoinEntry(input("Enter pennies: "))
    nickles = validations.validCoinEntry(input("Enter nickles: "))
    dimes = validations.validCoinEntry(input("Enter dimes: "))
    quarters = validations.validCoinEntry(input("Enter quarters: "))
    moneyEntered = pennies * .01 + nickles * .05 + dimes * .10 + quarters * .25
    return moneyEntered

def refund(cost, moneyInMachine):
    change = moneyInMachine - cost
    print("Here is your change: " + str(change))

def getPrice(orderNumber):
    if orderNumber == 0 :
        cost = menuData["espresso"]["cost"]
    elif orderNumber == 1:
        cost = menuData["latte"]["cost"]
    elif orderNumber == 2:
        cost = menuData["cappuccino"]["cost"]
    print("Your order is now $" + str(cost))
    return cost

def serve(num):
    if num == 0:
        print("Here is your Espresso!")
    elif num == 1:
        print("Here is your Latte!")
    elif num == 2:
        print("Here is your cappuccino!")

def lookupItemName(orderNumber):
    if orderNumber == 0:
        return "espresso"
    elif orderNumber == 1:
        return "latte"
    elif orderNumber == 2:
        return "cappuccino"

def maintenanceReport(name):
    # machine starting stocks
    stockWater = 300.0
    stockCoffee = 100.0
    stockOatMilk = 200.0

    # used stock
    usedWater = float(menuData[name]["ingredients"]["water"])
    usedCoffee = float(menuData[name]["ingredients"]["coffee"])
    usedMilk = float(menuData[name]["ingredients"]["milk"])

    # remaining stock
    remainingWater = stockWater - usedWater
    remainingCoffee = stockCoffee - usedCoffee
    remainingOatMilk = stockOatMilk - usedMilk
    print("************************* System Report ************************* ")
    print("Water: " + str(remainingWater))
    print("Coffee: " + str(remainingCoffee))
    print("Milk: " + str(remainingOatMilk))

# func calls
if __name__ == '__main__':
    main()