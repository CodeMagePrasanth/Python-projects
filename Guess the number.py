while True:
    import random

    lower_limit=int(input("Enter Lower limit: "))
    upper_limit=int(input("Enter Upper limit: "))

    random_number=random.randint(lower_limit,upper_limit)
    print("you will have to choose a number between",upper_limit,"and",lower_limit)
    
    chance=0
    while chance<8:
        chance+=1
        guess = int(input("ente your guess: "))
        
        if random_number == guess:
            print("Congtagulatins, you did it.The number was",random_number)
            break
        elif guess < random_number:
            print("you gueesed a samll number.")
        
        elif guess > random_number:
            print("you gueesed a large number.")

        if chance ==7:
            print("\n Your've run out of chances")
            
            print("\n the number was ",random_number)
            
            print("\n Better luck nexrt time")
            break
    print("\n")
    break
