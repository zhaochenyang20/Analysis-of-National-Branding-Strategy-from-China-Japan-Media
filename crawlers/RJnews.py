import selenium.webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions as e
from selenium.webdriver.remote.webdriver import WebDriver as WD


user_info = {
    "username": "tsinghua_uesrname",
    "password": "tsinghua_password"
}

driver = wd.Firefox()


def init_search_page(d: WD):
    d.maximize_window()
    d.implicitly_wait(0.5)
    d.get("https://eproxy.lib.tsinghua.edu.cn/reader/user/login")
    d.implicitly_wait(0.5)
    inputs = d.find_elements(By.TAG_NAME, "input")
    inputs[0].send_keys(user_info['username'])
    inputs[1].send_keys(user_info['password'])
    d.find_element(By.TAG_NAME, "button").click()
    wdw(d, 5).until(lambda dvr: dvr.find_element(By.XPATH, "//a[contains(@class, 'category-link')]"))
    d.get('https://eproxy.lib.tsinghua.edu.cn/user/resource/visit?id=363')

    def expected_states_predicate(_d):
        try:
            # this state has 3 input tags
            target = ec.element_to_be_clickable((By.CLASS_NAME, "nk-home-bundle-search-button"))(_d)
            return target
        except e.NoSuchElementException:
            # note that the 'return' in finally block will replace the previous one !!!!
            buttons = _d.find_elements(By.TAG_NAME, "input")
            if len(buttons) == 14:
                _d.implicitly_wait(0.5)
                buttons[0].click()
                _d.implicitly_wait(0.5)
                print("Someone else has logged in, try to login")
            # note that there are possibility that target will be but has not been loaded
            return False

    wdw(d, 300).until(expected_states_predicate)
    print("initial search page loaded")


def get_visible_ok_button(_d: WD):
    buttons = _d.find_elements(By.CLASS_NAME, "nk-popup-ok")
    for b in buttons:
        if b.is_displayed():
            return b
    return None


def search_and_save(d: WD, keyword: str):
    while True:
        d.implicitly_wait(2)
        d.execute_script(f"document.getElementsByClassName('nk-home-bundle-search-input')[0].value = '{keyword}'")
        d.implicitly_wait(2)
        try:
            wdw(d, 5).until(ec.element_to_be_clickable((By.CLASS_NAME, "nk-home-bundle-search-button"))).click()
            d.implicitly_wait(0.5)
        except e.ElementClickInterceptedException:
            input('please click the button manually ...')
        else:
            try:
                d.find_element(By.CLASS_NAME, 'nk-msg-text')
            except e.NoSuchElementException:
                break
            print(f'Fail to send keyword {keyword}, retrying ...')

    wdw(d, 5).until(ec.element_to_be_clickable((By.CLASS_NAME, "nk-popup-ok"))).click()
    news_count = int(d.find_element(By.CLASS_NAME, "bundle-list-count").text)
    page_num = 1
    items_per_page = 20

    try:
        items_per_page = int(input("Please manually adjust the results \nEnter items per page"))
    except ValueError:
        pass

    while True:
        wdw(d, 5).until(ec.element_to_be_clickable((By.CLASS_NAME, 'nk-list-check')))
        d.find_element(By.CLASS_NAME, 'nk-navigator-select-all').click()

        d.implicitly_wait(4)

        wdw(d, 5).until(ec.element_to_be_clickable((By.CLASS_NAME, "nk-list-navigator-honbun"))).click()
        wdw(d, 5).until(get_visible_ok_button).click()
        page_HTML = wdw(d, 20).until(ec.visibility_of_element_located((By.CLASS_NAME, "nk-gv-page"))).get_attribute(
            "innerHTML")
        d.implicitly_wait(0.5)
        d.find_element(By.CLASS_NAME, "nk-gv-close").click()
        with open(f'{keyword}_{page_num}.html', 'w', encoding='utf-8') as f:
            f.write(page_HTML)
        page_num += 1

        # next page
        if news_count - (page_num - 1) * items_per_page > 0:
            d.implicitly_wait(4)
            first_headline = d.find_element(By.CLASS_NAME, "nk-list-headline").text
            d.find_element(By.CLASS_NAME, "nk-navigator-next").click()
            wdw(d, 5).until(lambda x: x.find_element(By.CLASS_NAME, "nk-list-headline").text != first_headline)
        else:
            break


def exit_sys(d: WD):
    d.find_element(By.XPATH, '//input[@class="logout"]').click()
    wdw(d, 5).until(get_visible_ok_button).click()
    d.quit()


def partial_search(d: WD, keyword: str, news_count: int, items_per_page: int = 20, page_num: int = 1):
    while True:
        wdw(d, 5).until(ec.element_to_be_clickable((By.CLASS_NAME, 'nk-list-check')))
        d.find_element(By.CLASS_NAME, 'nk-navigator-select-all').click()
        d.implicitly_wait(3)
        wdw(d, 5).until(ec.element_to_be_clickable((By.CLASS_NAME, "nk-list-navigator-honbun"))).click()
        wdw(d, 5).until(get_visible_ok_button).click()
        page_HTML = wdw(d, 25).until(ec.visibility_of_element_located((By.CLASS_NAME, "nk-gv-page"))).get_attribute(
            "innerHTML")
        d.implicitly_wait(0.5)
        d.find_element(By.CLASS_NAME, "nk-gv-close").click()
        with open(f'{keyword}_{page_num}.html', 'w', encoding='utf-8') as f:
            f.write(page_HTML)
        page_num += 1

        # next page
        if news_count - (page_num - 1) * items_per_page > 0:
            d.implicitly_wait(4)
            first_headline = d.find_element(By.CLASS_NAME, "nk-list-headline").text
            d.find_element(By.CLASS_NAME, "nk-navigator-next").click()
            wdw(d, 5).until(lambda x: x.find_element(By.CLASS_NAME, "nk-list-headline").text != first_headline)
        else:
            break

init_search_page(driver)
partial_search(driver, '五輪', news_count=int(input("news_count")), items_per_page=400, page_num=int(input("page_num")))
exit_sys(driver)