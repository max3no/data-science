from sklearn import tree

#[height,weight,show size]
X = [[181,80,33],[177,70,43],[160,60,38],[166,67,39],
    [175,80,42],[168,72,38],[155,48,36],[163,60,38],[171,65,40]]

Y = ['male','female','female','male','male','male','female','male','female']    

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

prediction = clf.predict([[175,81,42]])

print(prediction)