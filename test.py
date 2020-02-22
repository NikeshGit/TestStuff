import json
with open('input.json','r') as input:
	obj = json.load(input)
	with open('output.json','w') as output:
		output.write(obj['name'] + "enjoys: ")
		for hobby in obj['Hobbies']:
			output.write(hobby + "/n")
