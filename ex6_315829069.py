''' Exercise #6. Python for Engineers.'''

#########################################
# Question 1.a - do not delete this comment
#########################################
def four_bonacci_rec(n):
        if n<4:
            return n
        return four_bonacci_rec(n-1)+four_bonacci_rec(n-2)+four_bonacci_rec(n-3)+four_bonacci_rec(n-4)
#replace this with your implementation

#########################################
# Question 1.b - do not delete this comment
#########################################
def four_bonacci_mem(n, memo=None):
    if n<4:
        return n
    if memo==None:
        memo={}
    if n not in memo:
        memo[n]=four_bonacci_mem(n-1,memo)+four_bonacci_mem(n-2,memo)+four_bonacci_mem(n-3,memo)+four_bonacci_mem(n-4,memo)
    return memo[n]#replace this with your implementation


#########################################
# Question 2 - do not delete this comment
#########################################
def climb_combinations_memo(n, memo=None):
    def stairs_fibo(k,memi=None):
        if k<2:
            return k
        if memi==None:
            memi={}
        if k not in memi:
            memi[k]=stairs_fibo(k-1,memi)+stairs_fibo(k-2,memi)
        return memi[k]
    if n<=3:
        return n
    if memo==None:
        memo={}
    if n not in memo:
        memo[n]=stairs_fibo(n+1)
    return memo[n]

#########################################
# Question 3 - do not delete this comment
#########################################
def catalan_rec(n,memo=None):
    if n<=1:
        return 1
    if memo==None:
        memo={}
    a=0
    if n not in memo:
        for k in range(n):
            a+=catalan_rec(k,memo)*catalan_rec(n-1-k,memo)
            memo[n]=a
    return memo[n] #replace this with your implementation
    

#########################################
# Question 4.a - do not delete this comment
#########################################
def find_num_changes_rec(n, lst):
    lst=sorted(lst)
    if lst[0]==0:
        lst.remove(0)
    def combos(n, lst):
        if n==0:
            return 1
        if lst==[]:
            return 0
        if n<0:
            return 0
        return combos(n-lst[0],lst)+combos(n,lst[1:])
    return combos(n,lst) #replace this with your implementation
    

#########################################
# Question 4.b - do not delete this comment
#########################################
def find_num_changes_mem(n, lst, memo=None):
    lst=sorted(lst)
    if lst[0]==0:
        lst.remove(0)
    def combos(n, lst, memo=None):
        if n==0:
            return 1
        if lst==[]:
            return 0
        if n<0:
            return 0
        if memo==None:
            memo={}
        k=(n, len(lst))
        if k not in memo:
            memo[k]=combos(n-lst[0],lst,memo)+combos(n,lst[1:],memo)
        return memo[k]
    return combos(n,lst) #replace this with your implementation


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################

#Question 1.a tests - you can and should add more    
print(four_bonacci_rec(0) == 0)
print(four_bonacci_rec(5) == 12)
print(four_bonacci_rec(8) == 85)

#Question 1.b tests - you can and should add more    
print(four_bonacci_mem(0) == 0)
print(four_bonacci_mem(5) == 12)
print(four_bonacci_mem(8) == 85)

#Question 2 tests - you can and should add more    
print(climb_combinations_memo(4) == 5)
print(climb_combinations_memo(42) == 433494437)

#Question 3 tests - you can and should add more    
cat_list = [1,1,2,5,14,42,132,429]
for n,res in enumerate(cat_list):
    print(catalan_rec(n) == res)

#Question 4.a tests - you can and should add more        
print(find_num_changes_rec(5,[1,2,5,6]) == 4)
print(find_num_changes_rec(4,[1,2,5,6]) == 3)
print(find_num_changes_rec(0.9,[1,2,5,6]) == 0)

#Question 4.b tests - you can and should add more        
print(find_num_changes_mem(5,[1,2,5,6]) == 4)
print(find_num_changes_mem(4,[1,2,5,6]) == 3)
print(find_num_changes_mem(0.9,[1,2,5,6]) == 0)

# ============================== END OF FILE =================================
