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
    #search for first name
    if(searchFor == '1'):
      name = input('Enter First Name: ')
      name = name.capitalize()
      cursor.execute('SELECT * FROM LifePathNumbers WHERE First_Name=?', (name,))
      rows = cursor.fetchall()
      #check if rows is empty
      if(bool(rows) == False):
       print('Sorry not in records')
      for row in rows:
       print(row)
    #search for last name
    elif(searchFor == '2'):
      name = input('Enter Last Name: ')
      name = name.capitalize()
      cursor.execute('SELECT * FROM LifePathNumbers WHERE Last_Name=?', (name,))
      rows = cursor.fetchall()
      if(bool(rows) == False):
       print('Sorry not in records')
      for row in rows:
       print(row)
    #search for life path number
    elif(searchFor == '3'):
      num = input('Enter Life Path Number: ')
      cursor.execute('SELECT * FROM LifePathNumbers WHERE Life_Path_Number=?', (num,))
      rows = cursor.fetchall()
      if(bool(rows) == False):
       print('Sorry not in records')
      for row in rows:
       print(row)
    #reruns function if incorrect input
    else:
      print('Invalid Input')
      searchUser()

#adding digits function
def digitSum(num):
    
    #indexs the num for how many digits it has
    indexDigits = [int(i)  for i in str(num)]

    #if/elif statements to add number indexs together
    if(len(indexDigits) == 1):
        return indexDigits[0]
    
    #sum for day, month, year
    elif(len(indexDigits) == 2):
        return indexDigits[0] + indexDigits[1]
    
    #sum for year variable
    elif(len(indexDigits) == 4):
        return indexDigits[0] + indexDigits[1] + indexDigits[2] + indexDigits[3]
    

def monthInput():
   
   #flags for validating data
   validMonth = False
   
   #prompt for birth month
   birthMonth = input('Birth Month(1-12):\n')
   while(validMonth == False):

    #checks if the input is a digit
    if(birthMonth.isdigit() == False):
       birthMonth = input('Invalid input. Please enter a month between 1-12.\n')
    birthMonth = int(birthMonth)

    #checks if the number is within the range
    if(birthMonth < 1 or birthMonth > 12):
     birthMonth = input('Invalid input. Please enter a month between 1-12.\n')
    elif(birthMonth > 0 or birthMonth < 13):
     validMonth = True
     birthMonth = str(birthMonth)
   return birthMonth

def dayInput():
   
   #flag for validating data
   validDay = False

  #prompt for birth day
   birthDay = input('Birth Day(1-31):\n')
   while(validDay == False):

    #checks if the input is a digit
    if(birthDay.isdigit() == False):
       birthDay = input('Invalid input. Please enter a day between 1-31.\n')
    birthDay = int(birthDay)

    #checks if the number is within the range
    if(birthDay < 1 or birthDay > 31):
     birthDay = input('Invalid input. Please enter a day between 1-31.\n')
    elif(birthDay > 0 or birthDay < 32):
     validDay = True
     birthDay = str(birthDay)
   return birthDay
   

def yearInput():
   
   #flag for validating data
   validYear = False

  #prompt for birth year
   birthYear = input('Birth Year(1899-2100):\n')
   while(validYear == False):

    #checks if the input is a digit
    if(birthYear.isdigit() == False):
       birthYear = input('Invalid input. Please enter a year between 1899-2100.\n')
    birthYear = int(birthYear)

    #checks if the number is within the range
    if(birthYear < 1899 or birthYear > 2100):
     birthYear= input('Invalid input. Please enter a year between 1899-2100.\n')
    elif(birthYear > 1898 or birthYear < 2101):
     validYear = True
     birthYear = str(birthYear)
   return birthYear

#add the month day and year numbers together
def totalNumSum():
  print('\nPlease enter your birthday in the order month | day | year\n')
  month = monthInput()
  day = dayInput()
  year = yearInput()
  total = digitSum(month) + digitSum(day) + digitSum(year)
  return total
  
#determines if a num is a double number or if it is a regular life path number
def lifePathNum():
  num = totalNumSum()
  if(num == 11):
    finalNum = 11
  elif(num == 22):
    finalNum = 22
  elif(num == 33):
    finalNum = 33
  else:
    finalNum = digitSum(num)
  return finalNum

#dictionary stores filenames with correlating life path number as values
fileNames = dict()
keys = ['Life Path 1.txt','Life Path 2.txt','Life Path 3.txt','Life Path 4.txt','Life Path 5.txt',
'Life Path 6.txt','Life Path 7.txt','Life Path 8.txt','Life Path 9.txt','Life Path 11.txt','Life Path 22.txt','Life Path 33.txt']
values = [1,2,3,4,5,6,7,8,9,11,22,33]

#add key/values to dictionary
for i in range(len(keys)):
    fileNames[keys[i]] = values[i]


#function to open file to life path information
def openFile(num):
  try:
   #create lists of values and keys from dictionary
   key_list = list(fileNames.keys())
   val_list = list(fileNames.values())
  
   #indexes the values
   num = int(num)
   position = val_list.index(num)

   #returns the file requested
   File = open(key_list[position], 'r' )
   print('\n' + File.read())

  except:
   print('life path number does not exist')
  
#function for main menu selection
def optionSelection():
  print(mainMenu)
  selection = input()

  #menu selection
  if(selection == '1'):
    addOptionSelection()
  elif(selection == '2'):
    viewOptionSelection()
  else:
    print('Invalid input.')
    optionSelection()
    
#function for add menu selection
def addOptionSelection():
  #validSelection = False
  print(addMenu)
  selection = input()
  
  
  if(selection == '1'):
     print('Add life path number entry')
     exit = ''
     
     while(exit != 'x'):
      firstName = input('Enter first name: \n')

      #valididates name input
      while(firstName.isalpha() == False):
        firstName = input('Invalid input. Please enter your first name\n')
      
      lastName = input('Enter last name: \n')
      while(lastName.isalpha() == False):
        lastName = input('Invalid input. Please enter your last name\n')

      #validates number input
      num = input('Enter life path number: \n')

      while(num.isdigit() == False):
       num = input('Invalid Input. Please enter a number. (1-9,11,22,33)\n')
       if(num.isdigit() == True):
            break
       num = int(num)

      #add life path number
      cursor.execute('INSERT INTO LifePathNumbers(First_Name,Last_Name, Life_Path_Number) VALUES(?,?,?)', (firstName.capitalize(),lastName.capitalize(), num))
      connection.commit()
      
      exit = input('Press x to exit or Enter to continue ')

  elif(selection == '2'):
     print( 'Find and add life path number entry')
     exit = ''
     while(exit != 'x'):
      num = lifePathNum()
      num = str(num)
      print('Life Path Number: ' + num)

      firstName = input('Enter first name: \n')

      #valididates firstName input
      while(firstName.isalpha() == False):
        firstName = input('Invalid input. Please enter your first name\n')
      
      #validates lastName input
      lastName = input('Enter last name: \n')
      while(lastName.isalpha() == False):
        lastName = input('Invalid input. Please enter your last name\n')
     
     #adds to dictionary
      cursor.execute('INSERT INTO LifePathNumbers(First_Name,Last_Name, Life_Path_Number) VALUES(?,?,?)', (firstName.capitalize(),lastName.capitalize(), num))
      connection.commit()

     #displays life path number info 
      openFile(num)

      exit = input('\nPress x to exit or Enter to continue ')
  elif(selection == 'x'):
     optionSelection()
  else:
    addOptionSelection()
   

#function for add menu selection
def viewOptionSelection():
  print(viewMenu)
  selection = input()
  
  if(selection == '1'):
     print('View user')
     user = ''
     while(user != 'x'):
      searchUser()
      user = input('\nPress x to exit or Enter to continue ')

  elif(selection == '2'):
     print('View life path numbers')
     num = ''
     while(num != 'x'):
      num = input('\nWhich life path number would you like information on? Press x to exit\n')
      if(num == 'x'):
        break
      num = int(num)
      print('\n')
      openFile(num)
     
  elif(selection == '3'):
     print('View dictionary')
     cursor.execute('SELECT * FROM LifePathNumbers')
     for row in cursor.fetchall():
      print(row)

  elif(selection == '4'):
     print('Find your life path number')
     num = ''
     while(num != 'x'):
      num = lifePathNum()
      if(num == 'x'):
       break
      num = str(num)
      print('Your life path number: ' + num)
      num = input('Press x to exit or Enter to continue\n')
  elif(selection == 'x'):
     optionSelection()
  else:
    viewOptionSelection()

#decision ladder
options = ''
while(options != 'x'):
  
  optionSelection()
 
  exitStatement = '''\nExit program press x.
Main Menu option press 1.
Add Menu option press 2.
View Menu option press 3.
'''

  options = input(exitStatement)

  if(options == 'x'):
   cursor.close()
   connection.close()
   break
  elif(options == '1'):
    optionSelection()
  elif(options == '2'):
    addOptionSelection()
  elif(options == '3'):
    viewOptionSelection()