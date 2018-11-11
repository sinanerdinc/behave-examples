from behave import given, when, then
import requests


@given('"{url}" adresine "{payload}" post ettiğimde')
def step_impl(context, url, payload):
    try:
        context.request = requests.post(url, data=payload)
    except Exception as e:
        print(e)


@then('Dönen değer içerisinde "{search}" olduğunu görmeliyim')
def step_impl(context, search):
    assert search in context.request.json()["data"], "Aranan değer, dönen sonuç içerisinde bulunamadı."

