from playwright.sync_api import Page, expect
from pages.locators import FormLocators
import allure


class HomePage():

    URL = 'https://fd7.formdesk.com/demo/application2'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.gender = page.locator(FormLocators.GENDER)
        self.name = page.locator(FormLocators.NAME)
        self.address = page.locator(FormLocators.ADDRESS)
        self.zipcode = page.locator(FormLocators.Zipcode)
        self.city = page.locator(FormLocators.CITY)
        self.phone = page.locator(FormLocators.PHONE)
        self.email = page.locator(FormLocators.EMAIL)
        self.birth = page.locator(FormLocators.BIRTH)
        self.submit = page.locator(FormLocators.SUBMIT)
        self.result = page.locator(FormLocators.RESULT)

    @allure.step('And load page')
    def load(self) -> None:
        self.page.goto(self.URL)

    @allure.step('And apply form')
    def apply_form(self, name, address, zipcode, city, phone, email, birth) -> None:
        self.gender.click()
        self.name.fill(name)
        self.address.fill(address)
        self.zipcode.fill(zipcode)
        self.city.fill(city)
        self.phone.fill(phone)
        self.email.fill(email)
        self.birth.fill(birth)
        self.submit.click()

    @allure.step('And check result')
    def check_result(self, text):
        expect(self.result).to_contain_text(text)
        return True
