

# 최대공약수 구하기
import random

a = random.randint(1, 100);  #(최소, 최대)
b = random.randint(1, 100);

print("a: ", a, ", b: ", b)

while a * b != 0: #a, b가 0이 아닌 동안 while문을 돈다
 if a < b:
     b = b - a
 else:
     a = a - b


if a == 0:
    print("gcd: ", b)
else:
    print("gcd: ", a)