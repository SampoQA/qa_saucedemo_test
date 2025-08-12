# SauceDemo UI Automation  
**End-to-End Testing with Playwright & Pytest**  

---

## 🇷🇺 Русская версия  
### 🎯 Цель проекта  
Автоматизация основного сценария покупки на демо-сайте [SauceDemo](https://www.saucedemo.com/):  
`Логин → Выбор товара → Корзина → Оформление → Подтверждение`  
С фокусом на позитивные тесты и планами по расширению  

### ⚡️ Особенности  
- **Page Object Model** - чистая архитектура  
- **dotenv** - безопасное хранение учетных данных  
- **HTML-отчеты** после каждого прогона  
- Подготовка к Docker-интеграции  

### 🚀 Быстрый старт  
```bash
# 1. Установка зависимостей
pip install -r requirements.txt

# 2. Запуск позитивных тестов
pytest tests/positive --headed

# 3. Генерация отчета
pytest --html=report.html
```

### 📂 Структура проекта  
```text
saucedemo-automation/
├── src/                          # Ядро проекта
│   ├── pages/                    # Page Object Model
│   │   ├── login_page.py         # Страница авторизации
│   │   ├── products_page.py      # Страница товаров
│   │   └── checkout_page.py      # Оформление заказа
│   ├── helpers/                  # Вспомогательные утилиты
│   └── config.py                 # Управление окружением
├── tests/                        
│   ├── positive/                 # Основные сценарии ✔️
│   └── negative/                 # Будущие негативные тесты
├── .env.example                  # Шаблон конфигурации
└── docker-compose.yml            # Для будущей Docker-интеграции
```

### 🔧 Конфигурация  
1. Создайте `.env` файл на основе `.env.example`  
2. Укажите тестовые учетные данные:  
```env
BASE_URL=https://www.saucedemo.com
STANDARD_USER=standard_user
PASSWORD=secret_sauce
```

### 🌟 Что сделано  
- Полный E2E сценарий покупки  
- Изолированные тесты с независимыми данными  
- Подготовка к CI/CD интеграции  

### 📅 Планы развития  
- [ ] Добавить негативные тесты  
- [ ] Реализовать Docker-образ  
- [ ] Параллельный запуск тестов  
- [ ] Интеграция с Allure Report  

---

## 🇬🇧 English Version  
### 🎯 Project Goal  
Automate core purchase flow on [SauceDemo](https://www.saucedemo.com/):  
`Login → Product Selection → Cart → Checkout → Confirmation`  
With focus on positive tests and expansion roadmap  

### ⚡️ Key Features  
- **Page Object Model** architecture  
- **dotenv** for credentials management  
- **HTML reports** after each run  
- Docker-ready infrastructure  

### 🚀 Quick Start  
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run positive tests
pytest tests/positive --headed

# 3. Generate report
pytest --html=report.html
```

### 📂 Project Structure  
```text
saucedemo-automation/
├── src/                          # Core components
│   ├── pages/                    # Page Object Model
│   │   ├── login_page.py         # Login page
│   │   ├── products_page.py      # Products page
│   │   └── checkout_page.py      # Checkout page
│   ├── helpers/                  # Helper utilities
│   └── config.py                 # Environment setup
├── tests/                        
│   ├── positive/                 ✅ Main scenarios
│   └── negative/                 # Future negative tests
├── .env.example                  # Configuration template
└── docker-compose.yml            # Future Docker setup
```

### 🔧 Configuration  
1. Create `.env` from `.env.example`  
2. Specify test credentials:  
```env
BASE_URL=https://www.saucedemo.com
STANDARD_USER=standard_user
PASSWORD=secret_sauce
```

### ✅ Current Implementation  
- Complete E2E purchase flow  
- Data-independent test cases  
- CI/CD-ready foundation  

### 📅 Roadmap  
- [ ] Add negative test scenarios  
- [ ] Implement Docker image  
- [ ] Parallel test execution  
- [ ] Allure Report integration  



Как создать окуржение для работы тестов

# Переходим в созданную директорию
cd tests

# Создаем виртуальное окружение Python
python -m venv venv

# АКТИВАЦИЯ ДЛЯ POWERSHELL (Windows):
# 1. Путь к скрипту активации в Windows отличается от Unix-систем
# 2. Используем точку перед командой для выполнения в текущей сессии
# 3. Указываем полный путь к скрипту активации
.\venv\Scripts\Activate.ps1

# Если возникает ошибка выполнения скриптов:
# Разрешаем выполнение скриптов только для текущей сессии
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force

# Повторно активируем окружение после изменения политики
.\venv\Scripts\Activate.ps1

# Устанавливаем пакеты:
# - playwright: фреймворк для автоматизации браузера
# - pytest-playwright: интеграция Playwright с pytest
# - python-dotenv: работа с переменными окружения
pip install playwright pytest-playwright python-dotenv

# Устанавливаем браузер Chromium
# Playwright требует явной установки браузерных бинарников
playwright install chromium


Чувствительные данные спрятаны dotenv 
