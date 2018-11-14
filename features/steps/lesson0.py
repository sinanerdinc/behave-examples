from behave import given, when, then


@given('eve gittiğimde')
def step_impl(context):
    pass


@when('buzdolabını açtığımda')
def step_impl(context):
    pass


@then('1 tencere yemek görmeliyim')
def step_impl(context):
    pass


# 1 tencere yerine dinamik birşeyler yapabilir miyiz?
# When ile yazılan bir adımı aynı anda then ile de kullanabilir miyim?
# Adımlar arasına yorum yazabilir miyim?
# Bir adım içinde farklı bir adımı çalıştırma? context.execute_steps("When buzdolabını açtığımda")
# Etiket ekleyebiliyor muyuz? --tags=test
# Desteklenen diller? behave --lang-list , # language: de
