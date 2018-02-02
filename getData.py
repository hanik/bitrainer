# /Users/actmember/workspace/take10-lstm/bitData/ALL_180130_23.txt
import json
import csv
import datetime
from os import walk

def write_row(json_data):
    date = json_data['data']['date']
    btc = json_data['data']['BTC']
    value = [date, int(btc['opening_price']), int(btc['max_price']), int(btc['min_price']), int(btc['closing_price']), btc['volume_1day']]
    writer.writerow(value)

filedir = '/Users/actmember/workspace/take10-lstm/bitData/'
# filedir = '/Users/actmember/workspace/take10-lstm/bitData/test/'
f = []
for (dirpath, dirnames, filenames) in walk(filedir):
    f.extend(filenames)
    break

employ_data = open('./csvData/ALL_180131.csv', 'a')
# employ_data = open('./csvData/test/ALL_180201.csv', 'a')
writer = csv.writer(employ_data)
writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])

for filename in f:
    print(filename)
    filepath = filedir + filename
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        # employ_data = open('./csvData/' + filename.replace('.txt', '.csv'), 'w')
        employ_data = open('./csvData/ALL_180131.csv', 'a')
        # employ_data = open('./csvData/test/ALL_180201.csv', 'a')
        writer = csv.writer(employ_data)
        # writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
        while line:
            try:
                json_parsed = json.loads(line)
                write_row(json_parsed)
            except:
                print('error')

            line = fp.readline()
            cnt += 1
        employ_data.close()
