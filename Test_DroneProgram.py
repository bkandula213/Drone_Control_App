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

    @patch('drone_program.connect')
    def test_changeThrottle(self, mock_connect):
        # Set up the mock vehicle object
        mock_vehicle = MagicMock()
        mock_connect.return_value = mock_vehicle

        # Create a Connect_vehicle object
        droneObj = Connect_vehicle()

        # Set up mock channels and overrides
        mock_vehicle.channels = MagicMock()
        droneObj.throttle = 1000
        droneObj.pitch = 1500
        droneObj.rudder = 1500
        droneObj.aileron = 1500

        # Call the changeThrottle method
        droneObj.changeThrottle(100)

        # Assert that the throttle value was updated
        self.assertEqual(droneObj.throttle, 1100)


    @patch('drone_program.connect')
    def test_changeElevation(self, mock_connect):
        # Set up the mock vehicle object
        mock_vehicle = MagicMock()
        mock_connect.return_value = mock_vehicle

        # Create a Connect_vehicle object
        droneObj = Connect_vehicle()

        # Set up mock channels and overrides
        mock_vehicle.channels = MagicMock()
        droneObj.throttle = 1000
        droneObj.pitch = 1500
        droneObj.rudder = 1500
        droneObj.aileron = 1500

        # Call the changeElevation method
        droneObj.changeElevation(1600)

        # Assert that the pitch value was updated
        self.assertEqual(droneObj.pitch, 1600)

    @patch('drone_program.connect')
    def test_changeRudder(self, mock_connect):
        # Set up the mock vehicle object
        mock_vehicle = MagicMock()
        mock_connect.return_value = mock_vehicle

        # Create a Connect_vehicle object
        droneObj = Connect_vehicle()

        # Set up mock channels and overrides
        mock_vehicle.channels = MagicMock()
        droneObj.throttle = 1000
        droneObj.pitch = 1500
        droneObj.rudder = 1500
        droneObj.aileron = 1500

        # Call the changeElevation method
        droneObj.changeRudder(1700)

        # Assert that the pitch value was updated
        self.assertEqual(droneObj.rudder, 1700)

    @patch('drone_program.connect')
    def test_changeAileron(self, mock_connect):
        # Set up the mock vehicle object
        mock_vehicle = MagicMock()
        mock_connect.return_value = mock_vehicle

        # Create a Connect_vehicle object
        droneObj = Connect_vehicle()

        # Set up mock channels and overrides
        mock_vehicle.channels = MagicMock()
        droneObj.throttle = 1000
        droneObj.pitch = 1500
        droneObj.rudder = 1500
        droneObj.aileron = 1500

        # Call the changeElevation method
        droneObj.changeAileron(1300)

        # Assert that the pitch value was updated
        self.assertEqual(droneObj.aileron, 1300)


if __name__ == '_main_':
    unittest.main()
