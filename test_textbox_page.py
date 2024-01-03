from .pages.textbox_page import TextBoxPage


def test_submit_with_all_field(browser):
    link = "https://demoqa.com/text-box"
    page = TextBoxPage(browser, link)
    page.open()
    page.submit_with_all_field()
