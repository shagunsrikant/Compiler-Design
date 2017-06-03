symbol_table = {}
def create_table(a,t):
    symbol_table[a] = t

def creating(tablename):
    print("CREATE TABLE "+tablename)
    print("(")
    for i in symbol_table.keys():
        print(i,symbol_table[i] + ",")
    print(")")
