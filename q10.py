from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X=[(1,0),(2,0),(3,0),(6,0),(6,0),(7,0),(10,0),(11,0)]
y=["dot","dot","cross","cross","cross","dot","dot","dot"]

X_train,X_test,y_train,y_test = train_test_split(X, y,test_size=0.5,random_state=2)  # dividing into two equal parts

knn = KNeighborsClassifier(n_neighbors=3) # given 3 as neigbours in the questioin 10

knn.fit(X_train,y_train)

predict = knn.predict(X_test)
#print(predict)
print("--------------------------Predicted-----------------------")
for i,j in zip(X_test,predict):
  print(i,":",j)

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

print("\nAccuracy=",accuracy_score(y_test,predict))

print("\nConfusison Matrix =\n",confusion_matrix(y_test,predict))

tn, fp, fn, tp = confusion_matrix(y_test, predict).ravel()
specificity = tn / (tn+fp)
print("\nspecificity=",specificity)

sensitivity=tp/(tp+fn)
print("\nsensitivity",sensitivity)