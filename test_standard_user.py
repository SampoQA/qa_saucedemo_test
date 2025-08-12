from config import Config # Использование относительного импорта (если файл в той же папке)
from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    
    # Загрузка конфигурации
    config = Config()
    
    # Переход на сайт
    page.goto(config.BASE_URL)
    
    # Использую явные CSS-селекторы
    page.locator("[data-test='username']").fill(config.USER_LOGIN)
    page.locator("[data-test='password']").fill(config.USER_PASSWORD)
    page.locator("[data-test='login-button']").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


