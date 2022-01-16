#project3
#A 2019 MSU undergraduate tuition calculater

print('2019 MSU Undergraduate Tuition Calculator.')
print()
calc = 'yes'
#set a basic first loop for the function
while calc == 'yes': 
    resident = input('Resident (yes/no): ').lower()
    #start a second loop for the resident and levels
    while resident == 'yes':
        level = input('Level—freshman, sophomore, junior, senior: ').lower()
        #narrow prompts for freshmen and sophomores
        if level == 'freshman' or level == 'sophomore':
            eng = input('Are you admitted to the College of Engineering (yes/no): ').lower()
            if eng == 'yes':
            #calculate tuiton cost for freshman and sophomore engineering students based on credit
                credit = input('Credits: ')
                #test if credit value is an integer greater than 0
                while not credit.isdigit() or int(credit)<=0: 
                    print('Invalid input. Try again.')
                    credit = input('Credits: ')
                credit = int(credit)
                #calculate cost of tuition    
                if credit < 12:
                    cost = credit * 482
                elif credit <=18:
                    cost = 7230 + 5 + 670
                else: 
                    cost = 7230 + 5 + ((credit-18)*482) + 670
            else:
                jmc = input('Are you in the James Madison College (yes/no): ').lower()
                if jmc == 'yes':
                #calculate tuition cost for freshman and sophomore JMC students based on credit
                    credit = input('Credits: ')
                    #test if credit value is an integer greater than 0
                    while not credit.isdigit() or int(credit)<=0: 
                        print('Invalid input. Try again.')
                        credit = input('Credits: ')
                    credit = int(credit)
                    #calculate cost of tuition 
                    if credit < 12:
                        cost = credit * 482 + 7.5
                    elif credit <=18:
                        cost = 7230 + 5 + 7.5
                    else: 
                        cost = 7230 + 5 + ((credit-18)*482) + 7.5
                else:
                    credit = input('Credits: ')
                    #test if credit value is an integer greater than 0
                    while not credit.isdigit() or int(credit)<=0: 
                        print('Invalid input. Try again.')
                        credit = input('Credits: ')
                    credit = int(credit)
                    #calculate cost of tuition    
                    if credit < 12:
                        cost = credit * 482
                    elif credit <=18:
                        cost = 7230 + 5
                    else: 
                        cost = 7230 + 5 + ((credit-18)*482)
            cost = cost + 24
            #print the final tuition cost with appropriate format
            if cost >= 1000:
                comma1 = cost // 1000
                comma2 = cost % 1000
                print('Tuition is $%d,%.2f.' %(comma1,comma2))
            else:
                print('Tuition is $%.2f.' %(cost))
            #exit the second loop for residents and levels
            break   
        #narrow prompts for juniors and seniors
        elif level == 'junior' or level == 'senior':
            college = None
            #prompt juniors and seniors for their college
            college = input('Enter college as business, engineering, health, sciences, or none: ').lower()
            #narrow prompts for juniors and seniors in the business college
            if college == 'business':
                cmse = input('Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ').lower()
                if cmse =='yes':
                #calculate tuiton cost for junior and senior business CMSE students based on credit
                    credit = input('Credits: ')
                    #test if credit value is an integer greater than 0
                    while not credit.isdigit() or int(credit)<=0: 
                        print('Invalid input. Try again.')
                        credit = input('Credits: ')
                    credit = int(credit)
                    #calculate cost of tuition     
                    if credit < 12:
                        cost = credit * 573
                    elif credit <=18:
                        cost = 8595 + 5 + 226 + 670
                    else: 
                        cost = 8595 + 5 + 226 + ((credit-18)*573) + 670
                else:
                #calculate tuiton cost for junior and senior business students based on credit
                    credit = input('Credits: ')
                    #test if credit value is an integer greater than 0
                    while not credit.isdigit() or int(credit)<=0: 
                        print('Invalid input. Try again.')
                        credit = input('Credits: ')
                    credit = int(credit)
                    #calculate cost of tuition     
                    if credit < 12:
                        cost = credit * 573
                    elif credit <=18:
                        cost = 8595 + 5 + 226
                    else: 
                        cost = 8595 + 5 + 226 + ((credit-18)*573)
            elif college == 'engineering':
                cmse = input('Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ').lower()
                if cmse =='yes':
                #calculate tuiton cost for junior and senior engineering CMSE students based on credit
                    credit = input('Credits: ')
                    #test if credit value is an integer greater than 0
                    while not credit.isdigit() or int(credit)<=0: 
                        print('Invalid input. Try again.')
                        credit = input('Credits: ')
                    credit = int(credit)
                    #calculate cost of tuition     
                    if credit < 12:
                        cost = (credit * 573) + 670
                    elif credit <=18:
                        cost = 8595 + 5 + 670
                    else: 
                        cost = 8595 + 5 + 670 +((credit-18)*573)
                else:
                #calculate tuiton cost for junior and senior engineering students based on credit
                    credit = input('Credits: ')
                    #test if credit value is an integer greater than 0
                    while not credit.isdigit() or int(credit)<=0: 
                        print('Invalid input. Try again.')
                        credit = input('Credits: ')
                    credit = int(credit)
                    #calculate cost of tuition     
                    if credit < 12:
                        cost = (credit * 573) + 670
                    elif credit <=18:
                        cost = 8595 + 5 + 670
                    else: 
                        cost = 8595 + 5 + 670 +((credit-18)*573)
            #narrow prompts for juniors and seniors in the health college
            elif college == 'health':
                cmse = input('Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ').lower()
                if cmse =='yes':
                #calculate tuiton cost for junior and senior health CMSE students based on credit
                    credit = input('Credits: ')
                    #test if credit value is an integer greater than 0
                    while not credit.isdigit() or int(credit)<=0: 
                        print('Invalid input. Try again.')
                        credit = input('Credits: ')
                    credit = int(credit)
                    #calculate cost of tuition     
                    if credit < 12:
                        cost = (credit * 555) + 670
                    elif credit <=18:
                        cost = 8325 + 670 + 5
                    else: 
                        cost = 8325 + ((credit-18) * 555) + 670
                else:
                #calculate tuiton cost for junior and senior health students based on credit
                    credit = input('Credits: ')
                    #test if credit value is an integer greater than 0
                    while not credit.isdigit() or int(credit)<=0: 
                        print('Invalid input. Try again.')
                        credit = input('Credits: ')
                    credit = int(credit)
                    #calculate cost of tuition     
                    if credit < 12:
                        cost = (credit * 555) + 100
                    elif credit <=18:
                        cost = 8325 + 100 + 5
                    else: 
                        cost = 8325 + ((credit-18)*555) + 100 + 5
            elif college == 'sciences':
                cmse = input('Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ').lower()
                if cmse =='yes':
                #calculate tuiton cost for junior and senior science CMSE students based on credit
                    credit = input('Credits: ')
                    #test if credit value is an integer greater than 0
                    while not credit.isdigit() or int(credit)<=0: 
                        print('Invalid input. Try again.')
                        credit = input('Credits: ')
                    credit = int(credit)
                    #calculate cost of tuition     
                    if credit < 12:
                        cost = (credit * 555) + 670
                    elif credit <=18:
                        cost = 8325 + 670 + 5
                    else: 
                        cost = 8325 + ((credit-18) * 555) + 670 + 5
                else:
                #calculate tuiton cost for junior and senior science students based on credit
                    credit = input('Credits: ')
                    #test if credit value is an integer greater than 0
                    while not credit.isdigit() or int(credit)<=0: 
                        print('Invalid input. Try again.')
                        credit = input('Credits: ')
                    credit = int(credit)
                    #calculate cost of tuition     
                    if credit < 12:
                        cost = (credit * 555) + 100
                    elif credit <=18:
                        cost = 8325 + 100 + 5
                    else: 
                        cost = 8325 + ((credit-18)*555) + 100 + 5
            else:
                cmse = input('Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ').lower()
                if cmse =='yes':
                    jmc = input('Are you in the James Madison College (yes/no): ').lower()
                    if jmc == 'yes':
                    #calculate tuition cost for freshman and sophomore JMC CMSE students based on credit
                        credit = input('Credits: ')
                        #test if credit value is an integer greater than 0
                        while not credit.isdigit() or int(credit)<=0: 
                            print('Invalid input. Try again.')
                            credit = input('Credits: ')
                        credit = int(credit)
                        #calculate cost of tuition 
                        if credit < 12:
                            cost = credit * 555 + 7.5 
                        elif credit <=18:
                            cost = 8325 + 5 + 7.5 + 670
                        else: 
                            cost = 8325 + 5 + ((credit-18)*555) + 7.5 + 670
                    else:
                    #calculate tuiton cost for junior and senior CMSE students based on credit
                        credit = input('Credits: ')
                        #test if credit value is an integer greater than 0
                        while not credit.isdigit() or int(credit)<=0: 
                            print('Invalid input. Try again.')
                            credit = input('Credits: ')
                        credit = int(credit)
                        #calculate cost of tuition     
                        if credit < 12:
                            cost = (credit * 555) + 670 + 5
                        elif credit <=18:
                            cost = 8325 + 670 + 5
                        else: 
                            cost = 8325 + ((credit-18)*555) + 670 + 5
                else:
                #calculate tuiton cost for junior and senior students based on credit
                    credit = input('Credits: ')
                    #test if credit value is an integer greater than 0
                    while not credit.isdigit() or int(credit)<=0: 
                        print('Invalid input. Try again.')
                        credit = input('Credits: ')
                    credit = int(credit)
                    #calculate cost of tuition     
                    if credit < 12:
                        cost = (credit * 555)
                    elif credit <=18:
                        cost = 8325 + 5
                    else: 
                        cost = 8325 + ((credit-18)*555) + 5
            cost = cost + 24
            #print the final tuition cost with appropriate format
            if cost >= 1000:
                comma1 = cost // 1000
                comma2 = cost % 1000
                print('Tuition is $%d,%.2f.' %(comma1,comma2))
            else:
                print('Tuition is $%.2f.' %(cost))
            #exit the second loop for residents and levels
            break
        else:
        #print the error statement and repeat second loop to the original level question
            print('Invalid input. Try again.')  
            
    #international students        
    else:
        inter = input('International (yes/no): ').lower()
        if inter == 'yes':
        #narrow prompts for freshmen and sophomores
            level = input('Level—freshman, sophomore, junior, senior: ').lower()
            if level == 'freshman' or level == 'sophomore':
                eng = input('Are you admitted to the College of Engineering (yes/no): ').lower()
                if eng == 'yes':
                #calculate tuiton cost for freshman and sophomore engineering students based on credit
                    credit = input('Credits: ')
                    #test if credit value is an integer greater than 0
                    while not credit.isdigit() or int(credit)<=0: 
                        print('Invalid input. Try again.')
                        credit = input('Credits: ')
                    credit = int(credit)
                    #calculate cost of tuition     
                    if credit < 12:
                        cost = 1325.50 * credit
                    elif credit <=18:
                        cost = 19888 + 670
                    else: 
                        cost = 19888 + (1325.50 * (credit-18)) + 670
                else:
                    jmc = input('Are you in the James Madison College (yes/no): ').lower()
                    if jmc == 'yes':
                    #calculate tuition cost for freshman and sophomore JMC students based on credit
                        credit = input('Credits: ')
                        #test if credit value is an integer greater than 0
                        while not credit.isdigit() or int(credit)<=0: 
                            print('Invalid input. Try again.')
                            credit = input('Credits: ')
                        credit = int(credit)
                        #calculate cost of tuition     
                        if credit < 12:
                            cost = credit * 482 + 7.5
                        elif credit <=18:
                            cost = 7230 + 5 + 7.5
                        else: 
                            cost = 7230 + 5 + ((credit-18)*482) + 7.5
                    else:
                    #calculate tuition cost for freshman and sophomore students based on credit
                        credit = input('Credits: ')
                        #test if credit value is an integer greater than 0
                        while not credit.isdigit() or int(credit)<=0: 
                            print('Invalid input. Try again.')
                            credit = input('Credits: ')
                        credit = int(credit)
                        #calculate cost of tuition
                        if credit < 12:
                            cost = 1325.50 * credit
                        elif credit <=18:
                            cost = 19888
                        else: 
                            cost = 19888 + (1325.50 * (credit-18))
                cost = cost + 24 + 750 
                #print the final tuition cost with appropriate format
                if cost >= 1000:
                    comma1 = cost // 1000
                    comma2 = cost % 1000
                    print('Tuition is $%d,%.2f.' %(comma1,comma2))   
                else:
                    print('Tuition is $%.2f.' %(cost))
            #narrow prompts for juniors and seniors
            elif level == 'junior' or level == 'senior':
                college = None
                #prompt juniors and seniors for their college
                college = input('Enter college as business, engineering, health, sciences, or none: ').lower()
                #narrow prompts for juniors and seniors in the business college
                if college == 'business':
                    cmse = input('Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ').lower()
                    if cmse =='yes':
                    #calculate tuiton cost for junior and senior business CMSE students based on credit
                        credit = input('Credits: ')
                        #test if credit value is an integer greater than 0
                        while not credit.isdigit() or int(credit)<=0: 
                            print('Invalid input. Try again.')
                            credit = input('Credits: ')
                        credit = int(credit)
                        #calculate cost of tuition
                        if credit < 12:
                            cost = credit * 1385.75
                        elif credit <=18:
                            cost = 20786 + 5 + 226 + 670
                        else: 
                            cost = 20786 + 5 + 226 + ((credit-18)*1385.75) + 670
                    else:
                    #calculate tuiton cost for junior and senior business students based on credit
                        credit = input('Credits: ')
                        #test if credit value is an integer greater than 0
                        while not credit.isdigit() or int(credit)<=0: 
                            print('Invalid input. Try again.')
                            credit = input('Credits: ')
                        credit = int(credit)
                        #calculate cost of tuition
                        if credit < 12:
                            cost = credit * 1385.75
                        elif credit <=18:
                            cost = 20786 + 5 + 226
                        else: 
                            cost = 20786 + 5 + 226 + ((credit-18)*1385.75)
                elif college == 'engineering':
                    cmse = input('Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ').lower()
                    if cmse =='yes':
                    #calculate tuiton cost for junior and senior engineering CMSE students based on credit
                        credit = input('Credits: ')
                        #test if credit value is an integer greater than 0
                        while not credit.isdigit() or int(credit)<=0: 
                            print('Invalid input. Try again.')
                            credit = input('Credits: ')
                        credit = int(credit)
                        #calculate cost of tuition
                        if credit < 12:
                            cost = credit * 1385.75
                        elif credit <=18:
                            cost = 20786 + 5 + 226 + 670
                        else: 
                            cost = 20786 + 5 + 226 + ((credit-18)*1385.75) + 670
                    else:
                    #calculate tuiton cost for junior and senior engineering students based on credit
                        credit = input('Credits: ')
                        #test if credit value is an integer greater than 0
                        while not credit.isdigit() or int(credit)<=0: 
                            print('Invalid input. Try again.')
                            credit = input('Credits: ')
                        credit = int(credit)
                        #calculate cost of tuition
                        if credit < 12:
                            cost = credit * 1385.75
                        elif credit <=18:
                            cost = 20786 + 5 + 226
                        else: 
                            cost = 20786 + 5 + 226 + ((credit-18)*1385.75)
                elif college == 'health':
                    cmse = input('Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ').lower()
                    if cmse =='yes':
                    #calculate tuiton cost for junior and senior health CMSE students based on credit
                        credit = input('Credits: ')
                        #test if credit value is an integer greater than 0
                        while not credit.isdigit() or int(credit)<=0: 
                            print('Invalid input. Try again.')
                            credit = input('Credits: ')
                        credit = int(credit)
                        #calculate cost of tuition
                        if credit < 12:
                            cost = (credit * 1366.75) + 670
                        elif credit <=18:
                            cost = 20501 + 670 + 5
                        else: 
                            cost = 20501 + ((credit-18) * 1366.75) + 670
                    else:
                        #calculate tuiton cost for junior and senior health students based on credit
                        credit = input('Credits: ')
                        #test if credit value is an integer greater than 0
                        while not credit.isdigit() or int(credit)<=0: 
                            print('Invalid input. Try again.')
                            credit = input('Credits: ')
                        credit = int(credit)
                        #calculate cost of tuition
                        if credit < 12:
                            cost = (credit * 1366.75) + 100
                        elif credit <=18:
                            cost = 20501 + 100 + 5
                        else: 
                            cost = 20501 + ((credit-18)*1366.75) + 100 + 5
                elif college == 'sciences':
                    cmse = input('Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ').lower()
                    if cmse =='yes':
                    #calculate tuiton cost for junior and senior science CMSE students based on credit
                        credit = input('Credits: ')
                        #test if credit value is an integer greater than 0
                        while not credit.isdigit() or int(credit)<=0: 
                            print('Invalid input. Try again.')
                            credit = input('Credits: ')
                        credit = int(credit)
                        #calculate cost of tuition
                        if credit < 12:
                            cost = (credit * 1366.75) + 670
                        elif credit <=18:
                            cost = 20501 + 670 + 5
                        else: 
                            cost = 20501 + ((credit-18) * 1366.75) + 670
                    else:
                        #calculate tuiton cost for junior and senior science students based on credit
                        credit = input('Credits: ')
                        #test if credit value is an integer greater than 0
                        while not credit.isdigit() or int(credit)<=0: 
                            print('Invalid input. Try again.')
                            credit = input('Credits: ')
                        credit = int(credit)
                        #calculate cost of tuition
                        if credit < 12:
                            cost = (credit * 1366.75) + 100
                        elif credit <=18:
                            cost = 20501 + 100 + 5
                        else: 
                            cost = 20501 + ((credit-18)*1366.75) + 100 + 5
                else:
                    cmse = input('Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ').lower()
                    if cmse =='yes':
                    #calculate tuiton cost for junior and senior CMSE students based on credit
                        credit = input('Credits: ')
                        #test if credit value is an integer greater than 0
                        while not credit.isdigit() or int(credit)<=0: 
                            print('Invalid input. Try again.')
                            credit = input('Credits: ')
                        credit = int(credit)
                        #calculate cost of tuition
                        if credit < 12:
                            cost = (credit * 1366.75) + 670
                        elif credit <=18:
                            cost = 20501 + 670 + 5
                        else: 
                            cost = 20501 + ((credit-18) * 1366.75) + 670
                    else:
                        #calculate tuiton cost for junior and senior students based on credit
                        credit = input('Credits: ')
                        #test if credit value is an integer greater than 0
                        while not credit.isdigit() or int(credit)<=0: 
                            print('Invalid input. Try again.')
                            credit = input('Credits: ')
                        credit = int(credit)
                        #calculate cost of tuition
                        if credit < 12:
                            cost = (credit * 1366.75)
                        elif credit <=18:
                            cost = 20501 + 5
                        else: 
                            cost = 20501 + ((credit-18)*1366.75) + 5
                cost = cost + 24 + 750
                #print the final tuition cost with the appropriate format
                if cost >= 1000:
                    comma1 = cost // 1000
                    comma2 = cost % 1000
                    print('Tuition is $%d,%.2f.' %(comma1,comma2))   
                else:
                    print('Tuition is $%.2f.' %(cost))
            else:
                #print the error statement and repeat second loop to the original level question
                print('Invalid input. Try again.')
        else:
            exit
    #repeat the first loop with a prompt        
    calc = input('Do you want to do another calculation (yes/no): ').lower()