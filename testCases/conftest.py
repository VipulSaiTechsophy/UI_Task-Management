import time
import pytest
from Base.DriverInitiation import Driver


@pytest.fixture(scope="class")
def beforeClass(request):
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
        driver.implicitly_wait(10)
    yield driver
    # driver.get_screenshot_as_png()
    driver.save_screenshot("/home/vipulsai/PycharmProjects/pythonProject7/screenShot/SC.png")
    time.sleep(5)
    driver.quit()


@pytest.fixture()
def beforeMethode():
    print("Before Methode")
    yield
    print("After Methode")