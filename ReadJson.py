
import json
import random


# Python program to read 
# json file    
   
# Opening JSON file 
with open('intents.json') as f:
  data = json.load(f)

  #inputTag = 'greeting'
def getResponseFromJSON(inputTag):
  # Output: {'name': 'Bob', 'languages': ['English', 'French']}
  myList = data['intents']
  for i in range(len(myList)):
    myData = myList[i]
    if(myData['tag'] == inputTag):
        return(myData['responses'][random.randint(0, len(myData['responses'])-1)])
  return('Sorry, I dont know!!')
    
    
