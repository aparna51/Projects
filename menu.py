x=int(input("enter 1 to view time \n 2 to reboot os \n 3 to create new user \n 4 to search on google \n 5 to print urls of 1st page of google \n 6 to chek ram and cpu info \n 7 to login to facebook and update status \n 8 to scan all ips"))
import datetime
import os
import webbrowser
import psutil
import google
#import scanip.scanip

if(x==1):
    print(datetime.datetime.now())
if(x==2):
    os.system('reboot')
if(x==3):
    u=input("enter user name")
    p=input("enter password")
    os.system('sudo -i useradd'+u)

if(x==4):
    y=raw_input("enter search")
    webbrowser.open_new_tab('https://www.google.com/search?q='+y)
if(x==5):
    print("")
if(x==6):
    print(psutil.virtual_memory())
if(x==7):
    from googlesearch import search
    z=input("enter your search")
    for i in search(z, tld="co.in",num=10,stop=1,pause=2):
        print(i)
if(x==8):
    print("scanning all ips")
    scanip.scanip.start_scan()
