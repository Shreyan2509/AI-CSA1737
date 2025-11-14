import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# Prepare data using pandas DataFrame
data = {
    'a1': ['T', 'T', 'T', 'F', 'F', 'F'],
    'a2': ['T', 'T', 'F', 'F', 'T', 'T'],
    'label': ['+', '+', '-', '+', '-', '-']
}

df = pd.DataFrame(data)

# Convert features to binary numeric form
df['a1_num'] = df['a1'].apply(lambda x: 1 if x == 'T' else 0)
df['a2_num'] = df['a2'].apply(lambda x: 1 if x == 'T' else 0)

X = df[['a1_num', 'a2_num']]
y = df['label']

# Train Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Export and print tree in text format
tree_text = export_text(clf, feature_names=['a1', 'a2'])
print(tree_text)
