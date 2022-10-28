#The author's name is Julia Bub
def count_hashtag(string, sub):
    total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(sub)] == sub:
            total += 1
            index += len(sub)
        else:
            index += 1
    return(total)

print(count_hashtag("#Halloweekend#taylorswift#hello#", "#"))

def hash_spam(string, sub):
    if count_hashtag(string, sub) >= 4 :
        print("this tweet will be considered as a spam!")
    else:
        return None
hash_spam("#Halloweekend#taylorswift#hello#", "#")
