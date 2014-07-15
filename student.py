# سیستم ساده مدیریت اطلاعات دانش آموزان
 
__metaclass__ = type  # تایید استفاده از کلاس جدید
class StudentInfo:  
    # اختصاص دادن اطلاعات دانش آموزان
    def setStudentInfo(self, name, age, stuId, scores = [0] * 4): #بصورت پیش فرض چهار درس در نظر گرفته شده است
        self.name, self.age, self.stuId, self.scores = (name, age, stuId, scores)
      
    # دریافت نام دانش آموز
    def getName(self):
        return self.name
    # دریافت سن دانش آموز
    def getAge(self):
        return self.age
    # شماره شماره ( آی دی ) دانش آموز
    def getStuId(self):
        return self.stuId
         
    # محاسبه معدل دانش آموز
    def average(self):
        return (sum(self.scores)) / 4 #بصورت پیش فرض چهار درس در نظر گرفته شده است
  
 # دریافت اطلاعات دانش آموز از کاربر   
name, age, stuId = (raw_input("Please enter student's name: "),
                    input("Please enter student's age: "), raw_input("Please enter student's ID: ")) 
# دریافت نمرات دانش آموز از کاربر
scores = []
for i in range(4): #بصورت پیش فرض چهار درس در نظر گرفته شده است
    print "Please enter student's grade %d score: " % (i + 1),
    scores.append(input())
 
stu = StudentInfo()
stu.setStudentInfo(name, age, stuId, scores)
 
# نمایش اطلاعات دانش آموز
print  stu.getName(), stu.getAge(), stu.getStuId(), stu.average()
