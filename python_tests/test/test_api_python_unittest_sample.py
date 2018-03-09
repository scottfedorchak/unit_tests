import json
import unittest
import urllib2


class TestApiPythonUnittestSample(unittest.TestCase):

    def setUp(self):
        self.ApiUrl = "http://jsonplaceholder.typicode.com/posts"

    def test_not_empty(self):
        # define api response
        testurl = (self.ApiUrl + '/1')
        print testurl
        response = urllib2.urlopen(testurl)

        # read response
        json_response = response.read()

        # print response
        print(json_response)
        self.assertTrue(json_response != "{}")
        self.assertTrue("userId" in json_response)


    def test_field_value(self):
        # define api response
        testurl = (self.ApiUrl + '/9')
        print testurl
        response = urllib2.urlopen(testurl)

        # read response
        json_response = response.read()

        # print response
        print(json_response)

        json_formatted_data=json.loads(json_response)

        title = json_formatted_data["title"]
        print("json title = " + title)

        self.assertTrue(title=="nesciunt iure omnis dolorem tempora et accusantium")

    def get_params(self, var1, var2, var3):
        return var1 + var2+ var3

    def test_params_python(self):
        output = TestApiPythonUnittestSample.get_params(self,1,2,3)
        print("params output = ",output)


if __name__ == "__main__":
    unittest.main()