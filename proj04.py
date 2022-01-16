###########################################################
    #  CSE 231 Project #4
    #
    #  Functions and Try/Except
    #    define various math functions
    #       sin, cos, pi, sum of natural squares
    #    input for an option
    #       call appropriate function
    #       output the value of the math function
    #    display closing message
    #
    ###########################################################

#import math module and define epsilon variable
import math
EPSILON = 1.0e-7

#menu display function
def display_options():
    ''' This function displays the menu of options'''

    MENU = '''\nPlease choose one of the options below:
             A. Display the sum of squares of the first N natural numbers.         
             B. Display the approximate value of Pi.
             C. Display the approximate value of the sine of X.
             D. Display the approximate value of the cosine of X.
             M. Display the menu of options.
             X. Exit from the program.'''
    print(MENU)

def sum_natural_squares(N):
    ''' This function calculates the sum of all the natural squares in a number'''
    total = 0
    #use try/except in case of any potential errors
    try:
        x = float(N)
        if x > 0.0 and x % 1.0 == 0.0:
            x = int(N)
            #solve for the sum of natural squares
            for i in range(1,x+1):
               total = total + i**2
            #determine the output
            print("\n\tThe sum: ",total)
            return total
        else:
            raise ValueError
    except:
        #output the error string and prompt for another value
        print("\n\tError: N was not a valid natural number. [{}]".format(N))
     
def approximate_pi(): 
    '''This function calculates the approximate value of pi'''
    #define constants
    n = 0 
    total = 0
    term = ((-1)**n/((2*n)+1))
    #set a loop that breaks when pi term is less than epsilon
    while abs(term) >= EPSILON:
        #use pi formula
        n += 1
        total += term
        term = ((-1)**n/((2*n)+1))
    total *= 4
    total = round(total,10)
    return total

def approximate_sin(X):
    '''This function calculates the approximate value of sin(x)'''
    #define constants
    n = 0 
    total = 0
    #use try/except in case of any potential errors
    try:
        x = float(X)
        #define the first term
        term = (((-1)**n)*(x**((2*n)+1)))/(math.factorial(2*n+1))
        #set a loop that breaks when sin term is less than epsilon
        while abs(term) >= EPSILON:
            #use sin formula
            n += 1
            total += term
            term = (((-1)**n)*(x**((2*n)+1)))/(math.factorial(2*n+1))
        #return total value
        total = round(total,10)
        return total
    except:
        return None

def approximate_cos(X):
    '''This function calculates the approximate value of cos(x)'''
    #define constants
    n = 0 
    total = 0
    #use try/except in case of any potential errors
    try:
        x = float(X)
        #define the first term
        term = (((-1)**n)*(x**(2*n)))/(math.factorial(2*n))
        #set a loop that breaks when cos term is less than epsilon
        while abs(term) >= EPSILON:
            #use cos formula
            n += 1
            total += term
            term = (((-1)**n)*(x**(2*n)))/(math.factorial(2*n))
        #return total value
        total = round(total,10)
        return total
    except:
        return None
        
def main():
    '''This function is the main menu that displays all the options and prints all the outputs'''
    display_options()
    choice = input("\n\tEnter option: ").lower()
    correct = 'abcdmx'
    #loop the options in the program 
    while choice == choice:
        #print error line if option is invalid
        if choice not in correct:
            print("\nError:  unrecognized option [{}]".format(choice.upper()))
            #show main menu and prompt an option again
            display_options()
        if choice == 'a':
            #prompt for input and call the appropriate function 
            N = input("\nEnter N: ")
            sum_natural_squares(N)
        if choice == 'b':
            #call the appropriate function 
            total = approximate_pi()
            #print approximate value, math module value, and difference
            print("\n\tApproximation: {:.10f}".format(total))
            mathpi = math.pi
            print("\tMath module:   {:.10f}".format(mathpi))
            diff = abs(mathpi - total)
            print("\tdifference:    {:.10f}".format(diff))
        if choice == 'c':
            #prompt for input and call the appropriate function 
            X = input("\n\tEnter X: ")
            total = approximate_sin(X)
            #output error line if needed
            if total is None:
                print("\n\tError: X was not a valid float. [{}]".format(X))
            else:
                #print approximate value, math module value, and difference
                print("\n\tApproximation: {:.10f}".format(total))
                X = float(X)
                mathsin = math.sin(X)
                print("\tMath module:   {:.10f}".format(mathsin))
                diff = abs(mathsin - total)
                print("\tdifference:    {:.10f}".format(diff))
        if choice == 'd':
            #prompt for input and call the appropriate function 
            X = input("\n\tEnter X: ")
            total = approximate_cos(X)
            #output error line if needed
            if total is None:
                print("\n\tError: X was not a valid float. [{}]".format(X))
            else:
                #print approximate value, math module value, and difference
                print("\n\tApproximation: {:.10f}".format(total))
                X = float(X)
                mathcos = math.cos(X)
                print("\tMath module:   {:.10f}".format(mathcos))
                diff = abs(mathcos - total)
                print("\tdifference:    {:.10f}".format(diff))
        if choice == 'm':
            #call the display options function 
            display_options()
        if choice =='x':
            #print closing line and exit program 
            print('Hope to see you again.')
            break
        
        choice = input("\n\tEnter option: ").lower()
    return

if __name__ == "__main__":
    #call the main function
    main()
    