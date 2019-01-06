from sklearn import tree
import numpy as nu
x=[[181,80,44],[177,70,43],[150,0,38],[150,80,55],[155,70,44]]
y=['male','male','female','female','female']
clf=tree.DecisionTreeClassifier()
clf.fit(x,y)
pred=clf.predict([[178,84,50],[150,80,80]])
print(pred)
