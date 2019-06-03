
import requests
from bs4 import BeautifulSoup
import urllib
import logging
 
url='https://www.opensecrets.org/lobby/firmagns.php?'
outputFile = open('C:\\Users\\DELL\\Downloads\\resultsFOREIGN_agencies`.csv','w')
 
def FirmID():
 
    lobby_csv = open('C:\\Users\\DELL\\Documents\\book1.csv','r') # input
 
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
            param = {'id': cmpid, 'year':i}
            encodedParam = urllib.parse.urlencode(param)
            urlWithParam = str(url + encodedParam)
            page = requests.get(urlWithParam)
            soup = BeautifulSoup(page.content, 'html.parser')
            length =len(soup.find_all('td'))
            firmName= soup.find('h1').get_text()
 
            if firmName.find(",") != -1:
                firmName = '"' + firmName + '"'
 
            if length == 0:
                continue
 
            else:
                for count in range(0,length,2):
                    agency= soup.find_all('td')[count].get_text()
                    if agency.find(",") != -1:
                        agency = '"' + agency + '"'
 
                    count= soup.find_all('td')[count+1].get_text()
 
                    s= firmName + "," + str(i) + "," + cmpid + "," + agency + "," +count                
                    print (s)
                    outputFile.write (s + "\n")
        except:
            logging.exception('') 
            continue
 
FirmID()

