import pytest
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(request):
    
    from seleniumwire import webdriver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    request.cls.driver = driver

