import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_text

# Data setup
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Windy': ['False', 'True', 'False', 'False', 'False', 'True', 'True', 'False', 'False', 'False', 'True', 'True', 'False', 'True'],
    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

# Create DataFrame
df = pd.DataFrame(data)

# Encode categorical features
le_outlook = LabelEncoder().fit_transform(df['Outlook'])
le_temp = LabelEncoder().fit_transform(df['Temperature'])
le_humidity = LabelEncoder().fit_transform(df['Humidity'])
le_windy = LabelEncoder().fit_transform(df['Windy'])
le_play = LabelEncoder().fit_transform(df['Play'])

# Prepare features and target
X = pd.DataFrame({
    'Outlook': le_outlook,
    'Temperature': le_temp,
    'Humidity': le_humidity,
    'Windy': le_windy
})

y = le_play

# Fit decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Export decision tree in text format
tree_text = export_text(clf, feature_names=['Outlook', 'Temperature', 'Humidity', 'Windy'])
print(tree_text)
