import re
from pprint import pprint
import json

with open('C:\\Users\\lawall\\Desktop\\26647\\2.A11_cp2e.smw', 'r') as myfile:
    data=myfile.read()

#print data
prog = re.compile('\[(.*?)\]', re.DOTALL)
result = prog.findall(data)

data = []

for t in result:
	obj1 = t.split('\n')
	obj = {}
	for o in obj1:
		if o == '':
			continue
		else:
			obj2 = o.split('=')
			obj[obj2[0]] = obj2[1]

	#pprint(obj)
	data.append(obj)

#print json.dumps(data, indent=4, sort_keys=True)

last = ""

for d in data:
	if 'ObjTp' not in d:
		continue
	if last != d['ObjTp']:
		print(d['ObjTp'])
		last = d['ObjTp']