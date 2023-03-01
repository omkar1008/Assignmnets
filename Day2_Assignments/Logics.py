
# Print prime and divisible by 7
list1 = [1, 21, 4, 10, 30, 49, 60, 70, 80 , 100, 1]
divisibleBy7 = []
primeNumbers = []
for each in list1:
    if each % 7 == 0:
        divisibleBy7.append(each)
    if each % 2 !=0:
        primeNumbers.append(each)

print('divisible by 7', divisibleBy7)
print('Prime Numbers', primeNumbers)

# Change odd characters to uppercase and even to lowercase in a string.

string_var = 'Jktech training'
UpdatedString = ''
for each in range(len(string_var)):
    if each % 2 == 0:
        UpdatedString += string_var[each].lower()
    else:
        UpdatedString += string_var[each].upper()

print(UpdatedString)

# count number of words in a string.Cover multiple spaces,tabs and lines as delimiters
test = "hello world  \n \n  python, java  \t platform"
numberofwords = len(test.split())
print ("The number of words in string are : ", numberofwords)