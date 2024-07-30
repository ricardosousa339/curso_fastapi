from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_create_existing_username(client):
    client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'blabla@hotmail.com',
            'password': 'secret123',
        },
    )

    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@gmail.com',
            'password': 'secret123',
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_existing_email(client):
    client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@hotmail.com',
            'password': 'secret123',
        },
    )

    response = client.post(
        '/users/',
        json={
            'username': 'aliceandra',
            'email': 'alice@hotmail.com',
            'password': 'secret123',
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    print(response)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': user.id,
    }


def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    print(response.json())

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }
