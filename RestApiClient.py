#API client for invoking GET/POST. It serves as a wrapper for Request Session
from requests import Session

class RestApiClient(Session):

    def __init__(self, base_url):
        super(RestApiClient, self).__init__()
        #TODO: Implement this to take from environment config
        #Hard coded url for the entire project
        self.base_url = 'http://www.testsite.com'

    def _build_url(self, extension):
        return '{base_url}{extension}'.format(
            base_url=self.base_url, extension=extension)

    def get(self, url, **kwargs):
        _url = self._build_url(extension=url)
        return super(RestApiClient, self).get(_url, **kwargs)

    def post(self, url, **kwargs):
        _url = self._build_url(extension=url)
        return super(RestApiClient, self).post(_url, **kwargs)