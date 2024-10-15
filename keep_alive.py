from flask import Flask
from threading import Thread


app = Flask('')

@app.route('/')
def home():
	return 'This File Is Made By @itz_villain_30'

def run():
  app.run(debug=True)

def keep_alive():
	'''
	Creates and starts new thread that runs the function run.
	'''
	t = Thread(target=run)
	t.start()
