import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_text

# ---------------------------------------
# 1. DATASET INSIDE THE CODE
# ---------------------------------------
data = {
    "a1": ["True","True","False","False","False","True","True","True","False","False"],
    "a2": ["Hot","Hot","Hot","Cool","Cool","Cool","Hot","Hot","Cool","Cool"],
    "a3": ["High","High","High","Normal","Normal","High","High","Normal","Normal","High"],
    "Class": ["No","No","Yes","Yes","Yes","No","No","Yes","Yes","Yes"]
}

df = pd.DataFrame(data)

# ---------------------------------------
# 2. CONVERT STRING LABELS TO NUMBERS
# ---------------------------------------
label_encoders = {}
for column in df.columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# ---------------------------------------
# 3. SPLIT FEATURES & TARGET
# ---------------------------------------
X = df.drop("Class", axis=1)
y = df["Class"]

# ---------------------------------------
# 4. TRAIN DECISION TREE
# ---------------------------------------
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

# ---------------------------------------
# 5. PRINT DECISION TREE RULES
# ---------------------------------------
tree_rules = export_text(model, feature_names=list(X.columns))
print("\n=== DECISION TREE RULES ===")
print(tree_rules)

# ---------------------------------------
# 6. TAKE USER INPUT
# ---------------------------------------
print("\nEnter values for prediction:")

a1_input = input("a1 (True/False): ")
a2_input = input("a2 (Hot/Cool): ")
a3_input = input("a3 (High/Normal): ")

new_sample = pd.DataFrame({
    "a1": [a1_input],
    "a2": [a2_input],
    "a3": [a3_input]
})

# Label encode input
for column in new_sample.columns:
    new_sample[column] = label_encoders[column].transform(new_sample[column])

# Predict
prediction = model.predict(new_sample)[0]
prediction_label = label_encoders["Class"].inverse_transform([prediction])[0]

print("\nPrediction Result =", prediction_label)
