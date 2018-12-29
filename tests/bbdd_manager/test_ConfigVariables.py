import unittest

import bbdd_manager.ConfigVariablesBbdd as ConfV

class TestDBConfig(unittest.TestCase):

    def test_server(self):
        self.assertTrue(hasattr(ConfV, 'server'), msg="DB server is not defined")
        print("DB server is {server:s}".format(server=ConfV.server))

    def test_port(self):
        self.assertTrue(hasattr(ConfV, 'port'), msg="DB Port is not defined")
        print("DB Port is {port:d}".format(port=ConfV.port))

    def test_name(self):
        self.assertTrue(hasattr(ConfV, 'database'), msg="DB Name is not defined")
        print("DB Name is {name:s}".format(name=ConfV.database))

