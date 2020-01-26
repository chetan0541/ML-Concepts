import pandas as pd
import re 
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

data = pd.read_csv("Data/Restaurant_Reviews.tsv", delimiter='\t', quoting= 3) # delimiter \t specifies the separation, quoting = 3 ignores quotes. Not necessary 


# Cleaning the texts
review = re.sub('[^a-zA-Z]',' ', data['Review'][0]) #keeps a-z and A-Z, replaces useless stuff with space.
review = review.lower() #Tolower case
# print(review)

# Get rid of irrelevant words
# nltk.download('stopwords')
#split the review into separate words
review = review.split() #easier to clean when separated 
ps = PorterStemmer()
review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]  #set makes it faster and  ps.stem stemms every word and puts them in the review
# reverting review back to a sentence
review = ' '.join(review)

print(review)