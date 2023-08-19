pip install requests
import requests
req = requests.get
req.encoding      # returns 'utf-8' 
req.status_code   # returns 200 
req.elapsed       # returns datetime.timedelta(0, 1, 666890) 
req.url           # returns 'https://tutsplus.com/' 
req.history      
# returns [<Response [301]>, <Response [301]>] 
req.headers['Content-Type']
# returns 'text/html; charset=utf-8'
