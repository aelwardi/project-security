import pytest
from app import app
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
def test_main_route(client):
    """Vérifie que la route principale répond 200"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'REST API' in rv.data
def test_login_fail(client):
    """Vérifie que le login échoue avec de mauvais identifiants"""
    rv = client.get('/login?username=wrong&password=wrong')
    assert rv.status_code == 403
