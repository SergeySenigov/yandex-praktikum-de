#!/usr/bin/env python
#import requests
#import pandas as pd
#from tabulate import tabulate
import platform

#def fetch():
#	status = requests.get("https://www.githubstatus.com/api/v2/summary.json").json()['components']
#	df = pd.DataFrame(status)[['name', 'status']]
#	print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

def print_version():
	print(platform.version())
	print(platform.system())
	print(platform.release())
	print(platform.platform())

if __name__ == "__main__":
#	fetch()
	print_version()

	
	
