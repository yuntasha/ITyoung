a=1;b=2

if a>b:
    print("a가 크다")
elif a<b:
    print("b가 크다")
else:
    print("같다")


max1 = a if a > b else b
print(max1)

name_list = ["홍길동", "정다인", "김철수"]
age_list= [500,5, 12]
for i, k in enumerate(name_list):
    print(name_list[i], end=' ')
    print(age_list[i])

nameTule = (1, 2, 4, 6)
for i in nameTule:
    print(i)

TestSet = (1,2,3,3,3,3,3,4,4,4,4,4)
for i in TestSet:
    print(i)
print(TestSet)


ExDict = {'a': 100, 'b' : 90, 'c' : 75, 'd' : 30}
for i in ExDict:
    print(i)

for i in ExDict:
    print(ExDict[i])


for k, v in ExDict.items():
    print(k,v)


li = [0] * 100

try:
    a = 3
    b = 5
    print(a/b)
except Exception as e:
    print(f"예외 : {e}")
finally:
    print("항상 실행되는 명령어")



try:
    a = 3
    b = 0
    print(a/b)
except ZeroDivisionError:
    print(f'영으로 나누면 안되요.')
except Exception as e:
    print(f"예외 : {e}")
finally:
    print("항상 실행되는 명령어")

def f1(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))

f1(1,2,3,10,20,30, aa=11, bb=12, cc=13)

# C 언어
# x = 3; y = 5 ;
# temp = x;
# x = y;
# y = temp;

a = 1 ; b = 11 ; c = 111
tuple1 = (a, b, c) # packing

(x, y, z) = tuple1

x=3;y=5
print(x,y)
x,y=y,x
print(x,y)