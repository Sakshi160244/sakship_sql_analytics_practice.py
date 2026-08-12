import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",

  user="root",
  password="",
  database="newdabase_db"
)

mycursor = mydb.cursor()

### Database, Table, INSERT & SELECT-------

# s = "INSERT INTO employees (emp_id, name, department, salary, city, age, joining_dates) VALUES ( %s, %s, %s, %s, %s, %s, %s )"
# value = [
# (101, 'Amit Sharma', 'IT', 55000, 'Delhi', 26, '2022-01-15'),
# (102, 'Priya Verma', 'HR', 45000, 'Noida', 28, '2021-08-20'),
# (103, 'Rahul Singh', 'Finance', 60000, 'Gurugram', 31, '2020-11-10'),
# (104, 'Neha Gupta', 'Marketing', 48000, 'Delhi', 25, '2023-03-05'),
# (105, 'Rohit Kumar', 'Sales', 52000, 'Jaipur', 29, '2021-06-18'),
# (106, 'Sneha Patel', 'IT', 65000, 'Ahmedabad', 27, '2022-09-12'),
# (107, 'Vikas Yadav', 'HR', 43000, 'Lucknow', 30, '2019-12-01'),
# (108, 'Pooja Mehta', 'Finance', 70000, 'Mumbai', 32, '2018-05-25'),
# (109, 'Karan Malhotra', 'Sales', 58000, 'Chandigarh', 26, '2024-02-14'),
# (110, 'Anjali Sinha', 'Marketing', 50000, 'Patna', 24, '2023-07-08')]

# mycursor.executemany(s, value)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

## 1 show all Show all employee records.
s= "SELECT * FROM employees"
mycursor.execute(s)
result = mycursor.fetchall()
print("------Show all employee records------")
for x in result:
    
    print(x)

## 2 show only employees name
e = "SELECT name FROM employees"
mycursor.execute(e)
result = mycursor.fetchall()
print("-----show only employees name------")
for x in result:
    
    print(x)

## 3 show employees name and salary

e = "SELECT name, salary FROM employees"
mycursor.execute(e)
result =mycursor.fetchall()
print("------show employees name and salary------")
for x in result:
    
    print(x)

## 4 show department column

d = "SELECT department FROM employees"
mycursor.execute(d)
result= mycursor.fetchall()
print("------show department column------")
for x in result:
    
    print(x)

## 5 show city name

c= "SELECT city FROM employees"
mycursor.execute(c)
result= mycursor.fetchall()
print("-----show city name------")
for x in result:
    
    print(x)

### 6 Show employee name, city and age.

a = "SELECT name, city, age FROM employees"
mycursor.execute(a)
result = mycursor.fetchall()
print("-----Show employee name, city and age-----")
for x in result:
    print(x)

### 7 Show salary and department.

d= "SELECT salary, department FROM employees"
mycursor.execute(d)
result= mycursor.fetchall()
print("------Show salary and department------")
for x in result:
    print(x)

### 8 Show joining date.

j= "SELECT joining_dates FROM employees"
mycursor.execute(j)
result = mycursor.fetchall()
print("-----Show joining date-----")
for x in result:
    print(x)

### 9 Show emp_id and name

n =" SELECT emp_id, name FROM employees"
mycursor.execute(n)
result = mycursor.fetchall()
print("-----Show emp_id and name------")
for x in result:
    print(x)

### 10 Show all columns using *

a = "SELECT* FROM employees"
mycursor.execute(a)
result = mycursor.fetchall()
print("-----Show all columns using *------")
for x in result:
    print(x)

#### WHERE, Comparison Operators, AND, OR, NOT, DISTINCT------
print(" .............*********------ WHERE, Comparison Operators, AND, OR, NOT, DISTINCT------**********8...............")

### 1 Show employees whose salary is greater than 50000

g= "SELECT * FROM employees WHERE salary > 50000"
mycursor.execute(g)
result = mycursor.fetchall()
print("......Show employees whose salary is greater than 50000.......")
for x in result:
    print(x)

### 2 Show employees from Delhi

d = "SELECT * FROM employees WHERE city = 'Delhi'"
mycursor.execute(d)
result = mycursor.fetchall()
print(".....Show employees from Delhi.....")
for x in result:
    print(x)

### 3 Show employees whose age is less than 28

a = "SELECT * FROM employees WHERE age < 28"
mycursor.execute(a)
result = mycursor.fetchall()
print(".....Show employees whose age is less than 28......")
for x in result:
    print(x)

### 4 Show employees from the HR department

h = "SELECT * FROM employees WHERE department = 'HR'"
mycursor.execute(h)
result = mycursor.fetchall()
print("......Show employees from the HR department......")
for x in result:
    print(x)

### 5 Show employees whose salary is 45000

s = "SELECT * FROM employees WHERE salary = 45000"
mycursor.execute(s)
result = mycursor.fetchall()
print("......Show employees whose salary is 45000.......")
for x in result:
    print(x)

### 6 Show employees from Delhi AND IT department

a = "SELECT * FROM employees WHERE city = 'Delhi' AND department = 'IT'"
mycursor.execute(a)
result = mycursor.fetchall()
print("....... Show employees from Delhi AND IT department.......")
for x in result:
    print(x)

#### 7 Show employees from Delhi OR Mumbai

c = "SELECT * FROM employees WHERE city = 'Delhi' OR city = 'Mumbai'"
mycursor.execute(c)
result = mycursor.fetchall()
print("......Show employees from Delhi OR Mumbai.....")
for x in result:
    print(x)

#### 8 Show employees whose age is greater than 25 AND salary is greater than 50000

a = "SELECT * FROM employees WHERE age >25 AND salary >50000"
mycursor.execute(a)
result = mycursor.fetchall()
print("......Show employees whose age is greater than 25 AND salary is greater than 50000.....")
for x in result:
    print(x)

### 9 Show employees who are NOT from Delhi

n = "SELECT * FROM employees WHERE NOT city = 'Delhi'"
mycursor.execute(n)
result = mycursor.fetchall()
print("......Show employees who are NOT from Delhi......")
for x in result:
    print(x)


### 10 Show unique cities

u = " SELECT DISTINCT city FROM employees"
mycursor.execute(u)
r = mycursor.fetchall()
print("......Show unique cities....")
for x in r:
    print(x)


### 11 Show employees whose salary is not equal to 50000

s = "SELECT * FROM employees WHERE NOT salary = 50000"
mycursor.execute(s)
r= mycursor.fetchall()
print(".....Show employees whose salary is not equal to 50000......")
for x in r:
    print(x)

### 12 Show employees whose department is not IT.

d="SELECT * FROM employees WHERE NOT department = 'IT'"
mycursor.execute(d)
r = mycursor.fetchall()
print(".....Show employees whose department is not IT......")
for x in r:
    print(x)

#### 13 Show employees from Pune OR Jaipur

p ="SELECT * FROM employees WHERE city = 'Pune' OR city = 'Jaipur'"
mycursor.execute(p)
r = mycursor.fetchall()
print(".....Show employees from Pune OR Jaipur......")
for x in r:
    print(x)

### 14 Show unique departments.

d = "SELECT DISTINCT department FROM employees"
mycursor.execute(d)
r = mycursor.fetchall()
print(".....Show unique departments......")
for x in r:
    print(x)

### 15 Show employees whose age is greater than or equal to 30
a = "SELECT * FROM employees WHERE age >= 30"
mycursor.execute(a)
r = mycursor.fetchall()
print(".....Show employees whose age is greater than or equal to 30......")
for x in r:
    print(x)


#### ******Bonus Challenge (Without Looking)******

###  1 Show employees from Finance

f = "SELECT * FROM employees WHERE department = 'Finance'"
mycursor.execute(f)
r = mycursor.fetchall()
print("----Show employees from Finance-----")
for x in r:
    print(x)

### 2 Show employees whose salary > 45000 AND city = Delhi

e = "SELECT * FROM employees WHERE salary >45000 AND city = 'Delhi'"
mycursor.execute(e)
r = mycursor.fetchall()
print(".....Show employees whose salary > 45000 AND city = Delhi.....")
for x in r:
    print(x)

### 3 Show employees whose city is not Mumbai.

c="SELECT * FROM employees WHERE NOT city = 'Mumbai'"
mycursor.execute(c)
r =mycursor.fetchall()
print("-----Show employees whose city is not Mumbai.------")
for x in r:
    print(x)

### 4 Show all unique ages

a ="SELECT DISTINCT age FROM employees"
mycursor.execute(a)
r = mycursor.fetchall()
print("....Show all unique ages....")
for x in r:
    print(x)

### 5 Show employees whose age <= 26

w = "SELECT * FROM employees WHERE age <=26"
mycursor.execute(w)
r = mycursor.fetchall()
print("....Show employees whose age <= 26....")
for x in r:
    print(x)


##### ORDER BY, LIMIT, LIKE
print("----------********ORDER BY, LIMIT, LIKE*********-----------")

### 1 Sort employees by salary (ascending)
a = "SELECT *  FROM employees ORDER BY salary"
mycursor.execute(a)
r = mycursor.fetchall()
print(".....Sort employees by salary (ascending).....")
for x in r:
    print(x)

### 2 Sort employees by salary (descending)
d = "SELECT * FROM employees ORDER BY salary DESC"
mycursor.execute(d)
r = mycursor.fetchall()
print("......Sort employees by salary (descending)......")
for x in r:
    print(x)

#### 3 Sort employees by age
a = "SELECT *   FROM employees ORDER BY age"
mycursor.execute(a)
r = mycursor.fetchall()
print(".....Sort employees by age......")
for x in r:
    print(x)

### 4 Sort employees by joining date (latest first)
j = "SELECT * FROM employees ORDER BY joining_dates DESC"
mycursor.execute(j)
r = mycursor.fetchall()
print(".....Sort employees by joining date (latest first).....")
for x in r:
    print(x)

### 5 Sort by department and then salary
d = "SELECT * FROM employees ORDER BY department ASC, salary ASC"
mycursor.execute(d)
r = mycursor.fetchall()
print("....Sort by department and then salary.....")
for x in r:
    print(x)

### 6 Show the first 5 employees
f = "SELECT * FROM employees LIMIT 5"
mycursor.execute(f)
r = mycursor.fetchall()
print("....Show the first 5 employees....")
for x in r:
    print(x)

### 7 Show the top 3 highest-paid employees
h = "SELECT * FROM employees ORDER BY salary DESC LIMIT 3"
mycursor.execute(h)
r = mycursor.fetchall()
print(".....Show the top 3 highest-paid employees....")
for x in r:
    print(x)

### 8 Show the lowest 2 salaries
l = "SELECT salary FROM employees ORDER BY salary ASC LIMIT 2"
mycursor.execute(l)
r = mycursor.fetchall()
print("....Show the lowest 2 salaries.....")
for x in r:
    print(x)

### 9 Show the youngest employee
y = "SELECT * FROM employees ORDER BY age ASC LIMIT 1"
mycursor.execute(y)
r = mycursor.fetchall()
print("....Show the youngest employee....")
for x in r:
    print(x)

### 10 Show the oldest employee
o = "SELECT * FROM employees ORDER BY age DESC LIMIT 1"
mycursor.execute(o)
r = mycursor.fetchall()
print(".....Show the oldest employee....")
for x in r:
    print(x)

### 11 Find names starting with A
n = "SELECT * FROM employees WHERE name LIKE 'A%' "
mycursor.execute(n)
r = mycursor.fetchall()
print("....Find names starting with A....")
for x in r:
    print(x)

### 12 Find names ending with a
e = "SELECT * FROM employees WHERE name LIKE '%a' "
mycursor.execute(e)
r = mycursor.fetchall()
print("....Find names ending with a...")
for x in r:
    print(x)

### 13 Find names containing it
c = "SELECT * FROM employees WHERE name LIKE '%it%'"
mycursor.execute(c)
r = mycursor.fetchall()
print("....Find names containing it....")
for x in r:
    print(x)

### 14 Find cities starting with D
c = "SELECT * FROM employees WHERE city LIKE 'D%'"
mycursor.execute(c)
r = mycursor.fetchall()
print("....Find cities starting with D....")
for x in r:
    print(x)

### 15 Find departments ending with s
d = "SELECT * FROM employees WHERE department LIKE '%s'"
mycursor.execute(d)
r = mycursor.fetchall()
print("....Find departments ending with s....")
for x in r:
    print(x)

### 16 Top 5 highest-paid IT employees
h = "SELECT * FROM employees WHERE department = 'IT' ORDER BY salary DESC LIMIT 5 "
mycursor.execute(h)
r = mycursor.fetchall()
print("....Top 5 highest-paid IT employees.....")
for x in r:
    print(x)

### 17 Delhi employees sorted by salary
d = "SELECT * FROM employees WHERE city = 'Delhi' ORDER BY salary"
mycursor.execute(d)
r = mycursor.fetchall()
print("....Delhi employees sorted by salary....")
for x in r:
    print(x)

### 18 Employees whose names contain a, sorted by age
n = "SELECT * FROM employees WHERE name LIKE '%a%' ORDER BY age "
mycursor.execute(n)
r = mycursor.fetchall()
print("....Employees whose names contain a, sorted by age.....")
for x in r:
    print(x)

### 19 Latest 3 joined employees.
j ="SELECT * FROM employees ORDER BY joining_dates DESC LIMIT 3"
mycursor.execute(j)
r = mycursor.fetchall()
print(".....Latest 3 joined employees.....")
for x in r:
    print(x)

### 20 Employees with exactly 5-letter names
e = "SELECT * FROM employees WHERE name LIKE '_'"
mycursor.execute(e)
p = mycursor.fetchall()
print("....Employees with exactly 5-letter names....")
for x in p:
    print(x)


#####  ........SQL Day 4 – IN, BETWEEN, IS NULL, IS NOT NULL......
print("----------*********SQL Day 4 – IN, BETWEEN, IS NULL, IS NOT NULL ********---------")

##### 1 Show employees from Delhi and Mumbai.
i = "SELECT * FROM employees WHERE city IN ('Delhi','Mumbai')"
mycursor.execute(i)
r = mycursor.fetchall()
print("......Show employees from Delhi and Mumbai......")
for x in r:
    print(x)

### 2 Show employees from Pune and Jaipur
p = "SELECT * FROM employees WHERE city IN ('Pune', 'Jaipur')"
mycursor.execute(p)
r = mycursor.fetchall()
print("....Show employees from Pune and Jaipur....")
for x in r:
    print(x)

### 3 Show employees in the IT or HR department
d = "SELECT * FROM employees WHERE department IN ('IT', 'HR')"
mycursor.execute(d)
r = mycursor.fetchall()
print("....Show employees in the IT or HR department.....")
for x in r:
    print(x)

### 4 Show employees whose age is 25, 27, or 30
a = "SELECT * FROM employees WHERE age IN (25, 27, 30)"
mycursor.execute(a)
r = mycursor.fetchall()
print("....Show employees whose age is 25, 27, or 30.....")
for x in r:
    print(x)

#### 5 Show employees whose salary is 50000, 60000, or 70000.
s = "SELECT * FROM employees WHERE salary IN (50000, 60000, 70000)"
mycursor.execute(s)
r = mycursor.fetchall()
print("....Show employees whose salary is 50000, 60000, or 70000.......")
for x in r:
    print(x)

#### 6 Show employees not from Delhi
d = "SELECT * FROM employees WHERE city  NOT IN ('Delhi') "
mycursor.execute(d)
r = mycursor.fetchall()
print("....Show employees not from Delhi....")
for x in r:
    print(x)

### 7 Show employees not in the HR department
d = "SELECT * FROM employees WHERE department NOT IN ('HR')"
mycursor.execute(d)
r = mycursor.fetchall()
print(".....Show employees not in the HR department.....")
for x in r:
    print(x)

### 8 Show employees whose age is not 24 or 25
a = "SELECT * FROM employees WHERE age NOT IN (24, 25)"
mycursor.execute(a)
r = mycursor.fetchall()
print(".....Show employees whose age is not 24 or 25.....")
for x in r:
    print(x)

### 9 Show employees not from Mumbai or Jaipur
c = "SELECT * FROM employees WHERE city NOT IN ('Mumbai', 'Jaipur')"
mycursor.execute(c)
r = mycursor.fetchall()
print("....Show employees not from Mumbai or Jaipur....")
for x in r:
    print(x)

### 10 Show employees not in Finance
f = "SELECT * FROM employees WHERE department NOT IN ('Finance')"
mycursor.execute(f)
r = mycursor.fetchall()
print(".....Show employees not in Finance.....")
for x in r:
    print(x)

### 11 Salary between 45000 and 60000
s = "SELECT salary FROM employees WHERE salary BETWEEN 45000 and 60000"
mycursor.execute(s)
r = mycursor.fetchall()
print(".....Salary between 45000 and 60000....")
for x in r:
    print(x)

### 12 Age between 25 and 30
a = "SELECT age FROM employees WHERE age BETWEEN 25 and 30"
mycursor.execute(a)
r = mycursor.fetchall()
print(".....Age between 25 and 30.....")
for x in r:
    print(x)

### 13 Joining dates between 2022-01-01 and 2023-12-31
d = "SELECT joining_dates FROM employees WHERE joining_dates BETWEEN '2022-01-01' and '2023-12-31'"
mycursor.execute(d)
r = mycursor.fetchall()
print("....Joining dates between 2022-01-01 and 2023-12-31....")
for x in r:
    print(x)

### 14 Salary between 40000 and 50000
s = "SELECT salary FROM employees WHERE salary BETWEEN 40000 and 50000"
mycursor.execute(s)
r = mycursor.fetchall()
print("....Salary between 40000 and 50000....")
for x in r:
    print(x)

### 15 Age between 26 and 32
a = "SELECT age FROM employees WHERE age BETWEEN 26 and 32"
mycursor.execute(a)
r = mycursor.fetchall()
print("....Age between 26 and 32....")
for x in r:
    print(x)

### 16 Salary not between 45000 and 60000
n = "SELECT salary FROM employees WHERE salary NOT BETWEEN 45000 and 60000"
mycursor.execute(n)
r = mycursor.fetchall()
print("....Salary not between 45000 and 60000....")
for x in r:
    print(x)

### 17 Age not between 25 and 30
a = "SELECT age FROM employees WHERE age  NOT BETWEEN 25 and 30 "
mycursor.execute(a)
r = mycursor.fetchall()
print("....Age not between 25 and 30......")
for x in r:
    print(x)

### null value k liye insert krni h ik row 
# i = "INSERT INTO employees VALUES (111,'Rohit','IT',58000,NULL,27,'2023-11-20')"
# mycursor.execute(i)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")

### 18 Show employees whose city is NULL
s = "SELECT * FROM employees WHERE city IS NULL"
mycursor.execute(s)
r= mycursor.fetchall()
print("....Show employees whose city is NULL....")
for x in r:
    print(x)

### 19 Show employees whose city is NOT NULL
c = "SELECT * FROM employees WHERE city IS NOT NULL"
mycursor.execute(c)
r = mycursor.fetchall()
print("....Show employees whose city is NOT NULL....")
for x in r:
    print(x)

### 20 Count how many employees have NULL city
c = "SELECT COUNT(*) FROM employees  WHERE  city IS NULL"
mycursor.execute(c)
r = mycursor.fetchall()
print("....Count how many employees have NULL city....")
for x in r:
    print(x)

##### CHALANGE ####
print(".....Chalange.....")

### 21 Delhi employees with salary between 50000 and 70000.
a = "SELECT * FROM employees WHERE city = 'Delhi' AND salary BETWEEN 50000 and 70000"
mycursor.execute(a)
r = mycursor.fetchall()
print(".....Delhi employees with salary between 50000 and 70000......")
for x in r:
    print(x)

#### 22 IT and Finance employees whose age is between 25 and 30.
b = "SELECT * FROM employees WHERE department IN ('IT','Finance') AND age BETWEEN 25 and 30"
mycursor.execute(b)
r = mycursor.fetchall()
print("....IT and Finance employees whose age is between 25 and 30.....")
for x in r:
    print(x)

### 23 Employees not from Delhi and not from Mumbai.
c= "SELECT * FROM employees WHERE city NOT IN ('Delhi','Mumbai')"
mycursor.execute(c)
r = mycursor.fetchall()
print(".....Employees not from Delhi and not from Mumbai......")
for x in r:
    print(x)

### 24 Employees whose joining date is not between 2022-01-01 and 2023-12-31
d = "SELECT * FROM employees WHERE joining_dates NOT BETWEEN '2022-01-01' and '2023-12-31'"
mycursor.execute(d)
r = mycursor.fetchall()
print("....Employees whose joining date is not between 2022-01-01 and 2023-12-31....")
for x in r:
    print(x)

### 25 Employees from Delhi, Jaipur, or Pune with salary greater than 45000.
e = "SELECT * FROM employees WHERE city IN ('Delhi','Jaipur','Pune') AND salary > 45000"
mycursor.execute(e)
r = mycursor.fetchall()
print("....Employees from Delhi, Jaipur, or Pune with salary greater than 45000.....")
for x in r:
    print(x)

### Show employees from Delhi and Jaipur whose salary is between 45,000 and 60,000
s = "SELECT * FROM employees WHERE city IN ('Delhi','Jaipur') AND salary BETWEEN 45000 and 60000"
mycursor.execute(s)
r = mycursor.fetchall()
print("....Show employees from Delhi and Jaipur whose salary is between 45,000 and 60,000....")
for x in r:
    print(x)


####.........Aggregate Functions  count(), avg(), sum(),min(), max().........######
print("####.........Aggregate Functions  count(), avg(), sum(),min(), max().........######")

### 1 Count total employees.
c = "SELECT COUNT(*) FROM employees "
mycursor.execute(c)
r = mycursor.fetchall()
print("......Count total employees......")
for x in r:
    print(x)

### 2 Count employees from Delhi.
c = "SELECT COUNT(*) FROM employees WHERE city = 'Delhi'"
mycursor.execute(c)
r = mycursor.fetchall()
print("....Count employees from Delhi.....")
for x in r:
    print(x)

### 3 Count employees in IT department
c = "SELECT COUNT(*) FROM employees WHERE department = 'IT'"
mycursor.execute(c)
r = mycursor.fetchall()
print(".....Count employees in IT department.....")
for x in r:
    print(x)

### 4 Count employees whose salary is greater than 50000
c = "SELECT COUNT(*) FROM employees WHERE salary > 50000"
mycursor.execute(c)
r = mycursor.fetchall()
print(".....Count employees whose salary is greater than 50000.....")
for x in r:
    print(x)

#### 5 Count employees whose age is above 25
c = "SELECT COUNT(*) FROM employees WHERE age > 25"
mycursor.execute(c)
r = mycursor.fetchall()
print("....Count employees whose age is above 25....")
for x in r:
    print(x)

### 6 Total salary of all employees.
s = "SELECT SUM(salary) FROM employees"
mycursor.execute(s)
r = mycursor.fetchall()
print("...Total salary of all employees....")
for x in r:
     print(x)

print(type(result[0][0]))

### 7 Total salary of IT department.
s = "SELECT SUM(salary) FROM employees WHERE department = 'IT'"
mycursor.execute(s)
r = mycursor.fetchall()
print("....Total salary of IT department.....")
for x in r:
    print(x)

### 8 Total salary of Delhi employees.
s = "SELECT SUM(salary) FROM employees WHERE city = 'Delhi'"
mycursor.execute(s)
r = mycursor.fetchall()
print("....Total salary of Delhi employees....")
for x in r:
    print(x)

### 9 Total salary of HR department.
s = "SELECT SUM(salary) FROM employees WHERE department = 'HR'"
mycursor.execute(s)
r = mycursor.fetchall()
print("....Total salary of HR department.....")
for x in r:
    print(x)

### 10 Total salary where age is above 28.
s = "SELECT SUM(salary) FROM employees WHERE age >28"
mycursor.execute(s)
r = mycursor.fetchall()
print("....Total salary where age is above 28.....")
for x in r:
    print(x) 

### 11 Average salary.
a = "SELECT AVG(salary) FROM employees "
mycursor.execute(a)
r = mycursor.fetchall()
print("...Average salary....")
for x in r:
    print(x)

### 12 Average salary of IT department.
a = "SELECT AVG(salary) FROM employees WHERE department = 'IT'"
mycursor.execute(a)
r = mycursor.fetchall()
print("...Average salary of IT department....")
for x in r:
    print(x)

### 13 Average age.
a = "SELECT AVG(age) FROM employees"
mycursor.execute(a)
r = mycursor.fetchall()
print("....Average age....")
for x in r:
    print(x)

### 14 Average salary of Delhi employees.
a = "SELECT AVG(salary) FROM employees WHERE city = 'Delhi'"
mycursor.execute(a)
r = mycursor.fetchall()
print("...Average salary of Delhi employees....")
for x in r:
    print(x)

### 15 Average salary where age is less than 30
a = "SELECT AVG(salary) FROM employees WHERE age<30"
mycursor.execute(a)
r = mycursor.fetchall()
print("....Average salary where age is less than 30....")
for x in r:
    print(x)

### 16 Minimum salary.
m = "SELECT MIN(salary) FROM employees"
mycursor.execute(m)
r = mycursor.fetchall()
print("...Minimum salary.....")
for x in r:
    print(x)

### 17 Minimum age.
m = "SELECT MIN(age) FROM employees"
mycursor.execute(m)
r = mycursor.fetchall()
print("....Minimum age....")
for x in r:
    print(x)

### 18 Lowest salary in HR department
m = "SELECT MIN(salary) FROM employees WHERE department = 'HR'"
mycursor.execute(m)
r = mycursor.fetchall()
print("....Lowest salary in HR department....")
for x in r:
    print(x)

### 19 Earliest joining date.
m = "SELECT MIN(joining_dates) FROM employees"
mycursor.execute(m)
r = mycursor.fetchall()
print("....Earliest joining date....")
for x in r:
    print(x)

### 20 Minimum salary in Delhi.
m = "SELECT MIN(salary) FROM employees WHERE city = 'Delhi'"
mycursor.execute(m)
r = mycursor.fetchall()
print("....Minimum salary in Delhi....")
for x in r:
    print(x)

### 21 Highest salary.
h = "SELECT MAX(salary) FROM employees"
mycursor.execute(h)
r = mycursor.fetchall()
print("...Highest salary....")
for x in r:
    print(x)

### 22 Maximum age.
h = "SELECT MAX(age) FROM employees"
mycursor.execute(h)
r = mycursor.fetchall()
print("...Maximum age....")
for x in r:
    print(x)

### 23 Highest salary in Finance
h = "SELECT MAX(salary) FROM employees WHERE department = 'Finance'"
mycursor.execute(h)
r = mycursor.fetchall()
print("...Highest salary in Finance....")
for x in r:
    print(x)

### 24 Latest joining date.
h = "SELECT MAX(joining_dates) FROM employees "
mycursor.execute(h)
r = mycursor.fetchall()
print("....Latest joining date....")
for x in r:
    print(x) 

### 25 Highest salary in Mumbai.
h="SELECT MAX(salary) FROM employees WHERE city = 'Mumbai'"
mycursor.execute(h)
r = mycursor.fetchall()
print("....Highest salary in Mumbai.....")
for x in r:
    print(x)

### 26 Count employees whose salary is between 45,000 and 60,000.
c = "SELECT COUNT(*) FROM employees WHERE salary BETWEEN 45000 and 60000"
mycursor.execute(c)
r = mycursor.fetchall()
print("...Count employees whose salary is between 45,000 and 60,000....")
for x in r:
    print(x)

### 27 Find the total salary of employees from Delhi and Jaipur.
t = "SELECT SUM(salary) FROM employees WHERE city IN ('Delhi' , 'Jaipur')"
mycursor.execute(t)
r = mycursor.fetchall()
print("...Find the total salary of employees from Delhi and Jaipur....")
for x in r:
    print(x)

### 28 Find the average salary of employees aged between 25 and 30.
a = "SELECT AVG(salary) FROM employees WHERE age BETWEEN 25 and 30"
mycursor.execute(a)
r = mycursor.fetchall()
print("...Find the average salary of employees aged between 25 and 30.....")
for x in r:
    print(x)

### 29 Find the highest salary in the IT department whose city is Delhi.
h = "SELECT MAX(salary) FROM employees WHERE department = 'IT' AND  city = 'Delhi'"
mycursor.execute(h)
r = mycursor.fetchall()
print("....Find the highest salary in the IT department whose city is Delhi.....")
for x in r:
    print(x)

### 30 Find the lowest salary among employees who joined after 2022-01-01.
l = "SELECT MIN(salary) FROM employees WHERE joining_dates >'2022-01-01' "
mycursor.execute(l)
r = mycursor.fetchall()
print("....Find the lowest salary among employees who joined after 2022-01-01.....")
for x in r:
    print(x)

#### "Find the average salary of employees in the HR department whose age is greater than 25."
e = "SELECT AVG(salary) FROM employees WHERE department = 'HR' AND age > 25"
mycursor.execute(e)
r = mycursor.fetchall()
print("....Find the average salary of employees in the HR department whose age is greater than 25.....")
for x in r:
    print(x)


##### ........GROUP BY AND GROUP BY WITH AGGREGATE FUNCTIONS && HAVING.......#######
print(".....******....##### ........GROUP BY AND GROUP BY WITH AGGREGATE FUNCTIONS && HAVING.......#######")

### 1 Count employees in each department.
c = "SELECT department, COUNT(*) FROM employees GROUP BY department"
mycursor.execute(c)
r = mycursor.fetchall()
print("....Count employees in each department.....")
for x in r:
    print(x)

### 2 Count employees in each city.
c = "SELECT city, COUNT(*) FROM employees GROUP BY city"
mycursor.execute(c)
r = mycursor.fetchall()
print(".....Count employees in each city.....")
for x in r:
    print(x)

### 3 Find total salary of each department.
t = "SELECT department, SUM(salary) FROM employees GROUP BY department"
mycursor.execute(t)
r = mycursor.fetchall()
print("....Find total salary of each department.....")
for x in r:
    print(x)

### 4 Find average salary of each department.
a = "SELECT department, AVG(salary) FROM employees GROUP BY department"
mycursor.execute(a)
r = mycursor.fetchall()
print("....Find average salary of each department.....")
for x in r:
    print(x)

### 5 Find highest salary in each department.
a = "SELECT department, MAX(salary) FROM employees GROUP BY department"
mycursor.execute(a)
r = mycursor.fetchall()
print("....Find highest salary in each department....")
for x in r:
    print(x)

### 6 Find lowest salary in each department.
l = "SELECT department, MIN(salary) FROM employees GROUP BY department"
mycursor.execute(l)
r = mycursor.fetchall()
print("....Find lowest salary in each department.....")
for x in r:
    print(x)

### 7 Find average age in each city
a = "SELECT city, AVG(age) FROM employees GROUP BY city"
mycursor.execute(a)
r = mycursor.fetchall()
print("....Find average age in each city....")
for x in r:
    print(x)

### 8 Find latest joining date in each department.
a = "SELECT department, MAX(joining_dates) FROM employees GROUP BY department"
mycursor.execute(a)
r = mycursor.fetchall()
print(".....Find latest joining date in each department......")
for x in r:
    print(x)

### 9 Find earliest joining date in each department.
a = "SELECT department, MIN(joining_dates) FROM employees GROUP BY department"
mycursor.execute(a)
r = mycursor.fetchall()
print(".....Find earliest joining date in each department.....")
for x in r:
    print(x)

### 10 Count employees in each age.
c = "SELECT age, COUNT(*) FROM employees GROUP BY age"
mycursor.execute(c)
r = mycursor.fetchall()
print("....Count employees in each age.....")
for x in r:
    print(x)

### 11 Show departments having more than 2 employees.
h = "SELECT department,COUNT(*) FROM employees GROUP BY department HAVING COUNT(*) >2 "
mycursor.execute(h)
r = mycursor.fetchall()
print("....Show departments having more than 2 employees....")
for x in r:
    print(x)

### 12 Show departments where average salary is greater than 50000
h = "SELECT department, AVG(salary) FROM employees GROUP BY department HAVING AVG(salary) >50000"
mycursor.execute(h)
r = mycursor.fetchall()
print("...Show departments where average salary is greater than 50000....")
for x in r:
    print(x)

### 13 Show cities having more than 1 employee.
h = "SELECT city, COUNT(*) FROM employees GROUP BY city HAVING COUNT(*) >1"
mycursor.execute(h)
r = mycursor.fetchall()
print("...Show cities having more than 1 employee....")
for x in r:
    print(x)

### 14 Show departments whose total salary is greater than 100000
h = "SELECT department, SUM(salary) FROM employees GROUP BY department HAVING SUM(salary) > 100000"
mycursor.execute(h)
r = mycursor.fetchall()
print("...Show departments whose total salary is greater than 100000...")
for x in r:
    print(x)

### 15 Show cities where average age is greater than 26.
h = "SELECT city, AVG(age) FROM employees GROUP BY city HAVING AVG(age)>26 "
mycursor.execute(h)
r = mycursor.fetchall()
print("....Show cities where average age is greater than 26....")
for x in r:
    print(x)

### 16 Count employees in each city and sort by count (highest first).
c = "SELECT city, COUNT(*) FROM employees GROUP BY city ORDER BY COUNT(*) DESC"
mycursor.execute(c)
r = mycursor.fetchall()
print("....Count employees in each city and sort by count (highest first).....")
for x in r:
    print(x)

### 17 Show department-wise average salary in descending order.
c = "SELECT department, AVG(salary) FROM employees GROUP BY department ORDER BY AVG(salary) DESC"
mycursor.execute(c)
r = mycursor.fetchall()
print("....Show department-wise average salary in descending order.....")
for x in r:
    print(x)

### 18 Show department-wise highest salary.
c = "SELECT department, MAX(salary) FROM employees GROUP BY department "
mycursor.execute(c)
r = mycursor.fetchall()
print("....Show department-wise highest salary.....")
for x in r:
    print(x)

### 19 Show city-wise total salary.
s = "SELECT city, SUM(salary) FROM employees GROUP BY city"
mycursor.execute(s)
r = mycursor.fetchall()
print("...Show city-wise total salary....")
for x in r:
    print(x)

### 20 Show department-wise employee count where count is at least 2.
s = "SELECT department, COUNT(*) FROM employees GROUP BY department HAVING COUNT(*) >=2"
mycursor.execute(s)
r = mycursor.fetchall()
print("...Show department-wise employee count where count is at least 2....")
for x in r:
    print(x)

### 21 Find the department with the highest average salary.
s = "SELECT department, AVG(salary) FROM employees GROUP BY department ORDER BY AVG(salary) DESC LIMIT 1 "
mycursor.execute(s)
r = mycursor.fetchall()
print("....Find the department with the highest average salary....")
for x in r:
    print(x)

### 22 Find the city with the maximum number of employees.
s = "SELECT city, COUNT(*) FROM employees GROUP BY city  ORDER BY city DESC LIMIT 1"
mycursor.execute(s)
r = mycursor.fetchall()
print("....Find the city with the maximum number of employees.....")
for x in r:
    print(x)

### 23 Show departments where the minimum salary is above 45000.
s = "SELECT department, MIN(salary) FROM employees GROUP BY department HAVING MIN( salary)  > 45000"
mycursor.execute(s)
r = mycursor.fetchall()
print("....Show departments where the minimum salary is above 45000....")
for x in r:
    print(x)

### 24 Show cities whose total salary is between 90000 and 150000.
s = "SELECT city, SUM(salary) FROM employees GROUP BY city HAVING SUM(salary) BETWEEN 90000 and 150000"
mycursor.execute(s)
r = mycursor.fetchall()
print("....Show cities whose total salary is between 90000 and 150000....")
for x in r:
    print(x)

### 25 Show departments with an average age less than 30.
s = "SELECT department, AVG(age) FROM employees GROUP BY department HAVING AVG(age)<30"
mycursor.execute(s)
r = mycursor.fetchall()
print("....Show departments with an average age less than 30....")
for x in r:
    print(x)

#####..........--------Date Functions CURDATE() NOW() YEAR() MONTH() DAY() DATEDIFF() DATE_FORMAT()........-------
print("#####..........--------Date Functions CURDATE() NOW() YEAR() MONTH() DAY() DATEDIFF() DATE_FORMAT()........-------")

mycursor.execute("DESCRIBE employees")
result = mycursor.fetchall()

for x in result:
    print(x)

#### 1 Display current date.
s = "SELECT CURDATE()"
mycursor.execute(s)
r = mycursor.fetchone()
print("....Display current date....")
for x in r:
    print(x)

#### 2 Display current date and time. 
s = "SELECT NOW()"
mycursor.execute(s)
r = mycursor.fetchone()
print("....Display current date and time....")
for x in r:
    print(x)

### 3 Show employee name and joining year.
s = "SELECT name, year(joining_dates) FROM employees "
mycursor.execute(s)
r = mycursor.fetchall()
print("....Show employee name and joining year....")
for x in r:
    print(x)

### 4 Show employee name and joining month.
m = "SELECT name, month(joining_dates) FROM employees"
mycursor.execute(m)
r = mycursor.fetchall()
print("....Show employee name and joining month....")
for x in r:
    print(x)

### 5 Show employee name and joining day.
m = "SELECT name, day(joining_dates) FROM employees"
mycursor.execute(m)
r = mycursor.fetchall()
print("....Show employee name and joining day....")
for x in r:
    print(x)

### 6 Find employees who joined in 2023.
y = "SELECT * FROM employees WHERE YEAR(joining_dates) = 2023"
mycursor.execute(y)
r = mycursor.fetchall()
print("...Find employees who joined in 2023....")
for x in r:
    print(x)

### 7 Find employees who joined in January.
j = "SELECT * FROM employees WHERE MONTH(joining_dates) = 1"
mycursor.execute(j)
r = mycursor.fetchall()
print("....Find employees who joined in January....")
for x in r:
    print(x)

### 8 Find employees who joined after 2022-12-31
d = "SELECT * FROM employees WHERE joining_dates > '2022-12-31'"
mycursor.execute(d)
r = mycursor.fetchall()
print("....Find employees who joined after '2022-12-31....'")
for x in r:
    print(x)

### 9 Display joining date in DD-MM-YYYY format.
d = "SELECT DATE_FORMAT(joining_dates,'%d-%m-%Y') FROM employees"
mycursor.execute(d)
r = mycursor.fetchall()
print("...Display joining date in DD-MM-YYYY format....")
for x in r:
    print(x)

### 10 Show number of days each employee has worked
d = "SELECT name, DATEDIFF(CURDATE(), joining_dates) FROM employees"
mycursor.execute(d)
r = mycursor.fetchall()
print("....Show number of days each employee has worked....")
for x in r:
    print(x)



### 11 Count employees who joined in 2023.
c = "SELECT COUNT(*) FROM employees WHERE YEAR(joining_dates) = 2023"
mycursor.execute(c)
r = mycursor.fetchall()
print("....Count employees who joined in 2023....")
for x in r:
    print(x)

### 12 Find earliest joining date.
e = "SELECT MIN(joining_dates) FROM employees"
mycursor.execute(e)
r = mycursor.fetchall()
print("....Find earliest joining date....")
for x in r:
    print(x)

### 13 Find latest joining date.
l = "SELECT MAX(joining_dates) FROM employees"
mycursor.execute(l)
r = mycursor.fetchall()
print("....Find latest joining date....")
for x in r:
    print(x)

### 14 Find employees who joined before 2022.
b = "SELECT * FROM employees WHERE joining_dates < '2022-01-01'"
mycursor.execute(b)
r = mycursor.fetchall()
print("....Find employees who joined before 2022....")
for x in r:
    print(x)

### 15 Show employees sorted by joining date (oldest first).
s = "SELECT * FROM employees ORDER BY joining_dates ASC"
mycursor.execute(s)
r = mycursor.fetchall()
print("....Show employees sorted by joining date (oldest first)....")
for x in r:
    print(x)

##### ******** Interview Questions ******** #####

### 16 Find employees who joined in the current year.
c = "SELECT * FROM employees WHERE YEAR(joining_dates) = YEAR(CURDATE())"
mycursor.execute(c)
r = mycursor.fetchall()
print("....Find employees who joined in the current year....")
for x in r:
    print(x)

### 17 Count employees who joined in the current month.
c = "SELECT COUNT(*) FROM employees WHERE MONTH(joining_dates) = MONTH(CURDATE())"
mycursor.execute(c)
r = mycursor.fetchall()
print("....Count employees who joined in the current month....")
for x in r:
    print(x)

### 18 Find employees who completed more than 3 years in the company.
c = "SELECT * FROM employees WHERE TIMESTAMPDIFF(YEAR, joining_dates, CURDATE()) > 3"
mycursor.execute(c)
r = mycursor.fetchall()
print("....Find employees who completed more than 3 years in the company....")
for x in r:
    print(x)

### 19 Show month-wise employee joining count.
m = """
SELECT MONTHNAME(joining_dates), COUNT(*) FROM employees
GROUP BY MONTH(joining_dates), MONTHNAME(joining_dates)
ORDER BY MONTH(joining_dates)
"""
mycursor.execute(m)
r = mycursor.fetchall()
print("....Show month-wise employee joining count....")
for x in r:
    print(x)

### 20 Find the month in which the maximum employees joined.
m = """SELECT MONTHNAME(joining_dates), COUNT(*) FROM employees
GROUP BY MONTH(joining_dates), MONTHNAME(joining_dates)
ORDER BY COUNT(*) DESC
LIMIT 1
"""
mycursor.execute(m)
r = mycursor.fetchall()
print("....Find the month in which the maximum employees joined....")
for x in r:
    print(x)

#### ........ Create Departments Table ........ ####

# c = """
# CREATE TABLE departments(
# department_id INT PRIMARY KEY,
# department_name VARCHAR(50),
# manager_name VARCHAR(50),
# location VARCHAR(50),
# budget INT
# )
# """

# mycursor.execute(c)
# print("Departments table created successfully.")

# #### ........ Insert Data into Departments Table ........ ####

# s = """
# INSERT INTO departments
# (department_id, department_name, manager_name, location, budget)
# VALUES
# (%s, %s, %s, %s, %s)
# """

# value = [
# (101, 'IT', 'Rajesh Khanna', 'Delhi', 500000),
# (102, 'HR', 'Meena Sharma', 'Noida', 250000),
# (103, 'Finance', 'Sanjay Gupta', 'Mumbai', 450000),
# (104, 'Marketing', 'Anita Verma', 'Gurugram', 300000),
# (105, 'Sales', 'Vikram Singh', 'Jaipur', 400000)
# ]

# mycursor.executemany(s, value)

# mydb.commit()

# print(mycursor.rowcount, "records inserted.")

#### .......INNER JOIN.......
print("********>>>>>>>INNER JOIN ...........********")

### 1 Show employee name and department.
i = "SELECT employees.name, departments.department_name FROM employees INNER JOIN departments ON employees.emp_id = departments.department_id"
mycursor.execute(i)
r = mycursor.fetchall()
print("...Show employee name and department....")
for x in r:
    print(x)

### 2 Show employee name, salary and department.
i = "SELECT employees.name, employees.salary, departments.department_name FROM employees INNER JOIN departments ON employees.emp_id = departments.department_id"
mycursor.execute(i)
r = mycursor.fetchall()
print("...Show employee name, salary and department....")
for x in r:
    print(x)

### 3 Show emp_id, employee name and department.
i = "SELECT employees.emp_id, employees.name, departments.department_name FROM employees INNER JOIN departments ON employees.emp_id = departments.department_id"
mycursor.execute(i)
r = mycursor.fetchall()
print(".....Show emp_id, employee name and department....")
for x in r:
    print(x)

### 4 Display all columns from both tables
i = "SELECT employees.* , departments.* FROM employees INNER JOIN departments ON employees.department = departments.department_name"
mycursor.execute(i)
r = mycursor.fetchall()
print("....Display all columns from both tables.....")
for x in r:
    print(x)


# s = "SELECT * FROM departments"
# mycursor.execute(s)

# r = mycursor.fetchall()

# for x in r:
#     print(x)

### 5 Show only Finance employees.
f = "SELECT employees.*,departments.* FROM employees INNER JOIN departments ON employees.department = departments.department_name WHERE department = 'Finance'"
mycursor.execute(f)
r = mycursor.fetchall()
print("....Show only Finance employees....")
for x in r:
    print(x)

### 6 Show all IT employees.
f = "SELECT employees.*,departments.* FROM employees INNER JOIN departments ON employees.department = departments.department_name WHERE department = 'IT'"
mycursor.execute(f)
r = mycursor.fetchall()
print("....Show all IT employees....")
for x in r:
    print(x)

### 7 Show employees with salary greater than 50000.
f = "SELECT employees.*,departments.* FROM employees INNER JOIN departments ON employees.department = departments.department_name WHERE salary > 50000"
mycursor.execute(f)
r = mycursor.fetchall()
print("....Show employees with salary greater than 50000.....")
for x in r:
    print(x)

### 8 Show employee name and department sorted by salary.
f = "SELECT employees.name,departments.department_name, employees.salary FROM employees INNER JOIN departments ON employees.department = departments.department_name ORDER BY salary"
mycursor.execute(f)
r = mycursor.fetchall()
print("....Show employee name and department sorted by salary......")
for x in r:
    print(x)

### 9 Show employee names in alphabetical order
f = "SELECT employees.*,departments.* FROM employees INNER JOIN departments ON employees.department = departments.department_name ORDER BY name "
mycursor.execute(f)
r = mycursor.fetchall()
print("....Show employee names in alphabetical order......")
for x in r:
    print(x)


### 10 Show employees working in HR.
h = """
SELECT employees.*, departments.department_name
FROM employees
INNER JOIN departments
ON employees.department = departments.department_name
WHERE departments.department_name = 'HR'
"""
mycursor.execute(h)
r = mycursor.fetchall()
print("....Show employees working in HR....")
for x in r:
    print(x)


### 11 Count employees in each department.
c = """
SELECT departments.department_name, COUNT(employees.emp_id)
FROM employees
INNER JOIN departments
ON employees.department = departments.department_name
GROUP BY departments.department_name
"""
mycursor.execute(c)
r = mycursor.fetchall()
print("....Count employees in each department....")
for x in r:
    print(x)


### 12 Find average salary of each department.
a = """
SELECT departments.department_name, AVG(employees.salary)
FROM employees
INNER JOIN departments
ON employees.department = departments.department_name
GROUP BY departments.department_name
"""
mycursor.execute(a)
r = mycursor.fetchall()
print("....Find average salary of each department....")
for x in r:
    print(x)


### 13 Find maximum salary of each department.
m = """
SELECT departments.department_name, MAX(employees.salary)
FROM employees
INNER JOIN departments
ON employees.department = departments.department_name
GROUP BY departments.department_name
"""
mycursor.execute(m)
r = mycursor.fetchall()
print("....Find maximum salary of each department....")
for x in r:
    print(x)


### 14 Find minimum salary of each department.
m = """
SELECT departments.department_name, MIN(employees.salary)
FROM employees
INNER JOIN departments
ON employees.department = departments.department_name
GROUP BY departments.department_name
"""
mycursor.execute(m)
r = mycursor.fetchall()
print("....Find minimum salary of each department....")
for x in r:
    print(x)


### 15 Find total salary of each department.
s = """
SELECT departments.department_name, SUM(employees.salary)
FROM employees
INNER JOIN departments
ON employees.department = departments.department_name
GROUP BY departments.department_name
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Find total salary of each department....")
for x in r:
    print(x)


### 16 Show departments having more than 2 employees.
h = """
SELECT departments.department_name, COUNT(employees.emp_id)
FROM employees
INNER JOIN departments
ON employees.department = departments.department_name
GROUP BY departments.department_name
HAVING COUNT(employees.emp_id) > 2
"""
mycursor.execute(h)
r = mycursor.fetchall()
print("....Show departments having more than 2 employees....")
for x in r:
    print(x)


### 17 Show departments whose average salary is greater than 50000.
h = """
SELECT departments.department_name, AVG(employees.salary)
FROM employees
INNER JOIN departments
ON employees.department = departments.department_name
GROUP BY departments.department_name
HAVING AVG(employees.salary) > 50000
"""
mycursor.execute(h)
r = mycursor.fetchall()
print("....Show departments whose average salary is greater than 50000....")
for x in r:
    print(x)


### 18 Find the highest-paid employee with department name.
h = """
SELECT employees.name,
       employees.salary,
       departments.department_name
FROM employees
INNER JOIN departments
ON employees.department = departments.department_name
ORDER BY employees.salary DESC
LIMIT 1
"""
mycursor.execute(h)
r = mycursor.fetchall()
print("....Find the highest-paid employee with department name....")
for x in r:
    print(x)


### 19 Find the lowest-paid employee with department name.
l = """
SELECT employees.name,
       employees.salary,
       departments.department_name
FROM employees
INNER JOIN departments
ON employees.department = departments.department_name
ORDER BY employees.salary ASC
LIMIT 1
"""
mycursor.execute(l)
r = mycursor.fetchall()
print("....Find the lowest-paid employee with department name....")
for x in r:
    print(x)


### 20 Show department-wise employee count in descending order.
d = """
SELECT departments.department_name,
       COUNT(employees.emp_id)
FROM employees
INNER JOIN departments
ON employees.department = departments.department_name
GROUP BY departments.department_name
ORDER BY COUNT(employees.emp_id) DESC
"""
mycursor.execute(d)
r = mycursor.fetchall()
print("....Show department-wise employee count in descending order....")
for x in r:
    print(x)


# # Employee without department
# i = """
# INSERT INTO employees
# (emp_id, name, department, salary, city, age, joining_dates)
# VALUES
# (112,'Akash',NULL,45000,'Delhi',26,'2024-08-15')
# """
# mycursor.execute(i)

# # Department without employee
# i = """
# INSERT INTO departments
# VALUES
# (106,'Admin','Rakesh Sharma','Delhi',350000)
# """
# mycursor.execute(i)

# mydb.commit()

print("##### ........ LEFT JOIN ........ #####")

### 1 Show all employees with department names.
q = """
SELECT employees.*, departments.department_name
FROM employees
LEFT JOIN departments
ON employees.department = departments.department_name
"""
mycursor.execute(q)
r = mycursor.fetchall()
print("....Show all employees with department names....")
for x in r:
    print(x)


### 2 Find employees without a department.
q = """
SELECT employees.*
FROM employees
LEFT JOIN departments
ON employees.department = departments.department_name
WHERE departments.department_name IS NULL
"""
mycursor.execute(q)
r = mycursor.fetchall()
print("....Find employees without a department....")
for x in r:
    print(x)


### 3 Show employee names with salary and department.
q = """
SELECT employees.name,
employees.salary,
departments.department_name
FROM employees
LEFT JOIN departments
ON employees.department = departments.department_name
"""
mycursor.execute(q)
r = mycursor.fetchall()
print("....Show employee names with salary and department....")
for x in r:
    print(x)


### 4 Show all employees sorted by department.
q = """
SELECT employees.*
FROM employees
LEFT JOIN departments
ON employees.department = departments.department_name
ORDER BY departments.department_name
"""
mycursor.execute(q)
r = mycursor.fetchall()
print("....Show all employees sorted by department....")
for x in r:
    print(x)


### 5 Count employees in each department using LEFT JOIN.
q = """
SELECT departments.department_name,
COUNT(employees.emp_id)
FROM departments
LEFT JOIN employees
ON employees.department = departments.department_name
GROUP BY departments.department_name
"""
mycursor.execute(q)
r = mycursor.fetchall()
print("....Count employees in each department using LEFT JOIN....")
for x in r:
    print(x)

print("##### ........ RIGHT JOIN ........ #####")

### 1 Show all departments.
q = """
SELECT departments.*
FROM employees
RIGHT JOIN departments
ON employees.department = departments.department_name
"""
mycursor.execute(q)
r = mycursor.fetchall()
print("....Show all departments....")
for x in r:
    print(x)


### 2 Find departments without employees.
q = """
SELECT departments.*
FROM employees
RIGHT JOIN departments
ON employees.department = departments.department_name
WHERE employees.emp_id IS NULL
"""
mycursor.execute(q)
r = mycursor.fetchall()
print("....Find departments without employees....")
for x in r:
    print(x)


### 3 Display department names with employee salaries.
q = """
SELECT departments.department_name,
employees.salary
FROM employees
RIGHT JOIN departments
ON employees.department = departments.department_name
"""
mycursor.execute(q)
r = mycursor.fetchall()
print("....Display department names with employee salaries....")
for x in r:
    print(x)


### 4 Count employees in each department.
q = """
SELECT departments.department_name,
COUNT(employees.emp_id)
FROM employees
RIGHT JOIN departments
ON employees.department = departments.department_name
GROUP BY departments.department_name
"""
mycursor.execute(q)
r = mycursor.fetchall()
print("....Count employees in each department....")
for x in r:
    print(x)


### 5 Show department names alphabetically.
q = """
SELECT departments.department_name
FROM employees
RIGHT JOIN departments
ON employees.department = departments.department_name
GROUP BY departments.department_name
ORDER BY departments.department_name
"""
mycursor.execute(q)
r = mycursor.fetchall()
print("....Show department names alphabetically....")
for x in r:
    print(x)

print("##### ........ FULL JOIN ........ #####")

### 1 Show all employees and departments.
q = """
SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments
ON employees.department = departments.department_name

UNION

SELECT employees.name, departments.department_name
FROM employees
RIGHT JOIN departments
ON employees.department = departments.department_name
"""
mycursor.execute(q)
r = mycursor.fetchall()
print("....Show all employees and departments....")
for x in r:
    print(x)


### 2 Show unmatched employees.
q = """
SELECT employees.*
FROM employees
LEFT JOIN departments
ON employees.department = departments.department_name
WHERE departments.department_name IS NULL
"""
mycursor.execute(q)
r = mycursor.fetchall()
print("....Show unmatched employees....")
for x in r:
    print(x)


### 3 Show unmatched departments.
q = """
SELECT departments.*
FROM employees
RIGHT JOIN departments
ON employees.department = departments.department_name
WHERE employees.emp_id IS NULL
"""
mycursor.execute(q)
r = mycursor.fetchall()
print("....Show unmatched departments....")
for x in r:
    print(x)


### 4 Show all matched and unmatched records.
q = """
SELECT employees.name,
departments.department_name
FROM employees
LEFT JOIN departments
ON employees.department = departments.department_name

UNION

SELECT employees.name,
departments.department_name
FROM employees
RIGHT JOIN departments
ON employees.department = departments.department_name
"""
mycursor.execute(q)
r = mycursor.fetchall()
print("....Show all matched and unmatched records....")
for x in r:
    print(x)


### 5 Display employee name with department (including unmatched).
q = """
SELECT employees.name,
departments.department_name
FROM employees
LEFT JOIN departments
ON employees.department = departments.department_name

UNION

SELECT employees.name,
departments.department_name
FROM employees
RIGHT JOIN departments
ON employees.department = departments.department_name
"""
mycursor.execute(q)
r = mycursor.fetchall()
print("....Display employee name with department (including unmatched)....")
for x in r:
    print(x)

#### alter the tabel

# c = """
# ALTER TABLE employees
# ADD manager_id INT
# """
# mycursor.execute(c)
# mydb.commit()
# print("manager_id column added.")

# ## values assign krni h 
# u = """
# UPDATE employees
# SET manager_id =
# CASE emp_id
# WHEN 101 THEN 106
# WHEN 102 THEN 107
# WHEN 103 THEN 108
# WHEN 104 THEN 110
# WHEN 105 THEN 109
# WHEN 106 THEN NULL
# WHEN 107 THEN NULL
# WHEN 108 THEN NULL
# WHEN 109 THEN NULL
# WHEN 110 THEN NULL
# WHEN 111 THEN 106
# END
# """
# mycursor.execute(u)
# mydb.commit()
# print("Manager IDs updated.")

# ## project id add krni h 
# c = """
# ALTER TABLE employees
# ADD project_id INT
# """
# mycursor.execute(c)
# mydb.commit()
# print("project_id column added.")

# ## project table create 
# c = """
# CREATE TABLE projects(
# project_id INT PRIMARY KEY,
# project_name VARCHAR(50),
# department_name VARCHAR(50),
# duration_months INT
# )
# """
# mycursor.execute(c)
# mydb.commit()
# print("Projects table created.")

# ## project tabel me values insert
# s = """
# INSERT INTO projects
# (project_id, project_name, department_name, duration_months)
# VALUES
# (%s,%s,%s,%s)
# """

# value = [

# (1,'Banking','IT',12),
# (2,'E-Commerce','IT',8),
# (3,'Recruitment','HR',6),
# (4,'Payroll','HR',10),
# (5,'Investment','Finance',15),
# (6,'Tax System','Finance',9),
# (7,'Digital Marketing','Marketing',7),
# (8,'Brand Promotion','Marketing',5),
# (9,'CRM','Sales',8),
# (10,'Retail Sales','Sales',11)

# ]

# mycursor.executemany(s,value)
# mydb.commit()

# print(mycursor.rowcount,"records inserted.")

# ## employees ko project assign krna h 
# u = """
# UPDATE employees
# SET project_id =
# CASE emp_id
# WHEN 101 THEN 1
# WHEN 102 THEN 3
# WHEN 103 THEN 5
# WHEN 104 THEN 7
# WHEN 105 THEN 9
# WHEN 106 THEN 2
# WHEN 107 THEN 4
# WHEN 108 THEN 6
# WHEN 109 THEN 10
# WHEN 110 THEN 8
# WHEN 111 THEN 1
# END
# """

# mycursor.execute(u)
# mydb.commit()

# print("Projects assigned.")

##### .... self join .....#####

# 1 Show employee and manager names
s = """
SELECT e.name AS employee_name,
       m.name AS manager_name
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.emp_id
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Show employee and manager names....")
for x in r:
    print(x)

## 2. Find employees without managers
s = """
SELECT e.name
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.emp_id
WHERE e.manager_id IS NULL
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Find employees without managers....")
for x in r:
    print(x)

## 3 Find manager of Riya
s = """
SELECT e.name AS employee_name,
       m.name AS manager_name
FROM employees e
JOIN employees m
ON e.manager_id = m.emp_id
WHERE e.name = 'Amit Sharma'
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Find manager of Riya....")
for x in r:
    print(x)

## 4. Count employees under each manager
s = """
SELECT m.name AS manager_name,
       COUNT(e.emp_id) AS employee_count
FROM employees e
JOIN employees m
ON e.manager_id = m.emp_id
GROUP BY m.emp_id, m.name
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Count employees under each manager....")
for x in r:
    print(x)

## 5 Show manager name with employee salary
s = """
SELECT e.name AS employee_name,
       e.salary,
       m.name AS manager_name
FROM employees e
JOIN employees m
ON e.manager_id = m.emp_id
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Show manager name with employee salary....")
for x in r:
    print(x)

### cross join

# s = "DESCRIBE departments"
# mycursor.execute(s)
# r = mycursor.fetchall()

# for x in r:
#     print(x)

## 6 Show every employee with every department
print(".....CROSS JOIN.....")

s = """
SELECT e.name AS employee_name,
       d.department_name AS department
FROM employees AS e
CROSS JOIN departments AS d
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Show every employee with every department....")
for x in r:
    print(x)

## 7 Count total rows after CROSS JOIN
s = """
SELECT COUNT(*)
FROM employees e
CROSS JOIN departments d
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Count total rows after CROSS JOIN....")
for x in r:
    print(x)

## 8 Show combinations sorted by employee
s = """
SELECT e.name AS employee_name,
       d.department_name
FROM employees e
CROSS JOIN departments d
ORDER BY e.name ASC
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Show combinations sorted by employee....")
for x in r:
    print(x)

## 9 Show only Finance combinations
s = """
SELECT e.name AS employee_name,
       d.department_name
FROM employees e
CROSS JOIN departments d
WHERE d.department_name = 'Finance'
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Show only Finance combinations....")
for x in r:
    print(x)

## 10 Show employees with every project
s = """
SELECT e.name AS employee_name,
       p.project_name
FROM employees e
CROSS JOIN projects p
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Show employees with every project....")
for x in r:
    print(x)

## multiple join 
## 11 Show employee, department and project
s = """
SELECT e.name AS employee_name,
       d.department_name,
       p.project_name
FROM employees e
JOIN departments d
    ON e.department = d.department_name
JOIN projects p
    ON e.project_id = p.project_id
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Show employee, department and project....")
for x in r:
    print(x)

## 12 Show project names with departments
s = """
SELECT p.project_name,
       d.department_name
FROM projects p
JOIN departments d
    ON p.department_name = d.department_name
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Show project names with departments....")
for x in r:
    print(x)

## 13 Show employees working on Banking project
s = """
SELECT e.name AS employee_name,
       p.project_name
FROM employees e
JOIN projects p
    ON e.project_id = p.project_id
WHERE p.project_name = 'Banking'
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Show employees working on Banking project....")
for x in r:
    print(x)

## 14 Count employees in each project
s = """
SELECT p.project_name,
       COUNT(e.emp_id) AS employee_count
FROM projects p
LEFT JOIN employees e
    ON p.project_id = e.project_id
GROUP BY p.project_id, p.project_name
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Count employees in each project....")
for x in r:
    print(x)

## 15 Show average salary project-wise
s = """
SELECT p.project_name,
       AVG(e.salary) AS average_salary
FROM projects p
JOIN employees e
    ON p.project_id = e.project_id
GROUP BY p.project_id, p.project_name
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Show average salary project-wise....")
for x in r:
    print(x)

#### join + group by 

## 16 Count employees department-wise
s = """
SELECT d.department_name,
       COUNT(e.emp_id) AS employee_count
FROM departments d
LEFT JOIN employees e
    ON d.department_name = e.department
GROUP BY d.department_id, d.department_name
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Count employees department-wise....")
for x in r:
    print(x)

## 17 Find average salary department-wise
s = """
SELECT d.department_name,
       AVG(e.salary) AS average_salary
FROM departments d
JOIN employees e
    ON d.department_name = e.department
GROUP BY d.department_id, d.department_name
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Find average salary department-wise....")
for x in r:
    print(x)

## 18 Find highest salary department-wise
s = """
SELECT d.department_name,
       MAX(e.salary) AS highest_salary
FROM departments d
JOIN employees e
    ON d.department_name = e.department
GROUP BY d.department_id, d.department_name
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Find highest salary department-wise....")
for x in r:
    print(x)

## 19 Find lowest salary department-wise
s = """
SELECT d.department_name,
       MIN(e.salary) AS lowest_salary
FROM departments d
JOIN employees e
    ON d.department_name = e.department
GROUP BY d.department_id, d.department_name
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Find lowest salary department-wise....")
for x in r:
    print(x)

## 20 Find total salary department-wise
s = """
SELECT d.department_name,
       SUM(e.salary) AS total_salary
FROM departments d
JOIN employees e
    ON d.department_name = e.department
GROUP BY d.department_id, d.department_name
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Find total salary department-wise....")
for x in r:
    print(x)

### join + having

## 21 Departments having more than 2 employees
s = """
SELECT d.department_name,
       COUNT(e.emp_id) AS employee_count
FROM departments d
JOIN employees e
    ON d.department_name = e.department
GROUP BY d.department_id, d.department_name
HAVING COUNT(e.emp_id) > 2
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Departments having more than 2 employees....")
for x in r:
    print(x)

## 22 Departments with average salary > 50000
s = """
SELECT d.department_name,
       AVG(e.salary) AS average_salary
FROM departments d
JOIN employees e
    ON d.department_name = e.department
GROUP BY d.department_id, d.department_name
HAVING AVG(e.salary) > 50000
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Departments with average salary greater than 50000....")
for x in r:
    print(x)

## 23 Departments where total salary > 100000
s = """
SELECT d.department_name,
       SUM(e.salary) AS total_salary
FROM departments d
JOIN employees e
    ON d.department_name = e.department
GROUP BY d.department_id, d.department_name
HAVING SUM(e.salary) > 100000
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Departments where total salary is greater than 100000....")
for x in r:
    print(x)

## 24 Projects having more than 1 employee
s = """
SELECT p.project_name,
       COUNT(e.emp_id) AS employee_count
FROM projects p
JOIN employees e
    ON p.project_id = e.project_id
GROUP BY p.project_id, p.project_name
HAVING COUNT(e.emp_id) > 1
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Projects having more than 1 employee....")
for x in r:
    print(x)

## 25 Departments where minimum salary > 45000
s = """
SELECT d.department_name,
       MIN(e.salary) AS minimum_salary
FROM departments d
JOIN employees e
    ON d.department_name = e.department
GROUP BY d.department_id, d.department_name
HAVING MIN(e.salary) > 45000
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Departments where minimum salary is greater than 45000....")
for x in r:
    print(x)

#### 
a = """SELECT
    d.department_name,
    COUNT(*) AS total_employees,
    AVG(e.salary) AS average_salary
FROM employees e
INNER JOIN departments d
    ON e.department = d.department_name
GROUP BY d.department_name
HAVING AVG(e.salary) > 50000
ORDER BY average_salary DESC"""
mycursor.execute(a)
r = mycursor.fetchall()
print("....Departments with average salary greater than 50000, ordered by average salary descending....")
for x in r:
    print(x)

####>>>>>>> subquery >>>>>>>>#######
print(".......Subquery......")

## 1. Find employees whose salary is greater than the average salary.
s = """
SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees whose salary is greater than average salary....")
for x in r:
    print(x)

## 2. Find the employee with the highest salary.
s = """
SELECT *
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employee with the highest salary....")
for x in r:
    print(x)

## 3. Find the employee with the lowest salary.
s = """
SELECT *
FROM employees
WHERE salary = (
    SELECT MIN(salary)
    FROM employees
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employee with the lowest salary....")
for x in r:
    print(x)

## 4. Find employees whose salary is equal to the highest salary.
s = """
SELECT name, salary
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees whose salary is equal to highest salary....")
for x in r:
    print(x)

## 5. Find employees whose salary is less than the average salary.
s = """
SELECT *
FROM employees
WHERE salary < (
    SELECT AVG(salary)
    FROM employees
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees whose salary is less than average salary....")
for x in r:
    print(x)

## 6. Find the second highest salary using a subquery.
s = """
SELECT MAX(salary)
FROM employees
WHERE salary < (
    SELECT MAX(salary)
    FROM employees
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Second highest salary....")
for x in r:
    print(x)

## 7. Find the employee who has the second highest salary.
s = """
SELECT *
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
    WHERE salary < (
        SELECT MAX(salary)
        FROM employees
    )
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employee with second highest salary....")
for x in r:
    print(x)

## 8. Find employees working in the IT department using a subquery.
s = """
SELECT *
FROM employees
WHERE department = (
    SELECT department_name
    FROM departments
    WHERE department_name = 'IT'
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees working in IT department....")
for x in r:
    print(x)

## 9. Find employees working in IT or HR using a subquery.
s = """
SELECT *
FROM employees
WHERE department IN (
    SELECT department_name
    FROM departments
    WHERE department_name IN ('IT', 'HR')
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees working in IT or HR....")
for x in r:
    print(x)

## 10. Find employees who are not working in the IT department using a subquery.
s = """
SELECT *
FROM employees
WHERE department NOT IN (
    SELECT department_name
    FROM departments
    WHERE department_name = 'IT'
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees not working in IT department....")
for x in r:
    print(x)

## 11. Find the third highest salary using nested subqueries.
s = """
SELECT MAX(salary)
FROM employees
WHERE salary < (
    SELECT MAX(salary)
    FROM employees
    WHERE salary < (
        SELECT MAX(salary)
        FROM employees
    )
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Third highest salary....")
for x in r:
    print(x)

## 12. Find employees whose salary is greater than the minimum salary.
s = """
SELECT *
FROM employees
WHERE salary > (
    SELECT MIN(salary)
    FROM employees
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees whose salary is greater than minimum salary....")
for x in r:
    print(x)

## 13. Find employees whose salary is less than the maximum salary.
s = """
SELECT *
FROM employees
WHERE salary < (
    SELECT MAX(salary)
    FROM employees
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees whose salary is less than maximum salary....")
for x in r:
    print(x)

## 14. Find total salary of employees whose salary is greater than average salary.
s = """
SELECT SUM(salary)
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Total salary of employees above average salary....")
for x in r:
    print(x)

## 15. Find count of employees whose salary is greater than average salary.
s = """
SELECT COUNT(*)
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Count of employees above average salary....")
for x in r:
    print(x)

### Subquery + Correlated Subquery + EXISTS
print(".....Subquery + Correlated Subquery + EXISTS.....")

## 1 Display every employee's salary along with the overall average salary.
s = """
SELECT name,
       salary,
       (SELECT AVG(salary) FROM employees) AS average_salary
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employee salary with overall average salary....")
for x in r:
    print(x)

## 2. Display employee name, salary and difference between employee salary and average salary.
s = """
SELECT name,
       salary,
       salary - (SELECT AVG(salary) FROM employees) AS salary_difference
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employee salary and difference from average salary....")
for x in r:
    print(x)

## 3. Using a subquery in FROM, display employee names and salaries.
s = """
SELECT employee_name,
       employee_salary
FROM (
    SELECT name AS employee_name,
           salary AS employee_salary
    FROM employees
) AS temp
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employee names and salaries using subquery in FROM....")
for x in r:
    print(x)

## 4. Find departments where at least one employee exists using EXISTS.
s = """
SELECT d.department_name
FROM departments d
WHERE EXISTS (
    SELECT 1
    FROM employees e
    WHERE e.department = d.department_name
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Departments having at least one employee....")
for x in r:
    print(x)

## 5. Find departments where no employee exists using NOT EXISTS.
s = """
SELECT d.department_name
FROM departments d
WHERE NOT EXISTS (
    SELECT 1
    FROM employees e
    WHERE e.department = d.department_name
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Departments having no employees....")
for x in r:
    print(x)

## 6. Find employees whose salary is greater than the overall average salary.
s = """
SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees earning more than overall average salary....")
for x in r:
    print(x)

## 7. Find employees whose salary is equal to the maximum salary.
s = """
SELECT *
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees with maximum salary....")
for x in r:
    print(x)

## 8. Find employees working in departments that have at least 2 employees.
s = """
SELECT *
FROM employees
WHERE department IN (
    SELECT department
    FROM employees
    GROUP BY department
    HAVING COUNT(*) >= 2
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees working in departments having at least 2 employees....")
for x in r:
    print(x)

## 9. Find departments whose total employee salary is greater than 100000.
s = """
SELECT department,
       SUM(salary) AS total_salary
FROM employees
GROUP BY department
HAVING SUM(salary) > 100000
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Departments whose total salary is greater than 100000....")
for x in r:
    print(x)

## 10. Find employees working in the same department as Rahul.
s = """
SELECT *
FROM employees
WHERE department = (
    SELECT department
    FROM employees
    WHERE name = 'Rahul Singh'
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees working in Rahul's department....")
for x in r:
    print(x)

## 11. Find employees whose salary is greater than their department's average salary.
s = """
SELECT e.name,
       e.department,
       e.salary
FROM employees e
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department = e.department
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees earning more than their department average....")
for x in r:
    print(x)

## 12. Find the highest-paid employee in each department using a correlated subquery.
s = """
SELECT e.name,
       e.department,
       e.salary
FROM employees e
WHERE e.salary = (
    SELECT MAX(e2.salary)
    FROM employees e2
    WHERE e2.department = e.department
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Highest-paid employee in each department....")
for x in r:
    print(x)


## 13. Find the lowest-paid employee in each department.
s = """
SELECT e.name,
       e.department,
       e.salary
FROM employees e
WHERE e.salary = (
    SELECT MIN(e2.salary)
    FROM employees e2
    WHERE e2.department = e.department
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Lowest-paid employee in each department....")
for x in r:
    print(x)


 ##14. Find departments whose average salary is greater than the company's overall average salary.
s = """
SELECT department,
       AVG(salary) AS department_average
FROM employees
GROUP BY department
HAVING AVG(salary) > (
    SELECT AVG(salary)
    FROM employees
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Departments above company average salary....")
for x in r:
    print(x)

## 15 Find employees who earn more than their manager.
s = """
SELECT e.name AS employee_name,
       e.salary,
       (
           SELECT m.salary
           FROM employees m
           WHERE m.emp_id = e.manager_id
       ) AS manager_salary
FROM employees e
WHERE e.salary > (
    SELECT m.salary
    FROM employees m
    WHERE m.emp_id = e.manager_id
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees earning more than their manager....")
for x in r:
    print(x)


print("##### ........ CASE WHEN ........ #####")


### 1. Display employee name, salary and salary category
# >= 60000 → High
# >= 50000 → Medium
# < 50000 → Low

s = """
SELECT name, salary,
CASE
    WHEN salary >= 60000 THEN 'High'
    WHEN salary >= 50000 THEN 'Medium'
    ELSE 'Low'
END AS salary_category
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employee salary category....")
for x in r:
    print(x)


### 2. If salary >= 50000 → Eligible, otherwise Not Eligible

s = """
SELECT name, salary,
CASE
    WHEN salary >= 50000 THEN 'Eligible'
    ELSE 'Not Eligible'
END AS eligibility
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Salary eligibility....")
for x in r:
    print(x)


### 3. Create department type
# IT → Technical
# HR → Non-Technical
# Others → Other

s = """
SELECT name, department,
CASE
    WHEN department = 'IT' THEN 'Technical'
    WHEN department = 'HR' THEN 'Non-Technical'
    ELSE 'Other'
END AS department_type
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Department type....")
for x in r:
    print(x)


### 4. Salary >= 60000 → Senior
# Salary < 60000 → Junior

s = """
SELECT name, salary,
CASE
    WHEN salary >= 60000 THEN 'Senior'
    ELSE 'Junior'
END AS employee_level
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employee level....")
for x in r:
    print(x)


### 5. Salary Even or Odd

s = """
SELECT name, salary,
CASE
    WHEN salary % 2 = 0 THEN 'Even'
    ELSE 'Odd'
END AS salary_type
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Salary Even/Odd....")
for x in r:
    print(x)


### 6. Salary categories
# 0–39999 → Very Low
# 40000–49999 → Low
# 50000–59999 → Medium
# 60000+ → High

s = """
SELECT name, salary,
CASE
    WHEN salary < 40000 THEN 'Very Low'
    WHEN salary < 50000 THEN 'Low'
    WHEN salary < 60000 THEN 'Medium'
    ELSE 'High'
END AS salary_category
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Detailed salary categories....")
for x in r:
    print(x)


### 7. IT + salary >= 60000 → Senior IT
# IT + salary < 60000 → Junior IT
# Others → Other

s = """
SELECT name, department, salary,
CASE
    WHEN department = 'IT' AND salary >= 60000 THEN 'Senior IT'
    WHEN department = 'IT' AND salary < 60000 THEN 'Junior IT'
    ELSE 'Other'
END AS employee_type
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....IT employee classification....")
for x in r:
    print(x)


### 8. Age categories
# age < 25 → Young
# 25–35 → Adult
# > 35 → Senior

s = """
SELECT name, age,
CASE
    WHEN age < 25 THEN 'Young'
    WHEN age <= 35 THEN 'Adult'
    ELSE 'Senior'
END AS age_category
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Age categories....")
for x in r:
    print(x)


### 9. Experience category using joining date
# More than 5 years → Experienced
# 3–5 years → Mid-Level
# Less than 3 years → Fresher

s = """
SELECT name, joining_dates,
CASE
    WHEN TIMESTAMPDIFF(YEAR, joining_dates, CURDATE()) > 5
        THEN 'Experienced'
    WHEN TIMESTAMPDIFF(YEAR, joining_dates, CURDATE()) >= 3
        THEN 'Mid-Level'
    ELSE 'Fresher'
END AS experience_category
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Experience category....")
for x in r:
    print(x)


### 10. Bonus category
# >= 60000 → 20%
# >= 50000 → 15%
# Otherwise → 10%

s = """
SELECT name, salary,
CASE
    WHEN salary >= 60000 THEN '20% Bonus'
    WHEN salary >= 50000 THEN '15% Bonus'
    ELSE '10% Bonus'
END AS bonus_category
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Bonus category....")
for x in r:
    print(x)


### 11. Count employees whose salary >= 50000 using CASE WHEN

s = """
SELECT
COUNT(
    CASE
        WHEN salary >= 50000 THEN 1
    END
) AS employees_50000_plus
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees earning >= 50000....")
for x in r:
    print(x)


### 12. Total salary of employees whose salary >= 50000

s = """
SELECT
SUM(
    CASE
        WHEN salary >= 50000 THEN salary
        ELSE 0
    END
) AS total_salary
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Total salary of employees earning >= 50000....")
for x in r:
    print(x)


### 13. Department-wise number of employees earning >= 50000

s = """
SELECT
department,
COUNT(
    CASE
        WHEN salary >= 50000 THEN 1
    END
) AS high_salary_employees
FROM employees
GROUP BY department
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Department-wise employees earning >= 50000....")
for x in r:
    print(x)


### 14. Department-wise total salary of employees earning >= 50000

s = """
SELECT
department,
SUM(
    CASE
        WHEN salary >= 50000 THEN salary
        ELSE 0
    END
) AS high_salary_total
FROM employees
GROUP BY department
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Department-wise high salary total....")
for x in r:
    print(x)


### 15. Department-wise average salary only for employees earning >= 50000

s = """
SELECT
department,
AVG(
    CASE
        WHEN salary >= 50000 THEN salary
    END
) AS average_high_salary
FROM employees
GROUP BY department
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Department-wise average salary >= 50000....")
for x in r:
    print(x)


# =========================================================
# CTE (COMMON TABLE EXPRESSION)
# =========================================================

print("##### ........ CTE (Common Table Expression) ........ #####")

### 1. Create a CTE containing all employees and display it.

s = """
WITH employee_data AS (
    SELECT *
    FROM employees
)
SELECT *
FROM employee_data
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....All employees using CTE....")
for x in r:
    print(x)


### 2. Create a CTE containing employees whose salary is greater than 50000.

s = """
WITH high_salary AS (
    SELECT *
    FROM employees
    WHERE salary > 50000
)
SELECT *
FROM high_salary
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees whose salary is greater than 50000....")
for x in r:
    print(x)


### 3. Using a CTE, display employee name and salary.

s = """
WITH employee_data AS (
    SELECT name, salary
    FROM employees
)
SELECT *
FROM employee_data
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employee name and salary using CTE....")
for x in r:
    print(x)


### 4. Using a CTE, calculate average salary.

s = """
WITH salary_data AS (
    SELECT salary
    FROM employees
)
SELECT AVG(salary)
FROM salary_data
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Average salary using CTE....")
for x in r:
    print(x)


### 5. Using a CTE, find maximum salary.

s = """
WITH salary_data AS (
    SELECT salary
    FROM employees
)
SELECT MAX(salary)
FROM salary_data
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Maximum salary using CTE....")
for x in r:
    print(x)


### 6. Create a CTE for department-wise average salary.

s = """
WITH dept_salary AS (
    SELECT
        department,
        AVG(salary) AS average_salary
    FROM employees
    GROUP BY department
)
SELECT *
FROM dept_salary
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Department-wise average salary....")
for x in r:
    print(x)


### 7. Using that CTE, show departments
#    with average salary greater than 50000.

s = """
WITH dept_salary AS (
    SELECT
        department,
        AVG(salary) AS average_salary
    FROM employees
    GROUP BY department
)
SELECT *
FROM dept_salary
WHERE average_salary > 50000
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Departments with average salary > 50000....")
for x in r:
    print(x)


### 8. Create a CTE containing employees from IT department.

s = """
WITH it_employees AS (
    SELECT *
    FROM employees
    WHERE department = 'IT'
)
SELECT *
FROM it_employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....IT employees using CTE....")
for x in r:
    print(x)


### 9. Create a CTE containing employees with salary >= 50000
#    and JOIN it with departments.

s = """
WITH high_salary AS (
    SELECT *
    FROM employees
    WHERE salary >= 50000
)
SELECT
    h.name,
    h.salary,
    d.department_name
FROM high_salary h
INNER JOIN departments d
ON h.department = d.department_name
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees earning >= 50000 with department....")
for x in r:
    print(x)


### 10. Create a CTE to calculate department-wise employee count.

s = """
WITH dept_count AS (
    SELECT
        department,
        COUNT(*) AS total_employees
    FROM employees
    GROUP BY department
)
SELECT *
FROM dept_count
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Department-wise employee count....")
for x in r:
    print(x)


### 11. Create a CTE that categorizes employees
#     into High, Medium and Low salary.

s = """
WITH salary_category AS (
    SELECT
        name,
        salary,
        CASE
            WHEN salary >= 60000 THEN 'High'
            WHEN salary >= 50000 THEN 'Medium'
            ELSE 'Low'
        END AS category
    FROM employees
)
SELECT *
FROM salary_category
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employee salary categories....")
for x in r:
    print(x)


### 12. Using that CTE, count employees in each salary category.

s = """
WITH salary_category AS (
    SELECT
        name,
        salary,
        CASE
            WHEN salary >= 60000 THEN 'High'
            WHEN salary >= 50000 THEN 'Medium'
            ELSE 'Low'
        END AS category
    FROM employees
)
SELECT
    category,
    COUNT(*) AS total_employees
FROM salary_category
GROUP BY category
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees in each salary category....")
for x in r:
    print(x)


### 13. Create a CTE for department-wise average salary
#     and find the department with highest average salary.

s = """
WITH dept_salary AS (
    SELECT
        department,
        AVG(salary) AS average_salary
    FROM employees
    GROUP BY department
)
SELECT
    department,
    average_salary
FROM dept_salary
ORDER BY average_salary DESC
LIMIT 1
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Department with highest average salary....")
for x in r:
    print(x)


### 14. Create two CTEs and JOIN them.

s = """
WITH employee_data AS (
    SELECT
        department,
        COUNT(*) AS total_employees
    FROM employees
    GROUP BY department
),
salary_data AS (
    SELECT
        department,
        AVG(salary) AS average_salary
    FROM employees
    GROUP BY department
)
SELECT
    e.department,
    e.total_employees,
    s.average_salary
FROM employee_data e
INNER JOIN salary_data s
ON e.department = s.department
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Two CTEs joined together....")
for x in r:
    print(x)


### 15. Create a CTE that calculates total salary
#     department-wise and show departments
#     where total salary > 100000.

s = """
WITH dept_salary AS (
    SELECT
        department,
        SUM(salary) AS total_salary
    FROM employees
    GROUP BY department
)
SELECT
    department,
    total_salary
FROM dept_salary
WHERE total_salary > 100000
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Departments with total salary > 100000....")
for x in r:
    print(x)

# =========================================================
# WINDOW FUNCTIONS
# =========================================================

print("##### ........ WINDOW FUNCTIONS ........ #####")

### 1. Assign a row number to all employees
###    based on salary descending.

s = """
SELECT
    name,
    salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Row number based on salary descending....")
for x in r:
    print(x)


### 2. Rank employees based on salary.

s = """
SELECT
    name,
    salary,
    RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees ranked by salary....")
for x in r:
    print(x)


### 3. Use DENSE_RANK() to rank employees based on salary.

s = """
SELECT
    name,
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees using DENSE_RANK....")
for x in r:
    print(x)


### 4. Display employee name, salary and overall average salary.

s = """
SELECT
    name,
    salary,
    AVG(salary) OVER () AS average_salary
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employee salary and overall average salary....")
for x in r:
    print(x)


### 5. Display employee name and previous employee's salary using LAG().

s = """
SELECT
    name,
    salary,
    LAG(salary) OVER (ORDER BY emp_id) AS previous_salary
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employee and previous employee salary....")
for x in r:
    print(x)


### 6. Find department-wise average salary using PARTITION BY.

s = """
SELECT
    name,
    department,
    salary,
    AVG(salary) OVER (PARTITION BY department) AS department_avg_salary
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Department-wise average salary....")
for x in r:
    print(x)


### 7. Assign row numbers separately for each department.

s = """
SELECT
    name,
    department,
    salary,
    ROW_NUMBER() OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS row_num
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Row number within each department....")
for x in r:
    print(x)


### 8. Rank employees separately within each department.

s = """
SELECT
    name,
    department,
    salary,
    RANK() OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS department_rank
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employee rank within each department....")
for x in r:
    print(x)


### 9. Find the highest-paid employee from each department.

s = """
WITH ranked_employees AS (
    SELECT
        name,
        department,
        salary,
        RANK() OVER (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS salary_rank
    FROM employees
)
SELECT
    name,
    department,
    salary
FROM ranked_employees
WHERE salary_rank = 1
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Highest-paid employee from each department....")
for x in r:
    print(x)


### 10. Find the top 2 employees from each department.

s = """
WITH ranked_employees AS (
    SELECT
        name,
        department,
        salary,
        ROW_NUMBER() OVER (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS row_num
    FROM employees
)
SELECT
    name,
    department,
    salary
FROM ranked_employees
WHERE row_num <= 2
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Top 2 employees from each department....")
for x in r:
    print(x)


### 11. Calculate running total of salaries.

s = """
SELECT
    name,
    salary,
    SUM(salary) OVER (
        ORDER BY emp_id
    ) AS running_total
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Running total of salaries....")
for x in r:
    print(x)


### 12. Calculate department-wise running total of salaries.

s = """
SELECT
    name,
    department,
    salary,
    SUM(salary) OVER (
        PARTITION BY department
        ORDER BY emp_id
    ) AS department_running_total
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Department-wise running salary total....")
for x in r:
    print(x)


### 13. Display current salary and previous salary.

s = """
SELECT
    name,
    salary AS current_salary,
    LAG(salary) OVER (
        ORDER BY emp_id
    ) AS previous_salary
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Current and previous salary....")
for x in r:
    print(x)


### 14. Display current salary and next salary.

s = """
SELECT
    name,
    salary AS current_salary,
    LEAD(salary) OVER (
        ORDER BY emp_id
    ) AS next_salary
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Current and next salary....")
for x in r:
    print(x)


### 15. Calculate difference between current salary
###     and previous salary using LAG().

s = """
SELECT
    name,
    salary AS current_salary,
    LAG(salary) OVER (
        ORDER BY emp_id
    ) AS previous_salary,
    salary - LAG(salary) OVER (
        ORDER BY emp_id
    ) AS salary_difference
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Difference between current and previous salary....")
for x in r:
    print(x)

# ######## WINDOW FUNCTIONS - PART 2 ########

print("######## WINDOW FUNCTIONS - PART 2 ########")


## 1. FIRST_VALUE() - highest salary alongside every employee
s = """
SELECT
    name,
    salary,
    FIRST_VALUE(salary) OVER (ORDER BY salary DESC) AS highest_salary
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Highest salary alongside every employee....")
for x in r:
    print(x)


## 2. FIRST_VALUE() - highest salary of each department
s = """
SELECT
    name,
    department,
    salary,
    FIRST_VALUE(salary) OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS department_highest_salary
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Highest salary of each department....")
for x in r:
    print(x)


## 3. LAG() - previous employee's salary
s = """
SELECT
    name,
    salary,
    LAG(salary) OVER (ORDER BY salary DESC) AS previous_salary
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Previous employee's salary....")
for x in r:
    print(x)


## 4. LEAD() - next employee's salary
s = """
SELECT
    name,
    salary,
    LEAD(salary) OVER (ORDER BY salary DESC) AS next_salary
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Next employee's salary....")
for x in r:
    print(x)


## 5. Difference between current salary and previous salary
s = """
SELECT
    name,
    salary,
    LAG(salary) OVER (ORDER BY salary DESC) AS previous_salary,
    salary - LAG(salary) OVER (ORDER BY salary DESC) AS salary_difference
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Difference between current and previous salary....")
for x in r:
    print(x)

# 6. Running total of salaries
s = """
SELECT
    name,
    salary,
    SUM(salary) OVER (
        ORDER BY salary
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Running total of salaries....")
for x in r:
    print(x)


## 7. Department-wise running total
s = """
SELECT
    name,
    department,
    salary,
    SUM(salary) OVER (
        PARTITION BY department
        ORDER BY salary
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS department_running_total
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Department-wise running total....")
for x in r:
    print(x)


## 8. 3-row moving average of salaries
s = """
SELECT
    name,
    salary,
    AVG(salary) OVER (
        ORDER BY emp_id
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_average
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....3-row moving average of salaries....")
for x in r:
    print(x)

## 9. Top 2 employees from every department
s = """
SELECT *
FROM (
    SELECT
        name,
        department,
        salary,
        ROW_NUMBER() OVER (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS row_num
    FROM employees
) AS ranked
WHERE row_num <= 2
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Top 2 employees from every department....")
for x in r:
    print(x)


## 10. Highest-paid employee from every department
#     using ROW_NUMBER()
s = """
SELECT *
FROM (
    SELECT
        name,
        department,
        salary,
        ROW_NUMBER() OVER (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS row_num
    FROM employees
) AS ranked
WHERE row_num = 1
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Highest-paid employee from every department....")
for x in r:
    print(x)


## 11. Second-highest-paid employee from each department
s = """
SELECT *
FROM (
    SELECT
        name,
        department,
        salary,
        DENSE_RANK() OVER (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS salary_rank
    FROM employees
) AS ranked
WHERE salary_rank = 2
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Second-highest-paid employee from each department....")
for x in r:
    print(x)

# 12. Difference between employee salary and
#     department's highest salary
s = """
SELECT
    name,
    department,
    salary,
    FIRST_VALUE(salary) OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS highest_salary,
    FIRST_VALUE(salary) OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) - salary AS salary_difference
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Difference from department's highest salary....")
for x in r:
    print(x)

# 13. Salary percentage change from previous employee
s = """
SELECT
    name,
    salary,
    LAG(salary) OVER (ORDER BY salary DESC) AS previous_salary,
    ROUND(
        (salary - LAG(salary) OVER (ORDER BY salary DESC))
        / LAG(salary) OVER (ORDER BY salary DESC) * 100,
        2
    ) AS percentage_change
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Salary percentage change from previous employee....")
for x in r:
    print(x)

# 14. Employees earning more than department average
s = """
SELECT
    name,
    department,
    salary,
    ROUND(
        AVG(salary) OVER (PARTITION BY department),
        2
    ) AS department_average
FROM employees
WHERE salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department = employees.department
)
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Employees earning more than department average....")
for x in r:
    print(x)

# 15. Salary category based on department average

s = """
SELECT
    name,
    department,
    salary,
    ROUND(
        AVG(salary) OVER (PARTITION BY department),
        2
    ) AS department_average,
    CASE
        WHEN salary > AVG(salary) OVER (PARTITION BY department)
            THEN 'Above Average'
        WHEN salary = AVG(salary) OVER (PARTITION BY department)
            THEN 'Average'
        ELSE 'Below Average'
    END AS salary_category
FROM employees
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Salary category based on department average....")
for x in r:
    print(x)

## 15 Create salary categories using CASE WHEN based on department-wise average salary.
s = """
WITH salary_data AS (
    SELECT
        name,
        department,
        salary,
        AVG(salary) OVER (PARTITION BY department) AS department_average
    FROM employees
)
SELECT
    name,
    department,
    salary,
    ROUND(department_average, 2) AS department_average,
    CASE
        WHEN salary > department_average THEN 'Above Average'
        WHEN salary = department_average THEN 'Average'
        ELSE 'Below Average'
    END AS salary_category
FROM salary_data
"""
mycursor.execute(s)
r = mycursor.fetchall()
print("....Salary category based on department average....")
for x in r:
    print(x)

print("##### ........ END OF SQL PRACTICE ........ #####")