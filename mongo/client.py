import subprocess
import Collection
import requests

import os
import csv

#####################################################################################################################
dbName = 'cafexapp_core_2_0_0'
ext = 'csv'
port = 8080

url='http://localhost'

collections = [
    Collection.Collection('kiosk', 'core.kiosk', ['_id']),
    Collection.Collection('order', 'core.order', ['customerId', 'kioskId'])
]

#####################################################################################################################

for c in collections:
    string = "mongoexport --db " + dbName + " --collection " + c.name + " --out " + c.name + "." + ext + " --" + ext + " --fields " + ",".join(c.fields)
    print string
    subprocess.call(string, shell=True)

for f in collections:
    files = {'file': open(f.name + '.' + ext, 'rb'), 'type' : f.type}
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    r = requests.post(url + ':' + str(port) + '/csv/' + f.type, files)
    print r