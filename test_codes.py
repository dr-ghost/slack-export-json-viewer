import os
import json
import urllib
import urllib.request as ur

"""
os.chdir("C:\\Users\Vijay\Desktop")
file = open("2019-06-07.json", "r")
message = json.load(file)
for vat in message:
    if 'text' in vat:
        if '@' in vat['text']:
            x = vat['text']
            str1 = x.split("<")
            str2 = str1[1].split(">")

# <@35sggswtgrg> is kiran , <@3654etsdfgsd> is gajni , is aaryan
i = 1
st3 = "Thank you <@35sggswtgrg> and <@3654etsdfgsd> and <@jlshfslaSf> so much."
str1 = st3.split("<")
length = len(str1)
str_n = str1[0]
while(i <= length-1):
    if '@' in str1[i]:
        str_p0 = str1[i].split(">")
        str_n += (str_p0[0] + str_p0[1])
        print(str_p0)
    i += 1
print(st3)
print(str1)
print(str_n)
"""
#emojisearch = "muscles"
#print(ur.urlopen("https://emojipedia.org/search/?q=" + emojisearch))
