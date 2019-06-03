import requests
from bs4 import BeautifulSoup
import urllib

url='https://www.opensecrets.org/lobby/firmsum.php?'
findata = open(r'C:\Users\DELL\Downloads\resultsFOREIGN_financial.csv', 'w')
findata2 = open(r'C:\Users\DELL\Downloads\resultsFOREIGN_financial2', 'w')
def FirmID():
    lobby_csv = open(r'C:\Users\DELL\Documents\book1.csv', 'r') # input
    for each_line in lobby_csv:
        lobbyfirm_id = each_line.strip()
        if lobbyfirm_id[0]== 'C'or lobbyfirm_id[0]=='N':
            continue
        else:
            data(lobbyfirm_id)
        
        
def data(cid):
    
    cmpid= str(cid)
    y= [2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000,1999,1998]    
    
    for i in y:
        try:
            param = {'id': cmpid, 'year':i} # assigning values
            encodedParam = urllib.parse.urlencode(param) #parsing parameters
            urlWithParam = str(url + encodedParam)        # combining url with parameters
            page = requests.get(urlWithParam)       # generating HTML page using get requests
            soup = BeautifulSoup(page.content, 'html.parser') #parsing using beautiful soup
            lst= soup.find_all('strong')[1].get_text()      # finding all relevant Strong Tags  
            lst2=lst.replace(',','')                # removing commas so as to avoid entries going to next cell in excel
            lst1= soup.find('h1').get_text()    # deriving company name 
            lst3 =lst2.replace('Total Lobbying Income: ','') # removing useless tag information
           # income=str(lst[1])
            lst12=lst1.replace(',','')  
            #cmpname=str(lst1)
            s= cmpid +"%"+ str(i)+"%"+lst3+"%"+lst12        # combining all the information
            print(s)
            if lst3[0]== 'F':
                findata2.write(s+"\n")
            else:
                findata.write(s+"\n")
            
        except:
            continue

FirmID()
findata.close()
