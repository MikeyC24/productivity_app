"""
# overall goal of this class
1. input all user data finance data - CC, banks, cash, other etc
2. aggregate that data while taking inputs from user to properly categorize 
3. output data into time frames, charts etc
4. let user set goals that can be checked on
# vars needed
1. db location 2. cc info inout 3. storage of cc output 
4. storage of goals

"""
import pandas as pd
import numpy as np
import sqlite3


class FinanceActivity:

	def __init__(self, db_location, cc_report_name, finance_out_report_name):
		self.db_location = db_location
		self.cc_report_name = cc_report_name
		self. finance_out_report_name = finance_out_report_name

	def user_menu(self):
		print('''Welcome to the finance part of the app, here is where you will manage
all inflows and outflows, see past actions and view info through various charts\n''')
		print('''To get started, type 1 to add new item/expense, press 2 to add
new budget or goals, press 3 to see past history and analyze, and lastly
press 4 to compare current progress to goals. enter 999 to quit''')
		menu_input = 0
		while menu_input != 999:
			menu_input = int(input('please enter selection: '))
			if menu_input == 1:
				print('add items')
				self.add_items_from_cc()
			elif menu_input ==  2:
				print('add goals')
			elif menu_input == 3:
				print('review numbers')
			elif menu_input == 4:
				print('compare')
			elif menu_input == 999:
				pass
			else:
				print('That was not a recongized command')
		else:
			print('goodbye')

	def add_items_from_cc(self):
		try:
			con = sqlite3.connect(self.db_location)
		except Exception as e:
			print(' no current datatable exists', e)
		try:
			df_to_write_to = df.read_sql_query('SELECT * FROM %s' % (table), con)
		except Exception as e:
			print(' no current table exists', e)
		print(str(self.db_location+self.cc_report_name))
		cc_df = pd.read_csv(self.db_location+self.cc_report_name)
		cc_df['categories'] = 'none selected yet'
		cc_df['additional_info'] = 'None added'
		for x in range(len(cc_df)):
			print('''You will be shown each entry in the report. After each entry you will be asked
to assign each charge to a category, which is mandatory. Then you will the option of adding
in a description, with a limit of 50 characters.''')
			print(cc_df.iloc[x])
			print('''For the charge what category will you like to enter. enter "list", 
to see all cateogiries currently entered''')
			user_input = input('please enter a category: ')
			"""
			while cc_df[categories]
			if user_input == 'list':
				try:
					print(cc_df['categories'].values.unique())
				except Exception as e:
					print('There appear to be no categories entered, or you have this error',e)
			"""
			cc_df['categories'].iloc[x] =  user_input
			user_input1 = input('please add in any additional data: ')
			if user_input1 is not None:
				cc_df['additional_info'].iloc[x] = user_input1
		print(cc_df.head(5))



db_location = '/home/mike/Documents/coding_all/productivity_app/'
cc_report_name = 'sample_cc_report.csv'
report_output = 'financial_data'
instance = FinanceActivity(db_location, cc_report_name, report_output)
instance.user_menu()