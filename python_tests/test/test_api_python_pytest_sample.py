import json
import pytest
import urllib2

class TestApiPythonPytestSample:
    @pytest.fixture
    def set_up(self):
        self.ApiUrl = "http://jsonplaceholder.typicode.com/posts"

    @pytest.mark.usefixtures("set_up")
    def test_not_empty(self):
        # define api response
        testurl = (self.ApiUrl + '/1')
        print testurl
        response = urllib2.urlopen(testurl)

        # read response
        json_response = response.read()

        # print response
        assert json_response != "{}"
        assert "userId" in json_response

    @pytest.mark.usefixtures("set_up")
    def test_404_not_found_exception(self):
        with pytest.raises(Exception) as excinfo:
            testurl = (self.ApiUrl + '/zzzzzzzzz')
            response = urllib2.urlopen(testurl)
            json_response = response.read()
        assert excinfo.value.code == 404
        assert excinfo.value.msg == "Not Found"

if __name__ == "__main__":
    pytest.main()