import os
import pytest
from datetime import datetime
import base64
from playwright.sync_api import Page
from typing import Optional

# Явно регистрируем плагин
pytest_plugins = ["pytest_html"]

def pytest_configure(config):
    """Создаем папку для отчетов перед запуском тестов"""
    report_dir = os.path.join(os.getcwd(), "reports")
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    
    # Добавляем кастомные стили для отчета
    config._metadata = {}
    config.option.htmlpath = os.path.join(report_dir, "report.html")

def pytest_html_report_title(report):
    """Устанавливаем заголовок отчета"""
    report.title = "SauceDemo Test Report"

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """Переименовываем отчет после завершения сессии"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = os.path.join("reports", f"report_{timestamp}.html")
    
    # Переименовываем основной отчет
    default_report = os.path.join("reports", "report.html")
    if os.path.exists(default_report):
        os.rename(default_report, report_path)

def capture_screenshot(page: Page) -> Optional[str]:
    """Делаем скриншот и возвращаем в base64"""
    try:
        screenshot = page.screenshot(full_page=True, type="png")
        return base64.b64encode(screenshot).decode("utf-8")
    except Exception as e:
        print(f"Ошибка при создании скриншота: {e}")
        return None

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Обрабатываем отчеты для каждого теста"""
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    
    # Добавляем скриншоты только для упавших тестов
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        
        if page and isinstance(page, Page):
            screenshot_b64 = capture_screenshot(page)
            
            if screenshot_b64 and pytest_html:
                # Добавляем скриншот в отчет
                html = f'<div><img src="data:image/png;base64,{screenshot_b64}" style="width:100%"></div>'
                extra = getattr(report, "extra", [])
                extra.append(pytest_html.extras.html(html))
                report.extra = extra