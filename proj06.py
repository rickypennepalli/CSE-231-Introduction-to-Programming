###########################################################
    #  CSE 231 Project #6
    #
    #  Functions and Try/Except
    #    open and read CSV files
    #       read for certain values in a CSV file
    #    output appropriate value in the function
    #       call appropriate functions
    #    display closing message
    #
    ###########################################################

#import csv from python
import csv

def open_file():
    ''' This function prompts for a file and opens it in read '''
    x = True
    #create a loop until correct file is input
    while x is True:
        try:
            filename = input("Enter filename: ")
            fp = open(filename, 'r')
            #fp = open('Scoring_per_Game.csv', 'r')
            x = False
        #output error message
        except:
            print("File not found! Please try again!")
    #return openned file
    return fp

def read_file(fp):
    ''' This function reads the file and creates a list of lists '''
    #read csvfile into lists and skip first line
    reader = csv.reader(fp)
    next(reader, None)
    master_list = []
    #append master_list with each line list
    for line_list in reader:
        if line_list[0].strip() == "":
            continue
        master_list.append(line_list)
    #return the master list
    return master_list 
    
def shoots_left_right(master_list):
    ''' This function counts the left and right shooters from the master list '''
    #set counts for left and right shooters
    left_count = 0
    right_count = 0
    #read for appropriate value and add to each count 
    for value in master_list:
        shoot = value[1].strip()
        if shoot == 'R':
            right_count += 1
        else:
            left_count += 1
    #return both values
    return left_count,right_count
    
def position(master_list):
    ''' This function counts the positions of shooters from the master list '''
    #set counts for all positions
    left_count = 0
    right_count = 0
    center_count = 0
    defense_count = 0
    #read for appropriate value and add to each count
    for value in master_list:
        pos = value[2].strip()
        if pos == 'R':
            right_count += 1
        elif pos == 'L':
            left_count += 1
        elif pos == 'C':
            center_count += 1
        else:
            defense_count += 1
    #return all the values
    return left_count,right_count, center_count, defense_count

def off_side_shooter(master_list):
    ''' This function counts the off side shooters from the master list '''
    #set counts for position_shot
    left_right = 0
    right_left = 0
    #read for appropriate values in both items and add to the counts
    for value in master_list:
        shoot = value[1].strip()
        pos = value[2].strip()
        if pos == 'R' and shoot == 'L':
            right_left += 1
        elif pos == 'L' and shoot == 'R':
            left_right += 1
        else:
            continue
    #return both the values
    return left_right,right_left

def points_per_game(master_list):
    ''' This function returns the top scoring shooters from the master list '''
    #create an empty list and print titles
    toplist = []
    print("{:^36s}".format("Top Ten Points-Per-Game"))
    print("{:<20s}{:>8s}{:>16s}".format('Player','Position','Points Per Game'))
    #read for each value
    for value in master_list:
        #convert to points to float
        points = float(value[18].strip())
        pos = value[2].strip()
        name = value[0].strip()
        #create a tuple and append to list
        tupone = (points,name,pos)
        toplist.append(tupone)
    #print and return top ten values
    toplist.sort(reverse=True)
    for i in toplist[:10]:
        print("{:<20s}{:>8s}{:>16.2f}".format(i[1],i[2],i[0]))
    return toplist[:10] 

def games_played(master_list):
    ''' This function returns the most games played players from the master list '''
    #create an empty list and print titles
    toplist = []
    print("{:^36s}".format("Top Ten Games-Played"))
    print("{:<20s}{:>16s}".format('Player','Games Played'))
    #read for each value
    for value in master_list:
        #convert games played to integer
        gp = int(value[3].strip().replace(',',''))
        name = value[0].strip()
        #create tuple and append to list
        tupone = (gp,name)
        toplist.append(tupone)
    #print and return top ten values
    toplist.sort(reverse=True)
    for i in toplist[:10]:
        print("{:<20s}{:>16,d}".format(i[1],i[0]))
    return toplist[:10]

def shots_taken(master_list):
    ''' This function returns the shots taken by players from the master list '''
    #create an empty list and print titles
    toplist = []
    print("{:^36s}".format("Top Ten Shots-Taken"))
    print("{:<20s}{:>16s}".format('Player','Shots Taken'))
    #read for each value
    for value in master_list:
        #skip values with no values
        if value[9].strip() == '--':
            continue
        else:
            #convert shots taken to integer
            shot = int(value[9].strip().replace(',',''))
            name = value[0].strip()
            #create tuple and append to list
            tupone = (shot,name)
            toplist.append(tupone)
    #print and return top ten values
    toplist.sort(reverse=True)
    for i in toplist[:10]:
        print("{:<20s}{:>16,d}".format(i[1],i[0]))
    return toplist[:10]
    
def main():
    ''' Main Function that calls all other functions '''
    #call all the functions and print appropriately
    fp = open_file()
    master_list = read_file(fp)
    print()
    print()
    print("{:^10s}".format("Shooting"))
    print("left:  {:4d}".format(shoots_left_right(master_list)[0]))
    print("right: {:4d}".format(shoots_left_right(master_list)[1]))
    print()
    print("{:^12s}".format("Position"))
    print("left:    {:4d}".format(position(master_list)[0]))
    print("right:   {:4d}".format(position(master_list)[1]))
    print("center:  {:4d}".format(position(master_list)[2]))
    print("defense: {:4d}".format(position(master_list)[3]))
    print()
    print("{:^24s}".format("Off-side Shooter"))
    print("left-wing shooting right: {:4d}".format(off_side_shooter(master_list)[0]))
    print("right-wing shooting left: {:4d}".format(off_side_shooter(master_list)[1]))
    print()
    points_per_game(master_list)
    print()
    games_played(master_list)
    print()
    shots_taken(master_list)
    
if __name__ == "__main__":
    main()