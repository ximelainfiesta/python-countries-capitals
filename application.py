# -*- coding: utf-8 -*

"""COUNTRIES AND CAPITALS """


import sys #imports some functions like the one to end program
enc = sys.stdin.encoding


import smtplib #modules to send email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


class ConCap(object):
    """ This Program saves in a dictionary, countries with capitals """

    def __init__(self):
        """Saves in a dictionary"""
        self.countries = {}
        #a dictionary with self

    def add(self):
        """adds the countries and capitals"""
        user_country = True #variable to repeat or stop the loop
        while user_country == True:
            country = raw_input("Enter the Country: ").decode(enc)
            country = country.title()
            try:
                text = country #turn into a string
                variable = True #another variable to verify
                for i in text:
                    if i.isalpha() == True or i == " ": #if the string is alfhabet
                        if variable == True: #if variable is true
                            variable = True #make it true
                    else:
                        variable = False #else, make it false
                if variable == False: #if variable is false
                    print "Do not enter numbers" #print message
                    user_country = True
                    #convert the original variable in true so it can repeat itself
                else:
                    user_country = False #if not, kill this part and go on
            except (ValueError, NameError, SyntaxError):
                print "-Do not enter numbers" #just verifies, any possible mistake
        user_capital = True #everything above
        while user_capital == True:
            capital = raw_input("Enter the Capital: ").decode(enc)
            capital = capital.title()
            try:
                text = capital
                variable = True
                for i in text:
                    if i.isalpha() == True or i == " ":
                        if variable == True:
                            variable = True
                    else:
                        variable = False
                if variable == False:
                    print "Do not enter numbers"
                    user_capital = True
                else:
                    user_capital = False
            except (ValueError, NameError, SyntaxError):
                print "-Do not enter numbers"
# I must keep close attention to identation, when they stop verifying
#they will add them to the dictionary
        self.countries[country] = capital
        print "Thank you for adding a country with its capital"
#This whole part verifies if the user wants to add another
        repeat = True  #variable to kill
        while repeat == True:
            again = raw_input("Do you want to enter another? Y/N: ") #asks to enter another
            again = again.lower()
            try:
                if again == "y":
                    self.add() #it ifs yes, it returns
                elif again == "n":
                    repeat = False #if no, kills this part
                    user_country = False #kills the other variable above
                    self.menu() #goes to the menu
                else:
                    print "Enter only Y or N"
            except ValueError:
                print "Only letter Y or N"

    def email(self): #method copied from internet
        """send email with the countries and capitals."""
        username = "ximena.lainfiesta@gmail.com"
        password = "saSA12!@"
        adress = "lgarcia@cognits.co"
        body = "Countries and Capitals: "

        # Body of email
        for key, item in self.countries.items():
            body += """
            """ + str(key) + " - " + str(item)

        # Forming the body of email
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = adress
        msg['Subject'] = "Countries and capitals by Ximena Lainfiesta"
        msg.attach(MIMEText(body, 'plain'))

        # This try controls if the email was sent
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(username, password)
            text = msg.as_string()
            server.sendmail(username, adress, text)
            server.quit()
            print "Email sent correctly"
            raw_input("Press enter to continue...")
        except:
            print "Error ocurred"

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
            user = True #variable to kill
            while user == True:
                if option.isalpha() == True: #if the answer is in letters
                    if option == "country":
                        self.add() #calls the method to add a country
                    elif option == "countries":
                        print "List of countries"
                        for i in self.countries: #lists the countries
                            print "-", i #prints a dash and the countries
                        user = False #kills the operation to return to the menu
                    elif option == "capital":
                        print "List of Capitals"
                        for i in self.countries:
                            print "-", self.countries[i] #prints a dash and the items
                        user = False #kills the operation to return to the menu
                    elif option == "all":
                        print "List of all countries with capitals"
                        for i in self.countries:
                            print i, "-", self.countries[i] #prints the keys, dash and the items
                        user = False #kills the operation to return to the menu
                    elif option == "allordered":
                        print "List of all countries with capitals in order"
                        for key, value in sorted(self.countries.iteritems(), key=lambda (k, v): (v, k)):
                            print "%s - %s" % (key, value)#internet way to sort a dic by its values
                        user = False #kills the operation to return to the menu
                    elif option == "allmail":
                        self.email()
                        user = False #kills the operation to return to the menu
                    elif option == "exit":
                        print "Bye Bye"
                        sys.exit() #command to exit the program
                    else:
                        print "Only write the above commands"
                else:
                    print "Use only letters"
                user = False #if the program gets in a loop, it stops it


PRUEBA = ConCap()
PRUEBA.menu()
