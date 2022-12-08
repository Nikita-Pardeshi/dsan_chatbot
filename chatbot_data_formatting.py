# import required libraries
import pandas as pd
import json


# Read the dataset
df= pd.read_csv("data/BERT_QA_corrected.csv")


# Data Transformation (Convert data into required json format for processing)
# create input 'intents.json' file
intent_json={}
list_of_tags=[]
# loop through the dataframe to fetch the patterns and responses for each tag
for i in range(0, len(df['tag'].unique())):
    d={}
    d['tag']=df['tag'].unique()[i]
    d['patterns']=df.loc[df['tag']==df['tag'].unique()[i], 'question'].tolist()
    d['responses']=df.loc[df['tag']==df['tag'].unique()[i], 'context'].tolist()
    d['context']=[""]
    list_of_tags.append(d) 
intent_json['intents']=list_of_tags
print(intent_json)


# Save json file
with open("data/intents.json", "w") as fp:
    json.dump(intent_json,fp)