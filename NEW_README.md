## Sportsy
***

### 1. [Функціонал](#1-функціонал)
1. [Реєстрація](#11-реєстрація) 
   * [Початкова реєстрація](#111-початкова-реєстрація)
   * [Реєстрація автора](#112-реєстрація-автора)
   * [Підтвердження пошти або телефону](#113-підтвердження-пошти-або-телефону)
2. [Аутентифікація](#12-аутентифікація)
3. [Авторизація](#13-авторизація)
4. [Типи користувачів](#14-типи-користувачів)
5. [Функціонал для автора](#15-функціонал-для-автора)
   * [Пости](#151-пости)
   * [Колекції](#152-колекції)
   * [Підписки](#153-підписки)
   * [Збори](#154-збори)
   * [Аналітика](#155-аналітика)
   * [Налаштування](#156-налаштування)
6. [Функціонал для користувача](#16-функціонал-для-підписника)
   * [Пошук авторів](#161-пошук-авторів)
   * [Підписка](#162-підписка)
   * [Перегляд постів](#163-перегляд-постів)
   * [Донати на збори](#164-донати-на-збори)
   * [Купівля колекцій](#165-купівля-колекцій-)
   * [Налаштування](#166-налаштування)
   * [Сторінка загального контенту](#167-сторінка-загального-контенту)
7. [Функціонал для гостя](#17-функціонал-для-гостя)
   * [Пошук авторів](#171-пошук-авторів)
   * [Реєстрація](#172-реєстрація)
8. [Відновлення пароля](#18-відновлення-пароля)


### 2. [Адмін панель](#2-адмін-панель)
   * [Управління користувачами]()
   * [Управління постами]()
   * [Управління ]()


### 3. [Схема бази данних](#3-схема-бд)


### 4. [Пропонований стек технологій](#4-пропонований-стек-технологій)


### 5. [Вимоги до дезайну](#5-вимоги-до-дизайну)

## 1. Функціонал
### 1.1 Реєстрація
(убрати пункт реєстрація автора она переходить сюда)
***
#### 1.1.1 Початкова реєстрація
Під початковою реєстрацією мається на увазі реєстрація першого облікового запису на платформі
тобто гість який захоче зареєструватися буде проходити реєстрацію спочатку як підписник, а потім 
вже буде мати можливість приєднатися як автор.

Тут будуть приставленні не всі таблиці, у користувача та автора буде більше.
Ознайомитись з повною базою ви можете в розділі ["Схема БД"](#2-схема-бд).

Початкова реєстрація проходить лише як для підписника.
Вони будуть вводити такі дані у вікні реєстрації: username - обов'язкове поле,
email або phone_number - одне із полів обов'язкове, на вибір.

#### 1.1.2 Реєстрація автора
Різниці між таблицею автора та таблицею підписника не буде за виключенням True або False
в полі is_creator. Коли це поле буде переходити в True для автора будуть створені такі таблиці:

* creator_profile_info {}
* creator_settings {}


Після реєстрації, користувач може стати автором, одразу після реєстрації натиснувши
на кнопку "Приєднатися як автор" в привітальному вікні що буде одразу після реєстрації.
Після натискання на кнопку "Приєднатися як автор", користувача перенаправлено
у вікно "Реєстрація автора".

Якщо користувач не натиснув кнопку "Приєднатися як автор" 
в привітальному вікні реєстрації то він не зможе більше зареєструватися як автор.
// Зроблено це по причинах особливості системи.

#### 1.1.3 Підтвердження пошти або телефону

Користувач може підтвердити пошту в "Налаштування профілю"(посилання на пункт 1.5.6), 
натиснувши на кнопку "Підвередити пошту" або "Підвередити номер телефону" під відповідними полями.

Після натискання на кнопку на email надходить лист з посиланням, 
або на мобільний телефон надходить сповіщення з посиланням для підтвердження, 
яким він може скористатися та увійти підтвердивши пошту, або телефон.

### 1.2 Аутентифікація
***
Загалом буде 3 можливості аутентифікації ('Google Oauth2', 'Password auth', 'OTP auth').

Перший спосіб за допомогою Google - тобто користувач у вікні аутентифікації
вводить пошту та після цього аутентифікується за допомогою перевірки Google.

Другий спосіб за допомогою пошти та паролю або телефону та паролю - користувачу
потрібно ввести логін та пароль після чого користувача аутентифіковано.

Третій спосіб за допомогою одноразового пароля - користувач вводить пошту в вікні після
чого на пошту відправляється одноразовий пароль з яким користувач може увійти за вздовж 5 хвилин.
### 1.3 Авторизація
***
Авторизація буде проходити через JWT - 'Jason Web Token'.

Одразу після аутентифікації в headers(заголовки) буде вноситись Token.
Приклад заголовка:
```
Authorization: Bearer eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJzdWIiOiAiMTIzNDU2Nzg5MCIsICJuYW1lIjogIkpvaG4gRG9lIiwgImlhdCI6IDE1MTYyMzkwMjJ9.rqqegcZ-W3UdYfV50fcjW7k8eX3ZIe8TWyC5U0HJ6kw
```
За допомогою цього токену буде відбуватися подальша авторизація користувача.

Які саме поля будуть знаходитись в токені треба буде ще вирішити. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

### 1.4 Типи користувачів
***
Програма передбачає 3 типи користувача Підписник, Автор, Гість.
Гість повинен мати мінімум можливостей для того, щоб він був вимушений реєструватися.

1. Підписник(споживач контенту) це користувач який буде куплять на нашому сервісі.
2. Автор це людина яка буде створювати контент на платформі.
3. Гість не авторизований користувач з мінімумом можливостей.


### 1.5 Функціонал для автора
***
#### 1.5.1 Пости
1. Створення постів - Пости автор буде створюватись після натиску на кнопку "Створити пост".

Після натиску на кнопку "Створити пост" автора буде переадресовано на спеціальну сторінку для 
створення постів. На цій сторінці буде невеликий редактор для тексту, можливість задати до
якої підписки цей пост належить, завантажувати фотографії до посту та яка буде ціна самого посту.

Коли Автор натискає на кнопку завантажити пост його буде перенаправлено на свою сторінку де буде показано
як той пост завантажується.


2. Редагування постів - Редагувати пости автор може на пряму з головної сторінки.

На головній сторінці під кожним з постів буде знаходитись кнопка натиск на яку буде 
перенаправляти на сторінку редагування постів (та сама сторінка на якій створюються пости)
де автор зможе змінити текст, фото чи відео. 

Після того як автор відредагує пост під постом для користувачів котрі мають підписку
або купили пост буде підпис біля посту відредаговано (Як в телеграмі)

3. Видалення постів - Архівація постів.

Видалення посту буде формальністю тобто з бази сам пост не буде видалятися пост 
буде переходити в стан is_deleted=True. Потрібно буде це для того, щоб користувач 
який купив пост напряму, або купив колекцію в якій був пост все ще мав доступ до 
контенту який придбав.

Також всі видалені пости будуть зберігатися в автора як архівовані та в будь-який
момент автор зможе розархівувати пост після чого він стане доступним для всіх.

#### Обкладинка посту
Обкладинка посту буде відображати Фотографію або обкладинку з відео та невиличкий текст в 
100 - 150 символів з надписом "читати далі..." якщо рівень підписки користувача не достатній на посту буде 
написано що пост заблоковано, при натисканні на надпис буде вилазити повідомлення "Не достатній рівень підписки."
якщо ж користувач має достатній рівень підписки його буде перенаправленно на сторінку з окремим постом.
``` text
"Якщо в автора діє звичайний план, то на платформі він може зберігати до 50 гб відео в форматі FullHD"
\\ Подумати с приводу планів для автора 
```

#### 1.5.2 Колекції
Чи буде це набір унікальних постів доступних лише для тих хто буде купувати колекцію

#### 1.5.3 Підписки
Підписки створювати зможе автор у відділі "підписки" на головному екрані.
Створити можна буде до 3 підписок.

Редагування таких полів буде дозволено при створенні або подальшому редагуванню підписки:
* name: назва підписки.
* price: ціна підписки.
* roll_name: назва ролі яку буде отримувати користувач після підписки: по типу - "спортхер". 
* bref_description: коротка фраза яка буде описувати плюси підписка, відображатиметься під підпискою.
* is_archived: чи архівовано.

Підписка буде надавати доступ до контенту який буде прив'язаним до неї автором.

Видалити підпису буде не можливо, можливо буде лише архівувати її у відділі "підписки"
на головному екрані в редакторі підписок та перед архівацією підписки треба буде
прив'язати всі пости які були до неї прив'язані до іншої підписки.

Після видалення у користувачів які купили підписку буду залишатися контент прив'язаний
до підписки до закінчення дії підписки(приблизно 30 днів з дня купівлі).
Після закінчення підписки користувачу буде зарекомендовано купити іншу підписку.


#### 1.5.4 Збори
Автор може почати збір на якусь ціль(наприклад мікрофон). Створити цю ціль він може
в вкладці "Цілі". Створення ціх цілей буде відбуватися в редакторі схожим на редактор
дял постів(посилання на 1.2.1).

При створенні або редагуванні можна буде задати такі поля:
* fundraising_name: назва цілі на яку буде йти збір.
* amount: сума яку треба зібрати.
* description: опис збору.
* message: сповіщення яке буде відображатись після того, як підписник задонатить.

Редагування буде доступно при натиску на кнопку редагування яка буде знаходитись
під збором. Також буде можливість закрити збір в будь-який момент.

#### 1.5.5 Аналітика
Аналітика буде містити дохід за підписки, колекції та збори. Також суму підписок за певний час.

Знаходитись вся аналітика буде в вкладці "Аналітика" на боковій панелі. Там автор зможе дивитися
свої доходи за місяць, рік, та за весь час. Аналітика за весь час буде відображатися в місяцях.
Якщо автор не має прибутків там буде відображатися надпис "Поки в вас не має прибутків".

Сама аналітика буде відображатися в стовпчиках, стовпчики будуть відображати прибуток за
місяць - 1 стовпчик=неділя, рік - 1 стовпчик=Місяць та за весь час - 1 стовпчик=Місяць.

#### 1.5.6 Налаштування
В налаштування профілю автор буде мати можливість змінити 2 типи даних: дані профілю та
налаштування сайту(повідомлення. тема сайту, Мова, ...).

1. Редагування профілю:
Налаштування профілю це налаштування які будуть належати до публічних даних таких 
як(біо, назва проєкту, слоган, Країна, ...) та особистих даних (пошта, номер телефону, ,,,)

Налаштування буде відбуватись в вкладці "Налаштування профілю" яка буде знаходитись на бокової панелі.

2. Редагування сервісу:
Налаштування сервісу це налаштування які будуть належати до таких даних 
як(повідомлення, тема сайту, Мова, ...)

### 1.6 Функціонал для Підписника
***
#### 1.6.1 Пошук авторів
Пошук авторів буде знаходитись в горі бокової панелі. Сама сторінка пошуку буде виглядати 
як вікно дл пошуку під яким будуть різні фільтри по типу "Вид спорту', "Країна", "Мова", ... 

Після натиску на кнопку пошуку підписнику буде відображатися всі автори схожі на запит.
Якщо збігів не було знайдено підписник буде отримувати відповідь з надписом 
"На жаль нам не вдалось знайти нікого за вашим запитом"

#### 1.6.2 Підписка
Купити підписку можна лише на сторінці автора.
Видалити або скасовувати підписку підписник зможе в вікні налаштуваннях в розділі "підписки".

Кошти за підписку будуть зніматися кожного місяця автоматично. Якщо на карті користувача не
достатньо коштів тоді сервіс буде знімати 1 раз на день впродовж 5 днів та якщо кошти так і не
вдалось зняти підписка буде скасована.

#### 1.6.3 Перегляд постів
В системі буде 2 способи подивитися пости.

1 спосіб: підписник повинен перейти на головний екран з новими постами
де будуть відображатись нові доступні пости на які підписник має підписку.

2 спосіб: підписник може перейти на сторінку автора де будуть відображатися
пости за його підпискою та пости за якими в нього не має підписки в вигляді 
постів з такою ж самою обкладинкою, але з підписом про те що пост заблоковано.
При натисканні на заблокований пост користувача буде запропоновано оновити 
підписку до підписки з відповідним дозволом. Детальніше про те що таке 
обкладинка посту можна ознайомитись в розділі [Обкладинка посту](#обкладинка-посту).

Для кожного зі способів перегляду постів повинна бути можливість фільтрувати пости.
Будуть доступні декілька видів фільтрів.
* Пости тільки за підпискою
* Найпопулярніші
* Найновіші
* ... ? чи потрібно взагалі додавати фільтри?

#### 1.6.4 Донати на збори
Переказати кошти підписник зможе натиснувши на збір який буде відображатися на боковій 
панелі на сторінці автора. Задонатити автору підписник може будь-яку суму та тим самим
закрити збір. Після оплати буде відображатися повідомлення яке задав автор збору.

Заданатити на збір який вже закінчено не можливо. Він просто буде відображатися на
боковій панелі. Активні збори в горі, а ті які вже закриті знизу.

#### 1.6.5 Купівля колекцій 
Таблиця збору буде мати такі поля: | почитати як буде проводитись оплата

Купівля колекцій буде можлива при переході до вкладки колекції у автора.
Користувач буде бачити невеликий опис цієї колекції. Щоб отримати постійний 
доступ до контенту колекції підписник має її купити.

Після чого залишається в підписника на завжди навіть якщо колекція була архівована.

#### 1.6.6 Налаштування.
В налаштування профілю підписник буде мати можливість змінити 2 типи даних: дані профілю та
налаштування сайту(повідомлення. тема сайту, Мова, ...).

1. Редагування профілю:
Налаштування профілю це налаштування які будуть належати до публічних даних таких 
як(гендер, пошта, країна, ім'я, номер телефону)

Налаштування буде відбуватись в вкладці "Налаштування профілю" яка буде знаходитись на бокової панелі.

2. Редагування сервісу:
Налаштування сервісу це налаштування які будуть належати до таких даних 
як(повідомлення, тема сайту, Мова, повідомлення про новий пост)

#### 1.6.7 Сторінка загального контенту
Сторінка загального контенту буде мати в собі нові пости від авторів на які підписний 
користувач. Користувач буде мати можливість фільтрувати пости за критеріями: 
* "Найновіші"
* "Всі", "За моєю підпискою" або "безкоштовні"
* "Найпопулярніші"

Вона мається на увазі як, наприклад головна сторінка інстаграму.

### 1.7 Функціонал для гостя
***
Гість це користувач сервісу який або не авторизований або не має облікового запису на платформі.

#### 1.7.1 Пошук авторів
Пошук авторів для гостя буде відбуватися таким самим чином як для [зареєстрованого користувача](#161-пошук-авторів).

#### 1.7.2 Реєстрація
Реєстрація буде відбуватися або по власній ініціативі користувача який може натиснути
на кнопку реєстрації в правій верхній частині екрана натиснувши на кнопку 
"Зареєструватися або увійти". Або коли гість захоче підписатися на автора його
буде перенаправлено до вікна [Реєстрації](#11-реєстрація) або [Входу](#13-авторизація).

### 1.8 Відновлення пароля
Відновити пароль користувач зможе на сторінці входу в профіль натиснувши на кнопку
"Забув пароль" після чого система попросить ввести пошту або телефон профілю від якого
було утрачено пароль. Після користувач повинен натиснути кнопку "Відновити пароль".

Одразу ж буде відправлено посилання яке діятиме не більше 10 хвилин на пошту або 
смс з посиланням на телефон. При переході на посилання користувач буде бачити сторінку 
на якій його попросять ввести новий пароль та підтвердити його. Після натискання на 
кнопку "Встановити новий пароль" користувача буде переадресовано на сторінку входу. 

Якщо користувач перейде за посиланням через 10 хвилин або більше,
буде виведена сторінка з текстом "Url відновлення не дійсний".

### 2. Адмін панель
Адмін панель буде великою окремою системою управління проєктом для Product owner(Власника проекту)

#### 2.1 Управління користувачами
#### 2.2 Управління 

## 3. Схема БД
Таблиця підписника та автора буде мати такі поля:
* uuid: int primary key (унікальний ключ uuid)
* username: varchar (нікнейм)
* password: varchar (пароль зберігатися буде хешованим)
* avatar: varchar (аватар користувача)
* email: varchar (електрона пошта)
* is_confirmed_email: bool (чи підтверджена пошта)
* is_active: bool (чи активний користувач)
* is_staff: bool (чи є користувач робітником сайту)
* is_creator: bool (чи є користувач автором)
* last_login: timestamp (остання дата входу)
* data_join: timestamp (час створення)
* updated_at: timestamp (час оновлення)

Таблиця підписки буде мати такі поля:
* id: int primary key(унікальний ключ)
* author_id: int foreign key (id автора)
* name: varchar (назва)
* price: positive int (ціна)
* roll_name: varchar (назва ролі яку буде отримувати користувач після підписки: по типу - "спортхер".) 
* bref_description: varchar (коротка фраза яка буде описувати плюси підписка, відображатиметься під підпискою)
* is_archived: bool = False (чи архівовано)
* is_archive_time: timestamp (час архівації)
* created_at: timestamp (час створення)

Таблиця посту буде мати такі поля:
* id: int primary key(унікальний ключ)
* author_id: int foreign key (id автора)
* title: varchar (заголовок)
* content: text (тіло)
* img_url: varchar (url фотографії) ||||? почитати як зберігати фотографії ! 
* is_archived: bool = False (чи було архівовано)
* archived_time: timestamp (час коли було архівовано)
* created_at: timestamp (час створення)
* updated_at: timestamp (час оновлення)

### Приклад !!!!!!!!!!!!
### [Схема бази](https://dbdiagram.io/d/65152138ffbf5169f0a6f384)
[![diagram](https://i.postimg.cc/YCKPM7xr/Screenshot-from-2023-10-07-14-00-15.png)](https://postimg.cc/YhRRzJVZ)




6. Функціонал оплати підписки або одноразової оплати та головна сторінка 
8. Функціонал інтеграції з Telegram 
9. Сповіщення

# 4. Пропонований стек технологій

Для реалізації системи пропонується наступний стек технологій:

* Бекенд:
     - Мова Python3.10
     - Фреймворк Django + Django-rest-framework
     - БД PostgreSQL, Redis
     - Celery for background tasks
     - Docker + Docker Compose
     - Aiogram для інтеграції з Telegram
     - PyTests 
* Фронтенд:
     - React
     - JavaScript

Для інтернет-еквайрингу розглядаються Paypall та CloudPayments,
у ході проекту треба порівняти технічні можливості платформ та комісії
за платежі. Важливо мати можливість оплати з Google Pay та Apple Pay, у тому
числі рекурентні платежі (якщо Google Pay та Apple Pay дозволяють таке
робити, уточнити під час проекту). Важливо відкрити в еквайрингу інші країни
для можливості приймання оплати не лише з UA, а й з інших країн. 
Обговорити це під час проекту з еквайрингом.

Зберігання файлів та зображень, що завантажуються автором, має здійснюватися
в S3-сумісному сховищі.


# 5. Вимоги до дизайну

Мінімалізм, лаконічність, акцент на контенті. Білий фон. Повинен бути присутнім
логотип системи з права в горі на сторінці.

У нижній частині сторінки має бути написано:

"Way to Bentley".
