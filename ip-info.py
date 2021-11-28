import urllib.request
import json

print("\t       [•]IP Information[•] ")

print("""\033[1;36;40m 
		            
		
██╗██████╗░░░░░░░██╗███╗░░██╗███████╗░█████╗░
██║██╔══██╗░░░░░░██║████╗░██║██╔════╝██╔══██╗
██║██████╔╝█████╗██║██╔██╗██║█████╗░░██║░░██║
██║██╔═══╝░╚════╝██║██║╚████║██╔══╝░░██║░░██║
██║██║░░░░░░░░░░░██║██║░╚███║██║░░░░░╚█████╔╝
╚═╝╚═╝░░░░░░░░░░░╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░
	--------------------------------------
By >> Logic232         
Twitter : Logic_232       
""")


while True:
	ipcheck = 0
	print("-" * 40)
	iip = input("Enter ip address: ")
	try:
		url = "https://ipinfo.io/" + iip
		req = urllib.request.Request(url)
		with urllib.request.urlopen(req) as response:
			data = response.read()
			data = json.loads(data)
	except:
		print("Not a valid ip")
		ipcheck = 1

	if ipcheck == 0:
		try:
			print("-" * 40)
			print("Ip address:" , data['ip'])
		except:
			print("Ip address: N/A")
		try:
			print("City:" , data['city'])
		except:
			print("City: N/A")
		try:
			print("State:" , data['region'])
		except:
			print("State: N/A")
		try:
			print("Country:" , data['country'])
		except:
			print("Country: N/A")
		try:
			print("Location:" , data['loc'])
		except:
			print("Location: N/A")
		try:
			print("timezone:" , data['timezone'])
		except:
			print("timezone: N/A")
		try:
			print("phone:" , data['phone'])
		except:
			print("phone: N/A")
		try:
			print("Zip:" , data['postal'])
		except:
			print("Zip: N/A")
		try:
			print("ISP:" , data['org'])
		except:
			print("ISP: N/A")
		try:
			print("network:" , data['network:'])
		except:
			print("network: N/A")
		print("-" * 40)
		
		
