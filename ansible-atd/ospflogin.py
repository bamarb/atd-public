#!/usr/bin/python
import os
import sys
import signal
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning

def check_for_first_login():
    '''simply need to login once to get around Folsom bugs'''
    CHECK_FILE = '/home/arista/.CVP_LOGIN_SUCCESS'

    if not os.path.isfile(CHECK_FILE):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r = requests.post('https://192.168.0.5/cvpservice/login/authenticate.do',json={"userId": "cvpadmin","password": "arista"}, verify=False)
        if r.status_code == 200:
            open(CHECK_FILE, 'a').close()

if sys.stdout.isatty():

  def signal_handler(signal, frame):
    print("\n")
    quit()

  signal.signal(signal.SIGINT, signal_handler)


  ans=True
  while ans:
    check_for_first_login()
    print ("""
Lab jump host for Arista virtual lab

Screen Instructions:

   * Select specific screen - Ctrl + a <number>
   * Select previous screen - Ctrl + a p
   * Select next screen - Ctrl + a n
   * Exit all screens (return to menu) - Ctrl + a \\

Device Menu:            Lab Controls

   1. EOS1               13. Reset All Devices to Base (reset)
   2. EOS2
   3. EOS3               
   4. EOS4               
   5. EOS5               
   6. EOS6               
   7. EOS7               
   8. EOS8               
   10. Screen (screen) - Opens a screen session to each of the hosts
   11. Shell (bash)
   12. Exit/Quit (exit)
    """)
    ans=raw_input("What would you like to do? ")
    if ans=="1" or ans=="EOS1":
      os.system('ssh 192.168.0.10')
    elif ans=="2" or ans=="EOS2":
      os.system('ssh 192.168.0.11')
    elif ans=="3" or ans=="EOS3":
      os.system('ssh 192.168.0.16')
    elif ans=="4" or ans=="EOS4":
      os.system('ssh 192.168.0.17')
    elif ans=="5" or ans=="EOS5":
      os.system('ssh 192.168.0.32')
    elif ans=="6" or ans=="EOS6":
      os.system('ssh 192.168.0.14')
    elif ans=="7" or ans=="EOS7":
      os.system('ssh 192.168.0.15')
    elif ans=="8" or ans=="EOS8":
      os.system('ssh 192.168.0.31')
    elif ans=="9" or ans=="cvx":
      os.system('ssh 192.168.0.44')
    elif ans=="10" or ans=="screen":
      os.system('/usr/bin/screen')
    elif ans=="11" or ans=="bash":
      os.system('/bin/bash')
    elif ans=="12":
      quit()
    elif ans=="13" or ans=="reset":
      os.system("ssh 192.168.0.5 './ConfigureTopology.py'")
    elif ans=="14" or ans=="mlag":
      os.system("ssh 192.168.0.5 './ConfigureTopology.py -t mlag -e leaf4' >> /tmp/ConfigureTopology.log")
    elif ans=="15" or ans=="bgp":
      os.system("ssh 192.168.0.5 './ConfigureTopology.py -t bgp' >> /tmp/ConfigureTopology.log")
    elif ans=="16" or ans=="vxlan":
      os.system("ssh 192.168.0.5 './ConfigureTopology.py -t vxlan' >> /tmp/ConfigureTopology.log")
    elif ans=="17" or ans=="l2evpn":
      os.system("ssh 192.168.0.5 './ConfigureTopology.py -t l2evpn -e leaf3' >> /tmp/ConfigureTopology.log")
    elif ans=="18" or ans=="l3evpn":
      os.system("ssh 192.168.0.5 './ConfigureTopology.py -t l3evpn -e leaf3' >> /tmp/ConfigureTopology.log")
    elif ans=="19" or ans=="cvp":
      os.system("ssh 192.168.0.5 './ConfigureTopology.py -t cvp' >> /tmp/ConfigureTopology.log")
    elif ans=="exit":
      quit()
    elif ans !="":
      print("\n Not Valid Choice Try again")
else:
  os.system("/usr/lib/openssh/sftp-server")