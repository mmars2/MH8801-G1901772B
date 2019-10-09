#Program C1
m_list=[9,41,12,3,74,15]
min_value=None
for i in m_list:
    if min_value==None:
        min_value=i
        continue
    if i<min_value:
        min_value=i
        
print('The list containing',m_list,'has:')
print('Minimum value:',min_value)

#Program C2  
def mymin(ls):
    min_value=None
    for i in ls:
        if min_value==None:
            min_value=i
            continue
        if i<min_value:
            min_value=i
    return min_value

def mymax(ls):
    max_value=None
    for i in ls:
        if max_value==None:
            max_value=i
            continue
        if i>max_value:
            max_value=i
    return max_value

def myaverage(ls):
    count=0
    sum=0
    for i in ls:
        count=count+1
        sum=sum+i
    average=sum/count
    return average

def mymedian(ls):
    ls.sort()
    if len(ls)%2==0:
        i=int(len(ls)/2)
        median_value=(ls[i-1]+ls[i])/2
    else:
        i=(len(ls)+1)/2
        median_value=ls[i]
    return median_value

def myrange(ls):
    range_value=max(ls)-min(ls)
    return range_value

print('The list containing',m_list, 'has:')
print('Minimum value:',mymin(m_list))
print('Maximum value:',mymax(m_list))
print('Average value:',myaverage(m_list))
print('Median value:',mymedian(m_list))
print('Range value:',myrange(m_list))

#Program C3
def getFileLines(fname):
    fhandle=open(fname)
    lines=[]
    for line in fhandle:
        line=line.rstrip()
        if line:
            lines.append(line)
    fhandle.close()
    return lines

the_list=getFileLines('MH8811-04-Data.csv')
the_list=list(map(float,the_list))

print('Minimum value:',mymin(the_list))
print('Maximum value:',mymax(the_list))
print('Average value:',myaverage(the_list))
print('Median value:',mymedian(the_list))
print('Range value:',myrange(the_list))

#Program H1
def sample_variance(ls):
    sum_total=0
    mean=myaverage(ls)
    for i in ls:
        sum_total+=(i-mean)**2
        variance=sum_total/(len(ls)-1)
    return variance

print('Sample Variance:',sample_variance(the_list))