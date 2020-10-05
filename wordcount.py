# put your code here.


def word_counter(file):
    """Take a file in and count how many words are in it"""

    word_count = {}
    short_poem = open(file)
    
    for line in short_poem:
        word_array = line.split()
        for word in word_array:
            word_count[word] = word_count.get(word,0) + 1

    return word_count

        
    

print(word_counter("test.txt"))