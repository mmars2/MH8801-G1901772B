import json

#serialize
def serialize(ls):
    if type(ls) == list:
        res ='list|'
        for i in ls:
            res = res + str(i)
            res = res + '|'
            res = res + str(type(i))
            res = res + '|'
        return res[:-1]
    elif type(ls) == dict:
        res = 'dict|'
        for x,y in ls.items():
            res = res + str(x)
            res = res + '|'
            res = res + str(type(x))
            res = res + '|'
            res = res + str(y)
            res = res + '|'
            res = res + str(type(y))
            res = res + '|'
        return res
    
#deserialize    
def deserialize(string):
    m=string.split('|')
    if m[0]=='list':
        ls=[]
        for i in range(1,len(m)-1,2):
            if 'float' in m[i+1]:
                ls.append(float(m[i]))
            elif 'int' in m[i+1]:
                ls.append(int(m[i]))
            else:
                ls.append(m[i])
        return ls
    else:
        dictionary={}
        for i in range(1,len(m)-1,4):
            if 'float' in m[i+1]:
                y=float(m[i])
            elif 'int' in m[i+1]:
                y=int(m[i])
            else:
                y=m[i]
            if 'float' in m[i+3]:
                j=float(m[i+2])
            elif 'int' in m[i+3]:
                j=int(m[i+2])
            else:
                j=m[i+2]
            dictionary[y]=j
        return dictionary

#compare datastructures      
def compare(ls1, ls2):
    if type(ls1) != type(ls2):
        print('Unsuccessful')
    else:
        if type(ls1) == type([]):
            if ls1 == ls2:
                print('Success!')
            else:
                print('Unsuccessful')
        if type(ls1) == type({}):
            if len(ls1) != len(ls2):
                print('Unsuccessful')
            for key in ls1:
                if key not in ls2:
                    print('Unsuccessful')
                if ls1[key] != ls2[key]:
                    print('Unsuccessful')
            print('Success!')

#ask user for file
file=input('Please type one of the following files: H1-1, H1-2, H1-3, H1-4, H1-5')
filename=file+'.json'
with open(filename,'r') as fh: 
    inputdata=json.load(fh)
fh.close()
serialized=serialize(inputdata)

#ask user for filename to store
file=input('Please type a filename:')
filename=file+'.json'
with open(filename,'w') as x:
    json.dump(serialized,x)
x.close()
with open(filename,'r') as y:
    serialz=json.load(y)
serialz=deserialize(serialz)

#compare datastructures
compare(inputdata, serialz)


