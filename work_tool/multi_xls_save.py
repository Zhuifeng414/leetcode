import pandas as pd

df1 = pd.DataFrame({'a':[3,2],'b':[4,5]})

with pd.ExcelWriter('test.xlsx') as writer:

    str1 = ['a','b','c']
    for i in str1:
        name = str(i)
        df1.to_excel(writer, sheet_name= name)
    writer.save()
writer.close()