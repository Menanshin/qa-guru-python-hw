from hw_data.utils.helpers import send_request


def verify_login(base_url, email, password):
    endpoint = 'api/verifyLogin'
    method = 'POST'
    form_data = {
        'email': email,
        'password': password,
    }

    result = send_request(base_url, endpoint, method, data=form_data)
    return result
