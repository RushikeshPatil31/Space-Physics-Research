import pandas as pd
import datetime
import numpy as np

df=pd.read_excel("Themis Jan 16 2018",header=None)
f=open("output.txt",mode='w+')
index=df.index
nRows=len(index)
counter=0
final = []
value = 0
average = 0.0
counter2=0

data=df.iloc[counter]
date = data[0]
time = data[1]
temp_time,temp_hour = time.minute,time.hour
while counter<nRows+1:
    if(counter>=nRows):
        average = value / counter2
        f.write(str(average)+'\n')
        break
    data=df.iloc[counter]
    time = data[1]
    if date == data[0] and temp_time == time.minute and temp_hour==time.hour:
        value+=data[2]
        counter2+=1  
    else:
        average = value / counter2
        f.write(str(average)+'\n')
        value = 0
        counter2 = 0
        data=df.iloc[counter]
        date = data[0]
        time=data[1]
        temp_time = time.minute
        temp_hour=time.hour
        counter-=1
    counter+=1
   

print(*final,sep='\n')
f.close()
