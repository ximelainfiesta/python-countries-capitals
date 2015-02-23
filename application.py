#Python Capitals and self.countries

import os
import sys

class ConCap(object):

	def __init__(self):
		"""Saves in a dictionary"""
		self.countries = {}
		
	def Add(self):
		"""Adds the countries and capitals"""
		user_country = True
		while user_country == True:
			country = raw_input("Enter the Country: ")
			country = country.title() 
			capital = raw_input("Enter the Capital: ")
			capital = capital.title()
			try:
				country = float(country)
				country = int(country)
				capital = float(capital)
				capital = int(capital)
				print "Enter valid country and capital"
			except (NameError, ValueError):
				print ""
				if len(country) <= 2 and len(capital) <= 2:
					print "Enter a valid country and capital"
				else:
					self.countries[country] = capital
				repeat = True
				while repeat == True:
					print "Thank you for adding a country with its capital"
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


	def menu(self):
		menu = True
		while menu == True:
			print """
			-----------------------MENU-----------------------
			Country: Add a country with its capital
			Countries: Show countries
			Capital: Show capitals
			All: Show countries with them capitals
			AllOrdered: Show countries with capitals in order
			AllMail: Send email with the list
			Exit: get out
			--------------------------------------------------
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