from selenium import webdriver
from behave import *

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Firefox()
    context.browser.get('driver')


@given('I am on the blog page')
def step_impl(context):
    context.browser = webdriver.Firefox()
    context.browser.get('driver/blog')


@then('I am on the blog page')
def step_impl(context):
    expected_url = 'driver/blog'
    assert context.browser.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    expected_url = 'driver/'
    assert context.browser.current_url == expected_url
