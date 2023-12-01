class Greet():
    def __init__(self):
        print("생성자")
    
    def hello(self):
        print("hello")
    
    def hi(self):
        print("hi")


himan1 = Greet()
himan1.hello()

class Student():
    def __init__(self, name, age, like):
        self.name = name
        self.age = age
        self.like = like
    def studentInfo(self):
        print(f"이름:{self.name}, 나이:{self.age} ,좋아하는것: {self.like})")

김철수 = Student("김철수", 17, "축구")
장다인 = Student("장다인", 5, "헬로카봇")
김철수.studentInfo()
장다인.studentInfo()