import pytest
import allure
import requests


@allure.title("Test POST Request - RestFUL BOOKER CREATION OF BOOKING")
@allure.description("TC#1 -> Verify that POST  Request with new BookingID creation")
# @allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Arpita Mukherjee")
@allure.testcase("TC#1")
# @pytest.mark.smoke

def test_post_booking_id_creation_positive ( ) :
    base_URL = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_URL + base_path
    headers = {"Content-Type" : "application/json"}
    payload = {
        "firstname" : "Priya",
        "lastname" : "Mukherjee",
        "totalprice" : 1500.00,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2024-09-28",
            "checkout" : "2024-10-15"
        },
        "additionalneeds" : "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)

    responseData = response.json()
    bookingId = responseData["bookingid"]
    firstName = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    totalPrice = responseData["booking"]["totalprice"]
    depositPaid = responseData["booking"]["depositpaid"]
    checkin = responseData["booking"]["bookingdates"]["checkin"]
    checkout = responseData["booking"]["bookingdates"]["checkout"]

    assert response.status_code == 200
    assert bookingId is not None
    assert bookingId > 0
    assert type(bookingId) == int
    assert firstName == payload['firstname']

    assert lastname == payload['lastname']
    assert totalPrice == payload['totalprice']
    assert depositPaid ==payload['depositpaid']
    assert checkin == payload['bookingdates']['checkin']
    assert checkout == payload['bookingdates']['checkout']

    print("Response checkout:", checkout)
    print("Request checkout:", payload['bookingdates']['checkout'])
