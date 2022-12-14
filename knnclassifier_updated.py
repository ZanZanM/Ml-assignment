# -*- coding: utf-8 -*-
"""kNNClassifier_updated.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jv-gFYAC-d47eA_vS0oDf2LLKHs2ONvV

##1. Dataset
"""

weather = ['sunny', 'overcast', 'sunny', 'rainy', 'overcast', 'rainy'] #weather features
temperature = ['hot', 'mild', 'hot', 'cold', 'mild', 'mild'] #temperature features
play = ['no', 'yes', 'no', 'no', 'yes', 'yes'] #Labels - output of the classifier

"""## 2. Vectorization of data

"""

from sklearn import preprocessing
le = preprocessing.LabelEncoder() #Create a label encoder
weather_encoded = le.fit_transform(weather) #Fit the encoder on the weather features.
print(weather_encoded)
temperature_encoded = le.fit_transform(temperature) #Fit the encoder on the temperature features.
print(temperature_encoded)
play_encoded = le.fit_transform(play) #Labels encoded
print(play_encoded)
#!Remember that you should define different label encoders for each feature vector if you will use back-transform or any other feature of the label encoder.

features = list(zip(weather_encoded, temperature_encoded)) #Make tuples from the two sets of features
print(features)

"""## 3. Build a KNN Classifier"""

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3, metric = 'euclidean') #Build a 3NN classifier using Euclidean distance metric.
model.fit(features, play_encoded) #Fit the KNN classifier on the training set and the corresponding labels.

"""## 4. Build a Naive Bayes Classifier"""

from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB() # Build a Multinomial Naive Bayes classifier.
model.fit(features, play_encoded) # Fit the Naive Bayes classifier on the training set and the corresponding labels.
result = model.predict([[0,1]]) #Prediction
print(result)
print(list(le.inverse_transform([1])))

"""## 4. Test/Prediction"""

result = model.predict([[0,1],[0,2]]) #Prediction for two instances: [overcast, hot], [overcast, mild] 
print(result) 
print(list(le.inverse_transform([1]))) #Back-transform to convert the numerical attribute produced as a result to its string value.