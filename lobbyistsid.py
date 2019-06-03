# -*- coding: utf-8 -*-
"""
Created on Fri May 17 22:47:45 2019

@author: DELL
"""

import requests
from bs4 import BeautifulSoup
import urllib

url='https://www.opensecrets.org/search?q='

url2='&type=indiv'
findata = open(r'C:\Users\DELL\Downloads\lobbyid.csv', 'w')
findata2 = open(r'C:\Users\DELL\Downloads\revid.csv', 'w')
def FirmID():
    lobby_csv = open(r'C:\Users\DELL\Documents\book2.csv', 'r') # input
    for each_line in lobby_csv:
        #try:
        lobbyfirm_id = each_line.strip()
        lobby=lobbyfirm_id.replace(' ','+')
        data(lobby)
        #except:
            #continue
        
        
        
def data(cid):
        urlWithParam = str(url + cid + url2)
        page = requests.get(urlWithParam)
        soup = BeautifulSoup(page.content, 'html.parser')
        main1= soup.find('tr', {'id': 'revolving-door'})
        
        main2=soup.find('tr', {'id': 'lobbyist'})
        
        if main1 is not None:
            rev= main1.find_all('td')
            s= str(cid.replace('+',' ')) +"%"+str(rev[1])
            s.replace(',',' ')
            findata.write(str(s) + "\n")
            print (str(s))
        if main2 is not None:
            lob= main2.find_all('td')
            s2= str(cid.replace('+',' ')) +"%"+str(lob[1])
            s2.replace(',',' ')
            findata2.write(str(s2) + "\n")
            print (str(s2))
            
            

    
    
FirmID()
findata.close()
findata2.close()