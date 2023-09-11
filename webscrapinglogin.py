import requests
from bs4 import BeautifulSoup

# Step 1: Send a GET request to the login page and retrieve cookies and csrf_token
login_url = 'https://example.com/login'
session = requests.Session()
login_response = session.get(login_url)
login_soup = BeautifulSoup(login_response.content, 'html.parser')
csrf_token = login_soup.select_one('input[name="csrf_token"]')['value']
cookies = login_response.cookies

# Step 2: Construct a dictionary containing the login credentials and csrf_token
username = 'my_username'
password = 'my_password'
login_data = {
    'username': username,
    'password': password,
    'csrf_token': csrf_token
}

# Step 3: Send a POST request to the login page with the login credentials and csrf_token
post_response = session.post(login_url, data=login_data, cookies=cookies)

# Step 4: Use BeautifulSoup to parse the HTML content of the response
if 'Welcome' in post_response.text:
    print('Login successful')
else:
    print('Login failed')

# Step 5: Navigate to the page that you want to scrape
target_url = 'https://example.com/target_page'
target_response = session.get(target_url, cookies=cookies)

# Step 6: Use BeautifulSoup to parse the HTML content of the target page
target_soup = BeautifulSoup(target_response.content, 'html.parser')
# Extract the data that you need