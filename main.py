#Variables 
futureAmount = 3

def run(amount: float, rate: float, years: int) -> float:
    # TODO
    global futureAmount
    futureAmount = amount * (1 + (rate/100)) ** years
    return futureAmount

#Codigo Principal 

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print("La capital es: " , futureAmount)
