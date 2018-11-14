Feature: Selenium örneği

  Scenario: Sinanerdinc.com anasayfa testleri.
    Given   anasayfaya gittiğimde
    When    son yazının detayına tıkladığımda
    Then    yazının başlığı "Python Selenium Modülü Kullanımı Ders 1" olmalı

  Scenario: Sinanerdinc.com linux kategorisi testleri.
    Given   "linux" kategorisine gittiğimde
    When    son yazının detayına tıkladığımda
    Then    yazının başlığı "Jq Paketi Kullanımı" olmalı
