from requests import get, Response
from json import loads, dumps

tested_url = 'http://54.91.213.16'
tested_port = 8000
paginator = 'players?page='
user = 'admin'
empty_user = ''
bad_user = 'bad_user'
password = 'admin'
empty_password = ''
bad_password = 'bad_password'

base_url = '{}:{}'.format(tested_url, tested_port)

first_page_full_test_url = '{}/{}{}'.format(base_url, paginator, 1)


def test_login():
    '''
    This test checks logging in with a correct user
    '''
    response = get(first_page_full_test_url, auth=(user, password)).status_code
    assert response == 200, 'test login failed with {} user and {} password'.format(user, password)


def test_login_without_authentication():
    '''
    This test checks logging in without any authentication
    '''
    response = get(first_page_full_test_url).status_code
    assert response == 401, 'test login failed to login without authentication'


def test_login_with_empty_password():
    '''
    This test checks logging in with an empty password
    '''
    response = get(first_page_full_test_url, auth=(user, empty_password)).status_code
    assert response != 200, 'test login succeeded with {} user and empty password'.format(user)


def test_login_with_bad_password():
    '''
    This test checks logging in with a bad password
    '''
    response = get(first_page_full_test_url, auth=(user, bad_password)).status_code
    assert response != 200, 'test login succeeded with {} user and {} password'.format(user, bad_password)


def test_login_with_empty_user():
    '''
    This test checks logging in with an empty user
    '''
    response = get(first_page_full_test_url, auth=(empty_user, password)).status_code
    assert response != 200, 'test login succeeded with an empty user and {} password'.format(password)



def test_login_with_bad_user():
    '''
    This test checks logging in with a bad user
    '''
    response = get(first_page_full_test_url, auth=(bad_user, password)).status_code
    assert response != 200, 'test login succeeded with {} user and {} password'.format(bad_user, password)


def test_response_data():
    '''
    This test checks the data within the response
    '''
    content = get(first_page_full_test_url, auth=(user, password)).json()
    for entry in content:
        for key, value in entry.items():
            assert len(str(key)) != 0, str(key) + 'key was found to be empty in the entry'
            assert len(str(value)) != 0, str(value) + 'value was found to be empty in the entry'


# def test_unique_content():
#     '''
#     This test asserts that sequential pages don't have the same data.
#     Can be randomized for better results
#     '''
#     pages_list = []
#     for i in range(1, 10):
#         full_test_url = '{}/{}{}'.format(base_url, paginator, i)
#         response = get(full_test_url, auth=(user, password)).json()
#         pages_list.append(response)
#     for i, page in enumerate(pages_list):
#         if i > 1:
#             assert pages_list[i] != pages_list[i-1]
