Feature: Sayfaların başarıyla açılıp açılmadığını kontrol eder.

  Scenario: Post Etme Testi
    Given   "http://httpbin.org/post" adresine "{'name':'sinan'}" post ettiğimde
    When    Geri dönen değerleri kontrol ettiğimde
    Then    status code değerinin "200" olduğunu görmeliyim
    Then    Dönen değer içerisinde "sinan" olduğunu görmeliyim