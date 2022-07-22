''' Exercise #3. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def sum_divisible_by_k(lst, k):
    temp_sum=0
    for num in lst:
        if num%k==0:
            temp_sum=temp_sum+num
    return temp_sum# replace this with your implementation
#########################################
# Question 2 - do not delete this comment
#########################################
def mult_odd_digits(n):
    global multlipication
    multipication=1
    temp_list=[int(x) for x in str(n)]
    for index in temp_list:
        if index%2==1:
            multipication= multipication*index
    return multipication  # replace this with your implementation
#########################################
# Question 3 - do not delete this comment
#########################################
def count_longest_repetition(s, c):
    k=1
    c2=c
    global yum
    yum=0
    if c not in s:
        yum=yum
    else:
        while c2 in s:
            if c*(k+1) in s:
              k=k+1
              c2=c*k
            else:
                yum=len(c2)
                c2=c2*(k+20)
    return yum# replace this with your implementation
#########################################
# Question 4 - do not delete this comment
#########################################
def upper_strings(lst):
    global yam
    yam=lst
    if type(lst)!=type([1,2,3]):
     yam= -1
    else:
        for indx in lst:
            if type(indx) is type("a"):
                lst[lst.index(indx)]=indx.upper()
                yam=lst
    return yam# replace this with your implementation

#########################################
# Question 5 - do not delete this comment
#########################################
def div_mat_by_scalar(mat, alpha):
    new_mat=[]
    for i in range(len(mat)):
        new_mat.append([])
        for j in range(len(mat[i])):
            new_mat[i].append(mat[i][j]//alpha)
    return new_mat
# replace this with your implementation
#########################################
# Question 6 - do not delete this comment
#########################################
def mat_transpose(mat):
    yay_mat=[]
    n=0
    while n<len(mat[0]):
     yay_mat.append([])
     n=n+1
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            yay_mat[j].append(mat[i][j])
    return yay_mat  # replace this with your implementation

