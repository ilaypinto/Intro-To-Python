""" Exercise #2. Python for Engineers."""

#########################################
# Question 1 - do not delete this comment
#########################################

a = 3  # Replace the assignment with a positive integer to test your code.
A = [1, 2, 3, 4, 5]  # Replace the assignment with other lists to test your code.
for num in A:
    if num%a==0:
      print(A.index(num))
      break
else:
    print(-1)
# End of code for question 1
#########################################
# Question 2 - do not delete this comment
#########################################
B = ['hello', 'world', 'course', 'python', 'day']
# Replace the assignment with other lists of strings (str) to test your code.
#calculating list average:
sum1=0
for word in B:
    sum1=float(sum1)+float(len(word))  
average= sum1/len(B)
# Write the code for question 2 using a for loop below here.
count=0
for word in B:
    if len(word)>average:
        count=count+1  
print('The number of strings longer than average is', count)
# Write the code for question 2 using a while loop below here..
count=0#נאפס בגלל שהספירה עומדת על מספר מלולאה קודמת
k=0
while k<len(B):
     if len(B[k])>average:
        count=count+1
     k=k+1
print('The number of strings longer than average is', count)
# End of code for question 2
#########################################
# Question 3 - do not delete this comment
#########################################
C = [0, 1, 2, 3, 4]  # Replace the assignment with other lists to test your code.
# Write the rest of the code for question 3 below here.
sum1=0
n=0
i=len(C)
if i==0:
    print(0)
elif i==1:
    print(C[0])
else:
    while n<i-1:
     sum1=C[n]*C[n+1]+sum1
     n=n+1
    print(sum1)
# End of code for question 3
#########################################
# Question 4 - do not delete this comment
#########################################
D = [1, 4, 0, 10,9,8]  # Replace the assignment with other lists to test your code.
# Write the rest of the code for question 4 below here.
new_list=[D[0]]
n=1
temp_sum=0
pre_sum=0
while n<len(D):
    temp_sum=D[n-1]-D[n]
    if abs(temp_sum)>abs(pre_sum):
        new_list.append(D[n])
        pre_sum=temp_sum
    else:
        D.pop(n)
        D.insert(1,0)
        pre_sum=D[n-2]-D[n-1]
    n=n+1
print(new_list)
# End of code for question 4
#########################################
# Question 5 - do not delete this comment
#########################################

my_string = 'abaadddefggg'  # Replace the assignment with other strings to test your code.
k = 3  # Replace the assignment with a positive integer to test your code.
for letter in my_string:
    if letter*k in my_string:
       print("For length", k,", found the substring", letter*k, "!") 
       break
else:
    print("Didn't find a substring for" ,k)
# End of code for question 5
