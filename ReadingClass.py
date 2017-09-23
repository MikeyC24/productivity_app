# goal is to have a list of books/articles/textbooks/etc to read
# workin progress section
# finished section
# goals/planning section

import pandas as pd
import numpy as np
import sqlite3
import datetime
import matplotlib.pyplot as plt

class ReadingClass:

	def __init__(self, db_location):
		self.db_location = db_location
		

	def user_menu(self):
		print('''Welcome to the reading class of this App. Here you can look at previosuly
read items, check target list and goals, and see where you are currently at. Enter 1 to add
a book or reading to target list. Enter 2 to move a new book to current read section. Enter
3 to input a book into finished list. Enter 4 to add and update your goals. Enter 999
to quit.''')
		menu_input = 0
		while menu_input != 999:
			# gonna need to add something to resee menu
			#try:
			menu_input = int(input('please enter selection(999 to quit): '))
			if menu_input == 1:
				print('add books')
				self.add_readings()
			elif menu_input ==  2:
				print('current reads')
			elif menu_input == 3:
				print('input book to finished list')
			elif menu_input == 4:
				print('add and update goals')
			elif menu_input == 999:
				pass
			else:
				print('That was not a recongized command')
			#except Exception as e:
			#	print('That command was not reconigzed, are you sure it was a number')
		else:
			print('goodbye')


	def add_readings(self):
		print('''You will be prompted a series of questions to enter your information. The reading/book
title, author and page numbers are mandatory, the genre, and reason for reading is optional.''')
		title_array = []
		author_array = []
		number_pages_array = []
		genre_array = []
		reason_read_array = []
		df = None
		user_input = None
		user_input = input('enter back to go to main menu, otherwise click any button to continue: ').lower()
		while user_input != 'back':
			try:
				title = input('Please enter the name of the book, be case sensitive: ')
				if len(title) < 0:
					print('cant be empty')
					raise ValueError()
				author = input('''Please enter the author, be case sensitive. If there is
more than one author, enter a comma after each auther: ''')
				if len(author) < 0:
					print('cant be empty')
					raise ValueError()
				number_pages = int(input('Please enter the number of pages: '))
				check = isinstance(number_pages, int)
				print(check)
				if check is False:
					print('not a number')
					raise ValueError()
				genre = 'None entered'
				genre = input('Please enter the genre: ')
				reason_read = 'None Entered'
				reason_read = input('please enter the reason for reading: ')
				title_array.append(title)
				author_array.append(author)
				number_pages_array.append(number_pages)
				genre_array.append(genre)
				reason_read_array.append(reason_read)
			except Exception as e:
				print('hit error,', e)
			user_input = input('''press any key to add another item, type back to go to main menu
 and type add to add to database: ''')
			if user_input == 'add':
				df = pd.DataFrame({'Title': title_array, 'Author':author_array, 
					'Number of Pages': number_pages_array, 'Genre': genre_array, 
					'Reason for reading': reason_read_array})
				print(df.head())
				user_input = 'back'

db_location = '/home/mike/Documents/coding_all/productivity_app/'
reading = ReadingClass(db_location)
reading.user_menu()

'''
not raising errors as it should
'''