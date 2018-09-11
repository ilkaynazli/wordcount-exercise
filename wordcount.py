# put your code here.
import sys
from collections import Counter
from operator import attrgetter

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

# for word in sorted(count_words):
#      print (f'{word} {count_words[word]}')      #sorting alphabetically

# for word in sorted(count_words, key=lambda word: count_words[word]):
#     print (f'{word} {count_words[word]}')         #sorting by value (integers -ascending order)


for word in sorted(count_words, key=lambda word: count_words[word], reverse=True):
    
    print (f'{word} {count_words[word]}')         #sorting by value (integers -descending order)

my_file.close()