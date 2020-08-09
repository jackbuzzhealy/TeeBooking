import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db, bcrypt
from application.models import Golfer, Booking, BookingLine, TimeSlots
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        hashed_pw = bcrypt.generate_password_hash('admin2020')
        admin = Golfer(foreName="admin", secondName="admin", email="admin@admin.com", password=hashed_pw)

        # create test non-admin user
        hashed_pw_2 = bcrypt.generate_password_hash('test2020')
        employee = Golfer(foreName="test", secondName="user", email="test@user.com", password=hashed_pw_2)

        # save users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_view(self):
        """
        Test that home page is accessible without login
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_timesheet_view(self):
        """
        Test that timesheet page is accessible without login
        """
        response = self.client.get(url_for('timesheet'))
        self.assertEqual(response.status_code, 200)
   
    def test_login_view(self):
        """
        Test that login page is accessible without login
        """
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        """
        Test that register page is accessible without login
        """
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)

    def test_account_view_login(self):
        """
        Test that Account page is accessible while logged in
        """
        with self.client:
             self.client.post(url_for('login')),
             data=dict(email="admin@admin.com",
                    password="admin2020"),
             follow_redirects=True
            
             response = self.client.post(url_for('account'))
             self.assertEqual(response.status_code, 302)

    def test_create_booking_view_login(self):
        """
        Test that create booking  page is accessible while logged in
        """
        with self.client:
             self.client.post(url_for('login')),
             data=dict(email="admin@admin.com",
                    password="admin2020"),
             follow_redirects=True

             response = self.client.post(url_for('createBooking'))
             self.assertEqual(response.status_code, 302)

    def test_update_booking_view_login(self):
        """
        Test that update booking  page is accessible while logged in
        """
        with self.client:
             self.client.post(url_for('login')),
             data=dict(email="admin@admin.com",
                    password="admin2020"),
             follow_redirects=True

             response = self.client.post(url_for('updateBooking'))
             self.assertEqual(response.status_code, 302)

    def test_delete_booking_view_login(self):
        """
        Test that delete booking  page is accessible while logged in
        """
        with self.client:
             self.client.post(url_for('login')),
             data=dict(email="admin@admin.com",
                    password="admin2020"),
             follow_redirects=True

             response = self.client.post(url_for('deleteBooking'))
             self.assertEqual(response.status_code, 302)

class TestCases(TestBase):

    def test_create_booking(self):
        """
        Test that creates a booking
        """
        #TODO 

    def test_account(self):
        """
        Test that views bookings in the account
        """
        #TODO    

    def test_delete_booking(self):
        """
        Test that deletes a booking
        """
        #TODO 

    def test_update_booking(self):
        """
        Test that updates a  booking
        """
        #TODO
