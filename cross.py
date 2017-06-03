import tables
def crossproduct(words):
    attr=[]
    for i in range(len(words)):
        if words[i]=='FROM':
            table1=words[i+1]
        if words[i]=='AND':
            table2=words[i+1]
        if words[i]=="GET" or words[i]=="SELECT" or words[i]=="RETRIEVE":
            while(words[i+1]!="FROM"):
                attr.append(words[i+1])
                i+=1
    if (tables.finderror(table1,attr))==2:
        print(table1+' NOT FOUND')
        return 0
    if (tables.finderror(table2,attr))==2:
        print(table2+' NOT FOUND')
        return 0
    if tables.finderror(table1, attr) == 0:
        print("Attribute not found in "+table1)
    elif tables.finderror(table2, attr) == 0:
        print("Attribute not found in "+table2)
    else:
        print("SELECT "+','.join(attr)+" FROM "+table1+' JOIN '+table2)
    return 0
