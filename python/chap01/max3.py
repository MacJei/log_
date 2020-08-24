import requests

# 세 정수를 입력받아 최댓값 구하기

print('세 정수의 최대값')
# a = int(input('정수 a 입력: '))
# b = int(input('정수 b 입력: '))
# c = int(input('정수 c 입력: '))
a = 10
b = 20
c = 33


max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c

print(f'최대값은 = {max_val}')

r = requests.get('https://www.google.com')
print(r.status_code)