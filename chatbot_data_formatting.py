import pandas as pd
import json

df= pd.read_csv("data/BERT_QA_corrected.csv")
# print(df.head())

#create input 'intents.json' file
intent_json={}
list_of_tags=[]
d={}
for i in range(0, len(df['tag'].unique())):
    d={}
    d['tag']=df['tag'].unique()[i]
    d['patterns']=df.loc[df['tag']==df['tag'].unique()[i], 'question'].tolist()
    d['responses']=df.loc[df['tag']==df['tag'].unique()[i], 'context'].tolist()
    d['context']=[""]
    #print(d)
    #print("\n")
    list_of_tags.append(d) 
intent_json['intents']=list_of_tags
print(intent_json)




with open("data/intents.json", "w") as fp:
    json.dump(intent_json,fp)