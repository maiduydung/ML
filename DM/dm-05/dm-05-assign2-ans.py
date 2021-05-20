# ### DM-05 Assignment 2: Sample program for interactive naive Bayes classifier 

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import POSStopFilter, LowerCaseFilter
from IPython.core.display import display

csv_in = 'text_dogs.csv'
df = pd.read_csv(csv_in, skiprows=0, delimiter=',', header=0)
print('Read {} train data'.format(df.shape[0]))

X_train = df['text']
y_train = df['category']

vectorizer = CountVectorizer(token_pattern='(?u)\\b\\w+\\b')
vectorizer.fit(X_train)

X_train_bow = vectorizer.transform(X_train)
model = MultinomialNB(alpha=1.0)
model.fit(X_train_bow, y_train)

token_filters = [ POSStopFilter(['助詞','助動詞']),
                  LowerCaseFilter(),
                ]
tokenizer = Tokenizer()
analyzer = Analyzer(tokenizer=tokenizer, token_filters=token_filters)

while True:
  s = input('Japanese text about dogs: ')
  #s = '大胆で知性があり、好奇心の強い超小型犬'  # sample1
  #s = '温和で忍耐力が強く、しつけやすい大型犬'  # sample2
  #s = '短毛の小型犬で、忠実な一方警戒心が強く番犬に適している'  # sample3
  if s == '': break
  X_test = [' '.join([t.base_form for t in analyzer.analyze(s)])]
  print(X_test[0])
  X_test_bow = vectorizer.transform(X_test)
  proba = model.predict_proba(X_test_bow)
  results = pd.DataFrame(proba, columns=model.classes_)
  display(results)
  print('Prediction:', model.predict(X_test_bow)[0])

