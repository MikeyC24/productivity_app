#flash card app, first will be playing around witha  csv until parsting is
# right, then develop classa

file = '/home/mike/Documents/credit/flashcards_test_note.txt'
file1 = '/home/mike/Documents/credit/Asset_based_financing_notes.txt'
f = open(file1, 'r')
#print(note_file.read())
lines = f.readlines()
f.close()
dict_topic = {}
questions_array = []
answer_array = []
topic = None
subtopic = None
topic_dict = {}
subtopic_dict = {}

"""
for i, line in enumerate(lines):
	print(i, line)
	if 'Topic:' in line:
		topic = line[7:]
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

for k, v in subtopic_dict.items():
	print('k', k)
	print('v', v)
	"""
	for kk, vv in v.items():
		print('kk', kk)
		print('vv', vv)
		"""