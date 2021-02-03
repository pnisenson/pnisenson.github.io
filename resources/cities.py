import pandas as pd 

df= pd.read_csv('cities.csv')
df.set_index('City_ID', inplace= True)

result = df.to_html()

text_file = open("cities.html", "w") 
text_file.write(result) 
text_file.close() 
