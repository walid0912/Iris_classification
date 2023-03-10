
import matplotlib.pyplot as plt #pour plotter les graphes 
from sklearn import svm, datasets #bibliothèque sklearn du machine learning
import numpy as np
import pandas as pd
import seaborn as sns
#loading iris dataset
data = sns.load_dataset("iris")
#displaying the first 10 line sof the dataset 
data.head(10)

#iris dataset infomration
data.info()

#classification SVM 3 classes avec deux attributs
from sklearn.model_selection import train_test_split
#on définit les colones des trois classes 
svm1 = data.replace({"species":  {"setosa":1,"versicolor":2, "virginica":3}})
#on spécifie les variables contenant les caractéristiques et les valeurs à prédire
X = svm1.drop(['species','sepal_width','petal_width'],axis=1)
Y = svm1['species']
#on split le dataset sur deux 20% pour le test et 80% pour le training
X_train1, X_test1, Y_train1, Y_test1 = train_test_split(X, Y, test_size=0.20)

#model training
from sklearn.svm import SVC
svm = SVC()
#classfication
clf=svm.fit(X_train1,Y_train1)
#predicting 
pred = svm.predict(X_test1)
#score de la prédiction effectuée sur le dataset 
svm.score(X_test1,Y_test1)

#fonction pour définir une grille d'affichage
def make_meshgrid(x, y, h=.02):
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    return xx, yy
#fonction pour affichage des contours
def plot_contours(ax, clf, xx, yy, **params):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

#on définit la figure et les axes 
figure, axis = plt.subplots()
# title for the plots
title = ('svm classification 3 classes avec deux attributs sur iris')
# on indique les labels des axes
X0, X1 = X["sepal_length"], X["petal_length"]
xx, yy = make_meshgrid(X0, X1)
plot_contours(axis, clf, xx, yy, cmap=plt.cm.coolwarm, alpha=0.8)
inv_name_dict = {"setosa":1,"versicolor":2, "virginica":3}
colors = [inv_name_dict[item] for item in data['species']]
axis.scatter(X0, X1,c=colors,cmap=plt.cm.coolwarm, s=20, edgecolors='k')
axis.set_ylabel('sepal length feature')
axis.set_xlabel('petal length feature')
axis.set_xticks(())
axis.set_yticks(())
axis.set_title(title)
plt.show()

#les tests de performances 
from sklearn.metrics import classification_report,confusion_matrix
print("Precision, Recall, Confusion matrix, in training\n")
#rapport de clasification avec les metrics precision, recall, f1-score
print(classification_report(Y_test1, pred))
print(confusion_matrix(Y_test1,pred))

#Svm classification avec 2 classes et deux attributs 
from sklearn.model_selection import train_test_split
svm2 = data.replace({"species":  {"setosa":1,"versicolor":2, "virginica":3}})
index = svm2[ (svm2['species'] == 1)].index
svm2.drop(index , inplace=True)
svm2.head(10)

X = svm2.drop(['species','sepal_width','petal_width'], axis = 1)
Y = svm2['species']
X_train2, X_test2, Y_train2, Y_test2 = train_test_split(X, Y, test_size=0.20)
from sklearn.svm import SVC
svm = SVC()
clf=svm.fit(X_train2,Y_train2) 
pred = svm.predict(X_test2)
print("taux de précision du modèle")
svm.score(X_test2,Y_test2)

#plotting 
figure, axis = plt.subplots()
title = ('svm classification sur iris 2 classes et deux attributs')
X0, X1 = X["sepal_length"], X["petal_length"]
xx, yy = make_meshgrid(X0, X1)
plot_contours(axis, clf, xx, yy, cmap=plt.cm.coolwarm, alpha=0.8)
axis.scatter(X0, X1, c="yellow", cmap=plt.cm.coolwarm, s=20, edgecolors='k')
axis.set_ylabel('sepal length')
axis.set_xlabel('petal length')
axis.set_xticks(())
axis.set_yticks(())
axis.set_title(title)
plt.show()

from sklearn.metrics import classification_report,confusion_matrix
print("Precision, Recall, Confusion matrix, in training\n")
# Precision Recall scores
print(classification_report(Y_test2, pred))
# Confusion matrix
print(confusion_matrix(Y_test2,pred))

#classification SVM de deux classes avec quatre attributs
from sklearn.model_selection import train_test_split
svm3 = data.replace({"species":  {"setosa":1,"versicolor":2, "virginica":3}})
act = data[ (data['species'] == 1)].index
data.drop(act , inplace=True)
data.head(10)

X = data.drop(['species'], axis = 1)
Y = data['species']
X.head(10)

#Entrainer le modèle et effectuer la classification SVM 
X_train, X_test, Y_train, Y_testo = train_test_split(X, Y, test_size=0.20)
#classification svm 
from sklearn.svm import SVC
svm = SVC()
clf=svm.fit(X_train,Y_train) 
predi = svm.predict(X_test)
print("taux de précision du modèle ")
svm.score(X_test,Y_testo)
