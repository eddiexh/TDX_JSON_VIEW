import requests
import json
import pyperclip as pc

app_id = '<<Client Id>>'
app_key = '<<Client Secret>>'
auth_url = "https://tdx.transportdata.tw/auth/realms/TDXConnect/protocol/openid-connect/token"

url = input("請輸入Request URL(輸入0結束程式):")

while url != '0':
    class Auth:
        def __init__(self, app_id, app_key):
            self.app_id = app_id
            self.app_key = app_key

        def get_auth_header(self):
            content_type = 'application/x-www-form-urlencoded'
            grant_type = 'client_credentials'

            return {
                'content-type': content_type,
                'grant_type': grant_type,
                'client_id': self.app_id,
                'client_secret': self.app_key
            }

    class data:
        def __init__(self, app_id, app_key, auth_response):
            self.app_id = app_id
            self.app_key = app_key
            self.auth_response = auth_response

        def get_data_header(self):
            auth_JSON = json.loads(self.auth_response.text)
            access_token = auth_JSON.get('access_token')
            return {
                'authorization': 'Bearer ' + access_token
            }

    def response(url, auth_response=None):
        global data_response
        if __name__ == '__main__':
            try:
                d = data(app_id, app_key, auth_response)
                data_response = requests.get(url, headers=d.get_data_header())
            except:
                a = Auth(app_id, app_key)
                auth_response = requests.post(auth_url, a.get_auth_header())
                d = data(app_id, app_key, auth_response)
                data_response = requests.get(url, headers=d.get_data_header())
        return data_response.text

    data_response = response(url)
    print(data_response)
    pc.copy(data_response)
    print("\n已複製輸出結果")
    url = input("\n請輸入Request URL(輸入0結束程式):")
