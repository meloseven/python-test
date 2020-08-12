#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# 注释

print('hello!')

if True:
    print('xxx')
else:
    print('yyy')

x = 1 + \
  2 + \
  3

print(x)

total = ['item_one', 'item_two', 'item_three',
  'item_four', 'item_five']
print(total)

str1 = ''''scs' '123' 


233'''
print(str1)

str2 = '\n\n1221'
print(str2)


str3='meloseven'
 
print(str3)                 # 输出字符串
print(str3[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str3[0])              # 输出字符串第一个字符
print(str3[2:5])            # 输出从第三个开始到第五个的字符
print(str3[2:])             # 输出从第三个开始后的所有字符
print(str3 * 2)             # 输出字符串两次
print(str3 + '你好') 
print('------------------------------')
 
print('hello\nrunoob'.split(' '))      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
