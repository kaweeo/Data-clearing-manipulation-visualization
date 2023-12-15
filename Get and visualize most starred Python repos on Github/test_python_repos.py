import unittest
import requests

# Make an API call, and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

repo_dicts = response_dict['items']
print("items:", repo_dicts)
# run a test


class MyTestCase(unittest.TestCase):
    def test_APIresponse(self):
        self.assertEqual(r.status_code, 200)

    def test_APIresponse(self):
        self.assertGreater(response_dict['total_count'], 7000000)


if __name__ == '__main__':
    unittest.main()
