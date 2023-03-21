# enter your code below
import configparser
import time
import requests

config = configparser.ConfigParser()
config.read('Ironhack/Config/config2.cfg')

token = config['GITHUB']['token']
headers = {'Authorization': 'token ' + token}