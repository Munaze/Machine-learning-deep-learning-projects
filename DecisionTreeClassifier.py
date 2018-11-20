from sklearn import tree

x = [[181,80,44],[177,70,43],[160,60,38],[166,654,40],[190,90,47],
[175,64,39],[177,70,40],[171,75,42],[181,85,43]]

y = ['male','female','female','male','female','male','male','female','male']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

pridiction = clf.predict([[190,70,43]])

print (pridiction)


input('<press enter>') 



