from urllib.request import urlopen
import json 
import pandas as pd
BASE_URL="https://jsonplaceholder.typicode.com/"
ENDPOINT="todos"
response = urlopen(BASE_URL+ENDPOINT)
data =json.loads(response.read())
df = pd.DataFrame(data)
df=df[df.completed !=1]
a = df.drop(["id","title"],axis=1)
df2 = a.rename(columns = { 'completed': 'pending todos'}, inplace = False)
c=df2.groupby(['userId']).count()
print(c)
