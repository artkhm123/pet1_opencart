<h1>Opencart ui testing</h1>

Этот репозиторий создан для практики автоматизации тестирования UI приложения 
https://demo.opencart.com/

Приложение запускается в докере.


<h2>Параметры запуска</h2>

    --browser - выбор браузера 
                choices = ["chrome", "firefox", "yandex", "MicrosoftEdge"]
    --drivers - путь до веб драйверов
    --url - URL тестового приложения
    --headless - для запуска тестирования в headless режиме
    --log_level" - выбор уровня логирования 
                default="DEBUG", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    --browser - выбор браузера
                default="chrome", choices=["chrome", "ff", "firefox", "yandex", "ya", "MicrosoftEdge"]
    --drivers - путь до веб драйверов
    --url - URL тестового приложения
    --headless - без отрисовки браузера
                default=False
    --log_level - уровень логирования 
                default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    --executor - выполняются тесты локально или удаленно
                default="192.168.31.28 (возможен запуск local)


    
<h2>Маркеры тестов</h2>

    slow : this is slow tests
    #TODO домаркировать оставшиеся тесты
    smoke : this mark is for smoke run
    regress : this is for regress ran
    

<h2>ПРИМЕЧАНИЕ!</h2>
<p>Загрузка некоторых страниц, таких как "Cтраница продукта" может происходить очень долго (до 30-40 сек).
Это связано с подгрузкой виджетов с заблокированных в РФ ресурсов (Facebook, Twitter и тд).
<p>В связи с этим тесты 
    
    test_product_card_page.py
    test_currency_change.py 
выполняются очень долго. В FireFox тесты вообще не завешаются.
<p>Для того что бы пропустить данные тесты - при запуске используйте параметр 
    
    -m "not slow"


<h2>Распаралеливание запусков тестов</h2>
Распаралеливание осуществляется с помощью плагина pythest-xdist.
Для запуска в несколько потоков при запуске необходимо прописать аргумент -n и количество потоков
    
    -n 4
