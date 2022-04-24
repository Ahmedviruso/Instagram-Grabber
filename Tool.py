# Python 3.10.4
# AhmedViruso (2022-04-24)

import requests
from json import loads
from json2table import convert
Username = input("Enter Wanted User: ")

Payload = '35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{"q":\"'+ Username +'\","guid":"b449de3c-1663-47bc-8cca-e83b570b60d1","device_id":"615d8b7997acf12b"}'
Browser = "Instagram 99.4.0"

Url = 'https://i.instagram.com/api/v1/users/lookup/'
Data = {'signed_body': Payload, "ig_sig_key_version":"9"}

Request = requests.post(Url, headers={'User-Agent':Browser}, data = Data)
Json = loads(Request.text)

Attrs = {"style" : "border: 1px solid black;background-color: grey;color: white"}
Html = convert(Json, table_attributes = Attrs)
with open("Save.html","w") as File:
  File.write(Html)