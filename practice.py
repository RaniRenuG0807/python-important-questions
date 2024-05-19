# Q1
subjects = ["python","java","c++","python","javascript","java","python","java","c++","c"]
# 1 classrome for 1 subject
# print(len(subjects))
sub_set = set(subjects)
print("required classroom",len(sub_set))

# question 2
word = {"table":["a piece of furniture","list of facts and figures"], "cat":"a small animal"}
print(word)
emp = {}
emp["table"]="a piece of furniture"
emp["fact"]=["fact1","fact2"]
emp["cat"]="a small animal"
# print(emp)
emp["table"]="list of facts & figures"
# print(emp)

# Question 3
marks = {}
# marks["Maths"] = int(input("Enter Maths Marks "))
# marks["Computer"] = int(input("Enter computer marks "))
# marks["English"] = int(input("Enter English Marks "))
print(marks)

# question 4
num = {9}
num2 = {str(9.0)}
print(num.union(num2))
print(num2.union(num))
# type 2
num_set = {("float",9.0),("int",9)}
print(num_set)