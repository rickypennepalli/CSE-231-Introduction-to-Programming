###########################################################
    #  CSE 231 Project #10
    #
    #  Classes and Functions
    #    import class file
    #       read for certain values in the class
    #    output appropriate value in the functions
    #       call appropriate functions
    #    display closing message
    #
    ###########################################################
    
import cards, random
random.seed(100) #random number generator will always generate 
                 #the same random number (needed to replicate tests)

def initialize():
    ''' This function creates, initializes, and returns the tableau '''
    #call the Deck class from the cards file
    x = cards.Deck()
    x.shuffle()
    #create and empty list and loop each card into the list
    cardlist = []
    for i in range(52):
        card = x.deal()
        cardlist.append(card)
    #create four different lists of 13 cards
    row1 = cardlist[:13]
    row2 = cardlist[13:26]
    row3 = cardlist[26:39]
    row4 = cardlist[39:]
    #append each of the four lists into a larger list
    tableau = []
    tableau.append(row1)
    tableau.append(row2)
    tableau.append(row3)
    tableau.append(row4)
    #return tableau list of four lists
    return tableau
        
def display(tableau):
    '''
        This function displays the current state of the game.
        It display four rows of 13 cards with row and column labels.
        Ace is displayed with a blank.
        
        parameters: 
            tableau: data structure representing the tableau 
        
        Returns: None
    '''

    print("{:3s} ".format(' '), end = '')
    for col in range(1,14):
        print("{:3d} ".format(col), end = '')
    print()
        
    for r,row_list in enumerate(tableau):
        print("{:3d}:".format(r+1), end = '')
        for c in row_list:
            if c.rank() == 1:
                print("  {}{}".format(' ',' '), end = '')
            else:
                print("{:>4s}".format(str(c)),end = '')
        print()

def validate_move(tableau,source_row,source_col,dest_row,dest_col):
    ''' This function will use the source and destination points to test if the move is valid '''
    #set valid range for input values
    valid_row = 0,1,2,3
    valid_col = 0,1,2,3,4,5,6,7,8,9,10,11,12
    #create variable to set boolean
    x = True
    #if parameters are not in the valid range, set variable to False
    if source_row not in valid_row or dest_row not in valid_row:
        x = False
    if source_col not in valid_col or dest_col not in valid_col:
        x = False
    #if numbers are in valid range, continue with the tests
    while x == True:
        #find the rank of the destination card
        new_row = tableau[dest_row]
        new_position = new_row[dest_col]
        ace = new_position.rank()
        #find the rank of the card left of destination card
        left_position = new_row[dest_col - 1]
        left_r = left_position.rank()
        left_s = left_position.suit()
        #find the rank of the source card
        old_row = tableau[source_row]
        old_position = old_row[source_col]
        old_r = old_position.rank()
        old_s = old_position.suit()
        #TEST 1: check if the destination is an Ace Card
        if ace != 1:
            x = False
            break
        #TEST 2: check that only a source card rank 2 can begin a row
        elif dest_col == 0 and old_r == 2:
            x = True
            break
        #TEST 3: check that the left card is one less than the source card and they have the same suit
        elif left_r + 1 != old_r or left_s != old_s:
            x = False
            break
        #if all tests pass, set variable to True
        else:
            x = True
            break
    #return the boolean variable
    return x

def move(tableau,source_row,source_col,dest_row,dest_col):
    ''' This function will move the card to the desired position if the move is valid '''
    #call validate function
    valid = validate_move(tableau,source_row,source_col,dest_row,dest_col)
    if valid == False:
        #return False if move is not valid
        return False
    else:
        #find the position of the destination card
        new_row = tableau[dest_row]
        new_position = new_row[dest_col]
        #find the position of the source card
        old_row = tableau[source_row]
        old_position = old_row[source_col]
        #swap the two cards in each row
        new_row[dest_col] = old_position
        old_row[source_col] = new_position
        #update the tableau and return True
        tableau[dest_row] = new_row
        tableau[source_row] = old_row
        return True
        
def shuffle_tableau(tableau):
    ''' This function will shuffle only certain cards in each row '''
#STEP 1: distinguish where each row's set ends
    #create an empty list and iterate through each row
    progress = []
    for row in tableau:
        #set variables for the card numbered position and its ordered rank
        number = 0
        order = 2
        #create an empty set for the suits
        suit_list = set()
        for card in row:
            #find each card rank and suit
            rank = card.rank()
            suit = card.suit()
            #add suit to the empty set and find the length of it
            suit_list.add(suit)
            match = len(suit_list)
            #there is a sequence if the rank corresponds to the order variable and the suit set has only one suit
            if rank == order and match == 1:
                #alter the variables and continue
                order += 1
                number += 1
                continue
            #if sequence ends, append card's numbered position to the progress list and exit loop
            else:
                progress.append(number)
                break
#STEP 2: create a list of cards that need to be shuffled
    card_list = tableau[0][progress[0]:]
    card_list += tableau[1][progress[1]:]
    card_list += tableau[2][progress[2]:]
    card_list += tableau[3][progress[3]:]
    #modify tableau to sequenced cards only
    tableau[0] = tableau[0][:progress[0]]
    tableau[1] = tableau[1][:progress[1]]
    tableau[2] = tableau[2][:progress[2]]
    tableau[3] = tableau[3][:progress[3]]
#STEP 3: shuffle list and remove aces
    random.shuffle(card_list)
    ace = []
    #iterate through card list
    for card in card_list:
        rank = card.rank()
        if rank == 1:
            card_list.remove(card)
            ace.append(card)
    #iterate through card list
    for card in card_list:
        rank = card.rank()
        if rank == 1:
            card_list.remove(card)
            ace.append(card)
#STEP 4: add aces to tableau
    tableau[0].append(ace[0])
    tableau[1].append(ace[1])
    tableau[2].append(ace[2])
    tableau[3].append(ace[3])
#STEP 5: distribute remaining cards to tableau
    #find how many cards need to be distributed by subtracting current list from 13
    deal1 = 13 - len(tableau[0])
    deal2 = 13 - len(tableau[1])
    deal3 = 13 - len(tableau[2])
    deal4 = 13 - len(tableau[3])
    #create loops to append the card to each row, while removing it from the card list
    for i in range(deal1):
        tableau[0].append(card_list[0])
        card_list.remove(card_list[0])
    for i in range(deal2):
        tableau[1].append(card_list[0])
        card_list.remove(card_list[0])
    for i in range(deal3):
        tableau[2].append(card_list[0])
        card_list.remove(card_list[0])
    for i in range(deal4):
        tableau[3].append(card_list[0])
        card_list.remove(card_list[0])
    
def check_win(tableau):
    ''' This function checks to see if the game is completed '''
    #create a loop for each row in the tableau
    for row in tableau:
        #create an empty set for the loops
        suit_list = set()
        #set a variable to indicate the first number in a completed game
        order = 2
        #create a loop for each card in the row
        for card in row[:-1]:
            #find its rank and suit
            rank = card.rank()
            suit = card.suit()
            #add the suit to the set and test if rank is in ascending order
            suit_list.add(suit)
            if rank != order:
                #return False if not in order
                return False
            order +=1
        #test if the last card is an Ace Card
        ace = row[-1].rank()
        if ace != 1:
            return False
        #test if each row has one suit in the set
        if len(suit_list) > 1:
            return False
    #if all tests pass, return True
    return True
                 
def main():
    ''' This function will call all other functions and begin the game play '''
    play = 'y'
    #create main loop to play game
    while play != 'n':
        #show title of game and initialize/display tableau
        print("Montana Solitaire.")
        tableau = initialize()
        display(tableau)
        #create nested loop
        y = True
        shuffle = 0
        while y == True:
            #prompt user for choice
            choice = input("Enter choice:\n (q)uit, (s)huffle, or space-separated: source_row,source_col,dest_row,dest_col: ")
            try:
                #split the choice into a list
                test = choice.split()
                correct = 'qs'
                #test if the choice is either four integers or 'q' or 's'
                if len(test) == 4:
                    for i in test:
                        i = int(i)
                elif len(test) == 1:
                    if choice not in correct:
                        raise ValueError
                else:
                    raise ValueError
            #output error code and continue the loop if choice fails the tests
            except:
                print('Error: invalid input.  Please try again.')
                continue
            #call shuffle function if prompted (no more than twice)
            if choice == 's':
                if shuffle < 5:
                    shuffle_tableau(tableau)
                    shuffle += 1
                #output error statement if necessary and continue the loop
                else:
                    print("No more shuffles remain.")
                    continue
            #exit loop if user quits
            elif choice == 'q':
                break
            else:
                #split input of numbers and call move function
                choice = choice.split()
                sr,sc,dr,dc = int(choice[0])-1,int(choice[1])-1,int(choice[2])-1,int(choice[3])-1
                check = validate_move(tableau,sr,sc,dr,dc)
                if check == False:
                    #set valid range for input values
                    valid_row = 0,1,2,3
                    valid_col = 0,1,2,3,4,5,6,7,8,9,10,11,12
                    #if parameters are not in the valid range, print error statements
                    if sr not in valid_row or dr not in valid_row:
                        print('Error: row and/or column out of range. Please Try again.')
                    elif sc not in valid_col or dc not in valid_col:
                        print('Error: row and/or column out of range. Please Try again.')
                    else:
                    #if range is valid but the move is invalid, print the appropriate error statement
                        print('Error: invalid move.  Please try again.')
                    continue
                else:
                    #execute move if valid
                    move(tableau,sr,sc,dr,dc)
            #call display function and check win function after every move   
            display(tableau)
            win = check_win(tableau)
            #break nested loop if player won
            if win == True:
                print("You won!")
                break
        #break main loop if player quits
        play = input("Do you want to play again (y/n)?")
    #output closing statement
    print('Thank you for playing.')

if __name__ == "__main__":
    #call main function 
    main()
