# 1. input
# 값1 = input("입력하세요 : ")
# print(type(값1))

# 2. 복소수 연습
comp1 = 3 + 4j
comp2 = complex(3, 4)

# 실습 3. 100까지 합을 출력하시오.
# print(list(range(3)))
sum1 = 0
for i in range(101):
    sum1 += i
print(f"합 : {sum1}")

# 실습 3-1
sum2 = sum(list(range(101)))
print(f"합 : {sum2}")

# 실습 3-2
sum3 = sum([i for i in range(101)])
print(f"합 : {sum3}")

# 실습 4. 100까지 홀수와 짝수의 합을 각각 출력하는 
# 프로그램을 작성하시오.
홀수합 = 0 ; 짝수합 = 0
for i in range(0, 101, 2):
    짝수합 += i
for i in range(1, 101, 2):
    홀수합 += i
print(f"홀수합 : {홀수합}, 짝수합 : {짝수합}")

# 실습 4-1
홀수합 = 0 ; 짝수합 = 0
for i in range(101):
    if (i % 2 == 0):
        짝수합 += i
    else:
        홀수합 += i
print(f"홀수합 : {홀수합}, 짝수합 : {짝수합}")

# 실습 4-2
짝수합 = [ i for i in range(101) if i % 2 == 0]
홀수합 = [ i for i in range(101) if i % 2 == 0]
print(f"홀수합 : {홀수합}, 짝수합 : {짝수합}")

# 실습5 리스트 정렬
exlist = [1, 3, 9, 2, 5]
relist1 = exlist.sort()
print(relist1)
print(exlist)

exlist = [1, 3, 9, 2, 5]
relist2 = sorted(exlist)
print(relist2)

l1 = [1, 2, 3]
l2 = l1
l2[2] = 100
print(l1)

l3 = list(l1)
l3[2] = 1000
print(l1)
print(l3)

a = [1, 2, 3]
print(a[::-1]) # 역순으로 출력
print(a[:-1]) # 제일 마지막 item을 제외하고 출력

prices = [135, -545, 922, 356, -992, 217]
mprices = [i if i>0 else 0 for i in prices]
print(mprices)

list1 = [10, 20, 30, 40, 50]
list2 = [sum(list1[0:i+1]) for i in range(len(list1))]
print(list1)
print(list2)