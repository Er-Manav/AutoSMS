import pandas as pd
import random
import math

filename = "samplee.csv" #filepath
df = pd.read_csv(filename)
# print(df)


ID=[]
data = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
leng = len(data)

phone=df['Mobile No.'].count()
for i in range(phone):
    otp=''
    for j in range(8):
        otp+=data[math.floor(random.random()*leng)]
    ID.append(otp)
df['ID']=ID
df=df.sort_values(by=["Name"])
df.to_csv("new.csv",index=False,columns=["Name","Mobile No.","ID"])


df2 = pd.read_csv("new.csv")
# df2 = df2.sort_values(by=['Name']) 


for name,mobile,id in zip(df['Name'], df['Mobile No.'],df['ID']):
    print("Dear " + name + ", Your ID is " + id + " send at mobile: " + str(mobile))

