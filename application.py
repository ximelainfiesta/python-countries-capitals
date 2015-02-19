#Python Capitals and Countries

Countries = {}

class ConCap(object):

	def __init__(self):
		pass
		
	def Add(self):
		"""Adds the countries and capitals"""
		user_country = True
		while user_country == True:
			country = raw_input("Enter the Country: ")
			country = country.lower() 
			capital = raw_input("Enter the Capital: ")
			capital = capital.lower()
			if country.isalpha() == True and capital.isalpha() == True:
				Countries[country] = capital
				menu()
			else:
				print "Only letters"

	def menu():
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
						enter = ConCap()
						enter.Add()


					elif option == "countries":
						print "List of Countries"
						for i in Countries:
							print i
						user = False
					elif option == "capital":
						print "List of Capitals"
						for x in Countries:
							print Countries[x]
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


menu()