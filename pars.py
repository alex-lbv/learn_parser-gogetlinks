from selenium import webdriver
import time
import csv
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class GogetlinksParser:

    def __init__(self):
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_setting_values': {'images': 2}}
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(executable_path='/Users/macbook/Desktop/Work/parser-gogetlinks/chromedriver', options=options)
        self.transin_to_site()
        self.login_in_site()
        self.transin_to_catalog()
        self.see_all_list()
        pages = 1
        while pages <= 343:
            print(pages, '________________________________', pages)
            self.pars_table()
            pagination = self.driver.find_element_by_xpath('//*[@id="div_search_table"]/div[1]/table/tbody/tr/td[2]')
            pagination.find_element_by_css_selector('label + a').send_keys(Keys.ENTER)
            pages += 1
            time.sleep(2.5)

    def transin_to_site(self):
        self.driver.maximize_window()
        self.driver.get("https://gogetlinks.net/")

    def login_in_site(self):
        email = self.driver.find_element_by_id("login_e_mail")
        email.send_keys('aal940722r')
        passw = self.driver.find_element_by_id("login_password")
        passw.send_keys('priy@max4TWON6kurs')
        login = self.driver.find_element_by_id("ok_button")
        login.click()
        time.sleep(.5)

    def transin_to_catalog(self):
        self.driver.get('https://gogetlinks.net/search_sites.php')
        time.sleep(.5)

    def see_all_list(self):
        element = self.driver.find_element_by_id("set_count_in_page")
        select = Select(element)
        select.select_by_value("50")
        time.sleep(1.3)

    def pars_table(self):
        table_id = self.driver.find_element_by_id('table_content')
        tbody = table_id.find_element_by_tag_name('tbody')
        rows = tbody.find_elements_by_tag_name('tr')
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            all_td = [(cells[i].text) for i in range(len(cells))]
            #print(all_td)
            with open("gogetlinks.csv", mode="a", encoding='utf-8') as w_file:
                file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r\n")
                file_writer.writerow([(cells[i].text) for i in range(len(cells))])

def main():
    gp= GogetlinksParser()

if __name__ == '__main__':
    main()