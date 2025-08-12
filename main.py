import os
import random
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

LINKEDIN_USER = os.getenv("LINKEDIN_USER")
LINKEDIN_PASS = os.getenv("LINKEDIN_PASS")
LINKEDIN_PROFILE = os.getenv("LINKEDIN_PROFILE")


def human_typing(element, text, min_delay=0.1, max_delay=0.3):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(min_delay, max_delay))


def human_scroll(driver):
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    current_pos = 0
    while current_pos < scroll_height:
        step = random.randint(100, 300)
        current_pos += step
        driver.execute_script(f"window.scrollTo(0, {current_pos});")
        time.sleep(random.uniform(1.0, 2.5))


def human_mouse_move(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.perform()
    time.sleep(random.uniform(1.0, 2.5))


def main():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://www.linkedin.com/login")
        time.sleep(random.uniform(1.5, 3))

        username_input = driver.find_element(By.ID, "username")
        time.sleep(random.uniform(1.5, 3))
        password_input = driver.find_element(By.ID, "password")

        human_mouse_move(driver, username_input)
        human_typing(username_input, LINKEDIN_USER)

        human_mouse_move(driver, password_input)
        human_typing(password_input, LINKEDIN_PASS)

        password_input.send_keys(Keys.RETURN)

        time.sleep(random.uniform(4, 6))

        human_scroll(driver)

        driver.get(LINKEDIN_PROFILE)
        time.sleep(random.uniform(3, 6))

        human_scroll(driver)

        driver.get(
            "https://www.linkedin.com/mynetwork/network-manager/people-follow/followers/"
        )
        time.sleep(random.uniform(4, 6))

        for _ in range(1):
            human_scroll(driver)
            time.sleep(random.uniform(2, 4))

        lista_xpath = "/html/body/div[6]/div[3]/div/div/div/div/div[2]/div/div/main/section/div/div[2]/div[1]/div/div/div/ul"
        lista = driver.find_element(By.XPATH, lista_xpath)

        itens = lista.find_elements(By.TAG_NAME, "li")

        hrefs = []
        for i, item in enumerate(itens, start=1):
            link_xpath = f"/html/body/div[6]/div[3]/div/div/div/div/div[2]/div/div/main/section/div/div[2]/div[1]/div/div/div/ul/li[{i}]/div/div/div/div[2]/div/div[1]/div/span/span/a"
            try:
                link_element = driver.find_element(By.XPATH, link_xpath)
                href = link_element.get_attribute("href")
                if href:
                    hrefs.append(href)
            except Exception as e:
                print(f"Erro ao pegar href do item {i}: {e}")

        with open("conexoes_links.txt", "w", encoding="utf-8") as f:
            for href in hrefs:
                f.write(href + "\n")

        print(f"{len(hrefs)} links salvos em conexoes_links.txt")

    finally:
        driver.quit()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Erro ao executar o script: {e}")
