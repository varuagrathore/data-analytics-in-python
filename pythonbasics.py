#this library is used for structured data  operations like import.csv files
#create dataframe and data preparation
import pandas as pd
d={'col1':[1,2,3,4,5],'col2':[6,7,8,9,10],'col3':[11,12,13,14,15]}
dataframe =pd.DataFrame(data=d)     #pd is ued to let python  know we want to activate dataframe from pandas library and when you see the output,
# print(dataframe)                    #you see 0 1 2 3 4 so in python counting start from zero zero point to the first row 
count_rows=dataframe.shape[0]                                 #in contrast when you want to print number of rows you can write 
print(count_rows)            #this print number of rows which is 5 in output 
count_column=dataframe.shape[1] #in contrast when you want to print number of columns you can write this 
print(count_column) #this print number of columns
print(dataframe.shape)   #this print number of columns and rows together (rows, columns)
