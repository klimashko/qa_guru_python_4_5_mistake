import os

from selene.support.shared import browser
from selene import be, have
import pytest
import time


def test_reg_form(browser_management):
    browser.open('/')
    browser.element('#firstName').should(be.blank).type('John')
    browser.element('[id="lastName"]').should(be.blank).type('Smith')
    browser.element('[id="userEmail"]').should(be.blank).type('john_smith_980yt304gy@gmail.com')
    browser.element('[for = "gender-radio-1"]').click()
    browser.element('[id="userNumber"]').should(be.blank).type('9079079079')
    #time.sleep(3)
    browser.element('[id="dateOfBirthInput"]').send_keys()
    browser.element('[class="react-datepicker__year-select"]').click()
    #time.sleep(3)
    browser.element('[value="1986"]').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('[value="5"]').click()
    browser.element('[aria-label="Choose Sunday, June 15th, 1986"]').click()
    #time.sleep(3)

    browser.driver.execute_script('window.scrollBy(0, 500)')
    browser.element('[id="subjectsInput"]').should(be.blank).type('m')
    #time.sleep(3)
    browser.element('[tabindex="-1"]').click()
    time.sleep(3)
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    time.sleep(3)
    picture_adress = os.getcwd()+'IMG_20230224_164633_1.jpg'
    print(picture_adress)
    #browser.element('[id="uploadPicture"]').double_click()
    #browser.element('[id="uploadPicture"]').send_keys(os.getcwd()+'IMG_20230224_164633_1.jpg')
    time.sleep(3)


#"C:\Users\klima\PycharmProjects\qa_guru_python_4_5\tests\IMG_20230224_164633_1.jpg"
# browser.driver.execute_script('window.scrollBy(0, 500)')

