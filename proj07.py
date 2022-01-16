###########################################################
    #  CSE 231 Project #7
    #
    #  Functions and Dictionaries
    #    open and read CSV files
    #       read for certain values in a CSV file
    #    output appropriate value in the function
    #       call appropriate functions
    #    display closing message
    #
    ###########################################################

import csv

def open_file():
    ''' This function prompts for a file and opens it in read '''
    x = True
    #create a loop until correct file is input
    while x is True:
        try:
            filename = input("Enter filename: ")
            fp = open(filename, 'r')
            #fp = open('data_2010.csv', 'r')
            x = False
        #output error message
        except FileNotFoundError:
            print("File not found! Please try again!")
    #return openned file
    return fp
def calc_multipliers():
    ''' This function calculates and creates a list of multipliers '''
    #create empty list
    multiplier=[]
    #append calculated values to the list for numbers 2-60
    for n in range(2,61):
        value = 1/((n*(n-1))**.5)
        multiplier.append(value)
    #return list of multipliers
    return multiplier
    
def calc_priorities(s,p,m):
    ''' This function calculates the priorities based on state, population, and multipliers '''
    priorities=[]
    for i in m:
        value = int(float(p)*i)
        values = (value,s)
        priorities.append(values)
    priorities.sort(reverse=True)
    return priorities

def read_file_make_priorities(fp,multipliers): 
    ''' This function outputs two big lists of state reps and priority tuples '''
    #read csv file and create master list
    reader = csv.reader(fp)
    next(reader,None)
    master_list = []
    #append master_list with each line list
    for i in reader:
        master_list.append(i)
    #create two seperate lists for all the states and populations
    states=[]
    for i in master_list:
        state = i[1].strip(' "')
        states.append(state)
    population=[]
    for i in master_list:
        value=int(i[2])
        population.append(value)
    #create state reps list with each state and minimum reps
    state_reps=[]
    for i in states:
        if i == 'Puerto Rico' or i == 'District of Columbia':
            continue
        reps=[i,1]
        state_reps.append(reps)
    state_reps.sort()
    #create priorities list with each state and priority value
    priorities=[]
    for y in range(len(master_list)):
        if states[y] == 'Puerto Rico' or states[y] == 'District of Columbia':
            continue
        for i in multipliers:
            value = int(population[y]*i)
            values = (value,states[y])
            priorities.append(values)

    priorities.sort(reverse=True)
 
    priorities=priorities[:385]
    #sort the lists appropriately and return them
    return state_reps,priorities
        

def add_to_state(state,state_reps):
    ''' This function adds to the states '''
    for i in range(len(state_reps)):
        if state_reps[i][0]==state:
            state_reps[i][1]+=1

def display(state_reps):
    ''' This function displays the information '''
    state_reps.sort()
    for i in state_reps:
        state=state_reps[0]
        rep=state_reps[1]
        print('{:<15s}{:>4d}'.format(state,rep))

def main():
    fp=open_file()
    multipliers=calc_multipliers()
    state_reps,priorities=read_file_make_priorities(fp,multipliers)
    for i in priorities:
        state=i[1]
        add_to_state(state,state_reps)
    print('{:<15s}{:>4s}'.format('State','Representatives'))
    display(state_reps)
    

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    