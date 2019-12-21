import pandas as pd 
from sklearn.preprocessing import Imputer #depriciated 
from sklearn.impute import SimpleImputer #new


data = pd.read_csv("Data.csv")

X = data.iloc[:,:-1].values
y = data.iloc[:,3]

# print("y:",y)

# print("X 1:2", X[:,1:2])
# print("X 1:3", X[:,1:3])
Imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)

# Imputer = SimpleImputer(missing_values='NaN', strategy='mean')
Imputer_X = Imputer.fit(X[:,1:3])
X[:,1:3] = Imputer_X.transform(X[:,1:3])
# Imputer_X = Imputer.fit_transform(X[:,1:3])

print("X:",X)
