# exception
while True:
  try:
    x = int(input('请输入一个整数：'))
    break
  except ValueError:
    print('输入错误，请重新输入')

print(f'你输入的是{x}')