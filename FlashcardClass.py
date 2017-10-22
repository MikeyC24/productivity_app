#flash card app, first will be playing around witha  csv until parsting is
# right, then develop classa

import json
import sqlite3
import datetime

file = '/home/mike/Documents/credit/flashcards_test_note.txt'
file_test_2_topics = '/home/mike/Documents/credit/Asset_based_financing_notes.txt'
file2 = '/home/mike/Downloads/Aba course 9.5.17 flashcard_format_only.docx'
file3 = '/home/mike/Documents/credit/flashcards_test_note_docx.docx'
file4 = '/home/mike/Documents/credit/flash_cards_aba_one_subtopic_docx.docx'
abl_full = '/home/mike/Documents/credit/Asset_based_financing_notes_full_flashcard_format'
test_multiple = '/home/mike/Documents/credit/flashcard_test_multiple.txt'
test_multiple_topics_only = '/home/mike/Documents/credit/flashcard_test_multiple_topics_only.txt'
test_multiple_topics_only_two = '/home/mike/Documents/credit/ABA_flashcard_format_test_purpose.txt'
f = open(file, 'r')
#print(note_file.read())
lines = f.readlines()
f.close()
dict_topic = {}
questions_array = []
answer_array = []
topic = None
subtopic = None
title = None
topic_dict = {}
subtopic_dict = {}
title_dict = {}
end_and_write = False

def notes_to_dict_full(file):
	f = open(file, 'r')
	lines = f.readlines()
	f.close()
	dict_topic = {}
	questions_array = []
	answer_array = []
	topic = None
	subtopic = None
	title = None
	topic_dict = {}
	subtopic_dict = {}
	title_dict = {}
	change_next = False
	end_and_write = False

	while end_and_write == False:
		for i, line in enumerate(lines):
			if 'break_program' in line:
				end_and_write = True
			#print(i, line)
			if 'Title:' in line:
				title = line[7:]
			# next change for topic
			if 'Topic:' in line:
				topic = line[6:]
				while change_next == False:
					#if 'Topic:' in line:
					#	change_next = True
						#continue
					if 'Subtopic:' in line:
						subtopic = line[9:]
						#continue
					if 'Q:' in line:
						questions_array.append(line)
						#continue
					if 'A:' in line:
						answer_array.append(line)
					if 'Topic:' in line:
						change_next = True
					print('topic', line)
					print('change_next', change_next)
					q_a_dict = dict(zip(questions_array, answer_array))
					subtopic_dict[subtopic] = q_a_dict
					topic_dict[topic] = subtopic_dict
					title_dict[title] = topic_dict
			change_next = False
			if 'Subtopic:' in line:
				subtopic = line[9:]
				while change_next == False:
					if 'Subtopic:' in line:
						change_next = True
						#continue
					if 'Q:' in line:
						questions_array.append(line)
						#continue
					if 'A:' in line:
						answer_array.append(line)
					print('subtopic', line)
					q_a_dict = dict(zip(questions_array, answer_array))
					subtopic_dict[subtopic] = q_a_dict
					topic_dict[topic] = subtopic_dict
					title_dict[title] = topic_dict
			print(i, line)
			#if 'Q:' in line:
			#	questions_array.append(line)
			#if 'A:' in line:
			#	answer_array.append(line)
			#print(line)
			#q_a_dict = dict(zip(questions_array, answer_array))
			#subtopic_dict[subtopic] = q_a_dict
			#topic_dict[topic] = subtopic_dict
			#title_dict[title] = topic_dict
		return title_dict

def notes_to_dict_just_topics(file):
	f = open(file, 'r')
	lines = f.readlines()
	f.close()
	dict_topic = {}
	topic = None
	title = None
	topic_dict = {}
	title_dict = {}
	topic_counter = 0

	while end_and_write == False:
		for i, line in enumerate(lines):
			#if 'break_program' in line:
			#	end_and_write = True
			#print(i, line)
			if 'Title:' in line:
				title = line[7:]
			if 'Topic:' in line:
				topic = line[6:]
				q_a_dict = None
				q_a_dict = grab_q_a_dict(lines, 'Topic:', topic_counter)
				topic_counter += 1
				topic_dict[topic] = q_a_dict
				#print(topic_dict)
				#break
		title_dict[title] = topic_dict
		return title_dict

# this method is used in notes to dict just topics method
# it is a way to grab only the  q and as under the next topic
# by feeding in the lines, keyword and the keyword count
# keyword count is kept in prior method, every time this below method
# is used the above mehod increases count and feeds it back
# below method return q and a in dict form
def grab_q_a_dict(lines, keyword, keyword_count):
	questions_array = []
	answer_array = []
	method_count = 0
	count_use = keyword_count + 1
	subtopic_dict = {}
	while method_count <  count_use:
		for x, line in enumerate(lines):
			#print('inside qa grab', x, line)
			#print('method count before increment', method_count)
			if keyword in line:
				method_count += 1
			#print('method count after increment', method_count)	
			if method_count - 1 == keyword_count:
				if 'Q:' in line:
					questions_array.append(line)
					#continue
				if 'A:' in line:
					answer_array.append(line)
	q_a_dict = dict(zip(questions_array, answer_array))
	return q_a_dict

"""
#blocked off for now, this is now going thru suer menu
title_dict = notes_to_dict_just_topics(test_multiple_topics_only)
title_dict_two = notes_to_dict_just_topics(test_multiple_topics_only_two)
# below is just to print full dict 10.21.22
for k,v in title_dict.items():
	print('first key')
	print(k)
	#print(v)
	for kk,vv in v.items():
		print('second key')
		print(kk)
		for k3, v3 in vv.items():
			print('third key')
			print(k3)
			print(v3)
"""			

#This are storage and retriveal methods of dicts, will come
#back to these once able to write dict with multiple topics
# this method takes a dict, turns it into a json file and then
# writes to csv based on given name
# if master dict is used, file name should prob always be the same
def write_dict_json_csv(dict, file_name):
	json_dict = json.dumps(dict, sort_keys=True, indent=3)
	location = '/home/mike/Documents/coding_all/productivity_app/deck_folder/' + file_name
	with open(location, 'w') as f:
		f.write(json_dict)

# this method takes in a fle name, that is a json dict
# and turns it back into regular dict
def read_dict_back_from_json(file_name):
	with open(file_name, 'r') as f:
		data = f.read()
		dict_back = json.loads(data)
		print(dict_back)
		print(type(dict_back))

"""
# bocked off for now, this is geting all json stuff
file_from_csv = '/home/mike/Documents/coding_all/productivity_app/json_csv_with_multiple_topic_upload'
write_dict_json_csv(title_dict, 'json_csv_with_multiple_topic_upload')
file_from_csv_two = '/home/mike/Documents/coding_all/productivity_app/json_csv_with_multiple_topic_upload_two'
write_dict_json_csv(title_dict_two, 'json_csv_with_multiple_topic_upload_two')

read_dict_back_from_json(file_from_csv)
read_dict_back_from_json(file_from_csv_two)
"""

# 10.21.17 now need method to retrieve dict or dicts we want to test
# options for user 1. store new dict or update dict
# 2. pick dict or dicts to test
# 3. make into outline, use [:] for the lines to drop
# all the structure, like q's, a's, and " "
"""
# storing dict
# at first will limit user to 20 falsh decks (maybe make a way to import/export)
each title will be stored as a separate csv, 
code will cycle thru csv
for csv_file in csv_folders:
	dict = read_dict_back_from_json(csv_file)
	if dict.get(user_title, False):
		dict[user_title]
	else:
		add dict
next make user option menu, always get all available title keys
then go into user options

"""

def user_menu():
	intro = '''Welcome to the Flashcard center. Below will show all current
flash card decks by title available. To use a current deck, enter 1. To add a 
new flash card debt press 2. To update a current deck press 3. To turn a deck into
an outline press 4. Enter 999 to quit.'''
	#path = '/home/mike/Documents/coding_all/productivity_app/*.csv'
	#print(intro)
	menu_input = 0
	while menu_input != 999:
		# gonna need to add something to resee menu
		#try:
			print(intro)
			import os
			import glob
			print('Below is a list of current decks, by deck name')
			path = '/home/mike/Documents/coding_all/productivity_app/deck_folder'
			path2 = '/home/mike/Documents/coding_all/productivity_app/deck_folder/*'
			if os.listdir(path) == []:
				print('There are no decks')
			else:
				for fname in glob.glob(path2):
					print('deck name: ', fname[61:])
			menu_input = int(input('please enter selection(999 to quit): '))
			if menu_input == 1:
				print('review cards')
			elif menu_input ==  2:
				print('add new deck')
				upload_new_deck()
			elif menu_input == 3:
				print('update deck')
			elif menu_input == 4:
				print('get outline')
			elif menu_input == 999:
				pass
			else:
				print('That was not a recongized command')
		#except Exception as e:
		#	print('That command was not reconigzed, are you sure it was a number')
	else:
		print('goodbye')


def upload_new_deck():
	print(""" You have chosen to upload a new deck. Before doing so please
make sure that the format is correct. There is a title labled as "title:" on the top.
Each topic is labeled as "Topic:" and all the contentis formated as Q: "" and A: "". 
If not sure please check the user guide for the proper outline/display""")
	# for now, to enter new deck, use will type in full file location
	#try:
	file_location = input('Please enter the file exactly: ')
	print(file_location)
	print(type(file_location))
	# create deck from user input
	deck_to_load = notes_to_dict_just_topics(file_location)
	# get title of deck to use for storage and retrieval 
	for k,v in deck_to_load.items():
		title = str(k)
	print(deck_to_load)
	print(k)
	import glob
	path2 = '/home/mike/Documents/coding_all/productivity_app/deck_folder/*'
	exists = False
	for fname in glob.glob(path2):
		title_check = fname[61:]
		if title_check == title:
			exists = True
	if exists == False:
		write_dict_json_csv(deck_to_load, title)
	else:
		print('This deck already exists, would you like to overwrite')
		save = input('Enter "yes" to overwrtie and anything else to not overwrite: ')
		if save == 'yes':
			write_dict_json_csv(deck_to_load, title)
		else:
			print('This deck was not saved')
	#except Exception as e:
	#	print('That file was note found or did not work,', e)


user_menu()

"""
10.22.17
looks like decks can now be uploaded or updated, get rid of update option 
and just have an update or upload option
print out list of decks is funky right now
next is make part that cycles thru flash cards
after that there needs smart learning around the cards, maybe wait till
some exploration with kivy and see how unique user login works




# /home/mike/Documents/credit/flashcard_test_multiple_topics_only.txt



"""
class DictQuery(dict):
	def get(self,path,default = None):
		keys = path.split('/')
		val = None
		print(keys)
		for key in keys:
			if val:
				if isininstance(val, list):
					val = [ v.get(key, default) if v else None for v in val]
				else:
					val = val.get(key, default)
			else:
				val = dict.get(self, key, default)

			if not val:
				break;
		return val

"""




"""
aspects to consider
notes not in format of Q/A function
picutres on page - best way to store combination of pics and data
what happens when A: is on same line of Q:, as in a short question
any way to provie a template and enter or a jump can quickly jump
down without having to click or insert Q/A
how to deal with quotes in notes, (this can be accomodated by three
quotes but that would be rly clunky/ugly without some template
and auto formatting)
"""

"""
game plan for today
add by subtopic, enter in title and topic
use logic to detmerine if title or topic exists
if it does append
elif create
how are these being stored?, how can sql database handle dict
look into seralizing dict with json
"""

"""
skipping pictures for now, develop core feature
pics will come with manual uplaods later
maybe a ulk script after that
for pictures need to fogure out if can use below two linlks
to open and parse odt and have it still work with saving to
database or be a text only mass upload, much more value
with pictres
https://pypi.python.org/pypi/odfpy
https://github.com/eea/odfpy/wiki/OpenDocumentClasses

# maybe https://github.com/python-openxml/python-docx/issues/40
from docx import *
document = Document(file4)
print(document)
questions_array = []
answer_array = []
for para in document.paragraphs:
	print('________________________')
	print(para)
for block in iter_block_items(document):
	print(block.text)



	if 'Topic:' in para:
		topic = para[7:]
		continue
	topic_check = topic
	if 'Subtopic:' in para:
		subtopic = para[9:]
		continue
	subtopic_check = subtopic
	if 'Q:' in para:
		questions_array.append(para)
		continue
	if 'A:' in para:
		answer_array.append(para)

for x in range(len(questions_array)):
	print('Q', questions_array[x])
	print('A', answer_array[x])
"""


""" 
turning python into app
https://www.quora.com/Can-I-make-an-Android-app-with-Python
"""