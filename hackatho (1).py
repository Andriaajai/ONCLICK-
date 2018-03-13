#this is the working one.

import re
pword=0
nword=0
#positive word list
file = open('positive-words.txt', 'r')
text = file.read().lower()
file.close()
text = re.sub('[^a-z\ \']+', " ", text)
positive_words = list(text.split())
#negative word list
file = open('negative-words.txt', 'r')
text = file.read().lower()
file.close()
text = re.sub('[^a-z\ \']+', " ", text)
negative_words = list(text.split())
print(negative_words)
#para break
sentiment_val=0
print("Program to review teacher feedback")
file = open('review.txt', 'r')
text = file.read().lower()
file.close()
text = re.sub('[^a-z\ \']+', " ", text)
review= list(text.split())
print(review)
for word in review:
	if(word in positive_words):
		sentiment_val=sentiment_val+1
		pword=pword+1
	if(word in negative_words):
		sentiment_val=sentiment_val-1
		nword=nword-1

if(sentiment_val>0):
	print('Well done')
else:
	print('Needs improvement')
print(pword)
print(nword)
