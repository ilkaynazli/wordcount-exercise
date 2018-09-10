# put your code here.
import sys
from collections import Counter

my_file = open(sys.argv[1])
count_words = {}

# for line in my_file:
#     words= line.split()
#     for word in words:
#         word = word.strip(",.?!*/:;#$%-+_&()[]")
#         count_words[word.lower()] = count_words.get(word.lower(),0)+1
# for word, count in count_words.items():
#     print (f'{word} {count}')


########## further study method ###########

words = (my_file.read()).split()
better_words = []
for word in words:
    word = word.strip(",.?!*/:;#$%-+_&()[]")
    better_words.append(word.lower())

count_words = Counter(better_words)

for word in sorted(count_words):
     print (f'{word} {count_words[word]}')


my_file.close()