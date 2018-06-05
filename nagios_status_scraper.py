!#/usr/bin/env python3
import requests
import re
from bs4 import BeautifulSoup

get_disabled_notifications = True
include_NOTOK = False

OK_statuses = ['statusEven', 'statusOdd']
NOTOK_statuses = ['statusBGCRITICAL', 'statusBGWARNING', 'statusBGUNKNOWN']
if include_NOTOK:
    status = OK_statuses + NOTOK_statuses
else:
    status = OK_statuses
    
session = requests.Session()
session.auth = (username, password)
url = 'http://nagios/nagios/cgi-bin/status.cgi?navbarsearch=1&host=*-ep0*db0*-vip&servicefilter=ping'
auth = session.post('http://nagios/nagios')
response = session.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table_data = soup.find_all("td",{'class': status})
for result in table_data:
    if len(result.find_all('a'))==3:
        tag = str(result.select_one("a[href*=service]")).replace('%3A',":")
        if(get_disabled_notifications==True):
            match = re.search('\S+host=(.*)&amp;service=(.*)">.*ndisabled(.*)" ', tag)
        else:
            match = re.search('\S+host=(.*)&amp;service=(.*)">', tag)
        try:
            if match:
                service_name = str(match.group(2)).replace("#comments","")
                print("ng_enable_notification -H {} -s {} -a uname -c case".format(match.group(1), service_name))
        except:
            pass
