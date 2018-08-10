from flask import Flask
import os
from app import app



if __name__ == '__main__':
	# app.run()
	port = int(os.environ.get("PORT", 5000))
	app.run(host='127.0.0.1', port=port)
