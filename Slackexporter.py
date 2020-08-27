import os
import json


#for slack messages
#os.chdir('')
def json_to_py():
    i = 0
    list_file = os.listdir()
    while(i <= len(list_file)):
        file = open(list_file[i])
        message_s = json.load(file)
        for var in message_s:
            print(var['text'])
        i += 1


list_Dict = os.listdir()
print(list_Dict)
for i in range(0, len(list_Dict), 1):
    os.chdir(list_Dict[i])
    print(list_Dict[i])
    json_to_py()

#print(os.getcwd())

