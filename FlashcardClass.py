#flash card app, first will be playing around witha  csv until parsting is
# right, then develop classa

import json
import sqlite3
import datetime

file = '/home/mike/Documents/credit/flashcards_test_note.txt'
file1 = '/home/mike/Documents/credit/Asset_based_financing_notes.txt'
file2 = '/home/mike/Downloads/Aba course 9.5.17 flashcard_format_only.docx'
file3 = '/home/mike/Documents/credit/flashcards_test_note_docx.docx'
file4 = '/home/mike/Documents/credit/flash_cards_aba_one_subtopic_docx.docx'
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

def notes_to_dict(file):
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
	for i, line in enumerate(lines):
		#print(i, line)
		if 'Title:' in line:
			title = line[7:]
			continue
		if 'Topic:' in line:
			topic = line[6:]
			continue
		topic_check = topic
		if 'Subtopic:' in line:
			subtopic = line[9:]
			continue
		subtopic_check = subtopic
		if 'Q:' in line:
			questions_array.append(line)
			continue
		if 'A:' in line:
			answer_array.append(line)
	q_a_dict = dict(zip(questions_array, answer_array))
	subtopic_dict[subtopic] = q_a_dict
	topic_dict[topic] = subtopic_dict
	title_dict[title] = topic_dict
	return title_dict
title_dict = notes_to_dict(file)
for k,v in title_dict.items():
	print(k)
	#print(v)
	for kk,vv in v.items():
		print(kk)
		for k3, v3 in vv.items():
			print(k3)
			for k4,v4 in v3.items():
				#print(k4)
				#print(v4)
				pass

def write_to_csv_as_json(dict, file_name):
	json_dict = json.dumps(dict, sort_keys=True, indent=4,ensure_ascii=False)
	with open(file_name, 'w') as outfile:
		outfile.write(json_dict)

def save_json_to_file(dict, file_name):
	out_file = open(file_name, 'w')
	json.dump(dict, out_file,  sort_keys=True, indent=4,ensure_ascii=False)
	out_file.close()

def three_time_json_to_csv(dict, file_name):
	json_dict = json.dumps(dict, sort_keys=True, indent=4)
	with open(file_name, 'w') as f:
		f.write(json_dict)

#write_to_csv_as_json(title_dict, 'json_csv_test')

# this works to write json to csv and to read from csv
def open_csv_convert_json_to_dict(file_name):
	f = open(file, 'r')
	print(f)
	print(type(f))
	data = f.read()
	print(data)
	print(type(data))
	dict = json.load(data)
	print(data)
	print(type(data))

def read_it_back(file_name):
	with open(file_name, 'r') as f:
		data = f.read()
		dict_back = json.loads(data)
		print(dict_back)
		print(type(dict_back))

file_from_csv = '/home/mike/Documents/coding_all/productivity_app/json_csv_test3'
three_time_json_to_csv(title_dict, 'json_csv_test3')
read_it_back(file_from_csv)

"""
def open_csv_convert_json_to_dict(file_name):
	in_file = (file_name, 'r')
	new_dict = json.load(in_file)
	in_file.close()
	return new_dict
"""
file_from_csv = '/home/mike/Documents/credit/json_csv_test1'
#open_csv_convert_json_to_dict(file_from_csv)
#new_dict = open_csv_convert_json_to_dict(file_from_csv)
#print(new_dict)

# json_dict = json.dumps(dict, sort_keys=True, indent=4)
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




title_dict = notes_to_dict(file)
key_to_get = 'Asset Based Finance/The Process of Asset-based Financing/Analyzing the borrower'
for item in title_dict.items():
	#print(item)
	print(DictQuery(item).get(key_to_get))
#print(q_as)
"""
"""
# checking for keys using above class
title_dict = notes_to_dict(file)
for key in title_dict.keys():
	key_use = key
	print(key)
	print(len(key))
print(len('Asset Based Finance'))
title_dict = notes_to_dict(file)
key_list = ['Asset Based Finance']
for key in key_list:
	check = title_dict.get(key)
	print(check)
"""
"""
# tutorial on passing json to dict (this example also cover pulling from web)
# http://www.prelc.si/koleznik/tutorial-for-parsing-json-and-creating-sqlite3-database-in-python/
# handling nested dicts and get requests https://www.haykranen.nl/2016/02/13/handling-complex-nested-dicts-in-python/
def store_json_to_db(dict, db_name, table_name):
	json_dict = json.dumps(dict, sort_keys=True, indent=4)
	print(type(json_dict))
	table_name = table_name
	con = sqlite3.connect(db_name)
	cur = con.cursor()
	cur.execute('''CREATE TABLE IF NOT EXISTS %s
				(cards_list)
				''' % (table_name))
	insert = "INSERT INTO {} VALUES (?)".format(table_name)
	cur.execute("INSERT INTO cards_list"
				"("
				"cards_list"
				") VALUES (?)",
				(json_dict))

	cur.execute(insert, json_dict)
	con.commit()


flashcards_db = '/home/mike/Documents/credit/flashcards_db'
flashcards_table = 'flashcards_table'
title_dict = notes_to_dict(file)
store_json_to_db(title_dict, flashcards_db, flashcards_table)
"""
"""
title_dict = notes_to_dict(file)
j_dict = json.dumps(title_dict, sort_keys=True, indent=4)
#print(j_dict)
print('json tpye', type(j_dict))
py_dict_from_j = json.loads(j_dict)
print('py json dict', type(py_dict_from_j))
"""
"""
for k,v in title_dict.items():
	print(k)
	#print(v)
	for kk,vv in v.items():
		print(kk)
		for k3, v3 in vv.items():
			print(k3)
			for k4,v4 in v3.items():
				#print(k4)
				#print(v4)
				pass
"""
"""
this above needs to be turned into a method that outputs a dict - done
turn dict to json and back for storage
then that dict is compared to data base
if its not there it creates a new section
otherwise it combines with whats currently there
"""







"""
for i, line in enumerate(lines):
	#print(i, line)
	if 'Topic:' in line:
		topic = line[7:]
		continue
	if 'Subtopic:' in line:
		subtopic = line[9:]
		continue
	if 'Q:' in line:
		questions_array.append(line)
		continue
	if 'A:' in line:
		answer_array.append(line)
		print(answer_array)
		continue
	if 'Subtopic:' in line:
		#print('q_a', questions_array)
		title = 'q_a_dict'+subtopic
		print(subtopic)
		print(title)
		title = dict(zip(questions_array, answer_array))
		for k,v in title.items():
			print('v', v)
		#print('q_a_dict', q_a_dict)
		subtopic_dict[subtopic] = title
		questions_array= []
		answer_array= []
		break

#q_a_dict = dict(zip(questions_array, answer_array))
#subtopic_dict[subtopic] = q_a_dict
"""

"""

line_check= 'continue'
for i, line in enumerate(lines):
	print(i, line)
	if 'Topic:' in line:
		topic = line[7:]
		continue
	if 'Subtopic:' in line:
		subtopic = line[9:]
		continue
	while line_check != 'break':
		line_check = line_check('Subtopic:', line)
		if 'Q:' in line:
			questions_array.append(line)
			continue
		if 'A:' in line:
			answer_array.append(line)
	else:
		print('hit next sub topic')
q_a_dict = dict(zip(questions_array, answer_array))
subtopic_dict[subtopic] = q_a_dict

def line_check(check_var, line):
	print(check_var)
	print(line)
	if check_var in line:
		return 'break'
"""
#print(questions_array, answer_array)
"""
for x in range(len(questions_array)):
	print('Q', questions_array[x])
	print('A', answer_array[x])
print(len(questions_array), len (answer_array))
print('topic', topic, 'subtopic', subtopic)

print(topic_check)
print(subtopic_check)


dict_2 = dict(zip(questions_array, answer_array))
for k,v in dict_2.items():
	print(k,v)
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