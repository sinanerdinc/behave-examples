from behave import given, when, then
import requests


@given('"{url}" adresine GET isteği gönderdiğimde')
def step_impl(context, url):
    context.request = requests.get(url)
    assert context.request.status_code is not None, "GET isteği atılamadı."


@when('Geri dönen değerleri kontrol ettiğimde')
def step_impl(context):
    assert context.request.status_code is not None, "HTTP isteği sonucunda status code dönmedi"


@then('status code değerinin "{status_code}" olduğunu görmeliyim')
def step_impl(context, status_code):
    assert context.request.status_code == int(status_code), "Beklenen status kod degeri yanlış."
