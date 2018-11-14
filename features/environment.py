# def before_all(context):
#     print("Before All")
#
#
# def before_feature(context, feature):
#     print("Before Feature")
#
#
# def before_scenario(context, scenario):
#     print("Before Scenario")
#
#
# def after_scenario(context, scenario):
#     print("After scenario")
#
#
# def after_feature(context, feature):
#     print("After Feature")
#
#
# def after_all(context):
#     print("After All")


# Selenium
# from selenium import webdriver
#
#
# def before_feature(context, feature):
#     context.browser = webdriver.Chrome()
#     context.HOMEPAGE = "https://www.sinanerdinc.com"
#     context.CATEGORIES = {
#         "python": context.HOMEPAGE + "/python",
#         "linux": context.HOMEPAGE + "/linux"
#     }
#
#
# def after_feature(context, feature):
#     context.browser.quit()
