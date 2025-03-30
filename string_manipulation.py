# First Reverse
# Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.
# Examples
# Input: "coderbyte"
# Output: etybredoc


'''
Read the input string 
reserve the each word in a list
split the string with spaces
join the all the words to string 
'''


def FirstReverse(strParam):

  strParam = strParam[::-1]
  
  words = strParam.split()

  reversed_words = [word for word in words]

  strParam = ' '.join(reversed_words)

  return strParam

# keep this function call here 
print(FirstReverse(input()))