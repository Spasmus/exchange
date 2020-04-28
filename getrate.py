import requests
import sched, time
import datetime
from twisted.internet import task, reactor
import smtplib, ssl

timeout = 60.0 # Sixty seconds

def ConsultaCotacao():

	now = datetime.datetime.now()
	print(str(now))
	
	#you can change currency, i am using usd only as example
	resp = requests.get('https://economia.awesomeapi.com.br/usd/')
	usdptax = 0
	if resp.status_code != 200:
	    # This means something went wrong.
	    pass
	for todo_item in resp.json():

	    print('{} {} {}'.format(todo_item['code'], todo_item['name'], todo_item['ask']))
	    usdptax = todo_item['ask']				
	


l = task.LoopingCall(ConsultaCotacao)
l.start(timeout) # call every sixty seconds

reactor.run()
