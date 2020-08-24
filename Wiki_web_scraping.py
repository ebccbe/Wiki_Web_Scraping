from opencage.geocoder import OpenCageGeocode
import pandas as pd
import xlsxwriter
from datetime import *
import sys

#Wikipedia Web Link
URL = input("Enter the Wikipedia Link:")
print(URL)

#Need to add URL validation logic

#Table Count
data = pd.read_html(URL)
ltable = int (len(data))
print("Table available in this page: ",ltable)


#Table Info - Need to add more validations
while True:
    tableno = input("Which Table do you wish to view ? ")
    tablen = int(tableno)
    l1table = tablen - 1

    try:
        tablen<=ltable
    except IndexError:
            print("Enter number less than or equal to %s", ltable)
    if tablen>0 and tablen<=ltable:
        stable = data[l1table]
        print(stable)
        #Save Table - Note needs to add some validation
        q2 = input("Do you want to save this table to excel? Enter y/n :")
        if q2 == "y":
            now = datetime.now()
            filename = "tabledata_"+(datetime.now().strftime("%Y-%m-%d_%H_%M_%S"))+".xlsx"
            stable.to_excel(filename)
            print("File has been saved")
        else:
            print("File not saved")
    else:
            print("Try again")
            exit



