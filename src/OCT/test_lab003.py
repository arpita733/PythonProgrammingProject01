import pytest
import allure

@allure.title("Test My First API Automation TCs")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")

def test_verify_sum_01 ( ) :
    assert 2 + 2 == 5


def test_verify_sub_02 ( ) :
    assert 2 - 2 == 0

#@pytest.mark.smoke
def test_verify_mul_03 ( ) :
    assert 2 * 2 == 4


#@pytest.mark.skip("not completed DIVISION ")
def test_verify_div_04 ( ) :
    assert 2 / 2 == 1
