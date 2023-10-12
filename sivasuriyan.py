import numpy as np
import pandas as pd
from sklearn.preprocessing import  StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

diabetes_data = pd.read_csv('dia.csv')
diabetes_data.head()
print(diabetes_data.head())
diabetes_data.shape
print(diabetes_data.shape)
diabetes_data.describe
print(diabetes_data.describe)
diabetes_data['Outcome'].value_counts()
print(diabetes_data['Outcome'].value_counts())
diabetes_data.groupby('Outcome').mean()
print(diabetes_data.groupby('Outcome').mean())

X= diabetes_data.drop( columns = 'Outcome', axis = 1)
Y = diabetes_data['Outcome']
print(Y)

scaler = StandardScaler()
scaler.fit(X)
strd_x_scl = scaler.transform(X)
print(strd_x_scl)

X = strd_x_scl

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2,stratify = Y,random_state= 1)

print(X.shape,X_train.shape,X_test.shape)

classifier = svm.SVC(kernel= 'linear')

classifier.fit(X_train,Y_train)

X_train_prdctn = classifier.predict(X_train)
trn_dta_accry = accuracy_score(X_train_prdctn,Y_train)
print("Training Data Accuracy : ",trn_dta_accry)

X_test_prdctn = classifier.predict(X_test)
tst_dta_accry = accuracy_score(X_test_prdctn,Y_test)
print("Test Data Accuracy : ",tst_dta_accry)

input_data = (7,196,90,0,0,39.8,0.451,41)

inp_as_npay = np.asarray(input_data)

inp_reshpe = inp_as_npay.reshape(1,-1)

std_data = scaler.transform(inp_reshpe)
print(std_data)


predtn = classifier.predict(std_data)
print(predtn)

if(predtn[0] == 0 ):
    print("The Person is not diabetic")
else:
    print("The Person is diabetic")
