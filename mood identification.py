from textblob import TextBlob
wiki = TextBlob("I am very happy")
print(wiki.tags)

print(wiki.words)
print(wiki.sentiment.polarity)

a = input(" press Enter to Exit")
