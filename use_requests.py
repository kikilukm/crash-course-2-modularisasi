import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'success! Response= {response.status_code}')
        print(f'content{response.text}')
    else:
        print(f'Woops the page you looking unavailable or encounter some errors {response.status_code}')
except Exception as e:
    print(f'There has an Error occurred: {e}')
print('Program Ended')
