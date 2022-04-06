from ppc import web_people
import pytest

@pytest.fixture()
def app():
    app = web_people()
    app.config.update({
                "TESTING": True,
                      })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()

def test():
    response = web_people().test_client().post('/items', json='[{"id":1001, "name":"Silly Format"}, {"id": 1002, "name":"42"}, {"id": 1003, "name":"mature"}]')
    print(response)

"""

def test_items(client):
    '''monolithic test for all test cases. TODO divide into smaller test cases'''
    response = client.post('/items', 
            json={
                    'items': [
                        {
                            'id':'1',
                            'name':'a'
                        },
                        {
                            'id':'2',
                            'name':'b'
                        },
                        {
                            'id':'3',
                            'name':'c'
                        }
                     ]
                 }
            )
    print(response.request.path)
"""
