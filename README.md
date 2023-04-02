<h1>Opencart ui testing</h1>

Этот репозиторий создан для практики автоматизации тестирования UI приложения 
https://demo.opencart.com/
и API тестирования приложения https://jsonplaceholder.typicode.com/

Для запуска тестов необходимо: 

    развернуть приложение opencart
    развернуть selenoid

<h2>Параметры запуска тестов</h2>

    --browser   - выбор браузера для UI тестов
                    default="chrome", 
                    choices=["chrome", "ff", "firefox", "yandex", "ya", "MicrosoftEdge"]
    --drivers   - путь до веб драйверов
    --url       - URL тестового приложения для UI тестов. default="http://192.168.31.28:8081"
    --api_url   - URL тестового приложения для API тестов. default="https://jsonplaceholder.typicode.com/"
    --headless  - запуск без отрисовки браузера
    --log_level - уровень логирования 
                    default="INFO", 
                    choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    --executor  - выполняются тесты локально или удаленно
                    default="192.168.31.28 (возможен запуск local)


    
<h2>Маркеры тестов</h2>

    slow : this is slow tests
    smoke : this mark is for smoke run
    regress : this is for regress ran
    api: api tests
    ui: ui tests
    

<h2>ВАЖНО! ОБРАТИ ВНИМАНИЕ!</h2>
<p>Загрузка некоторых страниц, таких как "Cтраница продукта" может происходить очень долго (до 30-40 сек).
Это связано с подгрузкой виджетов с заблокированных в РФ ресурсов (Facebook, Twitter и тд).
<p>В связи с этим тесты 
    
    test_product_page_add_to_cart.py/test_product_card_page.py
    tests/test_product_page_currency_change.py
выполняются очень долго. В FireFox тесты вообще не завешаются.
<p>Для того что бы пропустить данные тесты - при запуске используйте параметр 
    
    -m "not slow"


<h2>Распаралеливание запусков тестов</h2>
Распаралеливание осуществляется с помощью плагина pythest-xdist.
Для запуска в несколько потоков при запуске необходимо прописать аргумент -n и количество потоков
    
    -n 4

<h2>Контейнеризация</h2>
Так же можно упаковать тесты в докер контейнер с помощью команды:

    docker build -t tests

И запускать тесты из контейнера со всеми поддерживаемыми параметрами:
    
    docker run --name tests_run --network selenoid tests -m "not slow"
    
Для просмотра отчета о тестировании при запуске из контейнера:
    
    docker cp tests_run:/app/allure-report . \
    && allure serve allure-report
