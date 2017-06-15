import json
from pprint import pprint
import os, os.path
import csv


fileName = 'C:/Users/dvadithala/Desktop/Pinnion/Q2.json'


def stringifyJSON(inputJSON):

	myOutput = []
	tempFileName = os.path.basename(inputJSON)
	tempFileName = os.path.splitext(tempFileName)[0]
	myOutput.append(tempFileName)
	correctAnswer = ''

	with open(inputJSON) as data_file:    
	    data = json.load(data_file)

	myOutput.append(str(data['0']['question'][0]['text']))

	numberOfAnswers = len(data['0']['question'][0]['answer'])

	if int(data['0']['question'][0]['max']) == 1:
		myOutput.append('multi-select')

	for i in range(0, numberOfAnswers):
		if int(data['0']['question'][0]['max']) == 1:
			myOutput.append(data['0']['question'][0]['answer'][i]['text'])
			if int(data['0']['question'][0]['answer'][i]['correctFlag']) == 1:
				correctAnswer = str(i + 1)
		else:
				myOutput.append('multiple-select')
				correctAnswer = correctAnswer + ',' + str(i + 1)
		
	if numberOfAnswers + 1 < 6:
		for x in range(1, 6 - numberOfAnswers + 1):
			myOutput.append(' ')


	myOutput.append(correctAnswer)
	myOutput.append(str(data['0']['question'][0]['triviaText']))
	return myOutput


print(stringifyJSON(fileName))


def convertListToCSV():
	with open('C:/Users/dvadithala/Desktop/Pinnion/Output/BulkUpload_Questions.csv', 'w', newline='') as myFile:
		for eachFile in os.listdir('C:/Users/dvadithala/Desktop/Pinnion/'):
			if eachFile.endswith('.json'):
				inputList = stringifyJSON(eachFile)
				myWriter = csv.writer(myFile, quoting=csv.QUOTE_ALL, lineterminator='\n')
				myWriter.writerow(inputList)



convertListToCSV()
