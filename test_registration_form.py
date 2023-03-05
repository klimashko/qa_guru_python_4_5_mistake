from selene.support.shared import browser
from selene import be, have
import pytest
import time

#browser.config.hold_browser_open("true")
browser.open('https://demoqa.com/automation-practice-form')
browser.element('[id="firstName"]').should(be.blank).type('John')
browser.element('[id="lastName"]').should(be.blank).type('Smith')
browser.element('[id="userEmail"]').should(be.blank).type('john_smith_980yt304gy@gmail.com')
browser.element('[for = "gender-radio-1"]').click()
browser.element('[id="userNumber"]').should(be.blank).type('9079079079')
time.sleep(5)
browser.element('[id="dateOfBirthInput"]').send_keys()
browser.element('[class="react-datepicker__year-select"]').click()
time.sleep(5)
browser.element('[value="1986"]').click()
#value="1986"
browser.element('[class="react-datepicker__month-select"]').click()
browser.element('[value="5"]').click()

time.sleep(10)

#browser.driver.execute_script('window.scrollBy(0, 500)')
