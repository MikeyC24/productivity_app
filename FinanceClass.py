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
import datetime


class FinanceActivity:

	def __init__(self, db_location, db_name, cc_report_name, finance_out_report_name):
		self.db_location = db_location
		self.db_name= db_name
		self.cc_report_name = cc_report_name
		self.finance_out_report_name = finance_out_report_name

	def user_menu(self):
		print('''Welcome to the finance part of the app, here is where you will manage
all inflows and outflows, see past actions and view info through various charts\n''')
		print('''To get started, type 1 to add new item/expense, press 2 to add
new budget or goals, press 3 to see past history and analyze, and lastly
press 4 to compare current progress to goals. enter 999 to quit''')
		menu_input = 0
		while menu_input != 999:
			# gonna need to add something to resee menu
			#try:
			menu_input = int(input('please enter selection(999 to quit): '))
			if menu_input == 1:
				print('add items')
				#cc_df = self.add_items_from_cc()
				non_cc_df = self.add_items_non_cc()
				#self.combine_add_dfs(cc_df, non_cc_df)
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
			#except Exception as e:
			#	print('That command was not reconigzed, are you sure it was a number')
		else:
			print('goodbye')

	def add_items_from_cc(self):
		print(str(self.db_location+self.cc_report_name))
		cc_df = pd.read_csv(self.db_location+self.cc_report_name)
		#pd.DatetimeIndex(cc_df['Trans Date'], format='%m%d%Y', inplace=True)
		cc_df.set_index(pd.DatetimeIndex(cc_df['Trans Date']), inplace=True, drop=True)
		cc_df.drop('Trans Date', axis=1, inplace=True)
		cc_df['Amount'] = cc_df['Amount'].apply(lambda x: x * -1)
		print(cc_df.index)
		#cc_df.sort_values(by=index)
		cc_df.sort_index(ascending=True, inplace=True)
		print(cc_df.head(5))
		cc_df['Category'] = 'none selected'
		cc_df['Additional Info'] = 'None added'
		cc_df['Type'] = 'Credit Card'
		order = input('''Curenetly the data is shown by most recen transactions, would you
like to reverse that or keep it, type reverse to switch: ''')
		if order == 'reverse':
			print('Data has been reversed and will show oldest transactions')
			cc_df.sort_index(ascending=False, inplace=True)
			print(cc_df.head())
		else:
			print('Data will stay in current order')
		for x in range(len(cc_df)):
			print('''You will be shown each entry in the report. After each entry you will be asked
to assign each charge to a category, which is mandatory. Then you will the option of adding
in a description, with a limit of 50 characters.''')
			print(cc_df.iloc[x])
			print('''For the charge what category will you like to enter. enter "list", 
to see all cateogiries currently entered''')
			user_input = input('please enter a category: ')
			cc_df['Category'].iloc[x] =  user_input
			user_input1 = input('please add in any additional data: ')
			if user_input1 is not None:
				cc_df['Additional Info'].iloc[x] = user_input1
		print('Here are the changes you made, would you like to add additions to table? ')
		print(cc_df.head())
		return cc_df

	def add_items_non_cc(self):
		print('Here we will add cash and cash related expenses')
		user_select = 0
		date_array = []
		amount_array = []
		descrip_array = []
		type_array = []
		cateogry_array = []
		additional_info_array = []
		df = None
		user_select = input('''Type quit if there is nothing to add in cash form,
other press enter: ''')
		while user_select != 'quit':
			date = input('please enter the date of expense in the format m/d/yyyy: ')
			try:
				check = datetime.datetime.strptime(date, '%m/%d/%Y')
				print(type(check))
				if check is check.date:
					print('not a date')
					raise ValueError()
				amount = float(input('please enter the amount: '))
				check = isinstance(amount, float)
				print(check)
				if check is False:
					print('cant be empty or not a number')
					raise ValueError()
				descrip = input('please enter description of expense: ')
				if len(descrip) < 0:
					print('cant be empty')
					raise ValueError()
				additional_info = input('please enter any additonal info: ')
				if len(additional_info) == 0:
					additional_info = 'None Given'
				type_ = input('please enter the type, such as cash, venmo, paypal,etc: ')
				if len(type_) < 0:
					print('cant be empty')
					raise ValueError()
				category = input('please enter the category: ')
				if len(category) < 0:
					print('cant be empty')
					raise ValueError()
				date_array.append(date)
				amount_array.append(amount)
				descrip_array.append(descrip)
				cateogry_array.append(category)
				additional_info_array.append(additional_info)
				type_array.append(type_)
			except Exception as e:
				print('hit error', e)
			user_select = input('''press any key to add another item, type quit to go back
, type add to add to database: ''')
			if user_select == 'add':
				df = pd.DataFrame({'Trans Date': date_array, 'Amount':amount_array, 
					'Description': descrip_array, 'Type': type_array, 
					'Category': cateogry_array, 'Additional Info': additional_info_array})
				df.set_index(pd.DatetimeIndex(df['Trans Date']), inplace=True, drop=True)
				df.drop('Trans Date', axis=1, inplace=True)
				df.sort_index(ascending=True, inplace=True)
				print(df.head(10))
				user_select = 'quit'
		else:
			print('now going back')
		return df

	def combine_add_dfs(self, df1, df2):
		try:
			con = sqlite3.connect(self.db_location+ self.db_name)
		except Exception as e:
			print(' no current datatable exists,', e)
		if df2 is not None:
			df = pd.concat([df1,df2])
		else:
			df = df1
		df.sort_index(ascending=True, inplace=True)
		print('below is the combined data')
		print(df_new.head())
		add_to_db = input('type yes to add: ')
		if add_to_db == 'yes':
			print('added to database')
			df.to_sql(self.finance_out_report_name, con, if_exists='append')
		else:
			print('changes have not been added')




db_location = '/home/mike/Documents/coding_all/productivity_app/'
db_name = 'finance_db'
#cc_report_name = 'sample_cc_report.csv'
cc_report_name = 'sample_cc_report2.csv'
report_output = 'financial_data2'
instance = FinanceActivity(db_location, db_name, cc_report_name, report_output)
instance.user_menu()