import requests
import json
import pickle

def farsi_to_finglish(word : str):
  """
  farsi_to_finglish is a function that turns typing and spoken Persian into accurate Latin script. this function use 'laatingar.com' website.

  Parameters:
    word : a string include Persian text.    
  Returns:
    fn_name : a string or list include string(s) that show the finglish text of input.
  """

  url = "https://hhyz5zohp5.execute-api.us-east-2.amazonaws.com/production/farsi_to_latin"

  payload = f'{{"words":["{word}"],"debug":"on"}}'
  headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'text/plain',
    'origin': 'https://laatingar.com',
    'priority': 'u=1, i',
    'referer': 'https://laatingar.com/',
    'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  response = json.loads(response.text)
  fn_name = list(response["conversions"].values())[0]

  # processing
  if 'aa' in fn_name:
    fn_name = fn_name.replace("aa", "a")
  
  if "'" in fn_name:
    fn_name = fn_name.replace("'", "")

  # for names that end to 'eh' in social media needs to consider two type with 'h' or without 'h'.
  if fn_name.endswith("eh"):
    fn_name = [fn_name, fn_name[:-1]]

  return fn_name

# Combining scripted dictionaries from two sites
print("Starting combining phase!")

## Read dictionaries
with open('name_dict_website_1.pkl', "rb") as file:
    name_dict_website_1 = pickle.load(file)

with open('name_dict_website_2.pkl', "rb") as file:
    name_dict_website_2 = pickle.load(file)

## Combining seperately for boys and girls
girls_name = name_dict_website_1["Girl"] + name_dict_website_2["Girl"]
boys_name = name_dict_website_1["Boy"] + name_dict_website_2["Boy"]

## Making full dictionary
NameDictionary = {"Boy": list(set(boys_name)),
                  "Girl": list(set(girls_name))}

print("A comprehensive dictionary of Persian names has been fully maded.")

# Make Finglish dictionary

## Adding Finglish boy's name to NameDictionary
print("Starting making Finglish name for boys...")
NameDictionary["Boy_fn"] = [farsi_to_finglish(word) for word in NameDictionary["Boy"]]
print("The Finglish boy's name has been successfully added to the dictionary.")


## Adding Finglish girl's name to NameDictionary
print("Starting making Finglish name for girls...")
NameDictionary["Girl_fn"] = [farsi_to_finglish(word) for word in NameDictionary["Girl"]]
print("The Finglish girl's name has been successfully added to the dictionary.")

# Save dictionary
with open('NameDictionary.pkl', "wb") as file:
    pickle.dump(NameDictionary, file)

print("A comprehensive dictionary of Persian & Finglish names has been fully maded.")