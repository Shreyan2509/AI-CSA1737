from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_text

outlook=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy']
temperature=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
humidity=['High','High','High','High','Normal','Normal','High','High','Normal','Normal','Normal','High','Normal','High']
windy=['False','True','False','False','False','True','True','False','False','False','True','True','False','True']
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

le1=LabelEncoder()
le2=LabelEncoder()
le3=LabelEncoder()
le4=LabelEncoder()
le5=LabelEncoder()

o=le1.fit_transform(outlook)
t=le2.fit_transform(temperature)
h=le3.fit_transform(humidity)
w=le4.fit_transform(windy)
p=le5.fit_transform(play)

X=[[o[i],t[i],h[i],w[i]] for i in range(len(o))]

clf=DecisionTreeClassifier().fit(X,p)
print(export_text(clf,feature_names=['Outlook','Temperature','Humidity','Windy']))
