def word_count(s):
    # Case should be ignored. Output keys must be lowercase.
    s = s.lower()

    # Ignore each of the following characters:
    ignore = ['"', ':', ';', ',', '.', '-', '+',
              '=', '/', "\\", '|', '[', ']', '{',
              '}', '(', ')', '*', '^', '&']
    for char in ignore:
        s = s.replace(char, "")
    s = s.split()
    print(s)

    count = {}
    for word in s:
        if word not in count:
            count[word] = 0
        
        count[word] += 1
    return count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
"""
  for count in string:
        if count not in counts:
            counts[count] = 0
        counts[count] += 1
"""