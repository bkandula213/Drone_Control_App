import unittest
from unittest.mock import patch, MagicMock
from dronekit import Vehicle, VehicleMode
from drone_program import Connect_vehicle

class TestConnectVehicle(unittest.TestCase):
    @patch('drone_program.connect')
    def test_armDrone(self, mock_connect):
        # Set up the mock vehicle object
        mock_vehicle = MagicMock()
        mock_connect.return_value = mock_vehicle

        # Create a Connect_vehicle object
        droneObj = Connect_vehicle()

        # Call the armDrone method
        droneObj.armDrone()

        # Assert that the vehicle object was created with the correct connection string
        mock_connect.assert_called_once_with('udp:127.0.0.1:14550', wait_ready=False)

        # Assert that the vehicle mode was set to MANUAL
        mock_vehicle.mode.assert_called_once_with = VehicleMode('MANUAL')

        # Assert that the vehicle was armed
        self.assertTrue(mock_vehicle.armed)

if __name__ == '__main__':
    unittest.main()
