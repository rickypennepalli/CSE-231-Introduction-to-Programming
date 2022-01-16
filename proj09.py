###########################################################
    #  CSE 231 Project #9
    #
    #  Dictionaries and Functions
    #    open and read CSV files
    #       read for certain values in a CSV file
    #    output appropriate value in the function
    #       call appropriate functions
    #    display closing message
    #
    ###########################################################
    
import csv
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from operator import itemgetter


def open_file():
    ''' This function prompts for a file and opens it in read '''
    x = True
    #create a loop until correct file is input
    while x is True:
        try:
            filename = input("Data file: ")
            if filename == '':
                fp = open('ncov.csv', 'r')
            else:
                fp = open(filename, 'r')
            x = False
        #output error message
        except FileNotFoundError:
            print("Error. Try again.")
    #return openned file
    return fp

def build_dictionary(fp):
    ''' This function accepts the file pointer as input and returns the required dictionary '''
    #read csv file and create a master list
    reader = csv.reader(fp)
    next(reader,None)
    master_list = []
    #append master_list with each line list
    for i in reader:
        master_list.append(i)
    #create an empty dictionary for all the countries
    master_dict = {}
    for line in master_list:
        #iterate through each value in the master list
        areadict = {}
        country = line[2].strip()
        area = line[1].strip()
        if area == '':
            area = 'N/A'
        last_update = line[3].strip()
        cases = int(line[4].strip())
        deaths = int(line[5].strip())
        recovered = int(line[6].strip())
        #create a tuple to add into a smaller dictionary
        area_tup = (last_update, cases, deaths, recovered)
        areadict[area] = area_tup
        if country in master_dict:
            #if country is already in dictionary then append the smaller dictionary to the list
            master_dict[country].append(areadict)
        else:
            #if country is not already in dictionary then create a list with the smaller dictionary
            master_dict[country] = [areadict]
    #return the dictionary
    return master_dict
        
def top_affected_by_spread(master_dict):
    ''' This function accepts the dictionary and returns a list of the top 10 most affected countries '''
    #create an empty list
    area_list = []
    #iterate through each list in the dictionary
    for key,value in master_dict.items():
        #append the country and the length of its list to area list created above
        x = len(value)
        area_tup = (key, x)
        area_list.append(area_tup)
    #sort the list alphabetically and numerically
    area_list.sort()
    area_list.sort(key = itemgetter(1), reverse = True)
    #return the top ten results
    return area_list[:10]  

def top_affected_by_numbers(master_dict):
    ''' This function accepts the dictionary and returns a list of the countries with the top 10 cases '''
    #create an empty list
    area_list = []
    #iterate through each list in the dictionary
    for key,value in master_dict.items():
        x = 0
        #iterate through each dictionary in the list
        for case in value:
            #iterate through each value in the dictionary
            for i in case.values():
        #find the sum of the values and append the tuple to area list
                x += i[1]
        area_tup = (key, x)
        area_list.append(area_tup)
    #sort the list alphabetically and numerically
    area_list.sort()
    area_list.sort(key = itemgetter(1), reverse = True)
    #return the top ten results
    return area_list[:10]    

def is_affected(master_dict, country):
    ''' This function accepts in the dictionary and a country and returns a Boolean on whether a country is affected '''
    #set country to lowercase and provide a false boolean variable
    country = country.lower()
    x = False
    #iterate through the keys in the dictionary
    for keys in master_dict.keys():
        #change the boolean variable if the country matches the key
        if country == keys.lower():
            x = True
        #if country is not in the dictionary then continue
        else:
            continue
    #return the boolean
    return x

def plot_by_numbers(list_of_countries, list_of_numbers):
    '''
        This function plots the number of areas/people inffected by country.
        
        parameters: 
            list_of_countries: list of countries
            list_of_numbers: list of the number of areas/people inffected
            
        Returns: None
    '''
    fig, ax = plt.subplots()
    
    x_pos = [i for i, _ in enumerate(list_of_countries)]
    
    ax.barh(x_pos, list_of_numbers, align='center', color='red')
    ax.set_yticks(x_pos)
    ax.set_yticklabels(list_of_countries)
    ax.invert_yaxis()
    ax.set_xlabel('Count')
    ax.set_title('Novel Coronavirus statistics')
    
    plt.show()

def affected_states_in_country(master_dict, country):
    ''' This function accepts in the dictionary and a country and returns a set of affected areas '''
    #set country to lowercase and create an empty set
    country = country.lower()
    areas = set()
    #iterate through each item in the dictionary
    for keys,values in master_dict.items():
        #find a country that matches a key
        if country == keys.lower():
            #iterate through each key in each dictionary in the list
            for i in values:
                for area in i.keys():
                    #add the area to the empty set
                    areas.add(area)
        #if country is not in the dictionary then continue
        else:
            continue
    #return the set
    return areas


def main():
    BANNER = '''
.__   __.   ______   ______   ____    ____
|  \ |  |  /      | /  __  \  \   \  /   /
|   \|  | |  ,----'|  |  |  |  \   \/   / 
|  . `  | |  |     |  |  |  |   \      /  
|  |\   | |  `----.|  `--'  |    \    /   
|__| \__|  \______| \______/      \__/  
    '''
    print(BANNER)
    MENU = ''' 
[1] Countries with most areas infected
[2] Countries with most people affected
[3] Affected areas in a country
[4] Check if a country is affected
[5] Exit

Choice: '''
    #open file and call dictionary function
    fp = open_file()
    master_dict = build_dictionary(fp)
    x = True
    y = True
    #create a loop to prompt for the choices
    while y ==True:
        #create a nested loop to produce the error line in case of an error
        while x == True:
            #prompt for choice between 1 and 5
            try:
                choice = int(input(MENU))
                if 1 <= choice <= 5:
                    break
                #raise error if choice does not satisfy rules
                else:
                    raise ValueError
            #print error statement and loop
            except:
                print("Error. Try again.")
        
        if choice == 1:
            #create a table for areas affected
            print("{:<20s} {:15s}".format("Country", "Areas affected"))
            print("-"*40) 
            #call function
            areas = top_affected_by_spread(master_dict)
            #create empty plot lists for x and y values
            plot_x = []
            plot_y = []
            #iterate through the tuples and print the values appropriately
            for tups in areas:
                area = tups[0]
                number = tups[1]
                #add the values to the plot lists
                plot_x.append(area)
                plot_y.append(number)
                print("{:<20s} {:5d}".format(area,number))
            #plot first five points if plot prompt is yes
            plot = input('Plot? (y/n) ')
            if plot == 'y':
                plot_by_numbers(plot_x[:5],plot_y[:5])
                
        if choice == 2:
            #create a table for people affected
            print("{:<20s} {:15s}".format("Country", "People affected"))
            print("-"*40) 
            #call function
            areas = top_affected_by_numbers(master_dict)
            #create empty plot lists for x and y values
            plot_x = []
            plot_y = []
            #iterate through the tuples and print the values appropriately
            for tups in areas:
                area = tups[0]
                number = tups[1]
                #add the values to the plot lists
                plot_x.append(area)
                plot_y.append(number)
                print("{:<20s} {:5d}".format(area,number))
            #plot first five points if plot prompt is yes
            plot = input('Plot? (y/n) ')
            if plot == 'y':
                plot_by_numbers(plot_x[:5],plot_y[:5])
        
        if choice == 3:
            #prompt for a country and create table
            country = input("Country name: ")
            print("-"*30)
            #call function
            states = affected_states_in_country(master_dict,country)
            #if country is not in dictionary (or set is empty) then print error line
            if len(states) == 0:
                print("Error. Country not found.")
            else:
                #create table for the affected areas
                print("{:<30s}".format("Affected area"))
                print("-"*30)
                val = 1
                for state in sorted(states):
                    print("[{:02d}] {:<30s}".format(val,state))
                    val += 1
        
        if choice == 4:
            #prompt for a country and create table
            country = input("Country name: ")
            print("-"*30)
            #call function
            covid = is_affected(master_dict, country)
            #print appropriate lines
            if covid == True:
                print("{} is affected.".format(country))
            else:
                print("{} is not affected.".format(country))
                    
        if choice == 5:
            #print exit line and break loop
            print("Stay at home. Protect your community against COVID-19")
            break
    
if __name__ == "__main__":
    #call main function
    main()

    