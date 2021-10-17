import pytest
from PageObjects.PO_nr1 import Page_Object1


@pytest.mark.usefixtures("setup")
class Test_nr1():

    @pytest.mark.parametrize('parametry',["a", "b"])
    def test_pierwszy(self, parametry):
    
        po = Page_Object1(self.driver)

        po.driver.get("https://wyborcza.pl/0,0.html")

        po.click_on_item(po.coockies)
        print(parametry)
        print(po.driver.last_request.host)
        po.quit()



        # strona = BasePage.BasePage("https://kamil.kwapisz.pl/automatyzacja-selenium/")

