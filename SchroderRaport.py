from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer
from krovetzstemmer import Stemmer
from nltk.stem import RegexpStemmer

import pandas as pd
from nltk.tokenize import word_tokenize
import nltk
import numpy as np
import matplotlib.pyplot as plt

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowballeng = SnowballStemmer("english")
krovetz = Stemmer()
regexp = RegexpStemmer('ing$|s$|e$|able$', min=4)


df = pd.read_csv("SMSSpamCollection", delimiter='\t', names=['ID', 'MESSAGE'])
# print(df.head())

tresc = df['MESSAGE']
all_words = []
for t in tresc:
    words = word_tokenize(t)
    for w in words:
        all_words.append(w)

all_words = nltk.FreqDist(all_words)
all_words = [x for x in all_words if x not in set(nltk.corpus.stopwords.words('english')) and x.isalpha() and len(x) > 3]

print('Liczba słów: {}'.format(len(all_words)))
print("{0:20}{1:20}{2:20}{3:20}{4:20}{5:20}".format("Word","Porter Stemmer","Lancaster Stemmer", "Snowball Stemmer", "Krovetz Stemmer", "Regexp Stemmer"))
porownarka = []
for w in all_words:
    temp = [porter.stem(w),lancaster.stem(w),snowballeng.stem(w),krovetz.stem(w),regexp.stem(w)]
    print("{0:20}{1:20}{2:20}{3:20}{4:20}{5:20}".format(w,porter.stem(w),lancaster.stem(w),snowballeng.stem(w),krovetz.stem(w),regexp.stem(w)))
    porownarka.append(temp)

pary = []
for x in range(5):
    col = []
    for y in range(5):
        col.append(0)
    pary.append(col)

for word in porownarka:
    for w in range(0,5):
        if word[0] == word[w]:
            pary[0][w]+=1
        if word[1] == word[w]:
            pary[1][w]+=1
        if word[2] == word[w]:
            pary[2][w]+=1
        if word[3] == word[w]:
            pary[3][w]+=1
        if word[4] == word[w]:
            pary[4][w]+=1

for x in range(5):
    for y in range(5):
        pary[x][y] /= len(all_words)


print("")
print("{:8}".format("Stemmatyzer Porter Lancaster Snowball Krovetz Regexp"))
nazwy = ["Porter","Lancaster", "Snowball", "Krovetz", "Regexp"]

i = 0
for row in pary:
    print("{:8}".format(nazwy[i]), end=" ")
    for col in row:
        print("{:8.3f}".format(col), end=" ")
    print("")
    i+=1

fig = plt.figure(1)
nazwy2 = ["Porter Stemmer","Lancaster Stemmer", "Snowball Stemmer", "Krovetz Stemmer", "Regexp Stemmer"]
plt.title("Porównanie Stemmatyzatorów")
x = np.array(range(0,5))
for i, array in enumerate(pary):
    plt.plot(x, array, color = np.random.rand(3, ), marker = "o", label = nazwy2[i])

plt.legend(loc = "center left", bbox_to_anchor=(1, 0.5), borderaxespad=0.)
fig.savefig('wykres', bbox_inches='tight')
plt.show()

#wykres powinien zapisać się w całości w pliku