import pandas as pd
dict={
        "key" : [1,2,3],
        "name" : ["nilesh","mayur","kailas"]

    }
var=pd.DataFrame(dict)
print(var,"\n")

print(var.loc[1],"\n")


df=pd.DataFrame(dict,index=["day1","day2","day3"])
print(df)


#load files into dataframe

file=pd.read_csv("data.csv")
print(file)
