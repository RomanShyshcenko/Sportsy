# Sportsy
***
## 1. Опис системи

Система складається з наступних блоків:

1. Реєстрація, аутентифікація та авторизація
2. Функціонал для автора 
3. Функціонал оплати підписки або одноразової оплати та головна сторінка 
4. Функціонал для передплатник 
5. Функціонал інтеграції з Telegram 
6. Сповіщення про нові публікації


Типи користувачів:
Система передбачає два типи користувачів системи: автор та передплатник. Автор створює підписки та викладає контент.

2.1. Типи користувачів

Система передбачає два типи користувачів системи: автор та передплатник.
Автор створює підписки та викладає контент, передплатники відповідно
зі своїм рівнем підписки отримують доступ до дозволеного для них контенту
та можливо Telegram чату.


2.2. Реєстрація

Реєстрація проходить одним чином як для автора контенту, так і для споживача контенту.
Вони будуть вводити такі данні в окні реєстрації 

* email - обов'язкове поле
* username - обов'язкове поле
* phone number - опціональне поле

Після надсилання форми реєстрації передплатника йому на email надходить
лист із першим кодом, яким він може увійти. Аутентифікація буде
відбуватися за разовими кодами, що надходять на email.


2.3. Аутентифікація автора та передплатників
Користувач вводить авторизаційні дані, або підтверджує свій акаунт через Google.

2.4. Функціонал для автора

Автор після аутентифікації (введення логіну та пароля) отримує доступ до
своєму автороскому функціоналу у Системі. Цей функціонал складається з
наступних блоків:

1. Редагування даних профілю
2. Заклад та редагування типів передплат
3. Заклад та редагування контенту
4. Розсилки
5. Аналітика


### 2.4.1. редагування профілю(settings)

У цьому розділі автор має можливість редагування даних
свого профілю - email, назва проекту, опис проекту, соціальної мережі.
Можливі соціальні мережі:

* YouTube
* Instagram
* Facebook
* Twitch

Повинна бути можливість змінити пароль, підтвердивши свій старий пароль.

Якщо дизайн системи буде мати на увазі якісь зображення для кастомізації
сторінки Системи, то ці зображення також мають редагуватися з профілю
автора.


### 2.4.2. Заклад та редагування типів передплати

По кожному типу передплати задаються:

* назва підписки
* Опис передплати
* **можливо — обкладинка підписки для використання десь у дизайні покупки
тієї чи іншої підписки**
* Вартість щомісячної підписки в доларах 
* доступ до Telegram для цієї передплати — для деяких типів передплати буде
доступний чат у Telegram

Має бути можливість (опціональна) задати знижки за покупку
передплати на 3, 6 та 12 місяців. Знижка задається в відсотках.


### 2.4.3. Заклад та редагування контенту

Контент, що публікується автором, може бути форматованим текстом.
з можливість, як мінімум, виділення тексту жирним, курсивом, підкресленим,
перекресленим. Можливо, варто додати можливість створення заголовків різного
розмір для структурування довгого текстового контенту.

Повинна бути можливість додавання списків та зображень до контенту посту,
а також можливість прикріплення файлів.

У кожного посту має бути заголовок.

Має бути можливість створити тизер посту — обкладинку та текст опису
про те, що перебуває у цьому пості. Цей тизер буде видно гостям (не минулим
аутентифікацію користувачам Системи), а також тим, чий рівень підписки не
вистачає для перегляду посту.

Також для кожного посту має бути заданий рівень передплати, за якої
цей пост можна читати. Крім платних рівнів передплати має бути видно
рівень підписки «відкритий для всіх» — такі відкриті для всіх пости будуть видні
всім користувачам Системи, у тому числі гостям, що не пройшли аутентифікацію.

Також для посту має бути можливість задати окрему ціну. Тобто
деякі пости можуть бути куплені лише окремо за одиничний платіж
або можуть бути куплені окремі, і бути доступні у складі однієї з підписок.

Частинами посту є сам контент та тизер. Тізер це те, що бачить
на головній сторінці як той, хто має доступ до посту, так і той, хто
не має доступу до посту. По натисненю на тизер відкривається пост і в того,
хто має доступ до поста.

У сам контент може вставлятися: текст з форматуванням (заголовки,
жирний, курсивний, перекреслений текст), зображення (завантажуються з комп'ютера),
відео з YouTube (показуються у стандартному вбудованому YouTube плеєрі),
аудіо (завантажуються з комп'ютера, відтворюються в побудованому на Систему
аудіо плеєр, підтримується тільки MP3 формат). Також має бути можливість 
прикріпити довільний завантажений з комп'ютера файл для передплатників він 
буде відображатись як посилання на завантаження цього файлу.


### 2.4.4. Заклад та редагування цілей

Автор може здійснювати в Системі збирання на якусь мету. Для цього він створює
(і може відредагувати згодом) ціль, в рамках якої задається:

* Опис мети - невеликий текст з описом того, на що збираються гроші
* Сума до збору в долларах

На публічній сторінці мета відображається з описом та поточним прогресом
наприклад, «10 777$ із 13 000$. зібрано»

Цілей може бути кілька. Оплата мети - це разовий платіж, не рекурентний,
тобто не списується щомісяця.


### 2.4.5. Розсилки

Автор може здійснювати email розсилки із Системи. Задається текст листа,
редактор аналогічний тому, що використовується при створенні постів, вибирається,
кому надіслати листа — безкоштовним передплатникам чи передплатникам якогось рівня
чи всім. Можна вибрати кілька варіантів, наприклад, безкоштовним передплатникам
та передплатникам такого рівня.

### 2.4.6. Аналітика

Автор бачить таку аналітику:

1. Абсолютна та відносна кількість передплатників у різних
рівнях підписки. Можливе у вигляді діаграми pie-chart.

2. Платежі – списком, плюс експорт до Excel всіх платежів. Колонки:
дата-час платежу, сума платежу, період (для передплат, а не
разових платежів), передплатник - uuid4, ім'я, email.


2.5. Функціонал оплати передплати або разового платежу та головної сторінки

Головна сторінка Системи – це список постів автора. Якщо дивиться гість,
то він бачить тільки тизери постів та пости, відкриті для всіх. На цій же
сторінці видно можливі варіанти передплати - з назвою кожної передплати,
описом її, можливістю доступу до Telegram чат та ціною. Поряд із кожним
типом передплати - кнопка Підписатися, що веде на інтерфейс входу або
реєстрації передплатника та наступної оплати.

Поряд з кожним тизером прихованого поста повинен відображатися необхідний для
перегляду поста рівень підписки — або можливість придбати цю окрему посаду
за виставлену йому ціну.

Пагінація постів здійснюється кнопкою «Показати ще» внизу під уже
показаними постами. Натискання цієї кнопки призводить до підвантаження та відображення
більш старих постів. Нові пости з'являються згори, старі — знизу.

Також має бути можливість ставити лайки постам – можливість доступна
лише передплатникам. Кількість лайків видно всім.

Має бути можливість підписатися без оплати. Таким людям приходитимуть
апдейти на пошту.

При оплаті передплати має бути можливість сплатити відразу за
3, 6 або 12 місяців (автор може налаштувати знижки на такі платежі).

Кількість передплатників має показуватись загальним числом (і платні, і
безкоштовні) десь на тій же головній сторінці Системи.

У кожного посту має бути своє постійне посилання, яке можна кудись
собі зберегти. Ідентифікатор посту, зашитий на засланні, повинен представляти
собою UUID4, не int число, щоб не можна було зрозуміти кількість
постів у системі.


### 2.5.1. Рекурентні платежі

Рекурентні платежі мають списуватись через 30 днів після попередньої оплати.
Якщо зняти платіж не вдалося — протягом найближчих 5 днів має здійснюватись
щоденна спроба списати суму. Протягом цих 5 днів доступ зберігається,
а передплатник отримує після кожної неуспішної спроби листа на email. Після
успішного зняття суми за передплату передплатник також отримує лист на email.

Після 5 днів неуспішних спроб списати суму підписка зупиняється та
передплатник втрачає доступ до постів і можливо Telegram чату (якщо чат
входив до його передплати).

Шаблони листів не редагуються в інтерфейсах Системи, жорстко зашиті в
самій системі та їх можна відредагувати лише змінюючи ці шаблони в коді
Системи.

2.6. Функціонал для передплатника

Передплатник може дивитися пости та ставити їм лайки, а також підвищувати свій
рівень передплати та купувати окремим платежем пости, які не входять до нього
передплату.

Коментарів під постами не мають на увазі. Шеринг постів не мається на увазі
як окрема кнопка - хто хоче пошерити, зробить це шляхом публікації
посилання. Можна окремо показати лише вибрані пости.

Кожен пост можна додати до вибраного. У розділі вибране у передплатника
має бути можливість створювати тематичні списки. При додаванні посту
у вибране показати чек-боксами ці списки, в цей момент передплатник може
відразу помістити пост в один із них.
 
Також у передплатника має бути можливість на сторінці свого профілю
відредагувати його дані (
email: при оновленні треба знову підтверджувати листом на пошту, змінити пароль) та
скасувати передплату, що призведе до зупинки рекурентних щомісячних платежів та після
дати закінчення сплаченого періоду передплатник стає безкоштовним передплатником.

Отримувати листи на пошту предплатник може липше після її підтвердження. 

У профілі має бути можливість відключити email повідомлення від системи.


2.7. Функціонал інтеграції з Telegram

Система має керувати передплатниками в одному конкретному чаті. Після того,
як у передплатника закінчилася підписка, він повинен пропасти доступ і до чату.

Доступ до чату буде не на всіх підписках, це конфігурується автором
в інтерфейсі закладу та редагування передплат.


2.8. Повідомлення про нові пости

Автоматично передплатникам повинні надходити повідомлення на Email про всі нові
постах автора в Системі. Передплатники можуть скасувати ці та інші листи
налаштування у профілі.


# 3. Пропонований стек технологій

Для реалізації системи пропонується наступний стек технологій:

* Бекенд:
     - Мова Python3.10
     - Фреймворк Django + Django-rest-framework
     - БД PostgreSQL, Redis
     - Celery for background tasks
     - Docker + Docker Compose
     - Aiogram для інтеграції з Telegram
* Фронтенд:
     - React
     - JavaScript

Для інтернет-еквайрингу розглядаються Paypall та CloudPayments,
у ході проекту треба порівняти технічні можливості платформ та комісії
за платежі. Важливо мати можливість оплати з Google Pay та Apple Pay, у тому
числі рекурентні платежі (якщо Google Pay та Apple Pay дозволяють таке
робити, уточнити під час проекту). Важливо відкрити в еквайрингу інші країни
для можливості прийому оплати не лише з UA, а й із інших країн. 
Обговорити це під час проекту з еквайрингом.

Зберігання файлів та зображень, що завантажуються автором, має здійснюватися
в S3-сумісному сховищі.


# 4. Вимоги до дизайну

Мінімалізм, лаконічність, акцент на контенті. Білий фон. Повинен бути присутнім
логотип системи десь на сторінці. Логотип треба розробити у межах
цього проекту.

У нижній частині сторінки має бути написано:

"Way to Bentley".