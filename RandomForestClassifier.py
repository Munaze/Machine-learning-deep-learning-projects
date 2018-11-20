from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators = 3)
x = [[181,80,44],[177,70,43],[160,60,38],[166,654,40],[190,90,47],
[175,64,39],[177,70,40],[171,75,42],[181,85,43]]

y = ['male','female','female','male','female','male','male','female','male']

forest.fit(x,y)

pridiction = forest.predict([[190,70,43]])

print (pridiction)

a= input("Press Enter to Exit")


