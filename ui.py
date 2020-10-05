from database import Artist, Artwork




def menu_option(ui):
        #creates a menu option for the user to choose from
        response_entered = get_non_empty_string('Enter your choice')
        if response_entered in ['task1','task2','task3','task4','task5','task6','q']:
            return response_entered
        print('invalid choice. please choose from one of the tasks above.')


def message(msg):
    #prints message to the user
    print(msg)


def get_non_empty_string(question, max_length=None):
    #checks if a string is empty
    while True:
        user_response = input(f'{question}')
        if user_response:
            return user_response
        print("please enter something. Empty string not allowed")

def get_postive_float(question):
    #checks for positive float
    while True:
        try:
            response = float(input(f'{question}'))
            if response >= 0:
                return response
            else:
                print("please enter postive number")
        except ValueError:
            print('please enter a number') 

def get_email(question):
    #checks for email
    while True:
        response = input(f'{question}')
        if response:
            return response
        print('please enter email address')  
        
def get_name(question):
    #this method asks questions to retrieve name
    while True:
        response = input(f'{question}')
        if response:
            return response
        print('please enter name')

def check_whether_artist_exists(name):
    #checks if artist exists
    try:
        res = Artist.select().where(Artist.name == name).get()
        if res:
            return res.id
        else:
            return None
    except:
        return 'Artist does not exist'                    


def get_artwork_availability():
    #checks for artwork availability
  
    while True:
        response = input('Enter \'availabe\' if artwork is available or \'sold\' if the artwork is not available: ')
        if response.lower() in ['available', 'sold']:
            return response.lower() == 'available'
        else:
            print('Type \'available\' or \'sold\'')

def get_artwork_id():
    #asks for artwork Id
    while True:
        try:
            response = int(input('Enter artwork iD: '))
            if response >= 0:
                return response
            else:
                print("please enter postive number")
        except ValueError:
            print('please enter a number') 

