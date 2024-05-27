#Final Project
#Caleb VanDong
#CS125
#4/18

#import sql library
import sqlite3

#create a connection to sql database
connection = sqlite3.connect('Life Path Database.db')
cursor = connection.cursor()
#cursor.execute('CREATE TABLE IF NOT EXISTS LifePathNumbers(First_Name TEXT,Last_Name TEXT, Life_Path_Number INTEGER)')

#string variables(program name)
programName = 'Life Path Number Program \n'

#what the program does
programDescription = '''This program can tell you about yourself 
based on your life path number
which is determied by your birthday. \n'''

#main menu options
mainMenu = '''Options: \n
(1)Add: 
     select 1 if adding a user to the database\n
(2)View: 
     select 2 to view further options for viewing
'''
#view menu options
viewMenu = '''\nView Options:\n
(1)View user: 
     select 1 to view a person's life path number\n
(2)View life path number: 
     select 2 to view life path number info\n
(3)View dictionary: 
     select 3 to view all user entries\n
(4)Find your life path number: 
     select 4 to find your life path number \n
Press x to exit
'''

#add menu options
addMenu = '''\nAdd Options:\n
(1)Add life path number entry
     select 1 if life path number is known\n
(2)Find and add life path number entry
     select 2 if life path number is unknown\n
Press x to exit
'''

#print name & description
print(programName)
print(programDescription)

#function to search for users through the database
def searchUser():
    searchFor = input('''What would you like to search?
Press 1 for first name
Press 2 for last name
Press 3 for life path number
''')
    #search for 1, 2, or 3 corresponding with the options above, field directs the sql lookup to which field to look in
    if searchFor in ['1', '2', '3']:
        field = ['First_Name', 'Last_Name', 'Life_Path_Number'][int(searchFor) - 1]
        name = input(f'Enter {field.replace("_", " ")}: ').capitalize()
        cursor.execute(f'SELECT * FROM LifePathNumbers WHERE {field}=?', (name,))
        rows = cursor.fetchall()
        if not rows:
            print('Sorry not in records')
        for row in rows:
            print(row)
    else:
        print('Invalid Input')
        searchUser()

#adding digits function
def digitSum(num):
    
    #indexs the num for how many digits it has
    indexDigits = [int(i)  for i in str(num)]

    #if/elif statements to add number indexs together
    if len(indexDigits) == 1:
        return indexDigits[0]
    
    #sum for day, month, year
    elif len(indexDigits) == 2:
        return indexDigits[0] + indexDigits[1]
    
    #sum for year variable
    elif len(indexDigits) == 4:
        return sum(indexDigits)

#function to have the user enter their birth data, min_val and max_val determined in totalNumSum for the specific min and max values
def birthInput(prompt, min_val, max_val):
    validInput = False
    while not validInput:
        user_input = input(prompt)
        if user_input.isdigit() and min_val <= int(user_input) <= max_val:
            validInput = True
    return user_input

#add the month day and year numbers together
def totalNumSum():
    print('\nPlease enter your birthday in the order month | day | year\n')
    month = birthInput('Birth Month(1-12):\n', 1, 12)
    day = birthInput('Birth Day(1-31):\n', 1, 31)
    year = birthInput('Birth Year(1899-2100):\n', 1899, 2100)
    total = digitSum(month) + digitSum(day) + digitSum(year)
    return total
  
#determines if a num is a double number or if it is a regular life path number
def lifePathNum():
  num = totalNumSum()
  finalNum = num if num in [11, 22, 33] else digitSum(num)
  return finalNum

#dictionary sets filenames to the number finalNum 
fileNames = {
    'Life Path 1.txt': 1, 'Life Path 2.txt': 2, 'Life Path 3.txt': 3,
    'Life Path 4.txt': 4, 'Life Path 5.txt': 5, 'Life Path 6.txt': 6,
    'Life Path 7.txt': 7, 'Life Path 8.txt': 8, 'Life Path 9.txt': 9,
    'Life Path 11.txt': 11, 'Life Path 22.txt': 22, 'Life Path 33.txt': 33
}

#function to open file to life path information
def openFile(num):
    filename = f'Life Path {num}.txt'
    try:
        with open(filename, 'r') as file:
            print('\n' + file.read())
    except FileNotFoundError:
        print('Life path number information not found')
  
#function for main menu selection
def optionSelection():
  print(mainMenu)
  selection = input()

  #menu selection
  if selection == '1':
    addOptionSelection()
  elif selection == '2':
    viewOptionSelection()
  else:
    print('Invalid input.')
    optionSelection()
    
#function for add menu selection
def addOptionSelection():
   print(addMenu)
   selection = input()
    if selection == '1':
        while True:
            firstName = input('Enter first name: \n').capitalize()
            lastName = input('Enter last name: \n').capitalize()
            num = input('Enter life path number: \n')
            if num.isdigit() and int(num) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33]:
                cursor.execute('INSERT INTO LifePathNumbers(First_Name,Last_Name, Life_Path_Number) VALUES(?,?,?)',
                               (firstName, lastName, num))
                connection.commit()
                break
            else:
                print('Invalid Input. Please enter a number. (1-9,11,22,33)')
        print(f'Added {firstName} {lastName} with life path number {num}')
    elif selection == '2':
        num = lifePathNum()
        firstName = input('Enter first name: \n').capitalize()
        lastName = input('Enter last name: \n').capitalize()
        cursor.execute('INSERT INTO LifePathNumbers(First_Name,Last_Name, Life_Path_Number) VALUES(?,?,?)',
                       (firstName, lastName, num))
        connection.commit()
        print(f'Added {firstName} {lastName} with life path number {num}')
        openFile(num)
    elif selection != 'x':
        addOptionSelection()
   

#function for add menu selection
def viewOptionSelection():
    print(viewMenu)
    selection = input()
    if selection == '1':
        searchUser()
    elif selection == '2':
        num = input('\nWhich life path number would you like information on? Press x to exit\n')
        if num.isdigit():
            openFile(int(num))
    elif selection == '3':
        cursor.execute('SELECT * FROM LifePathNumbers')
        for row in cursor.fetchall():
            print(row)
    elif selection == '4':
        num = lifePathNum()
        print('Your life path number: ' + str(num))
    elif selection != 'x':
        viewOptionSelection()

#option loop allows the user to stay inside the program
options = ''
while options != 'x':
    optionSelection()
    options = input('\nExit program press x.\nMain Menu option press 1.\nAdd Menu option press 2.\nView Menu option press 3.\n')

cursor.close()
connection.close()