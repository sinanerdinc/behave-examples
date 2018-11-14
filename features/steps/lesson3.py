from behave import *


@given('anasayfaya gittiğimde')
def step_impl(context):
    context.browser.get(context.HOMEPAGE)


@given('"{category_name}" kategorisine gittiğimde')
def step_impl(context, category_name):
    context.browser.get(context.CATEGORIES[category_name])


@when('son yazının detayına tıkladığımda')
def step_impl(context):
    context.browser.find_element_by_css_selector('body > div > div > div > div > article:nth-child(1) > a > h2').click()


@then('yazının başlığı "{title}" olmalı')
def step_impl(context, title):
    site_title = context.browser.find_element_by_css_selector('body > header > div > div > div > div > div > h1').text
    assert title == site_title, "Yazının başlığı beklenen değer değil."

