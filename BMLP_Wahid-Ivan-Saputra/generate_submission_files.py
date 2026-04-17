import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
from datetime import datetime
import os

# Load data
url = "https://raw.githubusercontent.com/shaecodes/Analyzing-Transaction-Data-For-Fraud-Detection/main/data/bank_transactions.csv"
df = pd.read_csv(url)

# Preprocessing
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])
df['PreviousTransactionDate'] = pd.to_datetime(df['PreviousTransactionDate'])
df['TransactionHour'] = df['TransactionDate'].dt.hour
df['DayOfWeek'] = df['TransactionDate'].dt.dayofweek
df['TimeSinceLast'] = (df['TransactionDate'] - df['PreviousTransactionDate']).dt.total_seconds().abs()

cols_to_drop = ['TransactionID', 'AccountID', 'DeviceID', 'IP Address', 'MerchantID', 'TransactionDate', 'PreviousTransactionDate']
df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])

# Encoding
le = LabelEncoder()
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col] = le.fit_transform(df[col])

# Scaling
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Clustering
kmeans = KMeans(n_clusters=6, random_state=42, n_init='auto')
kmeans.fit(df_scaled)
df['Target'] = kmeans.labels_

# Save required files
output_dir = "BMLP_Wahid-Ivan-Saputra"
os.makedirs(output_dir, exist_ok=True)

df.to_csv(os.path.join(output_dir, "data_clustering.csv"), index=False)
joblib.dump(kmeans, os.path.join(output_dir, "model_clustering.h5"))

# Load decision tree model if it exists or train it
# From the notebook, it seems standard. Let's just copy it if available or train it quickly.
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X = df.drop('Target', axis=1)
y = df['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
joblib.dump(dt, os.path.join(output_dir, "decision_tree_model.h5"))

print("Files generated successfully in", output_dir)
