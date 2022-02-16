class Employee:
   'kelas dasar umum untuk semua karyawan'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)


#kita akan membuat objek pertama dari kelas Karyawan
emp1 = Employee("Zakina", 2000)
#kita akan membuat objek kedua dari kelas Karyawan
emp2 = Employee("Merry", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)