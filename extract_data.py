'''import requests
import pandas as pd

response=requests.get("https://jsonplaceholder.typicode.com/users")
data=response.json()
df=pd.DataFrame(data)
df=df[["id","name"]]
print(df)'''

import os 

token=os.getenv("TOKEN")

print(f"Token= ${token}")

if token=="1234":
    print("Valid")
else:
    print("Invalid")