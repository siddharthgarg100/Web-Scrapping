import requests
from bs4 import BeautifulSoup
import urllib

url='https://www.opensecrets.org/lobby/lobbyist_issues.php?'
findata = open(r'C:\Users\DELL\Documents\lobbying\New project\S&P\S&P_issue.csv', 'a')

def FirmID():
    lobby_csv = open(r'C:\Users\DELL\Documents\lobbying\New project\S&P\Lob.csv', 'r') # input
    for each_line in lobby_csv:
        try:
            lobbyfirm_id = each_line.strip()


            data(lobbyfirm_id)
        except:
            print ("Sorry, no records found in 2016")
            continue

        
def data(cid):
    
    cmpid= str(cid)
    y= [2018,2017,2016,2015,2014,2013,2012,2011]    
    
    for i in y:
        try:
            param = {'id': cmpid, 'year':i}
            encodedParam = urllib.parse.urlencode(param)
            urlWithParam = str(url + encodedParam)
            page = requests.get(urlWithParam)
            soup = BeautifulSoup(page.content, 'html.parser')
            length =len(soup.find_all('td'))
            if length == 0:
                continue
            else:
                for count in range(0,length,3):
                    lst= soup.find_all('td')[count].get_text()
                    lst1= soup.find_all('td')[count+1].get_text()
                    lst2= soup.find_all('td')[count+2].get_text()
                    lst4= soup.find('h1').get_text()
                    s= lst+'\t'+"%" +lst1+'\t'+"%"+lst2
                    final= lst4 + "%" + cmpid + "%"  +s +"%"+str(i)
                    final1= final.replace(',','')
                    print (final1)
                    findata.write (final1 + "\n")

        except:
            print ("Sorry, no records found in 2016")
            continue
    


        
FirmID()
findata.close()
   
