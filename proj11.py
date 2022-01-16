###########################################################
    #  CSE 231 Project #11
    #
    #  Classes and Methods
    #    import class file
    #       read for certain values in the class
    #    output appropriate value in the functions
    #       call appropriate functions
    #    display closing message
    #
    ###########################################################

MAP = {"U":"Up","D":"Down","L":"Left","R":"Right"}

class Student(object):
    ''' This class shows a student that knows the id of the room they are currently in and has a list of the inventory '''
    def __init__(self, item_list=None, classroom_id=-1):
        '''Initializes yourself, with an empty backpack by default. The default position of the student is room -1.'''

        if item_list == None:
            self.backpack = []
        else:
            self.backpack = item_list
        self.classroom_id = classroom_id

    def __repr__(self):
        '''Returns a string representation of the student.'''

        return self.__str__()

    def __str__(self):
        '''Returns a string representing the student's inventory.'''
        s = "Backpack: "
        if len(self.backpack) == 0:
            s += "Empty"
        else:
            for item in self.backpack:
                s += item + ", "
            else:
                s = s[:-2] # remove trailing comma and space
        return s

    def __eq__( self, S ):
        ''' Checks if Student‘s classroom id and backpack are equal to S '''
        #check if student info is equal to S and return True or False
        if self.classroom_id == S.classroom_id and self.backpack == S.backpack:
            return True
        else:
            return False
     
    def place(self, classroom_id):
        ''' Places the student in a classroom with the ID '''
        self.classroom_id = classroom_id
        
    def add_item(self, item):
        ''' Add up to six items to the backpack list '''
        #if length is not yet 6, add items to the backpack
        if len(self.backpack) == 6:
            print("Backpack is full.")
        else:
            self.backpack.append(item)
            
    def remove_item(self, item):
        ''' Remove item from the backpack list '''
        #check if item is in the backpack and remove it
        if item in self.backpack:
            self.backpack.remove(item)
        else:
            print("Failed to remove item from backpack.")
            
class Classroom(object):
    ''' This class represents a single classroom with a unique id, int, and course '''
    def __init__(self, text_desc="0 empty"):
        '''Initialzes a classroom. By default it has id 0 and is a "empty" room with no inventory or exits.'''
        description = text_desc.split()

        self.id = int(description[0])
        self.course = description[1] 

        # Initialize a dictionary of potential exits as empty
        self.exits = {}

        # Initialize a "backpack" of items as empty list
        self.backpack = []
        
        #iterate through each item in the description
        for item in description:
            #if no item, continue
            if item == 'empty':
                continue
            else:
                #define correct direction and items
                correct = 'UDLR'
                first = item[0]
                items = item[1:]
                #if item is alphabet add to backpack
                if first.islower() == True:
                    self.backpack.append(item) 
                #if 
                elif first in correct:
                    self.exits[first] = int(items)

    def __repr__(self):
        '''Returns a string representation of the classroom.'''
        classroom_repr = '''Classroom("''' + repr(self.id) + " " + self.course

        for direction in self.exits:
            classroom_repr += " {}".format(direction) + repr(self.exits[direction])

        for item in self.backpack:
            classroom_repr += " " + item

        classroom_repr += '''")'''

        return classroom_repr

    def __str__(self):
        ''' This method returns a string representing the room in a nice conversational style '''

        # Basic classroom description
        classroom_str = "You see a " + self.course + " classroom."

        # List the things in the classroom
        if len(self.backpack) == 1:
            classroom_str += " On the desk you see a " + \
                             self.backpack[0] + "."
        if len(self.backpack) == 2:
            classroom_str += " On the desk you see a " + \
                             self.backpack[0] + \
                             " and a " + self.backpack[1] + "."
        elif len(self.backpack) > 2:
            classroom_str += " On the desk you see "
            for item in self.backpack[:-1]:
                classroom_str += "a " + item + ", "
            classroom_str += "and a " + self.backpack[-1] + "."

        # List the exits
        if len(self.exits) == 0:
            classroom_str += " Run through the classroom grab what you need (if possible). Exit and run to the exam!"
        elif len(self.exits) == 1:
            classroom_str += " Run through the classroom grab what you need (if possible). Now, run into the hallway and go " + \
                             MAP[list(self.exits.keys())[0]] + "."
        elif len(self.exits) == 2:
            classroom_str += " Run through the classroom grab what you need (if possible). Now, run into the hallway and go " + \
                             MAP[list(self.exits.keys())[0]] + " or " + MAP[list(self.exits.keys())[1]] + "."
        elif len(self.exits) > 2:
            classroom_str += " Run through the classroom grab what you need (if possible). Now, run into the hallway and go "
            for direction in list(self.exits.keys())[:-1]:
                classroom_str += MAP[direction] + ", "
            classroom_str += "or " + MAP[list(self.exits.keys())[-1]] + "."

        return classroom_str
    
    def __eq__( self, C ):
        ''' This method checks if Classroom id, course, exits and backpack are equal to C '''
        #check if classroom info is equal to C and return True or False
        if self.id == C.id and self.backpack == C.backpack and self.exits == C.exits and self.course == C.course:
            return True
        else:
            return False
    
    def add_item(self, item):
        ''' This method adds item to the backpack '''
        self.backpack.append(item)

    def remove_item(self, item):
        ''' Remove item from the backpack list '''
        #check if item is in the backpack and remove it
        if item in self.backpack:
            self.backpack.remove(item)
        else:
            print('Failure to find the item in the classroom.')

    def get_room(self, direction):
        ''' This method checks if room id exists and returns it '''
        if direction in self.exits:
            return self.exits[direction]
        else:
            return False

class Rush(object):
    ''' This class is responsible for interactions between user, character, and rooms '''
    def __init__(self, filename="rushing.txt"):
        '''Initializes the student rushing to class.  The student starts in the classroom with the lowest id.'''

        # First make a student start with an empty inventory
        self.student = Student()

        # Create classrooms are an empty dictionary
        self.classrooms = {}
        
        # Now read the file to get the classroom lines
        fp = open(filename,'r')
        #iterate through the file and split each line as a string
        for file_line in fp:
            final_line = str(file_line).split()
            #add the first number to the classroom dictionary
            self.classrooms[int(final_line[0])] = Classroom(file_line)
    
        # Place the student in the room with lowest id
        self.student.place(min(self.classrooms.keys()))

    def __repr__(self):
        '''Returns a string representation.'''

        return self.__str__()

    def __str__(self):
        '''Returns a string representing the journey to the class, simply giving the number of rooms.'''
        search_str = "You are searched in "
        if len(self.classrooms) == 0:
            search_str += "no classrooms at all, you are in the hallway. You are late run in a random class and get items from the desks."
        elif len(self.classrooms) == 1:
            search_str += "a classroom."
        else:
            search_str += "a set of " + str(len(self.classrooms)) + \
                          " classrooms."
        return search_str

    def intro(self):
        '''Prints an introduction to the search for items because you are late
        This prompt includes the commands.'''
        print("\nAHHHH! I'm late for class\n")
        print("*runs out the house to catch the bus with an empty backpack*")

        print("\nYou're popular and have friends in many classes. Find and collect any items you find useful for your exam.")
        print("You are already late, and have a CSE231 Final Exam in 10 mins.\n")
        self.print_help()

    def print_help(self):
        '''Prints the valid commands.'''
        print("Use your instincts: ")
        print("*thinks*.. *thinks*.. what to do?!?!?!?!")
        print("*running*")
        print("S or search -- prints a description of the classroom you ran into")
        print("B or backpack - prints a list of items in your backpack")
        print("P pencil or pickup pencil - *mental* instruction to pick up an item called pencil")
        print("DR pencil or drop pencil - *mental* instruction to drop off an item called pencil")
        print("U or up - *mental* instruction to up the hallway to find another classroom")
        print("D or down - *mental* instruction to down the hallway to find another classroom")
        print("R or right - *mental* instruction to right in the hallway to find another classroom")
        print("L or left - *mental* instruction to left in the hallway to find another classroom")
        print("G or giveup - I have no more time, I need to get to class!!!")
        print("H or help - prints this list of options again")
        print()
        print("Remember that uppercase and lowercase SHOULD NOT matter. ")
        print("JUST GRAB WHAT YOU NEED AND GET TO CLASS TO START YOUR FINAL EXAM!!! HURRYYYY!!!")
        print()

    def prompt(self):
        '''Prompts for input and handles it, whether by error message or handling a valid command.
        Returns True as long as the user has not chosen to quit, False if they have.'''

        print("In room {} with course {}".format(self.student.classroom_id,self.classrooms[self.student.classroom_id].course))
        print(self.student)
        user_input = input("Enter a command (H for help): ")
        print()

        # Handle input: split for pickup/drop, capitalization unimportant for commands
        input_list = user_input.split()

        if len(input_list) == 0:
            user_input = "?"  # No command is not a valid command
            return False
        else:
            try:
                command = input_list[0].upper()  # The command
                if len(input_list) > 1:
                    item = input_list[1]
                if command == 'S':
                    self.search()
                elif command == 'B':
                    self.backpack()
                elif command == 'P':
                    self.pickup(item)
                elif command == 'DR':
                    self.drop(item)
                elif command in "UDLR":
                    self.move(command)
                elif command == 'G':
                    print("I have no more time, I need to get to class!!!")
                    return False
                elif command == 'H':
                     self.print_help() 
                else:
                    print("Unfortunately, that's not a valid option.")
                    return False
            except:
                print("Problem with the option or the item.")
                return False
        if self.win():
            return "win"
        return True

    def search(self):
        '''Prints the description of the current room.'''
        current_classroom = self.classrooms[self.student.classroom_id]
        print(current_classroom)

    def backpack(self):
        ''' This method prints the items in the backpack '''
        print(self.backpack)
    
    def pickup(self, item):
        '''
            WRITE DOCSTRING HERE!
        '''
    
        pass
            
    
    def drop(self, item):
        '''
            WRITE DOCSTRING HERE!
        '''
    
        pass

    def move(self, direction):
        '''
            WRITE DOCSTRING HERE!
        '''
    
        
        print("You went " + MAP[direction] + " and found a new classroom.")
        errMsg = "Unfortunately, you went " + MAP[direction] + " and there was no classroom."
        print(errMsg)
        pass

    def win(self):
        ''' This method checks if the class is CSE 231 and has a correct backpack '''
        winning_backpack = ['cheatsheet', 'eraser', 'paper', 'pencil']
        #define the course selected
        course = self.student.classroom_id
        #check if the course in the classroom is CSE 231 and items in students's backpack are correct
        if self.classrooms[course].course == 'CSE 231':
            for i in self.student.backpack:
                if i not in winning_backpack:
                    return False
        else:
            return False
        return True

def main():
    '''
    Prompts the user for a file, then plays that file until the user chooses to give up.
    Does not check formatting of input file.
    '''

    while True:
        try:
            filename = input("Enter a text filename: ")
            escapade = Rush(filename)
            break
        except IOError:
            print("Cannot open file:{}. Please try again.".format(filename))
            continue
    
    escapade.intro()
    escapade.__str__()
    escapade.search()
    
    keep_going = True
    while keep_going:
        keep_going = escapade.prompt()
        if keep_going == 'win':
            break
    if keep_going == 'win':
        print("You succeeded!")
    else:
        print("Thank you for playing")

if __name__ == "__main__":    
    main()