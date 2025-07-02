def count_word_frequency(file_name):
    word_count={}
    with open(file_name,'r') as file:
        for line in file:
            words=line.split()
            for word in words:
                word=word.lower().strip(",.:;!")
                word_count[word]=word_count.get(word,0)+1
    return word_count
print(count_word_frequency(file_name="sample.txt"))