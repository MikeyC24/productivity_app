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

	database_name = 'user_reading_database'
	user_book_list = 'user_book_list'
	current_read_table = 'current_read_table'

	def __init__(self, db_location):
		self.db_location = db_location
		

	def user_menu(self):
		print('''Welcome to the reading class of this App. Here you can look at previosuly
read items, check target list and goals, and see where you are currently at. Enter 1 to add
a book or reading to target list. Enter 2 to move a new book to current read section and/or
update goals. Enter 3 to input a book into finished list. Enter 4 to add and update your goals. Enter 999
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
				self.current_goals_and_reads()
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
title, author and page numbers are mandatory, the genre, and reason for reading are optional.''')
		title_array = []
		author_array = []
		number_pages_array = []
		genre_array = []
		reason_read_array = []
		df = None
		user_input = None
		user_input = input('''Enter back to go to main menu, enter show to see current list,
		 otherwise click any button to continue: ''').lower()
		while user_input != 'back':
			if user_input == 'show':
				try:
					print(user_input)
					con = sqlite3.connect(self.db_location + self.database_name)
					df_read = pd.read_sql('SELECT * FROM %s' % (self.user_book_list), con, index_col='index')
					print(df_read.head(100))
				except Exception as e:
					print('not info exists or there was an error, ', e)
					print('Please enter info or type back to go back')
			print(user_input)
			try:
				print(user_input)	
				title = input('Please enter the name of the book, be case sensitive: ').capitalize()
				if len(title) < 1:
					print('cant be empty')
					raise ValueError()
				author = input('''Please enter the author, be case sensitive. If there is
	more than one author, enter a comma after each auther: ''').capitalize()
				if len(author) < 1:
					print('cant be empty')
					raise ValueError()
				number_pages = int(input('Please enter the number of pages: '))
				check = isinstance(number_pages, int)
				print(check)
				if check is False:
					print('not a number')
					raise ValueError()
				genre = 'None entered'
				genre = input('Please enter the genre: ').capitalize()
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
				user_input = input('''you have chosen add, enter back to go back, 
		otherwise, if data is correct, press any key to add to database''')
				if user_input != 'back':
					try:
						con = sqlite3.connect(self.db_location + self.database_name)
					except Exception as e:
						print(' no current datatable exists,', e)
					try:
						df.to_sql(self.user_book_list, con, if_exists='append')
						user_input = 'back'
					except Exception as e:
						print('could not write to database,', e)

	def current_goals_and_reads(self):
		intro = '''Please enter show to see list of books on book list, current to see books
you are currently reading, enter add to add a book to current read and enter finish
to move a book out of current read to finished list'''
		print(intro)
		user_input = None
		con = None
		try:
			con = sqlite3.connect(self.db_location + self.database_name)
		except Exception as e:
			print(' no current datatable exists,', e)
		while user_input != 'back':
			user_input = input('Please enter choice: ')
			if user_input == 'show':
				df_read = pd.read_sql('SELECT * FROM %s' % (self.user_book_list), con, index_col='index')
				print(df_read.head(100))
				print(intro)
			elif user_input == 'current':
				try:
					df_user_read = pd.read_sql('SELECT * FROM %s' % (self.current_read_table), con, index_col='index')
					print(df_user_read.head(100))
				except Exception as e:
					print('no list exists or hit error, ', e)
				print(intro)
			elif user_input == 'add':
				book_to_add_df = None
				print('Do you want to move a book over from your read list or add new book to current read')
				choice = input('enter move or new: ')
				if choice == 'move':
					try:
						df_read = pd.read_sql('SELECT * FROM %s' % (self.user_book_list), con, index_col='index')
						print(df_read.head(100))
					except Exception as e:
						print('could not find database or an error occurred, ', e)
					print(df_read.index)
					try:
						book_number = int(input('Enter the index number of the book to add: '))
						check_if_int(book_number)
					except Exception as e:
						print('not a number, ', e)
					try:
						if book_number > df_read.shape[0]:
							raise ValueError()
						book_to_add = df_read.iloc[book_number]
					except Exception as e:
						print('not an option or out of range, or prior error, ', e)
					#print(book_to_add)
					#rerun books here if there are more to add
					#book_to_add = book_to_add.transpose()
					try:
						book_to_add_df =  pd.DataFrame(book_to_add).transpose()
						pages = pd.to_numeric(book_to_add_df['Number of Pages'])
						book_to_add_df['Number of Pages'] = pages
						book_to_add_df['date_added'] = datetime.datetime.now()
						book_to_add_df['page number goal'] = None
						book_to_add_df['finish_page_date'] = None
						book_to_add_df['date_to_finish'] = None

						goal = input('''Would you like to set goals around this book, please 
	enter yes or no ''')
						if goal == 'yes':
							try:
								date_to_finish = input('''please enter date you would like to finish by,
	enter in the format of m/d/yyyy: ''')
								print(date_to_finish)
								print(type(date_to_finish))
								check_if_date(date_to_finish)
								book_to_add_df['date_to_finish'] = date_to_finish
								interm_page_goal = input('enter yes to input interm goals, these will show up on goal trackers: ')
								if interm_page_goal == 'yes':
									interm_pages = int(input('''Please enter the amount of apges you would like to read and you will then 
			be prompted for a daten to read them by. pages: '''))
									check = isinstance(interm_pages, int)
									if check is True:
										book_to_add_df['page number goal'] = interm_pages
										date_interm = input('''When would you like to finish them by, 
				please enter in the format d/m/yyyy: ''')
										try:
											check_if_date(date_interm)
											book_to_add_df['finish_page_date'] = date_interm
										except Exception as e:
											print('improper date', e)
									else:
										pass
							except Exception as e:
								print('improper date, ', e)
							else:
									pass
					except Exception as e:
						print('could not make dataframe, no book picked up, ', e)
					print('Here is what you entered, would you like to add?')	
					print(book_to_add_df)
					# book added here for add
					add_to_db = input('enter yes to add: ')
					if add_to_db == 'yes':
						try:
							book_to_add_df.to_sql(self.current_read_table, con, if_exists='append')
							print(book_to_add_df)
							print('You have added book')
						except Exception as e:
							print('book was not added because ',e)
					print(intro)
				elif choice == 'new':
					print('new section not done yet')
					# basically same all functinonality has been done for this, take info from
					# adding new pick and combine with goals part
					# the question is, should this re factored, prob yes
					# method to take in new book for dataframe, method to load to 
					# dataframe and add goals to it
				else:
					print('That choice wasnt recongized')
					print(intro)
			elif user_input == 'finish':
				pass
			elif user_input == 'back':
				pass
			else:
				print('not an option')
				print(intro)
		else:
			print('You have entereed back')

def check_if_date(date):
	check = datetime.datetime.strptime(date, '%m/%d/%Y')
	if check is check.date:
		print('not a date')
		raise ValueError()

def check_if_int(number):
	check = isinstance(number, int)
	print(check)
	if check is False:
		print('cant be empty or not a number')
		raise ValueError()

db_location = '/home/mike/Documents/coding_all/productivity_app/'
reading = ReadingClass(db_location)
reading.user_menu()



'''
not raising errors as it should
'''