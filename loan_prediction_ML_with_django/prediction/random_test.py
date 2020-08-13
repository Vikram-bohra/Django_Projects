def modeltrain(filename):
	import pandas as pd


	# Importing the dataset
	dataset = pd.read_csv(filename)


	dataset['Gender'].fillna(dataset['Gender'].mode()[0], inplace=True)
	dataset['Married'].fillna(dataset['Married'].mode()[0], inplace=True)
	dataset['Dependents'].fillna(dataset['Dependents'].mode()[0], inplace=True)
	dataset['Loan_Amount_Term'].fillna(dataset['Loan_Amount_Term'].mode()[0], inplace=True)
	dataset['Credit_History'].fillna(dataset['Credit_History'].mode()[0], inplace=True)
	dataset['Self_Employed'].fillna(dataset['Self_Employed'].mode()[0], inplace=True)
	dataset['LoanAmount'].fillna(dataset['LoanAmount'].mean(), inplace=True)



	dataset.Gender.replace({'Male':1,'Female':0},inplace=True)



	dataset.Married.replace({'Yes':1,'No':0},inplace=True)

	dataset.Dependents.replace({'0':3,'1':0,'2':2,'3+':1},inplace=True)
	dataset.Education.replace({'Graduate':0,'Not Graduate':1},inplace=True)
	dataset.Self_Employed.replace({'Yes':1,'No':0},inplace=True)

	dataset.Property_Area.replace({'Urban':2,'Rural':0,'Semiurban':1},inplace=True)

	dataset.Loan_Status.replace({'Y':1,'N':0},inplace=True)


	X = dataset.iloc[:, 1:12].values
	y = dataset.iloc[:, 12].values

	# Feature Scaling
	from sklearn.preprocessing import StandardScaler
	sc = StandardScaler()
	X = sc.fit_transform(X)


	from sklearn.model_selection import train_test_split
	X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)


	#Applying the model
	from sklearn.ensemble import RandomForestClassifier
	classifier = RandomForestClassifier(n_estimators = 100, criterion = 'entropy')
	classifier.fit(X_train, y_train)
	import pickle

	pickle.dump(classifier, open('model.pkl', 'wb'))
	# save the scaler
	pickle.dump(sc, open('scaler.pkl', 'wb'))

def retrain(filename):
	import pandas as pd


	# Importing the dataset
	dataset = pd.read_csv(filename)


	dataset['Gender'].fillna(dataset['Gender'].mode()[0], inplace=True)
	dataset['Married'].fillna(dataset['Married'].mode()[0], inplace=True)
	dataset['Dependents'].fillna(dataset['Dependents'].mode()[0], inplace=True)
	dataset['Loan_Amount_Term'].fillna(dataset['Loan_Amount_Term'].mode()[0], inplace=True)
	dataset['Credit_History'].fillna(dataset['Credit_History'].mode()[0], inplace=True)
	dataset['Self_Employed'].fillna(dataset['Self_Employed'].mode()[0], inplace=True)
	dataset['LoanAmount'].fillna(dataset['LoanAmount'].mean(), inplace=True)



	dataset.Gender.replace({'Male':1,'Female':0},inplace=True)
	dataset.Married.replace({'Yes':1,'No':0},inplace=True)
	dataset.Dependents.replace({'0':3,'1':0,'2':2,'3+':1},inplace=True)
	dataset.Education.replace({'Graduate':0,'Not Graduate':1},inplace=True)
	dataset.Self_Employed.replace({'Yes':1,'No':0},inplace=True)
	dataset.Property_Area.replace({'Urban':2,'Rural':0,'Semiurban':1},inplace=True)
	dataset.Loan_Status.replace({'Y':1,'N':0},inplace=True)


	X = dataset.iloc[:, 1:12].values
	y = dataset.iloc[:, 12].values


	# Feature Scaling
	from pickle import load
	sc = load(open('scaler.pkl', 'rb'))
	X = sc.transform(X)



	# Retrainin the model
	from pickle import load
	classifier = load(open('model.pkl', 'rb'))

	classifier.fit(X, y, batch_size = 10,epochs = 100)


	import pickle

	pickle.dump(classifier, open('model.pkl', 'wb'))
	# save the scaler
	pickle.dump(sc, open('scaler.pkl', 'wb'))

def predict(val):
	import numpy as np
	val = np.array(val)
	val = val.reshape(1,-1)
	from pickle import load
	sc = load(open('scaler.pkl', 'rb'))
	val = sc.transform(val)
	classifier = load(open('model.pkl', 'rb'))
	y_pred = classifier.predict(val)
	return y_pred
	


