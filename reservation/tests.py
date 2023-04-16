from django.test import TestCase
from datetime import date, timedelta
from .models import Reservation
import uuid


# Ensures the database can add and query data
class ReservationModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        # Set up non-modified objects used by all test methods
        cls.car_id = uuid.uuid4()
        cls.reservation = Reservation.objects.create(
            carId=cls.car_id,
            userId=12345,
            startDate=date(2023, 4, 1),
            endDate=date(2023, 4, 5),
            pickUpAddress="123 Main St, Anytown USA",
            needsPickup=True,
            hasInsurance=True,
            isReturned=False,
        )

    def test_reservation_creation(self):
        reservation = Reservation.objects.get(carId=self.car_id)
        self.assertEqual(reservation.userId, 12345)
        self.assertEqual(reservation.startDate, date(2023, 4, 1))
        self.assertEqual(reservation.endDate, date(2023, 4, 5))
        self.assertEqual(reservation.pickUpAddress, "123 Main St, Anytown USA")
        self.assertTrue(reservation.needsPickup)
        self.assertTrue(reservation.hasInsurance)
        self.assertFalse(reservation.isReturned)


# Ensures the database can update data
class ReservationUpdateTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.car_id = uuid.uuid4()
        cls.reservation = Reservation.objects.create(
            carId=cls.car_id,
            userId=12345,
            startDate=date(2023, 4, 1),
            endDate=date(2023, 4, 5),
            pickUpAddress="123 Main St, Anytown USA",
            needsPickup=True,
            hasInsurance=True,
            isReturned=False,
        )

    def test_reservation_update(self):
        # Update the reservation end date
        new_end_date = date(2023, 4, 7)
        self.reservation.endDate = new_end_date
        self.reservation.save()

        # Retrieve the reservation from the database
        updated_reservation = Reservation.objects.get(carId=self.car_id)

        # Test that the reservation was updated correctly
        self.assertEqual(updated_reservation.endDate, new_end_date)


# Ensures the database can be deleted
class ReservationDeleteTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.car_id = uuid.uuid4()
        cls.reservation = Reservation.objects.create(
            carId=cls.car_id,
            userId=12345,
            startDate=date(2023, 4, 1),
            endDate=date(2023, 4, 5),
            pickUpAddress="123 Main St, Anytown USA",
            needsPickup=True,
            hasInsurance=True,
            isReturned=False,
        )

    def test_reservation_delete(self):
        # Delete the reservation
        self.reservation.delete()

        # Try to retrieve the reservation from the database
        with self.assertRaises(Reservation.DoesNotExist):
            Reservation.objects.get(carId=self.car_id)


# Ensures specific elements of the database can be deleted
class ReservationSpecificDeleteTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.car_id1 = uuid.uuid4()
        cls.car_id2 = uuid.uuid4()
        cls.reservation1 = Reservation.objects.create(
            carId=cls.car_id1,
            userId=12345,
            startDate=date(2023, 4, 1),
            endDate=date(2023, 4, 5),
            pickUpAddress="123 Main St, Anytown USA",
            needsPickup=True,
            hasInsurance=True,
            isReturned=False,
        )
        cls.reservation2 = Reservation.objects.create(
            carId=cls.car_id2,
            userId=54321,
            startDate=date(2023, 4, 2),
            endDate=date(2023, 4, 6),
            pickUpAddress="456 Oak Ave, Somecity USA",
            needsPickup=False,
            hasInsurance=False,
            isReturned=True,
        )

    def test_reservation_specific_delete(self):
        # Delete the reservation with car_id1
        Reservation.objects.filter(carId=self.car_id1).delete()

        # Try to retrieve the reservation with car_id1 from the database
        with self.assertRaises(Reservation.DoesNotExist):
            Reservation.objects.get(carId=self.car_id1)

        # Retrieve the reservation with car_id2 from the database
        remaining_reservation = Reservation.objects.get(carId=self.car_id2)

        # Test that the remaining reservation was not deleted
        self.assertEqual(remaining_reservation.userId, 54321)


