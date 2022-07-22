''' Exercise #4. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def second_most_popular_character(my_string):
    dic={}
    d=1
    last=[]
    my_list=sorted(list(my_string))
    for indx in range(len(my_list)):
        if my_list[indx] not in dic.keys():
            d=1
            dic[my_list[indx]]=d
        else:
            dic[my_list[indx]]=d+1
            d=d+1
    keys=dic.keys()
    value_sort=sorted(keys, key=dic.get, reverse=True)
    for indx in range(len(value_sort)):
        if dic[value_sort[0]]>dic[value_sort[indx]]:
            last.append(value_sort[indx])
    if dic[value_sort[0]]==dic[value_sort[-1]]:
            last=[]
            last.append(value_sort[0])
    return last[0]# remove this


#########################################
# Question 2 - do not delete this comment
#########################################
def diff_sparse_matrices(lst):
    dic={}
    k=0
    for r in range(len(lst)):
        k=k+1
        if r==0:
            for a in lst[r]:
                if a not in dic:
                    dic[a]=lst[r][a]
                dic_keys=dic.keys()
        else:
            for a in lst[r]:
                if a not in dic:
                    dic[a]=lst[r][a]*-1
                dic_keys=dic.keys()
        for key in dic_keys:
            if k==len(lst):
                break
            elif key in lst[k]:
                dic[key]=dic[key]-lst[k][key]
    sorted_zero=[]
    for t in dic.keys():
        if dic[t]==0:
            sorted_zero.append(t)
    for i in sorted_zero:
        dic.pop(i)
    return dic # remove this


#########################################
# Question 3 - do not delete this comment
#########################################
def find_substring_locations(s, k):
    base=list(s)
    dic={}
    t=0
    if k!=1:
        for i in range(len(base)):
            if i==len(base)-k:
                break
            else:
                for e in range(k-1):
                    base[i]=base[i]+base[i+e+1]
        while t<k:
            base.pop()[-1]
            t=t+1
    base2= list(s)
    base.append(base[-1][1:]+base2[-1])
    for indx in range(len(base)):
        if base[indx] not in dic:
            dic[base[indx]]=[indx]
        else:
            dic[base[indx]].append(indx)
    return dic  # remove this

#########################################
# Question 4 - do not delete this comment
#########################################
def count_lines(in_file, out_file):
    with open(in_file, 'r') as f:
        i=0
        for line in f:
            i+=1
    with open(out_file, 'w') as g:
        g.write(str(i))
    pass #replace this with your implementation

#########################################
# Question 5 - do not delete this comment
#########################################
def simple_sent_analysis(in_file):
    try:
        dic={'happy':0, 'sad':0}
        newords=[]
        newerwords=[]
        temp=[]
        last=[]
        l=[".", "$", "%", ";", "-", ",", "?", "!"]
        k=0
        with open(in_file, 'r') as f:
            words = list(f.read().split())
            for item in words:
                newords.append(item.lower())
            for item in newords:
                for i in range(len(item)):
                    for char in l:
                       if item[-1] is char:
                          item=item[:-1]
                       if item[0] is char:
                          item=item[1:]
                newerwords.append(item)
            for char in newerwords:
                if char == 'happy':
                    dic['happy']+=1
                elif char == 'sad':
                    dic['sad']+=1
                elif 'happy' in char:
                    temp.append(char)
                elif 'sad' in char:
                    temp.append(char)
            for p in temp:
                for char in l:
                    if char in p:
                        last=p.split(char)
                        for t in last:
                            if t == 'happy':
                                dic['happy']+=1
                            elif t == 'sad':
                                dic['sad']+=1
        return dic
    except IOError:
        dic={}
        print("Cannot encode " + in_file + " due to IO error")
        return dic
#replace this with your implementation


#########################################
# Question 6 - do not delete this comment
#########################################
def calc_profit_per_group(in_file):
        dic={'happy':'NA', 'sad':'NA', 'neutral':'NA'}
        ident=dic.keys()
        fix_csv=[]
        happies=[]
        neutrals=[]
        sads=[]
        averageH=0
        averageN=0
        averageS=0
        dupli_check=[]
        try:
            with open(in_file, 'r') as f:
                lines_list=f.readlines() 
                for line in lines_list:
                    fix_csv.append(line.rstrip('\n').split(','))
                for i in range(len(fix_csv)):
                    if len(fix_csv[i])!=3:
                        raise ValueError('Invalid input')
                    if float(fix_csv[i][1]) is ValueError:
                        raise ValueError('Invalid input')
                    if fix_csv[i][2] not in ident:
                        raise ValueError('Invalid input')
                    if fix_csv[i][2] == 'happy':
                        happies.append(fix_csv[i])
                    if fix_csv[i][2] == 'neutral':
                        neutrals.append(fix_csv[i])
                    if fix_csv[i][2] == 'sad':
                        sads.append(fix_csv[i])
                for i in range(len(fix_csv)):
                    if fix_csv[i][0] not in dupli_check:
                        dupli_check.append(fix_csv[i][0])
                    else:
                        raise ValueError('The series '+fix_csv[i][0]+' appears more than once')
                for i in range(len(happies)):
                    averageH+=float(happies[i][1])
                try:
                    averageH=averageH/len(happies)
                    dic['happy']=averageH
                except ZeroDivisionError:
                    dic['happy']='NA'
                for i in range(len(neutrals)):
                    averageN+=float(neutrals[i][1])
                try:
                    averageN=averageN/len(neutrals)
                    dic['neutral']= averageN
                except ZeroDivisionError:
                    dic['neutral']='NA'
                for i in range(len(sads)):
                    averageS+=float(sads[i][1])
                try:
                    averageS=averageS/len(sads)
                    dic['sad']= averageS
                except ZeroDivisionError:
                    dic['sad']='NA'
                return dic
        except IOError:
            return print("Cannot use " + in_file + " due to IO error") #replace this with your implementation

#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################

# ============================== END OF FILE =================================
