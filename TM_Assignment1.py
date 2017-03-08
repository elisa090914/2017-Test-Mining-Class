import nltk

text = open('building_global_community.txt').read()
lines = [line.strip() for line in text.splitlines()]

from nltk import word_tokenize
words = []

for line in lines:
    # Split words in each sentence by using word_tokenize()
    for word in word_tokenize(line):
        words.append(word)

words = [word.lower() for word in words]

from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))

filted_words = [word for word in words
                if (word.isalpha() or word.isdigit() or word.isalnum()) and word not in stopwords]


from collections import Counter

counter = Counter(filted_words)
print(counter.most_common(20))
