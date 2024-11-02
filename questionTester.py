from datetime import datetime
import os
import signal
import sys
import random
import textwrap

file_path = 'PSM I Prep Questions.md'
# file_path = 'PSM II Prep Questions.md'
# file_path = 'PSPO I Prep Questions.md'
# file_path = 'PSD I Prep Questions.md'

number_of_questions = 15

def clear():

    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def safe_print(text_to_print):
	text_to_print = textwrap.fill(text_to_print,os.get_terminal_size().columns)
	print(text_to_print)
	
def show_results():
	duration = datetime.now() - start
	clear()
	percentage_correct = int(correct_questions/number_of_questions*100)

	safe_print(f'You had {correct_questions} of the {question_counter} correct that is a score of {percentage_correct}%! The total dictionary of questions consists of {dict_length} questions. Answering the questions took you {duration} Below the questions you had wrong.')

	for question in wrong_question_list:
		safe_print(f'- ({question["number"]}) {question["question"]}')
		safe_print(f'      given answer: {question["given_answer"]}    correct answer: {question["correct_answer"]}')
		safe_print(f'Answer choices: \n{question["answers"]}')

def signal_handler(sig, frame):
	show_results()
	sys.exit(0)
	
signal.signal(signal.SIGINT, signal_handler)

start = datetime.now()

questions_dict = {}

current_question = ''

with open(file_path, 'r') as file:
	for line in file:
		line = line.strip()
		if not line:
				continue
		elif line.startswith('###'):
			current_question = line[3:].strip()
			questions_dict[current_question] = []
		elif line.startswith('- [ ]'):
			answer = line[5:].strip()
			questions_dict[current_question].append({'result':'wrong','answer':answer})
		elif line.startswith('- [x]'):
			answer = line[5:].strip()
			questions_dict[current_question].append({'result':'correct','answer' : answer})
			
dict_length = len(questions_dict)

question_counter = 0

correct_questions = 0

wrong_question_list = []

while question_counter < number_of_questions:

	questionNumber = int(len(questions_dict) * random.random())
	
	clear()
	question = list(questions_dict.keys())[questionNumber]
	
	safe_print(f'({question_counter+1}/{number_of_questions})')
	safe_print(question)
	
	iterator = 0
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	correct_answer = ''
	
	answer_list = questions_dict.pop(question)
	answer_string = ''
	
	for answer in answer_list:
		answer_string = f'{alphabet[iterator]}) {answer["answer"]}\n'	
		if answer['result'] == 'correct':
			correct_answer += alphabet[iterator]
		iterator += 1
		safe_print(answer_string)
	
	guess = input()
	
	
	if guess == correct_answer:
		correct_questions+=1
	else:
		wrong_question_list.append({'question':question,'given_answer':guess,'correct_answer':correct_answer,'answers':answer_string,'number':question_counter+1})
	
	question_counter += 1

show_results()

