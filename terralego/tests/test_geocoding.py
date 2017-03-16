from unittest import TestCase, mock

from terralego import geocoding


class TestGeocoding(TestCase):

    @mock.patch('requests.get')
    def test_search(self, mocked_get):
        mocked_response = mock.MagicMock()
        mocked_response.json.return_value = {'features': []}
        mocked_get.return_value = mocked_response

        results = geocoding.search('nantes')

        self.assertEqual(mocked_get.call_count, 1)
        self.assertDictEqual(results, {'features': []})

    @mock.patch('requests.get')
    def test_reverse(self, mocked_get):
        mocked_response = mock.MagicMock()
        mocked_response.json.return_value = {'features': []}
        mocked_get.return_value = mocked_response

        results = geocoding.reverse('1.24', '42')

        self.assertEqual(mocked_get.call_count, 1)
        self.assertDictEqual(results, {'features': []})

    @mock.patch('requests.get')
    def test_autocomplete(self, mocked_get):
        mocked_response = mock.MagicMock()
        mocked_response.json.return_value = {'features': []}
        mocked_get.return_value = mocked_response

        results = geocoding.autocomplete('nantes')

        self.assertEqual(mocked_get.call_count, 1)
        self.assertDictEqual(results, {'features': []})
