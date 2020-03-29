import sys 
sys.path.append('../Flask-Rest-API/scripts/')
import pytest 
import myRetailLocalVersion as server

# Creates a fixture whose name is "app"
# and returns our flask server instance
@pytest.fixture
def app():
    app = server.app
    return app