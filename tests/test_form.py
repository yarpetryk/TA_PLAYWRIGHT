import pytest

from helpers.GenerateData import GenerateUser
from pages.home_pages import HomePage


faker = GenerateUser()
faker_data = [faker.first_name(),
              faker.address(),
              faker.zip_code(),
              faker.city(),
              faker.phone_number(),
              faker.email(),
              faker.birth_day()]
response_text = 'Thank you very much'

@pytest.mark.form
def test_apply_form(fill_form: HomePage) -> None:

    # Go to form page
    fill_form.load()

    # Apply the form
    fill_form.apply_form(*faker_data)

    # Assert the form result
    assert fill_form.check_result(response_text)
