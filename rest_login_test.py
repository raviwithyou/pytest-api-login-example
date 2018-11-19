# Code with Test cases
from rest_api_fixture import testapi
#TC-0001
def test_correct_login(testapi):
    payload = {
        'user': 'correct',
        'password': 'correct',
    }
    response = testapi.post('/login', data = payload)
    outputResponse = response.json()
    assert (response.status_code == 200 or response.status_code == 201) and (outputResponse['status'] == '1')

#TC-0002
def test_correct_login_mobile(testapi):
    payload = {
        'mobile': 'correct',
        'password': 'correct',
    }
    response = testapi.post('/login', data = payload)
    outputResponse = response.json()
    assert (response.status_code == 200 or response.status_code == 201) and (outputResponse['status'] == '1')

#TC-0003
def test_correct_login_user_mobile(testapi):
    payload = {
        'user': 'correct',
        'password': 'correct',
        'mobile': 'correct',
    }
    response = testapi.post('/login', data = payload)
    outputResponse = response.json()
    assert (response.status_code == 200 or response.status_code == 201) and (outputResponse['status'] == '1')

#TC-0004
def test_incorrect_login_mobile_pwd(testapi):
    payload = {
        'mobile': 'correct',
        'password': 'incorrect',
    }
    response = testapi.post('/login', data = payload)
    outputResponse = response.json()
    assert (response.status_code == 200 or response.status_code == 201) and (outputResponse['status'] == '0' and outputResponse['errorCode'] == '123')

#TC-0005
def test_incorrect_login_user_pwd(testapi):
    payload = {
        'user': 'correct',
        'password': 'incorrect',
    }
    response = testapi.post('/login', data = payload)
    outputResponse = response.json()
    assert (response.status_code == 200 or response.status_code == 201) and (outputResponse['status'] == '0' and outputResponse['errorCode'] == '124')

#TC-0006
def test_incorrect_login_user_both(testapi):
    payload = {
        'user': 'incorrect',
        'password': 'incorrect',
    }
    response = testapi.post('/login', data = payload)
    outputResponse = response.json()
    assert (response.status_code == 200 or response.status_code == 201) and (outputResponse['status'] == '0' and outputResponse['errorCode'] == '125')

#TC-0007
def test_incorrect_login_usermob(testapi):
    payload = {
        'user': 'incorrect',
        'password': 'correct',
        'mobile': 'correct',
    }
    response = testapi.post('/login', data = payload)
    outputResponse = response.json()
    assert (response.status_code == 200 or response.status_code == 201) and (outputResponse['status'] == '0' and outputResponse['errorCode'] == '126')