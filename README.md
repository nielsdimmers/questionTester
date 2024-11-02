# Question tester

Simple python script with some functionality to test your skill on several example questions. To keep it lightweight, this question tester uses the commandline.

# Change history

## (2) Bugfixes
* (bug) when displaying wrong answers, only the last answer possibility was shown. This is fixed now.

## (1) 2024-11-01 First Upload

Functionalities include:
* Reading in the file based on the configuration in the script
* Parsing the questions based on the following rules:
    * Everything which starts with ``###`` is a question
    * This is followed by two or more instances of ``- [ ]`` or ``- [x]`` in any order, to be possible multiple-choice answers
    * ``- [ ]`` is a wrong answer
    * ``- [x]`` is a correct answer
    * Everything else is discarded
* Questions are displayed and asked, the screen is cleared with each new question
* Answers are submitted by typing them in order they appear
* The number of questions asked is configurable by in-script variable
* After the questions, or when pressing Ctrl-C, show a summary. Summary contains 
    * The number of questions answered
    * the number of correct questions
    * the time taken 
    * the total count of questions in the list
    * The specific questions with the answer you gave, and the correct answer
* Words are layed-out properly
* Time is kept how long you take for the total test
