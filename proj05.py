###########################################################
    #  CSE 231 Project #5
    #
    #  Functions and Try/Except
    #    open and read file
    #       read for certain values in the file
    #    output appropriate value in the function
    #       call appropriate functions
    #    display closing message
    #
    ###########################################################
   
def open_file():
    ''' This function prompts for a file and opens it in read '''
    x = True
    #create a loop until correct file is input
    while x is True:
        try:
            filename = input("Input a file name: ")
            fp = open(filename, 'r')
            #fp = open('MMR.txt', 'r')
            x = False
        #output error message
        except:
            print("Error: file not found. Please try again.")
    #return openned file
    return fp

def get_us_value(fp):
    ''' This functions reads the file and returns US coverage value '''
    #set the correct string value
    right = 'United States'
    #create loop for each line in fp
    for line in fp:
        if right in line:
            #attain the correct line with string value
            x = line
            break
        else:
            continue
    #strip the line and turn it into a float
    x = float((x[-10:]).strip())
    return x
    
def get_min_value_and_state(fp):
    ''' This function reads the file by line and return lowest coverage value '''
    #seek for appropriate line and read first two lines
    fp.seek(0)
    fp.readline()
    fp.readline()
    #set variables
    minvalue = 100
    state = ''
    #create loop for each line in fp
    for line in fp:
        x = line[-10:].strip()
        #check if x is a number and if is lesser than previous value
        if x != 'NA':
            x = float(x)
            if x <= minvalue:
                #assign state with lowest value
                minvalue = x
                state = str(line[:25].strip())
            else:
                continue
    print("State with minimal MMR coverage: {} {}%".format(state,minvalue))
    return state,minvalue
    

def get_max_value_and_state(fp):
    ''' This function reads the file by line and return largest coverage value '''
    #seek for appropriate line and read first two lines
    fp.seek(0)
    fp.readline()
    fp.readline()
    #set variables
    maxvalue = 0
    state = ''
    #create loop for each line in fp
    for line in fp:
        x = line[-10:].strip()
        #check if x is a number and if is greater than previous value
        if x != 'NA':
            x = float(x)
            if x >= maxvalue:
                #assign state with largest value
                maxvalue = x
                state = str(line[:25].strip())
            else:
                continue
    print("State with maximum MMR coverage: {} {}%".format(state,maxvalue))
    return state,maxvalue
        
def display_herd_immunity(fp):
    ''' This function reads the file by line and returns coverage value less than 90'''
    #seek for appropriate line and read first two lines
    fp.seek(0)
    fp.readline()
    fp.readline()
    #set variables
    value = 0
    state = ''
    #create loop for each line in fp
    for line in fp:
        x = line[-10:].strip()
        #check if x is a number and if is greater than previous value
        if x != 'NA':
            x = float(x)
            if x < 90:
                #assign state with largest value
                value = x
                state = str(line[:25].strip())
                herd = []
                herd.append(state)
                herd.append(value)
            else:
                continue
            print("{:<25s}{:>5.1f}%".format(herd[0],herd[1]))

def write_herd_immunity(fp):
    ''' This function writes certain coverage values into another file '''
    #open new file and write headers
    outfile = open("herd.txt","w")
    outfile.write("\nStates with insufficient Measles herd immunity.")
    outfile.write("\n{:<25s}{:>5s}".format("State","Percent"))
    
    '''repeat previous function '''
    #seek for appropriate line and read first two lines
    fp.seek(0)
    fp.readline() 
    fp.readline()
    #set variables
    value = 0
    state = ''
    #create loop for each line in fp
    for line in fp:
        x = line[-10:].strip()
        #check if x is a number and if is greater than previous value
        if x != 'NA':
            x = float(x)
            if x < 90:
                #assign state with largest value
                value = x
                state = str(line[:25].strip())
                herd = []
                herd.append(state)
                herd.append(value)
            else: 
                continue
            #write content in another file and close the file
            outfile.write("\n{:<25s}{:>5.1f}%".format(herd[0],herd[1]))
    outfile.write('\n')
    outfile.close()

def main():   
    fp = open_file()
    title = fp.readline()
    #output title
    print()
    print(title)
    #call each function appropriately
    print("Overall US MMR coverage: {}%".format(get_us_value(fp)))
    get_min_value_and_state(fp)
    get_max_value_and_state(fp)
    print("\nStates with insufficient Measles herd immunity.")
    print("{:<25s}{:>5s}".format("State","Percent"))
    display_herd_immunity(fp)
    write_herd_immunity(fp)
if __name__ == "__main__":
    #call main function 
    main()    