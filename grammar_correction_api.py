import requests 
import json


url ="https://api.languagetoolplus.com/v2/check"


def grammar_correction(text): 
  data = {
    "text": text,
    "language": "auto"
  }
  response_data = requests.post(url, data=data)
  # print(type(response_data.text))
  # convert string into dictionary
  response = json.loads((response_data.text))
  print(f"Your input: {response['matches'][0]['sentence']}")
  print(f"Language detected: {response['language']['name']} ")
  
  if len(response['matches']) > 0: 
    print(f"{len(response['matches'])} possible typo/s were found.")
    for word in response['matches']:
      print(f"\n{response['matches'].index(word)+1}. TYPO:")
      print(f'Message: {word["message"]}')
      print("Possible replacements:")
      for key_value in word["replacements"]:
        print(f'{key_value["value"]}')
  else:
    print("No typos were found")
    

def main_grammar():
  text = input("Your text: ")
  grammar_correction(text) 


