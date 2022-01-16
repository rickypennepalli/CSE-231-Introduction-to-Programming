#project2
#car rental program using while loops and boolean expressions

BANNER = "\nWelcome to car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BDW) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)" 
PROMPT = '''\nWould you like to continue (Y/N)? '''
show = print(BANNER)
ask = input(PROMPT)
 #prints program information and prompts user to continue

while ask == "Y":
    code = input("\nCustomer code (BDW): ")
    #prompts user for a budget, daily, or weekly selection
    
    if code == "D":
        days = int(input("\nNumber of days: "))
        start = int(input("Odometer reading at the start: "))
        end = int(input("Odometer reading at the end:   "))
        #prompts user for car rental information
        mile = (end-start)/10
        avg = mile/days
        #calculates total miles driven and average mileage per day
        if avg <= 100:
            cost = 60.00*days
        else:
            cost = ((0.25*days)*(avg-100))+(60*days)
        #calculates total amount due based on average mileage per day
        print("\nCustomer summary:")
        print("\tclassification code: D")
        print("\trental period (days):",days)
        print("\todometer reading at start:",start)
        print("\todometer reading at end:  ",end)
        print("\tnumber of miles driven: ",mile)
        print("\tamount due: $",cost)
        #prints user input and calculated variables above
        ask = input(PROMPT)
        #prompts user to continue the program
        
    elif code == "B":
        days = int(input("\nNumber of days: "))
        start = int(input("Odometer reading at the start: "))
        end = int(input("Odometer reading at the end:   "))
        #prompts user for car rental information
        mile = (end-start)/10
        if mile <=0:
            mile=100000+mile
        #calculates total miles driven while accounting for a larger ending odometer
        cost = float((mile*.25)+(40*days))
        #calculates total amount due based on total miles driven and number of days
        print("\nCustomer summary:")
        print("\tclassification code: B")
        print("\trental period (days):",days)
        print("\todometer reading at start:",start)
        print("\todometer reading at end:  ",end)
        print("\tnumber of miles driven: ",round(mile,1))
        print("\tamount due: $",round(cost,2))
        #prints user input and calculated variables above
        ask = input(PROMPT)
        #prompts user to continue the program
        
    elif code == "W":
        days = int(input("\nNumber of days: "))
        start = int(input("Odometer reading at the start: "))
        end = int(input("Odometer reading at the end:   "))
        #prompts user for car rental information
        mile = (end-start)/10
        if days % 7 == 0:
            weeks = days//7 
        else:
            weeks = (days//7)+1
        avg = mile/weeks
        #calculates total miles driven and average mileage per week (rounding up fractions)
        cost = (190.00*weeks)
        if avg <= 900:
            cost = cost
        elif avg <= 1500:
            cost = cost+(100.0*weeks)
        else:
            cost = cost+(200.0*weeks)+((0.25*weeks)*(avg-1500))
        #calculates total amount due based on average milage per week
        print("\nCustomer summary:")
        print("\tclassification code: W")
        print("\trental period (days):",days)
        print("\todometer reading at start:",start)
        print("\todometer reading at end:  ",end)
        print("\tnumber of miles driven: ",mile)
        print("\tamount due: $",cost)
        #prints user input and calculated variables above
        ask = input(PROMPT)
        #prompts user to continue the program
        
    else:
        print("\n\t*** Invalid customer code. Try again. ***")
        #returns user to the selection options
        
if ask == "N":
    print("Thank you for your loyalty.")
    #exits program
    
