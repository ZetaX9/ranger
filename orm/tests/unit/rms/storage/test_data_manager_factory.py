import unittest

from orm.services.region_manager.rms.storage import data_manager_factory
from orm.services.region_manager.rms.storage.my_sql import data_manager
from orm.services.region_manager.rms.storage.my_sql.data_manager import DataManager

from mock import patch


class StorageFactoryTests(unittest.TestCase):

    @patch.object(data_manager_factory, 'conf')
    @patch.object(data_manager, 'db_session')
    def test_get_data_manager(self, conf_mock, db_session_mock):
        """ Check the returned object from get_region_resource_id_status_connection
        is instance of  DataManager
        """
        obj = data_manager_factory.get_data_manager()
        self.assertIsInstance(obj, DataManager)
