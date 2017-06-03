def helpcom(w):
    if (w=="SELECT"):
        print("SELECT [ATTRIBUTE_LIST] FROM [TABLE_NAME]")
        print("With SELECT, you can also use:")
        print("SELECT * FROM [TABLE_NAME] when you have to select every record from the given table")
        print("Also, there can be WHERE, GROUP BY clauses with SELECT to make the selection more particular like,")
        print("SELECT [ATTRIBUTE_LIST] FROM [TABLE_NAME] WHERE [CONDITION]")
    if (w=="TABLES"):
        print("With TABLES, you can use:")
        print("1. DROP [TABLE_NAME] ")
        print("2. DELETE [ATTRIBUTE_LIST] FROM [TABLE_NAME]")
        print("3. SELECT [ATTRIBUTE_LIST] FROM [TABLE_NAME] ")
        print("4. SELECT * FROM [TABLE_NAME] ")
        print("5. CREATE [TABLE_NAME] ([ATTRIBUTE_NAME] [ATTRIBUTE_TYPE])")
        print("6. UPDATE [TABLE_NAME] SET [COLUMN1 = VALUE1, COLUMN2 = VALUE2...] WHERE [CONDITION]")
        print("7. ALTER TABLE [TABLE_NAME] ADD [COLUMN_NAME DATATYPE")
    if (w=="UPDATE"):
        print("6. UPDATE [TABLE_NAME] SET [COLUMN1 = VALUE1, COLUMN2 = VALUE2...] WHERE [CONDITION]")
    if (w=="ALTER"):
        print("7. ALTER TABLE [TABLE_NAME] ADD [COLUMN_NAME DATATYPE")
    if (w=="DROP"):
        print("1. DROP [TABLE_NAME] ")
    if (w=="DELETE"):
        print("2. DELETE [ATTRIBUTE_LIST] FROM [TABLE_NAME]")
