from .base_page import BasePage
from .locators import TestBoxPageLocators
from faker import Faker


class TextBoxPage(BasePage):
    fake = Faker('ru_RU')

    fullname = fake.name()
    email = fake.email()
    cur_address = fake.address()
    per_address = fake.address()

    def submit_with_all_field(self):
        self.input_fullname()
        self.input_email()
        self.input_cur_address()
        self.input_per_address()
        self.click_to_submit()
        self.should_be_output()
        self.fullname_equal_on_output()
        self.email_equal_on_output()
        self.cur_address_equal_on_output()
        self.per_address_equal_on_output()

    def input_fullname(self, fullname=fullname):
        fullname_field = self.browser.find_element(*TestBoxPageLocators.FULL_NAME_FIELD)
        print(fullname)
        fullname_field.send_keys(fullname)

    def input_email(self, email=email):
        fullname_field = self.browser.find_element(*TestBoxPageLocators.EMAIL_FIELD)
        print(email)
        fullname_field.send_keys(email)

    def input_cur_address(self, cur_address=cur_address):
        fullname_field = self.browser.find_element(*TestBoxPageLocators.CURRENT_ADDRESS_FIELD)
        print(cur_address)
        fullname_field.send_keys(cur_address)

    def input_per_address(self, per_address=per_address):
        fullname_field = self.browser.find_element(*TestBoxPageLocators.PERMANENT_ADDRESS)
        print(per_address)
        fullname_field.send_keys(per_address)

    def click_to_submit(self):
        submit_button = self.browser.find_element(*TestBoxPageLocators.SUBMIT_BUTTON)
        submit_button.click()

    def should_be_output(self):
        assert self.is_element_present(*TestBoxPageLocators.OUTPUT_FORM)

    def fullname_equal_on_output(self, fullname=fullname):
        output_name = self.browser.find_element(*TestBoxPageLocators.OUTPUT_NAME).text
        assert fullname in fullname, f"Output name {output_name} is not equal {fullname}"

    def email_equal_on_output(self, email=email):
        output_email = self.browser.find_element(*TestBoxPageLocators.OUTPUT_EMAIL).text
        assert email in output_email, f"Output email {output_email} is not equal {email}"

    def cur_address_equal_on_output(self, cur_address=cur_address):
        output_cur_address = self.browser.find_element(*TestBoxPageLocators.OUTPUT_CURRENT_ADDRESS).text
        print('dfdf'+output_cur_address)
        assert cur_address in output_cur_address, f"Output cur_address {cur_address} is not equal {output_cur_address}"

    def per_address_equal_on_output(self, per_address=per_address):
        output_per_address = self.browser.find_element(*TestBoxPageLocators.OUTPUT_PERMANENT_ADDRESS).text
        assert per_address in output_per_address, f"Output per_address {per_address} is not equal {output_per_address}"
