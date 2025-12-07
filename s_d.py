# Serialization
import json
D = {
    'name':'Aditya',
    'age':'20',
    'country':'India'
}

with open('demo.json','w') as f:
    json.dump(D,f,indent=4)


# Deserialization
with open('demo.json','r') as f:
    print(json.load(f))

 
 # Pickle vs JSON
 # Pickle store data in binary format while JSON stores data in text format.
 # Pickle can serialize a wider range of Python objects compared to JSON.

import pickle
# Serialization
data = {'name':'Aditya', 'age':20, 'is_student':True, 'courses':['Math','Science']}
with open('data.pkl','wb') as f:
    pickle.dump(data,f) 
    
# Deserialization
with open('data.pkl','rb') as f:
    print(pickle.load(f))