#Python Capitals and self.countries

class ConCap(object):

	def __init__(self):
		"""Saves in a dictionary"""
		self.countries = {}
		
	def Add(self):
		"""Adds the countries and capitals"""
		user_country = True
		while user_country == True:
			country = raw_input("Enter the Country: ")
			country = country.lower() 
			capital = raw_input("Enter the Capital: ")
			capital = capital.lower()
			if country.isalpha() == True and capital.isalpha() == True:
				self.countries[country] = capital
				repeat = True
				while repeat == True:
					again = raw_input("Do you want to enter another? Y/N: ")
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
			else:
				print "Only letters"

	def menu(self):
		menu = True
		while menu == True:
			print """
			-------------MENU-------------
			Country
			Countries
			Capital
			All
			AllOrdered
			AllMail
			Exit
			------------------------------
			"""
			option = raw_input(">")
			option = option.lower()
			user = True
			while user == True:
				if option.isalpha() == True:
					if option == "country":
						self.Add()
					elif option == "countries":
						print "List of countries"
						for i in self.countries:
							print i
						user = False
					elif option == "capital":
						print "List of Capitals"
						for x in self.countries:
							print self.countries[x]
						user = False
					elif option == "all":
						user = False
					elif option == "allordered":
						user = False
					elif option == "allmail":
						user = False
					elif option == "exit":
						print "Bye Bye"
						user = False
						menu = False
					else:
						print "Only write the above commands"
				else:
					print "Use only letters"
				user = False

PRUEBA = ConCap()
PRUEBA.menu()