Feature: Sayfaların başarıyla açılıp açılmadığını kontrol eder.

  Scenario: Tek bir sayfanın kontrolü
      Given   "https://httpbin.org/status/200" adresine GET isteği gönderdiğimde
      When    Geri dönen değerleri kontrol ettiğimde
      Then    status code değerinin "200" olduğunu görmeliyim

  Scenario Outline: Birden çok sayfanın kontrolü
      Given   "<url>" adresine GET isteği gönderdiğimde
      When    Geri dönen değerleri kontrol ettiğimde
      Then    status code değerinin "<status_code>" olduğunu görmeliyim

    Examples: Kategoriler
      | url                                  | status_code |
      | https://httpbin.org/status/200       | 200         |
      | https://httpbin.org/status/300       | 300         |
      | https://httpbin.org/status/404       | 404         |
