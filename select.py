def sel(attribute, tablename):
    print("SELECT "+ ','.join(attribute)+" FROM "+tablename)

def dele(attribute, tablename):
    print("DELETE "+','.join(attribute)+" FROM "+tablename)
