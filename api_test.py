import requests

# Get List User
def test_get_request():
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)
    
    # Check if response status code is 200 (OK)
    assert response.status_code == 200, "GET request failed"

    # Add more assertions based on your API response data
    # For example:
    # assert response.json()['status'] == 'success', "Unexpected response status"

    print("GET request successful")

# API Register User
def test_post_request_register():
    url = 'https://reqres.in/api/register'
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(url, json=data)
    
    # Check if status response 200 (OK)
    assert response.status_code == 200, "POST request failed"
    
    print("POST request for registration successful")

# API LOGIN
def test_post_request_login():
    url = 'https://reqres.in/api/login'
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(url, json=data)

    # Check if response status code is 200 (OK)
    assert response.status_code == 200, "POST request failed"

    print("POST request for login successful")

if __name__ == "__main__":
    test_get_request()
    test_post_request_register()
    test_post_request_login()
