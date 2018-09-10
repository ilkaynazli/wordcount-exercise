# put your code here.
my_file = open('test.txt')
count_words = {}
for line in my_file:
    words= line.split()
    for word in words:
        word = word.strip(",.?!*/:;#$%-+_&()[]")
        count_words[word.lower()] = count_words.get(word.lower(),0)+1
for word, count in count_words.items():
    print (f'{word} {count}')

