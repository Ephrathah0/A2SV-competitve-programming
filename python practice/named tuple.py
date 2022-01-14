from collections import namedtuple
N = int(input())
columns = ",".join(input().split())
Student = namedtuple('Student' ,columns)
sum_marks = 0 
  
for i in range(N):
    row = input().split()
    stud = Student(*row)
    sum_marks += int(stud.MARKS)
print(sum_marks/N)       
        
        
