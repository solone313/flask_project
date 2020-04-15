from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    print(response)
    assert response.status_code == 200


def hello(name):
    return 'Hello {}!'.format(name)