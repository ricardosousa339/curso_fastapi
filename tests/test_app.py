from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@gmail.com',
            'password': 'secret123',
        },
    )
    print('resposta')

    print(response.json())
    print('resposta')
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@gmail.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'username': 'alice', 'email': 'alice@gmail.com', 'id': 1}]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_deleted_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
