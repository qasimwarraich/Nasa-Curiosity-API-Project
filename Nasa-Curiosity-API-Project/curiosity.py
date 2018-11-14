import requests   # Allows us to retrieve form a URL
import config    #Allows us access to our API Key
import json #Imports json functionality, goal is to produce a file from retrieved info. 
import webbrowser #Import webbrowser library to allow for opening browser tabs. 
from pathlib import Path  #make directory paths? navigate ... 

data = "" #To aide with accessing dump.json 
jsonFilePath = Path.cwd()/"Nasa-Curiosity-API-Project"/"dump.json"  #Declaring variable pointing to json file target path to assist with json file writing. 


try: 
    response=requests.get(f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={config.key}') #Test API URL assigned to Response , used f to assist in formatting to permit config key link. 
    data = response.json()
except Exception as e: #Prints errors to console; debug. 
    print(e)

try:
    with open(jsonFilePath , 'w' ) as bobbeh:  #Opens our defined path using context manager and calls it bobbeh. 
        json.dump(data,bobbeh,indent=4) #Takes dict file from our response and dumps it into bobbeh. Indent to make it more readable. 
except Exception as e: 
    print(e)

webbrowser.open_new_tab(data["photos"][0]["img_src"])  #Opens the first saved json element image url in a browser.
print(len(data)) #Data access testing





#--------DEBUGGING TOOLS--------#

# print(jsonFilePath) #Testing path accuracy 

# print(response.status_code) #API status check 
# print(response.url) #Config check to confirm retrieved URL
# print(response.json()) #Testing json functionalitys



#  print(type(data))
# print(type(response.json()))  #Checking data types

#---------- GRAVEYARD ----------#

#     with open(jsonFilePath , 'w' ) as bobbeh:
#         jason =  json.dumps(response.json(),indent=4)
#         bobbeh.write(jason)
# except Exception as e: 
#    print(e)