import requests
from bs4 import BeautifulSoup
import urllib

url='https://www.opensecrets.org/lobby/lobbyist.php?'
findata = open(r'C:\Users\DELL\Documents\lobbying\New project\S&P\S&P_summary.csv', 'a')

def FirmID():
    lobby_csv = open(r'C:\Users\DELL\Documents\lobbying\New project\S&P\Lob.csv', 'r') # input
    for each_line in lobby_csv:

        lobbyfirm_id = each_line.strip()


        data(lobbyfirm_id)
        '''except:
            print ("Sorry, no records found in 2016")
            continue'''


        
def data(cid):
    
    cmpid= str(cid)
    y= [2018,2017,2016,2015,2014,2013,2012,2011]    
    
    for i in y:
        #try:
        param = {'id': cmpid, 'year':i}
        encodedParam = urllib.parse.urlencode(param)
        urlWithParam = str(url + encodedParam)
        page = requests.get(urlWithParam)
        soup = BeautifulSoup(page.content, 'html.parser')
        length =len(soup.find_all('td'))
        lst4= soup.find('h1').get_text()
        if length == 0:
            continue
        else:
            for count in range(0,length,2):
                lst= soup.find_all('td')[count].get_text()
                s= lst4+"%"+str(i)+ "%" +cmpid+"%"+lst 
                s1=s.replace(',','')
                print (s1)
                findata.write (s1)
                    
                    #parent = soup.find('table', {'class': 'datadisplay'})
                main1= soup.find_all('td')
                children = main1[count+1].findChildren('a',recursive= True)
                print(children)
'''                 for child in children:
                        print(child.get_text()+"%")
                        lst10="%"+child.get_text()
                        lst1=lst10.replace(',','')
                        print (lst1)
                        findata.write (lst1)
                    findata.write ("\n")
                    
                   

        except:
            print ("Sorry, no records found in 2016")
            continue
    


findata.close()
    
'''
FirmID()