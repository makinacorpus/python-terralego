from unittest import TestCase, mock

from terralego import geodirectory


class TestGeodirectory(TestCase):

    @mock.patch('requests.post')
    def test_create_entry(self, mocked_post):
        mocked_response = mock.MagicMock()
        mocked_response.json.return_value = {'id': 'mocked_id'}
        mocked_post.return_value = mocked_response

        entry = geodirectory.create_entry('POINT(42 42)')

        self.assertEqual(mocked_post.call_count, 1)
        self.assertEqual(entry['id'], 'mocked_id')

    @mock.patch('requests.get')
    def test_get_entry(self, mocked_get):
        mocked_response = mock.MagicMock()
        mocked_response.json.return_value = {'id': 'entry_id', 'properties': 'mocked_properties'}
        mocked_get.return_value = mocked_response

        entry = geodirectory.get_entry('entry_id')

        self.assertEqual(mocked_get.call_count, 1)
        self.assertDictEqual(entry, {'id': 'entry_id', 'properties': 'mocked_properties'})

    @mock.patch('requests.put')
    def test_update_entry(self, mocked_put):
        mocked_response = mock.MagicMock()
        mocked_response.json.return_value = {'id': 'entry_id', 'properties': 'mocked_properties'}
        mocked_put.return_value = mocked_response

        entry = geodirectory.update_entry('entry_id', 'POINT(42 42)')

        self.assertEqual(mocked_put.call_count, 1)
        self.assertDictEqual(entry, {'id': 'entry_id', 'properties': 'mocked_properties'})

    @mock.patch('requests.delete')
    def test_delete_entry(self, mocked_delete):

        geodirectory.delete_entry('entry_id')

        self.assertEqual(mocked_delete.call_count, 1)
