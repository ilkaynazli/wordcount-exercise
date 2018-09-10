# put your code here.
my_file = open('twain.txt')
count_words = {}
for line in my_file:
    words= line.split()
    for word in words:
        count_words[word] = count_words.get(word,0)+1
for word, count in count_words.items():
    print (f'{word} {count}')

