'''
script to extract data from a binance API and put it into an SQLite3 database 

'''

import sqlite3
import os.path
import websocket, json
from datetime import datetime


base_endpoint = 'wss://stream.binance.com:9443'
extension = '/ws/btcusdt@kline_1m'
url = base_endpoint + extension

	
if os.path.isfile('trades.db') == False:
	
	conn = sqlite3.connect('trades.db')
	c=conn.cursor()
	c.execute("""CREATE TABLE trades (id int PRIMARY KEY, time int NOT NULL, price real NOT NULL)""")
	print ("Opened database successfully - table created")
else:
	conn = sqlite3.connect('trades.db')
	c = conn.cursor()
	print ("Opened database successfully")
	

def on_close(ws):
	print("Closing")

def on_message(ws, message):
	json_mess = json.loads(message)
	#print(json_mess)
	candle = json_mess['k']
	#if candle['x']:
		#print(candle)
	trade_time = int(candle['t'])
	#print(trade_time)
	price = float(candle['c'])
	sql_str= "INSERT INTO trades VALUES ({},{},{})".format('null', trade_time,  price)

	c.execute(sql_str)
	print('updated')


	c.execute("SELECT * FROM trades")
	#print(c.fetchall())
	
	time_val=[]
	data_val=[]
	
	for row in c:
		time_only = row[1]//1000
		time_only = str(datetime.fromtimestamp(time_only)).split()[1]
		#print(time_only)
		#print(row[2])
		time_val.append(time_only)
		data_val.append(row[2])
		#print(time_val)
		#print(data_val)

	conn.commit()




ws = websocket.WebSocketApp(url,on_message = on_message, on_close = on_close)

ws.run_forever()
