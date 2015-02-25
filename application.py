#Python Capitals and self.countries
"""COUNTRIES AND CAPITALS """

import sys #imports some functions like the one to end program

class ConCap(object): 
    """ This Program saves in a dictionary, countries with capitals """

    def __init__(self):
        """Saves in a dictionary"""
        self.countries = {} #a dictionary with self

    def add(self):
        """adds the countries and capitals"""
        user_country = True
        while user_country == True:
            country = raw_input("Enter the Country: ")
            try:
                text = country
                for i in text:
                    if i.isalpha() == True or i == " ":
                        user_country = False
                    else:
                        print "Do not enter numbers"
            except:
                user_country = True
        user_capital = True
        while user_capital == True:
            capital = raw_input("Enter the Capital: ")
            try:
                text = capital
                for i in text:
                    if i.isalpha() == True or i == " ":
                        user_capital = False 
                    else: 
                        print "Do not enter numbers"
            except:
                user_capital = True
            self.countries[country] = capital
            print "Thanks for adding"

            repeat = True
            while repeat == True:
                again = raw_input("Do you want to enter another? Y/N: ") #asks to enter another
                again = again.lower()
                try:
                    if again == "y":
                        self.add()
                    elif again == "n":
                        repeat = False
                        user_country = False
                        self.menu()
                    else:
                        print "Enter only Y or N"
                except ValueError:
                    print "Only letter Y or N"

    def menu(self):
        """Runs the program with a menu """
        menu = True
        while menu == True:
            print """
-----------------------MENU-----------------------
Country: add a country with its capital
Countries: Show countries
Capital: Show capitals
All: Show countries with them capitals
AllOrdered: Show countries with capitals in order
AllMail: Send email with the list
Exit: ends the program
--------------------------------------------------
"""
            option = raw_input(">")
            option = option.lower()
            user = True
            while user == True:
                if option.isalpha() == True:
                    if option == "country":
                        self.add()
                    elif option == "countries":
                        print "List of countries"
                        for i in self.countries:
                            print "-", i
                        user = False
                    elif option == "capital":
                        print "List of Capitals"
                        for i in self.countries:
                            print "-", self.countries[i]
                        user = False
                    elif option == "all":
                        print "List of all countries with capitals"
                        for i in self.countries:
                            print i, "-", self.countries[i]
                        user = False
                    elif option == "allordered":
                        print "List of all countries with capitals in order"
                        user = False
                    elif option == "allmail":
                        user = False
                    elif option == "exit":
                        print "Bye Bye"
                        sys.exit()
                    else:
                        print "Only write the above commands"
                else:
                    print "Use only letters"
                user = False

PRUEBA = ConCap()
PRUEBA.menu()
