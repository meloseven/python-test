# reverse 字符串
def reverseWords(inputWord):

  inputWordArr = list(inputWord)

  inputWordArr = inputWordArr[-1::-1]

  return ''.join(inputWordArr)

myname = 'melo'
print(reverseWords(myname))