from sklearn.tree import DecisionTreeClassifier, export_text

a1=['T','T','T','F','F','F']
a2=['T','T','F','F','T','T']
y=['+','+','-','+','-','-']

X=[[1 if a1[i]=='T' else 0,1 if a2[i]=='T' else 0] for i in range(len(a1))]
clf=DecisionTreeClassifier().fit(X,y)
tree=export_text(clf,feature_names=['a1','a2'])
print(tree)
