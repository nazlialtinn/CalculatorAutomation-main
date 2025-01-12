Specification Heading
=====================

     
Yatirim Hesapamasi Calculator
----------------
//senaryoda yıllık basit faiz hesaplaması yapılır,
//servisten dönen yanlış cevap ile olması gereken
//sonuç karşılaştırılır ve beklenen sonuç görüntülenmezse : FAIL Basıyor
* "https://catchylabs-webclient.testinium.com/" sayfası açılır
* "nazli.altin@testinium.com" textini "username" elemente yaz
* "rewsan1907" textini "password" elemente yaz
* "login button" butonuna tıklanır
* "open calculator button" butonuna tıklanır
* Hesaplanacak degerler girilir ve hesaplanir
* 105 kontrol edilir


Aylik Butce Hesaplamasi Calculator
----------------
//senaryoda aylık bütçe hesaplaması yapılır, servisten dönen yanlış cevap ile olması gereken
//sonuç karşılaştırılır ve hata logu basılır, Burada hesaplanan değerler hatalı olduğu durumda
//senaryoyu faıl ile kesmedim, Hata LOGU bastım.
* "https://catchylabs-webclient.testinium.com/" sayfası açılır
* "nazli.altin@testinium.com" textini "username" elemente yaz
* "rewsan1907" textini "password" elemente yaz
* "login button" butonuna tıklanır
* "open calculator button" butonuna tıklanır
* Hesaplanacak degerler girilir ve hesaplanir 1000-800
* deger 200
* degerler temizlenir
* Hesaplanacak degerler girilir ve hesaplanir 1000-1000
* deger 0
* degerler temizlenir
* Hesaplanacak degerler girilir ve hesaplanir 1000-1200
* deger -200
* degerler temizlenir
* Hesaplanacak degerler girilir ve hesaplanir 2000-1000
* deger 1000
* degerler temizlenir
* Hesaplanacak degerler girilir ve hesaplanir 1500-500
* deger 1000


Kisa Vadeli Yatirim Hesaplamasi Calculator
----------------
//senaryoda kısa vadeli yatırım hesaplaması yapılır, servisten dönen yanlış cevap ile olması gereken
//sonuç hesaplanıp karşılaştırılırken Hesap Makinesi Timeout'a düşüyor.
//Hata Logu bastım ve Case'i FAIL ile kestim.
* "https://catchylabs-webclient.testinium.com/" sayfası açılır
* "nazli.altin@testinium.com" textini "username" elemente yaz
* "rewsan1907" textini "password" elemente yaz
* "login button" butonuna tıklanır
* "open calculator button" butonuna tıklanır
* 6 ay vadeli %3 faiz 500 TL
* deger 507,5
* "15" saniye bekle
* request timeout gelmediyse devam et
