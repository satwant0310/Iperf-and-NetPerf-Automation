#!/usr/bin/env python3
import subprocess
res=[]
n = int(input("Please enter the no of time you want to execute:"))
a = input("Please mention the Ip:")
b = input("Enter port no:")
for i in range(0,n):
	bashCommand = "netperf -H "+ a +" -p " + b
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE,stderr=subprocess.PIPE, text = True)
	output, error =process.communicate()
	print(output)
	output = output.split("  ")
	res.append(float(output[-2]))
print(res)
avg = sum(res)/len(res)
#round(avg, 2)
print("The average throughput is:",avg)
