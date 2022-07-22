''' Exercise #5. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def reverse_string(s):
    if s=='':
        return s
    if len(s)==1:
        return s[0]
    if len(s)>1:
        a=s[-1]
    return a + reverse_string(s[:-1])  # replace this with your implementation


#########################################
# Question 2 - do not delete this comment
#########################################
def find_maximum(lst):
    if lst==[]:
        return -1
    elif len(lst)==1:
        return lst[0]
    elif len(lst)>1:
        if lst[0]>lst[1]:
            lst.pop(1)
            return find_maximum(lst)
        else:
            lst.pop(0)
            return find_maximum(lst)
# replace this with your implementation


#########################################
# Question 3 - do not delete this comment
#########################################
def is_palindrome(s):
    if len(s)==1:
        return True
    if len(s)<1:
        return False
    if len(s)==3:
        if s[0]==s[-1]:
            return True
        else:
            return False
    if len(s)%2==1 and len(s)!=3:
        s=s[:int(len(s)/2)]+s[int(len(s)/2+1):]
        return is_palindrome(s)
    if len(s)%2==0:
        if len(s)==2:
            if s[0]==s[-1]:
                return True
        if len(s)>2:
            if s[0]!=s[-1]:
                return False
            if s[0]==s[-1]:
                return is_palindrome(s[1:-1])
            
# replace this with your implementation


#########################################
# Question 4 - do not delete this comment
#########################################
def climb_combinations(n):
    def stairs_fibo(k):
        if k<2:
            return k
        return stairs_fibo(k-1)+stairs_fibo(k-2)
    if n<=3:
        return n
    else:
        return stairs_fibo(n+1)
  # replace this with your implementation


#########################################
# Question 5 - do not delete this comment
#########################################
def is_valid_paren(s, cnt=0):
    if len(s)==1:
        if s[0]=='(':
            cnt+=1
        if s[0]==')':
            cnt-=1
        if cnt==0:
            return True
        else:
            return False
    elif len(s)>1:
        if s[0]=='(':
            cnt+=1
        elif s[0]==')':
            cnt-=1
        if s[0]!='(' or s[0]!=')':
            return is_valid_paren(s[1:],cnt)
        if cnt<0:
            return False
        elif cnt>=0:
            return is_valid_paren(s[1:],cnt)
    
# replace this with your implementation


#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################

print(reverse_string("abc") == 'cba')
print(reverse_string("Hello!") == '!olleH')

print(find_maximum([9,3,0,10]) == 10)
print(find_maximum([9,3,0]) == 9)
print(find_maximum([]) == -1)

print(is_palindrome("aa") == True)
print(is_palindrome("aa ") == False)
print(is_palindrome("caca") == False)
print(is_palindrome("abcbbcba") == True)

print(climb_combinations(3) == 3)
print(climb_combinations(10) == 89)

print(is_valid_paren("(.(a)")== False)
print(is_valid_paren("p(()r((0)))")== True )

# ============================== END OF FILE =================================
