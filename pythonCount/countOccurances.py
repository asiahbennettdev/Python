# Python3 count occurances of characters, words, and numbers

# count spaces
string1 = 'Hello world, today was one of those good long days'.count(' ')
print(string1)

string2 = 'Hello world, today was one of those good long days'
print('count of spaces in string1 is {}'.format(string2.count(' ')))


# count letter
string3 = 'aaaabbbbbbcccccc'
print(string3.count('a'))


# count numbers
list1 = [1,2,2,2,3,4,5,5,5,5,6,]
print(list1.count(5))

# count words
string4 = 'Put that thing down flip it and reverse it, flip it'
print(string4.count('flip'))
