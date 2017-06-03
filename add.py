import update, creat, select, help, tables,cross
def main():
    stat1= input("Enter the statement")
    stat= stat1.upper()
    words=[]
    word = []
    attr = []
    flag=0
    word=stat.split(" ")
    for w in word:
        words.append(w.strip(','))
    for i in range(len(words)):
        if words[i]=="FROM":
            tablename=words[i+1]

        elif words[i]=="TABLE":
            tablename=words[i+1]


    if "CREATE" in words:
        attr_list = []
        for i in range(len(words)):
            if words[i] == "OF":
                att = words[i-1]
                i += 1
                attr_list.append(att)
                if words[i] == "TYPE":
                    type_att = words[i + 1]
                creat.create_table(att,type_att)
                i += 1
        if tables.finderror(tablename,attr)==2:
            creat.creating(tablename)
            tables.appe(tablename,attr_list)
        return 0

    for i in range(len(words)):
        if words[i] == "HELP":
            w = words[i+1]
            help.helpcom(w)
            return 0

    if "SET" in words or "ADD" in words:
        a_name = []
        if tables.finderror(tablename, attr) == 2:
            print("Table not found")
            return 0
        else:
            for i in range(len(words)):
                if words[i] == "SET":
                    a_name.append(words[i+1])
                    i += 3
                    a_value = words[i]
                    #print(tablename,a_name)
                    if tables.finderror(tablename,a_name) == 0:
                        print("Attribute not found")
                        return 0
                    else:
                        update.edit_update(tablename,a_name,a_value)
                if words[i] == "ADD":
                    a_name.append(words[i+1])
                    if tables.finderror(tablename,a_name) == 1:
                        print("Attribute already exists")
                        return 0
                    else:
                        update.edit_alter(tablename,a_name)
                return 0
    if 'AND' in words:
        x=cross.crossproduct(words)
        return 0

    if "DROP" in words or "DELETE" in words and "FROM" not in words:
        s = tables.finderror(tablename, attr)
        if (s==2):
            print("Table not found")
        elif ((s==0) and ("DROP" not in words)):
            print("Attributes not found in table" + tablename)
        else:
            tables.drop(tablename)
        return 0

    for i in range(len(words)):
        if words[i]=="GET" or words[i]=="SELECT" or words[i]=="RETRIEVE":
            while(words[i+1]!="FROM"):
                attr.append(words[i+1])
                i+=1
            flag=1
        elif words[i]=="REMOVE" or words[i]=="DELETE":
            while (words[i + 1] != "FROM"):
                attr.append(words[i + 1])
                i += 1
            flag=2
    if "ALL" in words or "EVERY" in words:
        attr=["*"]

    s=tables.finderror(tablename,attr)

    if s==2:
        print("Table not found")
    elif s==0:
        print("Attributes not found")
    else:
        if flag==1:
            select.sel(attr, tablename)
        if flag==2:
            select.dele(attr, tablename)

t = main()
