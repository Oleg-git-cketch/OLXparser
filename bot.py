import time
from selenium import webdriver
from bs4 import BeautifulSoup
import telebot
import threading

bot = telebot.TeleBot('7587537078:AAH3JxwjB5rKFp3Oe5WIyqkkyoTReXnEnt4')



def scrape_olx(url, file_path='logi.txt'):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('')


    driver = webdriver.Chrome()
    driver.get(f"https://www.olx.uz/list/q-{ url }/")
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "lxml")
    sales = soup.find_all('div', class_='css-1r93q13')
    limit = 0

    for sale in sales:
        name_tag = sale.find("h4", class_='css-hzlye5')
        price_tag = sale.find("p", {"data-testid": "ad-price"})
        link_tag = sale.find('a', class_='css-1tqlkj0')

        if not (name_tag and price_tag and link_tag):
            continue

        name_text = name_tag.text.strip()
        price_text = price_tag.text.strip()
        href = link_tag['href']
        full_link = 'https://www.olx.uz' + href

        if f'{url}' not in name_text.lower():
            continue
        driver.get(full_link)
        time.sleep(2)

        soup_detail = BeautifulSoup(driver.page_source, "lxml")
        desc_tag = soup_detail.find('div', class_='css-19duwlz')
        description = desc_tag.text.strip() if desc_tag else "Описание отсутствует"

        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(
                "------------------------\n"
                f"Название: {name_text}\n"
                f"Цена: {price_text}\n"
                f"Описание: {description}\n"
                f"Ссылка: {full_link}"
            )



        driver.back()
        time.sleep(1)
        limit += 1
        if limit > 3:
            break

    driver.quit()



@bot.message_handler(commands=['analiz'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Введите название товара для поиска:')
    bot.register_next_step_handler(message, url_ask)



def url_ask(message):
    user_id = message.from_user.id
    text = message.text
    bot.send_message(user_id, "Начинаю сбор данных, это займёт несколько секунд...")

    def background_task():
        scrape_olx(text)  # долгий процесс
        with open('logi.txt', 'r', encoding='utf-8') as file:
                bot.send_message(user_id, 'Сбор завершён:\n')
                bot.send_document(user_id, file)


    threading.Thread(target=background_task).start()


bot.polling()