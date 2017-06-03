import tables
def edit_update(tablename,attr_name,attr_value):
    print("UPDATE "+tablename)
    print("(SET "+','.join(attr_name)+" = "+attr_value+")")
def edit_alter(tablename,attr_name):
    print("ALTER TABLE "+tablename+" ADD "+','.join(attr_name))
    tables.listoftables[tablename].append(attr_name)
