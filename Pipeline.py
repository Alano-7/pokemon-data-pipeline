#This is importing all the modules and tools that im gonna need

import requests#Communicating with your data source from the internet
import json #Reads the data that the API(URL) sends back
import pandas as pd #Panda for structuring the data into a table
import time# To be "polite" and pause betweem requests. Essentilyy gives the server some breathing room in between each request to prevent spam.
import sqlalchemy
from sqlalchemy import create_engine, text
import mysql.connector
from urllib.parse import quote_plus

#PHASE 1: This is the E in ETL. Here is where Im going to ingest and extract the information
####################################################################################################
######################################################################################################
pokemon_list=["pikachu","charizard","bulbasaur","squirtle","mewtwo","gyarados","jigglypuff"] # This is the input for the entire raw pipeline. "Shopping list"

all_pokemon_data=[] # This is a emmpty place for you to input the clean data that you want."Like the shopping cart"

for name in pokemon_list:   #This is where the loop begins.For loop.
    print(f"Fetching data for {name}") # This is  just logging. To make things prettier and more understandable for you in the terminal.
    url=f"https://pokeapi.co/api/v2/pokemon/{name}"# This is the first part of the data ingestion. You build the URL/ Insert the api and in this case left the last part of the URL as variable name so that, it can change
    response=requests.get(url)# This request.get, gets the data from the internet

    if response.status_code !=200: #This is just some error handling. 404 for example is a gateway error.
        print(f"Couldnt find data for {name}")
        continue#Take not of the continue thing over here. WHich means despite if an exception occurs, you continue with the program.

    data=response.json() #This line essentially coverts the response variable into json format and then puts it in the data variable now.

#This is more or less where PHASE 2 will begin
#KEEP IN MIND THAT ITS STILL PART OF THE FOR LOOP!!
    extracted_data = {      # This is  the start of the data transformation. this is liek setting up table. I want these
        'name': data['name'],
        'height': data['height'],
        'weight': data['weight'],
        'attack': None, # fill with none, good habit.
        'defense': None,
    }

    for x in data["stats"]:
        stat_name=x["stat"]["name"]
        if stat_name in extracted_data:
            extracted_data[stat_name]=x["base_stat"]
    

    all_pokemon_data.append(extracted_data)
    print(f"Succesfully printed {name}")

    time.sleep(0.5)

df=pd.DataFrame(all_pokemon_data)

print(df)
print(f"Strongest Pokemon:{df.loc [df['attack'].idxmax(), 'name']}")
print(f"Most Resilient pokemon: {df.loc[df['defense'].idxmax(),'name']}")

#This is phase 3 with mySQL instead of sqite

db_config={
    "user":"root",
    "password": "Shakatak@1",
    "host": "localhost",
    "database":"pokemon_db"
}

encoded_password=quote_plus(db_config["password"])
db_connection_str=f"mysql+mysqlconnector://{db_config['user']}:{encoded_password}@{db_config['host']}/{db_config['database']}"

engine=create_engine(db_connection_str)

try:
    with engine.connect() as conn:
        df.to_sql("pokemon",con=conn, if_exists="replace",index=False)
        print("[SUCCESS] data loaded into mySQL")

        result=conn.execute(text("SELECT * FROM pokemon LIMIT 7;"))
        rows=result.fetchall()
        column_names=result.keys()

        print(column_names)
        for row in rows:
            print(row)
except Exception as e:
    print(f"Database operation failed: {e}")








#2nd attempt

'''
url = "https://pokeapi.co/api/v2/pokemon/pikachu"  #Ths is is a API and within there, there is the endpoint for pikachu
response=requests.get(url) # You get different types of requests, this is a GET request.
data=response.json()  #Storing the data in a variable

extracted_data={
    "name":data["name"],
    "height":data["height"],
    "weight":data["weight"],
    "attack":None,
    "defense":None,
    
}

for x in data["stats"]:
    stat_name=x["stat"]["name"]
    if stat_name in extracted_data:
        extracted_data[stat_name]=x["base_stat"]

df=pd.DataFrame([extracted_data])        

print(df)

'''













#1st Attempt

'''
print(f"If 200 it works, if 404 there is an error. The result is: {response.status_code}")# This is the HTTP status code(202 = success and 404=Error)

print(json.dumps(data, indent=4))  #Printing the raw response

name=data["name"]
height=data["height"]
weight=data["weight"]
base_attack_stat=None
for x in data["stats"]:
    if x["stat"]["name"]=="attack":
        base_attack_stat=x["base_stat"]
        break
base_defense_stat=None
for x in data ["stats"]:
    if x["stat"]["name"]=="defense":
        base_defense_stat=x["base_stat"]
        break



print(f"Name: {name}")
print(f"Height: {height}")
print(f"Weight: {weight}")
print(f"Base attacking power is: {base_attack_stat}")
print(f"Base defence is: {base_defense_stat}")

'''