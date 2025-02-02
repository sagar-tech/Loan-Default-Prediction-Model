import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split





import os
print(os.listdir("C:\\Users\\DELL\\Desktop\\Class\\Imarticus Project"))





df = pd.read_excel("C:\\Users\\DELL\\Desktop\\Class\\Imarticus Project\\Final.xls")

df.head()



df.default.value_counts()


df.info()


df.isna().mean().round(4)*100



df_main=df[df.columns[df.isnull().mean() < 0.3]]


df_main.isna().mean().round(4)*100


df_main.head()


df_main=df_main.dropna()



df_main.isna().mean().round(4)*100

df_main.default.value_counts()

corr=df_main.corr()
corr

sns.countplot(x="default", data=df_main)
plt.show()

countdefault=len(df_main[df_main.default==1])
countNoNdefault=len(df_main[df_main.default==0])
print("count of dafaulter is: {:.2f}%".format((countdefault/len(df_main.default)*100)))
print("count of NoNdafaulter is: {:.2f}%".format((countNoNdefault/len(df_main.default)*100)))


df_main[['term','month']]=df.term.str.split(expand=True)


df_main.head()


df_main.drop(["month","application_type","purpose","open_acc","collections_12_mths_ex_med","delinq_2yrs","pub_rec","id"],axis=1,inplace=True)


df_main.head()

df_dummies=pd.get_dummies(df_main)

df_dummies.head()


from sklearn.preprocessing import StandardScaler


x=df_dummies.drop(['default'],axis=1).values



y=df_dummies.default.values



scaler = StandardScaler()
x = scaler.fit_transform(x)
x





x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.25,random_state=0)

#LogisticRegression


LR = LogisticRegression()

LR.fit(x_train,y_train)



Y_pred = LR.predict(x_test)

from sklearn import metrics

print('AC is :' ,round(metrics.accuracy_score(y_test,Y_pred),2)*100,'%')


#RandomForest


from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators = 1000, random_state = 1)
rf.fit(x_train, y_train)

acc = rf.score(x_test,y_test)*100
print("Random Forest Algorithm Accuracy Score : {:.2f}%".format(acc))


#Knn


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 2)  # n_neighbors means k
knn.fit(x_train, y_train)
prediction = knn.predict(x_test)

print("{} NN Score: {:.2f}%".format(2, knn.score(x_test, y_test)*100))

#Svm


from sklearn.svm import SVC
svm = SVC(random_state = 1)
svm.fit(x_train, y_train)

acc = svm.score(x_test,y_test)*100
print("Test Accuracy of SVM Algorithm: {:.2f}%".format(acc))


#Naive Bayes


from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(x_train, y_train)

acc = nb.score(x_test,y_test)*100

print("Accuracy of Naive Bayes: {:.2f}%".format(acc))


# DecisionTree

from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()
dtc.fit(x_train, y_train)

acc = dtc.score(x_test, y_test)*100
acc_DecisionTree = acc
print("Decision Tree Test Accuracy {:.2f}%".format(acc))


# Predicted values
y_head_LR = LR.predict(x_test)
knn3 = KNeighborsClassifier(n_neighbors = 2)
knn3.fit(x_train, y_train)
y_head_knn = knn3.predict(x_test)
y_head_svm = svm.predict(x_test)
y_head_nb = nb.predict(x_test)
y_head_dtc = dtc.predict(x_test)
y_head_rf = rf.predict(x_test)


# Confusion_matrix


from sklearn.metrics import confusion_matrix

cm_LR = confusion_matrix(y_test,y_head_LR)
cm_knn = confusion_matrix(y_test,y_head_knn)
cm_svm = confusion_matrix(y_test,y_head_svm)
cm_nb = confusion_matrix(y_test,y_head_nb)
cm_dtc = confusion_matrix(y_test,y_head_dtc)
cm_rf = confusion_matrix(y_test,y_head_rf)




plt.figure(figsize=(24,12))

plt.suptitle("Confusion Matrixes",fontsize=24)
plt.subplots_adjust(wspace = 0.4, hspace= 0.4)

plt.subplot(2,3,1)
plt.title("Logistic Regression Confusion Matrix")
sns.heatmap(cm_LR,annot=True,cmap="Blues",fmt="d",cbar=False, annot_kws={"size": 24})

plt.subplot(2,3,2)
plt.title("K Nearest Neighbors Confusion Matrix")
sns.heatmap(cm_knn,annot=True,cmap="Blues",fmt="d",cbar=False, annot_kws={"size": 24})

plt.subplot(2,3,3)
plt.title("Support Vector Machine Confusion Matrix")
sns.heatmap(cm_svm,annot=True,cmap="Blues",fmt="d",cbar=False, annot_kws={"size": 24})

plt.subplot(2,3,4)
plt.title("Naive Bayes Confusion Matrix")
sns.heatmap(cm_nb,annot=True,cmap="Blues",fmt="d",cbar=False, annot_kws={"size": 24})

plt.subplot(2,3,5)
plt.title("Decision Tree Classifier Confusion Matrix")
sns.heatmap(cm_dtc,annot=True,cmap="Blues",fmt="d",cbar=False, annot_kws={"size": 24})

plt.subplot(2,3,6)
plt.title("Random Forest Confusion Matrix")
sns.heatmap(cm_rf,annot=True,cmap="Blues",fmt="d",cbar=False, annot_kws={"size": 24})

plt.show()



tn, fp, fn, tp = cm_dtc.ravel()


# Sensitivity


print(tp/(tp+fn))


# Specificity


print(tn/(tn+fp))
