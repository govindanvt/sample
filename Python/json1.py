import json
d={'101':"Abhi",'102':"Deepak",'103':"Hari"}
jsonStr=json.dumps(d)
print("Created Sucessfully...!\n\n\n",d)

#the string made in previous example is now available in JsonStr
nD=json.loads(jsonStr)
print("\n\n",nD['102'])

#this will display the JSON conveersion of the list of numbers
L=[10,30,40,50]
print("\n\n",json.dumps(L))


