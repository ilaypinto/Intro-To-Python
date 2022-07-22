''' Exercise #1 - Python.'''

#########################################
# Question 1 - do not delete this comment
#########################################
R = 5.0 # Replace ??? with a positive float of your choice.
# Write the rest of the code for question 1 below here.
π = 3.14
print("Diameter is: " ,2*R)
print("Circumference is: " ,2*π*R)
print("Area is: " ,π*R*R)

#########################################
# Question 2 - do not delete this comment
#########################################
s = "Hello, dear world!" # Replace ??? a string of your choice.
# Write the rest of the code for question 2 below here.
if len(s)>10:
    print(str.lower(s[:10])+str.upper(s[10:]))
else:
    print(("$")+str.replace(s[1:],s[-1],"@"))

#########################################
# Question 3 - do not delete this comment
#########################################
number  = 100 # Replace ??? with a int of your choice.
# Write the rest of the code for question 3 below here.
if (number%2==0):
    print( "I am" ,number,"and I am even")
else:
    print( "I am", number,"and I am odd")

#########################################
# Question 4 - do not delete this comment
#########################################
a = 9 # Replace ??? with a positive int of your choice.
b = 5  # Replace ??? with a positive int of your choice.
c = 5  # Replace ??? with a positive int of your choice.
# Write the rest of the code for question 4 below here.
eq1=(a+b)**(1/c)
eq2=(a**b)**(1/c)
eq3=(a/b)-(b/c)
print("%.5f" % (eq1) )
print("%.5f" % (eq2) )
print("%.5f" % (eq3))

#########################################
# Question 5 - do not delete this comment
#########################################
year = 1900 # Replace ??? with a positive int of your choice.
# Write the rest of the code for question 5 below here.
if (year%4==0 and year%100!=0)or year%400==0:
    print(year, " is a leap year")
else:
    print(year, " is not a leap year")


