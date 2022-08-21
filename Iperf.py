#!/usr/bin/env python3

import subprocess
import re
n = int(input("Please enter the no of time you want to execute:"))

def test(a):
#	n = int(input("Please enter the no of time you want to execute:"))
	abc=[] 
	regexp= r'\d{3}\s\bMbits/sec\s'
#regexp= r'\d{3}'
	for i in range(0,n):
		bashCommand = "iperf3 -c 192.168.212.132"
		process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE,stderr=subprocess.PIPE, text = True)
		output, error =process.communicate()
		print(output)
		tsl = re.findall(regexp,output)
		print(tsl)
		abc.append(float(tsl[-2][0:3]))
	print(abc)
	avg = sum(abc)/len(abc)
	print("The average throughput is:",avg)
test(n)

