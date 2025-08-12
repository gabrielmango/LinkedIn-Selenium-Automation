import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

LINKEDIN_USER = os.getenv("LINKEDIN_USER")
LINKEDIN_PASS = os.getenv("LINKEDIN_PASS")
LINKEDIN_PROFILE = os.getenv("LINKEDIN_PROFILE")


def main():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://www.linkedin.com/login")
        time.sleep(2)

        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")

        username_input.send_keys(LINKEDIN_USER)
        password_input.send_keys(LINKEDIN_PASS)
        password_input.send_keys(Keys.RETURN)

        time.sleep(5)

        driver.get(LINKEDIN_PROFILE)
        time.sleep(5)

    finally:
        driver.quit()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Erro ao executar o script: {e}")
