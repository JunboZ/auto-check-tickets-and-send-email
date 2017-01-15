#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# coding="utf-8"


# from docopt import docopt
# from pprint import pprint
# from station_map import stations
# from prettytable import PrettyTable
import requests
import time
from envelopes import Envelope, GMailSMTP

def send(date):

	envelope = Envelope(
		from_addr=(u'example@gmail.com', u'GoodNews'),
		to_addr=(u'example@qq.com', u'GetReady'),
		subject=u'Tickets!',
		text_body=unicode(str(date))
	)
	# envelope.add_attachment('/Users/bilbo/Pictures/helicopter.jpg')

	# Send the envelope using an ad-hoc connection...
	envelope.send('smtp.gmail.com', login='example@gmail.com', password='passport', tls=True)

	# Or send the envelope using a shared GMail connection...
	# gmail = GMailSMTP('from@example.com', 'password')
	# gmail.send(envelope)

def check_ticket(date):
	url="https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date={}&leftTicketDTO.from_station=XUG&leftTicketDTO.to_station=BJP&purpose_codes=ADULT".format(date)
	r=requests.get(url, verify=False)
	if 'data' not in r.json():
			print '未找到相应信息！'		
	#print r.json()
	arr = r.json()['data']
	print arr
	for row_train in arr:
		rowtrain=row_train['queryLeftNewDTO']
		print rowtrain["yw_num"]+rowtrain['ze_num']
		if rowtrain['yw_num'] not in u'0 -- \u65e0' or rowtrain['ze_num'] not in u'0 -- \u65e0' :
			# send(date)
			temp=1
		else:
			temp=0
		
	return temp
        

while True:
	a=check_ticket('2017-02-04')+check_ticket('2017-02-05')+check_ticket('2017-02-06')
	print a
	if a != 0:
		time.sleep(1800)
	else:
		time.sleep(30)
	



