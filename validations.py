# avoid runtime errors
def validateOrderNumber(inp):
    while True:
        try:
            soFarSoGood = int(inp)
            if soFarSoGood >= 0 and soFarSoGood < 3:
                return soFarSoGood
            else:
                raise ValueError
        except ValueError:
            inp = input("Please enter just: 0, 1, or 2...  ")

# avoid runtime errors
def validCoinEntry(inp):
    while True:
        try:
            inp = int(inp)
            if inp >= 0:
                return inp
            else:
                raise ValueError
        except ValueError:
            inp = input("Please enter an amount of 0 or more...  ")