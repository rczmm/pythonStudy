import requests

url = '''
http://110.185.163.49:22222/stage-api/ins/insTask/list?pageNum=1&pageSize=10
'''

headers = {
    'authorization': r'Bearer eyJhbGciOiJIUzUxMiJ9.eyJ0ZW5hbnRfaWQiOiI0NDIxMSIsIm9zIjoiQ2hyb21lIiwidXNlcl9pZCI6MjA4LCJ1c2VyX2tleSI6Ijk3ZGVlNTNjLTVkZWUtNGJjNy1hM2RmLWVjYTIyNmZkYzFhOCIsImRlcHRfbmFtZSI6IjQ0MjExIiwiZGVwdF9pZCI6NDE5LCJ1c2VybmFtZSI6ImRjIn0.bUW8B3MhwQeJptSMBPRws7h_qyljTTUjRP3q-uZx0gzkeFTBC8L158-9Zn0K68cIkia73q4UwakfU_ybBu9pUg'
}

j = 0

for i in range(500):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        j += 1

print(j)
