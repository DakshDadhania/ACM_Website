import logging
import requests
r=requests.Session()
r.post("http://localhost:3000/admin")
