import json

file = open("json-sample.json", "r")

data = json.load(file)


file.close()

# 'imdata' -> [{'sldkfj': {sd;jkf:sdlkjf, lksdjf:lskdf, }}, {dskl;f: dslkfj}, ]

list1 = []
list2 = []
list3 = []

for x in data["imdata"]:
	for dic1 in x:
		for dic2 in x[dic1].values():
			
			list1.append(dic2["dn"])
			list2.append(dic2["speed"])
			list3.append(dic2["mtu"])

o = len(list1[0])
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
for i in range(len(list1)):
	print(list1[i], end="")
	if len(list1[i]) != o:
		print("                              ", end=" ")
	else:
		print("                              ", end="")
	print(list2[i], end="")
	print("   ", end="")
	print(list3[i])


