import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import random
import datetime

exe_path = r"c:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=exe_path)


# def okon(number): ##Выправляет окончания числительных
    #chiclo = number+10
    #if (chiclo % 10) == 1:
        #print(number+' минута')
    #elif:

def exep_orb_reborn():
    for i in range(2):
        server_online = True
        while server_online:
            try:
                driver.get('https://m.vten.ru/profs/receipt/rawOre')
                server_online = False
            except selenium.common.exceptions.ElementClickInterceptedException or selenium.common.exceptions.NoSuchElementException:
                time.sleep(60)
                driver.get('https://m.vten.ru/profs/receipt/rawOre')




def iron_ore():
    many = int(input("Сколько нужно руды: "))  ##Запрос нужного кол-ва руды
    driver.get('https://m.vten.ru/profs/receipt/rawOre')
    driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[3]/div[1]/span/a').click()
    time.sleep(.5)
    driver.find_element_by_xpath('//*[@id="bodyContainer"]/div[4]/div[3]/div/a').click()
    now = datetime.datetime.now()
    print("Производство начато в " + now.strftime("%H:%M:%S"))
    print(
        'Расчетное время работы - ' + str(round(many * 174 / 60)) + ' минут') ##Вернуть обратно, после окончания бонуса
    time.sleep(random.randint(172, 176))
    counter = 0
    if many > 1:
        while counter <= many:
            driver.get('https://m.vten.ru/profs/receipt/rawOre')
            try:
                time.sleep(.5)
                driver.find_element_by_class_name('go-btn._single.center._night.pt5.pb5.mr5').click()
            except selenium.common.exceptions.ElementClickInterceptedException:
                driver.get('https://m.vten.ru/profs/receipt/rawOre')
                driver.find_element_by_class_name('go-btn._single.center._night.pt5.pb5.mr5').click()
            now = datetime.datetime.now()
            print("Уже готово: " + str(counter) + " Цикл обновился в " + now.strftime("%H:%M:%S"))
            time.sleep(random.randint(172, 176))
            counter += 1
        driver.find_element_by_xpath('//*[@id="bodyContainer"]/div[4]/table/tbody/tr[1]/td[4]/a').click()
        print('Задача завершена')
    else:
        driver.get('https://m.vten.ru/profs/receipt/rawOre')
        driver.find_element_by_xpath('//*[@id="bodyContainer"]/div[4]/table/tbody/tr[1]/td[4]/a').click()
        print('Задача завершена')


def platina():
    many = int(input('Сколько платины изготовить? '))
    driver.get('https://m.vten.ru/profs/receipt/platinum')
    pl = driver.find_element_by_xpath('')
    pl.click()
    time.sleep(.5)
    pl = driver.find_element_by_xpath('//*[@id="bodyContainer"]/div[4]/div[3]/div/a')
    pl.click()
    now = datetime.datetime.now()
    print("Производство начато в " + now.strftime("%H:%M:%S"))
    counter = 1
    for i in range(many):
        to = random.randint(1680, 1690)
        time.sleep(to)
        driver.get('https://m.vten.ru/profs/receipt/platinum')
        try:
            time.sleep(.5)
            pl = driver.find_element_by_class_name('')
            pl.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            time.sleep(.5)
            driver.get('https://m.vten.ru/profs/receipt/platinum')
            pl = driver.find_element_by_class_name('')
            pl.click()
        now = datetime.datetime.now()
        print("Уже готово: " + str(counter) + " Цикл обновился в " + now.strftime("%H:%M:%S"))
        counter += 1


def potion_str():
    many = int(input("Сколько нужно зелий?: "))
    driver.get('https://m.vten.ru/profs/receipt/alchemy-str-1')
    potion = driver.find_element_by_xpath('//*[@id="bodyContainer"]/div[3]/div[3]/div[1]/span/a')
    potion.click()
    time.sleep(.5)
    potion = driver.find_element_by_xpath('//*[@id="bodyContainer"]/div[4]/div[3]/div/a')
    potion.click()
    now = datetime.datetime.now()
    print("Производство начато в " + now.strftime("%H:%M:%S"))
    counter = 1
    for i in range(many):
        to = random.randint(10, 11)
        time.sleep(to)
        driver.refresh()
        try:
            time.sleep(.5)
            potion = driver.find_element_by_class_name('go-btn._single.center._night.pt5.pb5.mr5')
            potion.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            time.sleep(.5)
            driver.get('https://m.vten.ru/profs/receipt/alchemy-str-1')
            potion = driver.find_element_by_class_name('go-btn._single.center._night.pt5.pb5.mr5')
            potion.click()
        now = datetime.datetime.now()
        print("Уже готово: " + str(counter) + " Цикл обновился в " + now.strftime("%H:%M:%S"))
        counter += 1


def entrance():
    try:
        driver.find_element_by_xpath('//*[@id="bodyContainer"]/div[2]/div/a[2]').click()
        time.sleep(.5)
        driver.find_element_by_xpath('//*[@id="login"]').send_keys('Toy War')
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('eqV-LBn-t5Z-TUJ')
        driver.find_element_by_xpath('//*[@id="submit"]').click()
        boo = (bool((driver.find_elements_by_xpath('/html/body/div[2]/div[4]/div/form/div[4]/div/img'))))
        if boo:
            a = input("Введите капчу: ")
            driver.find_element_by_xpath('//*[@id="captcha"]').send_keys(a)
            driver.find_element_by_xpath('//*[@id="submit"]').click()
        else:
            time.sleep(.5)
            driver.get('https://m.vten.ru/city')
    except selenium.common.exceptions.NoSuchElementException:
        print('Сервер недоступен, попробуйте позже')


def potion_crit():
    many = int(input("Сколько нужно зелий?: "))
    driver.get('https://m.vten.ru/profs/receipt/alchemy-crit-1')
    potion = driver.find_element_by_xpath('//*[@id="bodyContainer"]/div[3]/div[3]/div[1]/span/a')
    potion.click()
    time.sleep(.5)
    potion = driver.find_element_by_xpath('//*[@id="bodyContainer"]/div[4]/div[3]/div/a')
    potion.click()
    now = datetime.datetime.now()
    print("Производство начато в " + now.strftime("%H:%M:%S"))
    counter = 1
    for i in range(many):
        to = random.randint(10, 11)
        time.sleep(to)
        driver.refresh()
        try:
            time.sleep(.5)
            potion = driver.find_element_by_class_name('go-btn._single.center._night.pt5.pb5.mr5')
            potion.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            time.sleep(.5)
            driver.get('https://m.vten.ru/profs/receipt/alchemy-crit-1')
            potion = driver.find_element_by_class_name('go-btn._single.center._night.pt5.pb5.mr5')
            potion.click()
        now = datetime.datetime.now()
        print("Уже готово: " + str(counter) + " Цикл обновился в " + now.strftime("%H:%M:%S"))
        counter += 1


def potion_def():
    many = int(input("Сколько нужно зелий?: "))
    driver.get('https://m.vten.ru/profs/receipt/alchemy-def-1')
    potion = driver.find_element_by_xpath('//*[@id="bodyContainer"]/div[3]/div[3]/div[1]/span/a')
    potion.click()
    time.sleep(.5)
    potion = driver.find_element_by_xpath('//*[@id="bodyContainer"]/div[4]/div[3]/div/a')
    potion.click()
    now = datetime.datetime.now()
    print("Производство начато в " + now.strftime("%H:%M:%S"))
    counter = 1
    for i in range(many):
        to = random.randint(10, 11)
        time.sleep(to)
        driver.refresh()
        try:
            time.sleep(.5)
            potion = driver.find_element_by_class_name('go-btn._single.center._night.pt5.pb5.mr5')
            potion.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            time.sleep(.5)
            driver.get('https://m.vten.ru/profs/receipt/alchemy-def-1')
            potion = driver.find_element_by_class_name('go-btn._single.center._night.pt5.pb5.mr5')
            potion.click()
        now = datetime.datetime.now()
        print("Уже готово: " + str(counter) + " Цикл обновился в " + now.strftime("%H:%M:%S"))
        counter += 1


def eli_str():
    many = int(input("Сколько нужно зелий?: "))
    driver.get('https://m.vten.ru/profs/receipt/alchemy-str-2')
    potion = driver.find_element_by_xpath('//*[@id="bodyContainer"]/div[3]/div[3]/div[1]/span/a')
    potion.click()
    time.sleep(.5)
    potion = driver.find_element_by_xpath('//*[@id="bodyContainer"]/div[4]/div[3]/div/a')
    potion.click()
    now = datetime.datetime.now()
    print("Производство начато в " + now.strftime("%H:%M:%S"))
    counter = 1
    for i in range(many):
        to = random.randint(21, 22)
        time.sleep(to)
        driver.refresh()
        try:
            time.sleep(.5)
            potion = driver.find_element_by_class_name('go-btn._single.center._night.pt5.pb5.mr5')
            potion.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            time.sleep(.5)
            driver.get('https://m.vten.ru/profs/receipt/alchemy-str-2')
            potion = driver.find_element_by_class_name('go-btn._single.center._night.pt5.pb5.mr5')
            potion.click()
        now = datetime.datetime.now()
        print("Уже готово: " + str(counter) + " Цикл обновился в " + now.strftime("%H:%M:%S"))
        counter += 1


def eli_def():
    many = int(input("Сколько нужно зелий?: "))
    driver.get('https://m.vten.ru/profs/receipt/alchemy-def-2')
    potion = driver.find_element_by_xpath('//*[@id="bodyContainer"]/div[3]/div[3]/div[1]/span/a')
    potion.click()
    time.sleep(.5)
    potion = driver.find_element_by_xpath('//*[@id="bodyContainer"]/div[4]/div[3]/div/a')
    potion.click()
    now = datetime.datetime.now()
    print("Производство начато в " + now.strftime("%H:%M:%S"))
    counter = 1
    for i in range(many):
        to = random.randint(21, 22)
        time.sleep(to)
        driver.refresh()
        try:
            time.sleep(.5)
            potion = driver.find_element_by_class_name('go-btn._single.center._night.pt5.pb5.mr5')
            potion.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            time.sleep(.5)
            driver.get('https://m.vten.ru/profs/receipt/alchemy-def-2')
            potion = driver.find_element_by_class_name('go-btn._single.center._night.pt5.pb5.mr5')
            potion.click()
        now = datetime.datetime.now()
        print("Уже готово: " + str(counter) + " Цикл обновился в " + now.strftime("%H:%M:%S"))
        counter += 1


def eli_crit():
    many = int(input("Сколько нужно зелий?: "))
    driver.get('https://m.vten.ru/profs/receipt/alchemy-crit-2')
    potion = driver.find_element_by_xpath('//*[@id="bodyContainer"]/div[3]/div[3]/div[1]/span/a')
    potion.click()
    time.sleep(.5)
    potion = driver.find_element_by_xpath('//*[@id="bodyContainer"]/div[4]/div[3]/div/a')
    potion.click()
    now = datetime.datetime.now()
    print("Производство начато в " + now.strftime("%H:%M:%S"))
    counter = 1
    for i in range(many):
        to = random.randint(21, 22)
        time.sleep(to)
        driver.refresh()
        try:
            time.sleep(.5)
            potion = driver.find_element_by_class_name('go-btn._single.center._night.pt5.pb5.mr5')
            potion.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            time.sleep(.5)
            driver.get('https://m.vten.ru/profs/receipt/alchemy-crit-2')
            potion = driver.find_element_by_class_name('go-btn._single.center._night.pt5.pb5.mr5')
            potion.click()
        now = datetime.datetime.now()
        print("Уже готово: " + str(counter) + " Цикл обновился в " + now.strftime("%H:%M:%S"))
        counter += 1


pas1 = "eqV-LBn-t5Z-TUJ"
log1 = "Toy War"

driver.get('https://m.vten.ru')
time.sleep(1)
entrance()

menu = True
while menu:
    ask = int(input('Что вы хотите сделать? 1 - Горное дело, 2 - Алхимия '))
    menu = False
    if ask == 1:
        gorka = True
        while gorka:
            ask = int(input('Что вы хотите сделать? 1 - Руда, 2 - Платина '))
            gorka = False
            if ask == 1:
                iron_ore()
                menu = True
            elif ask == 2:
                platina()
            else:
                print('Введите число из списка ')
                gorka = True
    elif ask == 2:
        alchemy = True
        while alchemy:
            ask = int(input('Что вы хотите сварить? 1 - Зелья 2 - Эликсиры? 0 - вернуться'))
            alchemy = False
            if ask == 1:
                zelya = True
                while zelya:
                    ask = int(input('Какое зелье варим? 1 - силы, 2 - защиты, 3 - ярости, 0 - вернуться'))
                    zelya = False
                    if ask == 1:
                        potion_str()
                    elif ask == 2:
                        potion_def()
                    elif ask == 3:
                        potion_crit()
                    elif ask == 0:
                        alchemy = True
                    else:
                        print('Введите число из списка: ')
                        zelya = True
            elif ask == 2:
                elix = True
                while elix:
                    ask = int(input('Какой эликсир варим? 1 - силы, 2 - защиты, 3 - ярости, 0 - вернуться'))
                    elix = False
                    if ask == 1:
                        eli_str()
                    elif ask == 2:
                        eli_def()
                    elif ask == 3:
                        eli_crit()
                    elif ask == 0:
                        alchemy = True
                    else:
                        print('Введите число из списка ')
                        elix = True
            elif ask == 0:
                menu = True
            else:
                print('Введите число из списка ')
                alchemy = True
    else:
        print('Введите число из списка')
        menu = True

