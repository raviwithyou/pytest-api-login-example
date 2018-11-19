#Fixture for Rest API
from pytest import fixture
from RestApiClient import RestApiClient

@fixture(scope='module')
def testapi(request):
    url = request.config.getoption('base_url')
    return RestApiClient(base_url=url)