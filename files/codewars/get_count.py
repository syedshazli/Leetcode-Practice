def get_count(sentence):
    count = 0
    for i in sentence:
        if i == 'a' or i == 'e' or i == 'o' or i == 'i' or i == 'u':
            count +=1
    return count
    pass
