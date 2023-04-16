from django.test import TestCase
from .models import Vehicle

class VehicleModelTestCase(TestCase):
    def setUp(self):
        # Create a test Vehicle
        self.test_vehicle = Vehicle.objects.create(
            vehicleYear=2022,
            vehicleMake='Test Make',
            vehicleModel='Test Model',
            vehiclePrice=10000,
        )

    def test_vehicle_values(self):
        # Retrieve the test Vehicle from the database
        vehicle = Vehicle.objects.get(vehicleID=self.test_vehicle.vehicleID)

        # Test that the values of the test Vehicle match the expected values
        self.assertEqual(vehicle.vehicleYear, 2022)
        self.assertEqual(vehicle.vehicleMake, 'Test Make')
        self.assertEqual(vehicle.vehicleModel, 'Test Model')
        self.assertEqual(vehicle.vehiclePrice, 10000)
        self.assertFalse(vehicle.vehicleIsRetired)


    def test_vehicle_is_retired(self):
        # Set the test Vehicle as retired
        self.test_vehicle.vehicleIsRetired = True
        self.test_vehicle.save()

        # Retrieve the test Vehicle from the database
        vehicle = Vehicle.objects.get(vehicleID=self.test_vehicle.vehicleID)

        # Test that the value of vehicleIsRetired has been updated correctly
        self.assertTrue(vehicle.vehicleIsRetired)


    def test_update_vehicle_year(self):
        # Update the vehicleYear attribute of the test Vehicle
        updated_year = 2023
        self.test_vehicle.vehicleYear = updated_year
        self.test_vehicle.save()

        # Retrieve the test Vehicle from the database
        vehicle = Vehicle.objects.get(vehicleID=self.test_vehicle.vehicleID)

        # Test that the vehicleYear attribute has been updated correctly
        self.assertEqual(vehicle.vehicleYear, updated_year)


    def test_update_vehicle_make(self):
        # Update the vehicleMake attribute of the test Vehicle
        updated_make = 'Updated Make'
        self.test_vehicle.vehicleMake = updated_make
        self.test_vehicle.save()

        # Retrieve the test Vehicle from the database
        vehicle = Vehicle.objects.get(vehicleID=self.test_vehicle.vehicleID)

        # Test that the vehicleMake attribute has been updated correctly
        self.assertEqual(vehicle.vehicleMake, updated_make)


    def test_update_vehicle_model(self):
        # Update the vehicleModel attribute of the test Vehicle
        updated_model = 'Updated Model'
        self.test_vehicle.vehicleModel = updated_model
        self.test_vehicle.save()

        # Retrieve the test Vehicle from the database
        vehicle = Vehicle.objects.get(vehicleID=self.test_vehicle.vehicleID)

        # Test that the vehicleModel attribute has been updated correctly
        self.assertEqual(vehicle.vehicleModel, updated_model)


    def test_update_vehicle_price(self):
        # Update the vehiclePrice attribute of the test Vehicle
        updated_price = 20000
        self.test_vehicle.vehiclePrice = updated_price
        self.test_vehicle.save()

        # Retrieve the test Vehicle from the database
        vehicle = Vehicle.objects.get(vehicleID=self.test_vehicle.vehicleID)

        # Test that the vehiclePrice attribute has been updated correctly
        self.assertEqual(vehicle.vehiclePrice, updated_price)


    def test_delete_vehicle(self):
        # Delete the test Vehicle
        self.test_vehicle.delete()

        # Test that the test Vehicle has been deleted
        with self.assertRaises(Vehicle.DoesNotExist):
            Vehicle.objects.get(vehicleID=self.test_vehicle.vehicleID)


    def test_delete_all_vehicles(self):
        # Create more test Vehicles
        vehicle1 = Vehicle.objects.create(
            vehicleYear=2022,
            vehicleMake='Test Make 1',
            vehicleModel='Test Model 1',
            vehicleImage='test_image_1.jpg',
            vehiclePrice=10000,
        )
        vehicle2 = Vehicle.objects.create(
            vehicleYear=2022,
            vehicleMake='Test Make 2',
            vehicleModel='Test Model 2',
            vehicleImage='test_image_2.jpg',
            vehiclePrice=20000,
        )

        # Delete all test Vehicles
        Vehicle.objects.all().delete()

        # Test that all test Vehicles have been deleted
        with self.assertRaises(Vehicle.DoesNotExist):
            Vehicle.objects.get(vehicleID=self.test_vehicle.vehicleID)
        with self.assertRaises(Vehicle.DoesNotExist):
            Vehicle.objects.get(vehicleID=vehicle1.vehicleID)
        with self.assertRaises(Vehicle.DoesNotExist):
            Vehicle.objects.get(vehicleID=vehicle2.vehicleID)    