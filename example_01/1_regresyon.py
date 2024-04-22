from sklearn.linear_model import LinearRegression
import pandas as pd 
import scipy
df=pd.read_csv("student.csv")
x=df[["number_courses","time_study"]]
y=df[["Marks"]]
l=LinearRegression()
model=l.fit(x,y)

df['Marks'].max()
model.score(x,y)