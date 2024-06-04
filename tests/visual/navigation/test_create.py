# tests/navigation/test_create.py

import pytest
from tests.helpers.selenium_helpers import find_elements, assert_elements_present

def test_custom_swim_navigation(driver):
    custom_swim_buttons = find_elements(driver, "//*[contains(text(), 'custom-swim-ctnr')]")
    assert_elements_present(custom_swim_buttons, "No 'custom-swim-ctnr' elements found")

    custom_swim_buttons[0].click()

    custom_swim_session_text = find_elements(driver, "//*[contains(text(), 'Custom Swim Session')]")
    assert_elements_present(custom_swim_session_text, "'Custom Swim Session' text not found")

def test_custom_swim_navigation1(driver):
    custom_swim_buttons = find_elements(driver, "//*[contains(text(), 'custom-swim-ctnr')]")
    assert_elements_present(custom_swim_buttons, "No 'custom-swim-ctnr' elements found")

    custom_swim_buttons[0].click()

    custom_swim_session_text = find_elements(driver, "//*[contains(text(), 'Custom Swim Session asdfds')]")
    assert_elements_present(custom_swim_session_text, "'Custom Swim Session' text not found")

def test_custom_swim_navigation2(driver):
    custom_swim_buttons = find_elements(driver, "//*[contains(text(), 'custom-swim-ctnr')]")
    assert_elements_present(custom_swim_buttons, "No 'custom-swim-ctnr' elements found")

    custom_swim_buttons[0].click()

    custom_swim_session_text = find_elements(driver, "//*[contains(text(), 'Custom Swim Session')]")
    assert_elements_present(custom_swim_session_text, "'Custom Swim Session' text not found")