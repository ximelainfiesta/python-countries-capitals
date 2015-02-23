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
            country = country.title() #capitalizes the asnwer
            capital = raw_input("Enter the Capital: ")
            capital = capital.title()
            try:
                country = float(country) #tries to convert this into numbers, to verifiy letters
                country = int(country)
                capital = float(capital)
                capital = int(capital)
                print "Enter valid country and capital"
            except (NameError, ValueError):
                print ""
                if len(country) <= 2 and len(capital) <= 2: #verifies lenght of the answer
                    print "Enter a valid country and capital"
                elif country.isalnum() == True and capital.isalnum() == True: #verifies that the answer has alfanumeric answer
                    print "Enter only letters"
                else:
                    self.countries[country] = capital #adds the capital and country to the dictionary
                repeat = True
                while repeat == True:
                    print "Thank you for adding a country with its capital"
                    again = raw_input("Do you want to enter another? Y/N: ") #asks to enter another
                    again = again.lower()
                    try:
                        if again == "y":
                            repeat = False
                            user_country = True
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
                            print i
                        user = False
                    elif option == "capital":
                        print "List of Capitals"
                        for i in self.countries:
                            print self.countries[i]
                        user = False
                    elif option == "all":
                        print "List of all countries with capitals"
                        user = False
                    elif option == "allordered":
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
