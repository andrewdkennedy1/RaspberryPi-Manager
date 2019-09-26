# RasberryPi Manager
 Flask webapp for sending commands to many rasberry pis at once via ssh. 

Python 3.7 recommended 

Clone or download then inside that directory 

`pip install -r requirements.txt` 

Modify credentials in reboot.py and refresh.py 

update pis.txt with a target pi per line 

`apt-get install xdotool` on all pis for the fresh functionality to work 

run main.py and goto the localhost:8081 #or whatever port you set in main.py 
