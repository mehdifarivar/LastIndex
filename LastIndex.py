import requests
import xlwings
import pandas as pd

isin_file = pd.read_excel('ISINs.xlsx')
isin_list = isin_file['isin'].values.tolist()
print (isin_list)
print (isin_list[3])




#wb =xlwings.Book("ISINs.xlsx")
#sheet=wb.sheets("Sheet1")
#for i in range(2,5):
#    response = requests.get("http://mdapi.tadbirrlc.com/API/symbol?$filter=SymbolISIN+eq+%27" + sheet.range(i, 1).value + "%27")
#    print(sheet.range(2,1).value)
#    print (response.text)
#sheet.range(r1,3).value="SALAM"

#print(sheet.range(2,1).value)



#isin ="IRO1NAFT0001"
#response = requests.get("http://mdapi.tadbirrlc.com/API/symbol?$filter=SymbolISIN+eq+%27" + isin + "%27")
#data = response.text
#$parsed = json.loads(data)
#x = parsed['List'][0]
#print (data)
