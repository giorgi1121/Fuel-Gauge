#make the loop
while True:
    #try-except statment to catch errors
    try:
        #create variables x and y
        x, y = input("Fraction: ").split("/")
        #calculate percentage
        percentage = round(int(x) / int(y) * 100)
        #check with conditionals
        #if percentage is less or equal 1 than print E
        if percentage <= 1:
            print("E")

        #if percentage is more than 100 continue the loop
        elif percentage > 100:
            continue

        #if percentage is equal or more than 99 print F
        elif percentage >= 99 and percentage <= 100:
            print("F")

        #if percentage is more than 1 and less than 99 print percentage
        else:
            print(f"{percentage}%")

    #if there will be ValueError this will catch it
    except ValueError:
        pass

    #if there will be ZeroDivisionError this will catch it
    except ZeroDivisionError:
        pass

    #if everything is correct break the loop
    else:
        break
