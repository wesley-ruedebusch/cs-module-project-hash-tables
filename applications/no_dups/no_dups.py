def no_dups(s):
    s = s.split()

    words = {}
    for word in s:
        if word not in words:
            words[word] = 0
        
        words[word] += 1
    
    l = list(words.keys())
    #print(l)
    string = ' '.join(l)
    return(string)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))