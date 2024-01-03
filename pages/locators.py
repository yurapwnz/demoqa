from selene import by


class TestBoxPageLocators():
    FULL_NAME_FIELD = by.id('userName')
    EMAIL_FIELD = by.id('userEmail')
    CURRENT_ADDRESS_FIELD = by.id('currentAddress')
    PERMANENT_ADDRESS = by.id('permanentAddress')
    SUBMIT_BUTTON = by.id('submit')
    OUTPUT_FORM = by.id('output')
    OUTPUT_NAME = by.id('name')
    OUTPUT_EMAIL = by.id('email')
    OUTPUT_CURRENT_ADDRESS = by.css("p[id='currentAddress']")
    OUTPUT_PERMANENT_ADDRESS = by.css("p[id='permanentAddress']")

