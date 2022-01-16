###########################################################
    #  CSE 231 Project #8
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
import pylab
from operator import itemgetter

def open_file():
    ''' This function prompts for a file and opens it in encoding '''
    x = True
    #create a loop until correct file is input
    while x is True:
        try:
            filename = input("Enter filename: ")
            fp = open(filename, encoding = 'utf-8')
            #fp = open('video_game_sales_2016.csv', encoding = 'utf-8')
            x = False
        #output error message
        except FileNotFoundError:
            print("File not found! Please try again!")
    #return openned file
    return fp

def read_file(fp):
    ''' This function reads fp and returns three dictionaries '''
    reader = csv.reader(fp)
    next(reader,None)
    master_list = []
    #append master_list with each line list
    for i in reader:
        master_list.append(i)
    #create the three dictionaries
    Dict1 = {}
    Dict2 = {}
    Dict3 = {}
    #iterate through master list for each value
    for line in master_list:
        name = line[0].strip().lower()
        platform = line[1].strip().lower()
        year = line[2].strip()
        if year == 'N/A':
            continue
        year = int(year)
        genre = line[3].strip().lower()
        publisher = line[4].strip().lower()
        na_sales = float(line[5].strip()) * 1000000
        europe_sales = float(line[6].strip()) * 1000000
        japan_sales = float(line[7].strip()) * 1000000
        other_sales = float(line[8].strip()) * 1000000
        global_sales = na_sales + europe_sales + japan_sales + other_sales
        #create tuple for names
        namestup = (name,platform,year,genre,publisher,global_sales)
        if name in Dict1:
            #if name is already in dictionary then append the tuple to the list
            Dict1[name].append(namestup)
        else:
            #if name is not already in dictionary then create a list with the tuple
            Dict1[name] = [namestup]
        #create tuple for genres
        genrestup = (genre,year,na_sales,europe_sales,japan_sales,other_sales,global_sales)
        if genre in Dict2:
            #if genre is already in dictionary then append the tuple to the list
            Dict2[genre].append(genrestup)
        else:
            #if genre is not already in dictionary then create a list with the tuple
            Dict2[genre] = [genrestup]        
        #create tuple for publishers
        publisherstup = (publisher,name,year,na_sales,europe_sales,japan_sales,other_sales,global_sales)
        if publisher in Dict3:
            #if genre is already in dictionary then append the tuple to the list
            Dict3[publisher].append(publisherstup)
        else:
            #if genre is not already in dictionary then create a list with the tuple
            Dict3[publisher] = [publisherstup]
    #sort each dictionary by key
    sortedDict1 = {}
    sortedDict2 = {}
    sortedDict3 = {}
    for key in sorted(Dict1):
        sortedDict1[key] = Dict1[key]
    for key in sorted(Dict2):
        sortedDict2[key] = Dict2[key]
    for key in sorted(Dict3):
        sortedDict3[key] = Dict3[key]
    #sort each dictionary by global sales in reverse order
    D1 = {}
    D2 = {}
    D3 = {}
    for key in sortedDict1:
        D1[key] = sorted(sortedDict1[key], key = itemgetter(-1), reverse = True)
    for key in sortedDict2:
        D2[key] = sorted(sortedDict2[key], key = itemgetter(-1), reverse = True)
    for key in sortedDict3:
        D3[key] = sorted(sortedDict3[key], key = itemgetter(-1), reverse = True)     
    #return final sorted dictionaries
    return D1,D2,D3

def get_data_by_column(D1, indicator, c_value):
    ''' This function iterates through the dictionary D1 and returns a subset of the data '''
    if indicator == 'year':
        #create an empty list
        yearlist = []
        #iterate through each tuple in each list in D1
        for lists in D1.values():
            for value in lists:
                #append tuple to list if it corresponds to c value
                if value[2] == int(c_value):
                    yearlist.append(value)
        #sort the list by global sales and platform
        yearlist.sort(key = itemgetter(-1), reverse = True)
        yearlist.sort(key = itemgetter(1))
        return yearlist
    elif indicator == 'platform':
        #create an empty list
        platformlist = []
        #iterate through each tuple in each list in D1
        for lists in D1.values():
            for value in lists:
                #append tuple to list if it corresponds to c value
                if value[1] == c_value:
                    platformlist.append(value)
        #sort the list by global sales and year
        platformlist.sort(key = itemgetter(-1), reverse = True)
        platformlist.sort(key = itemgetter(2))
        return platformlist
    
def get_publisher_data(D3, publisher):
    ''' This function iterates through the dictionary D3 and returns a subset of the data '''
    #create an empty list
    publisherlist = []
    #iterate through each tuple in each list in D3
    for lists in D3.values():
        for value in lists:
            #append tuple to list if it corresponds to publisher
            if publisher in list(value):
                publisherlist.append(value)
    #sort the list by global sales and name
    publisherlist.sort(key = itemgetter(1))
    publisherlist.sort(key = itemgetter(-1), reverse = True)
    return publisherlist

def display_global_sales_data(L, indicator):
    ''' This function prints a table of all the global game sales based on year or platform '''
    #establish headers for the table
    header1 = ['Name', 'Platform', 'Genre', 'Publisher', 'Global Sales']
    header2 = ['Name', 'Year', 'Genre', 'Publisher', 'Global Sales']
    if indicator == 'year':
        print("{:30s}{:10s}{:20s}{:30s}{:12s}".format('Name', 'Platform', 'Genre', 'Publisher', 'Global Sales'))
        for value in L:
            name = value[0]
            platform = value[1]
            year = value[2]
            genre = value[3]
            publisher = value[4]
            global_sales = value[5]
            print("{:30s}{:10s}{:20s}{:30s}{:<12,.02f}".format(name[:25],platform,genre[:15],publisher[:25],global_sales))
    elif indicator == 'platform':
        print("{:30s}{:10s}{:20s}{:30s}{:12s}".format('Name', 'Year', 'Genre', 'Publisher', 'Global Sales'))
        for value in L:
            name = value[0]
            platform = value[1]
            year = value[2]
            genre = value[3]
            publisher = value[4]
            global_sales = value[5]
            print("{:30s}{:10s}{:20s}{:30s}{:<12,.02f}".format(name[:25],year,genre[:15],publisher[:25],global_sales))

def get_genre_data(D2, year):
    ''' This function iterates through the dictionary D2 and returns a subset of the data '''
    #create an empty list
    genrelist = []
    #iterate through each tuple in each list in D2
    for genre,lists in D2.items():
        #set all variables to 0
        count = 0
        total_na_sales = 0
        total_europe_sales = 0
        total_japan_sales = 0
        total_other_sales = 0
        total_global_sales = 0
        #iterate through each tuple and add numbers to the counts
        for value in lists:
            if value[1] == year:
                count += 1
                total_na_sales += value[2]
                total_europe_sales += value[3]
                total_japan_sales += value[4]
                total_other_sales += value[5]
                total_global_sales += value[6]
            else:
                continue
        #return empty list if count = 0
        if count == 0:
            continue
        #create a tuple and append it to the list
        tup = (genre,count,total_na_sales,total_europe_sales,total_japan_sales,total_other_sales,total_global_sales)
        genrelist.append(tup)
    #sort tuple alphabetically and by global sales
    genrelist.sort()
    genrelist.sort(key = itemgetter(-1), reverse = True)
    return genrelist

def get_totals(L, indicator):
    ''' This function iterates through the dictionary D1 and returns two lists of years/platforms and global sales '''
    #create empty dictionary
    Dict = {}
    #add sales and year/platform to the dictionary
    if indicator == 'year':
        for value in L:
            if value[1] in Dict:
                Dict[value[1]] += value[5]
            else:
                Dict[value[1]] = value[5]
    elif indicator == 'platform':
        for value in L:
            if value[2] in Dict:
                Dict[value[2]] += value[5]
            else:
                Dict[value[2]] = value[5]
    #create the two lists
    keylist = []
    saleslist = []
    #append all the keys in alphabetical order
    for key in Dict.keys():
        keylist.append(key)
    keylist.sort()
    #append all the sales based on the keys
    for sales in keylist:
        saleslist.append(Dict[sales])
    #return both lists
    return keylist,saleslist
        







