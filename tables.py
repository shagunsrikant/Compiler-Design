listoftables={"STUDENT":["NAME","USN","AGE","GRADE","*"], "EMPLOYEE":["NAME","AGE","EMPID","SALARY","*"],
                  "BOOKS":["TITLE","AUTHOR","PRICE","*"],"MOVIES":["NAME","YEAR","DIRECTOR","*"],
                  "TRAINS":["NAME","TRAINID","NUM_STATIONS","SOURCE","DESTINATION","*"]}
def finderror(tablename,attributes):
    if tablename in listoftables:
        for i in range(len(attributes)):
            if attributes[i] not in listoftables[tablename]:
                return 0
        return 1
    else:
        return 2

def appe(tablename,list_attr):
    list_attr.append("*")
    listoftables[tablename]=list_attr


def drop(tablename):
    print("DROP TABLE " + tablename)
    del listoftables[tablename]
    print(listoftables)
