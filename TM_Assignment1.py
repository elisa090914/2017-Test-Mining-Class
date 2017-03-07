import nltk
nltk.download('punkt')

text = open('building_global_community.txt').read()
lines = [line.strip() for line in text.splitlines()]

from nltk import word_tokenize
words = []
for line in lines:
    split_words = word_tokenize(line)
    words.append(split_words)

for sentence in words:
    for word in sentence:
        sentence[sentence.index(word)] = word.lower()

nltk.download('stopwords')

from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))

filted_words = []
for sentence in words:
    for word in sentence:
        if word.isalpha() or word.isdigit() or word.isalnum():
            if word not in stopwords:
                filted_words.append(word) 

#filted_words

from collections import Counter

counter = Counter(filted_words)
print(counter.most_common(20))
