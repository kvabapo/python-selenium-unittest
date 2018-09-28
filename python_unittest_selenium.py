import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GalenWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://testapp.galenframework.com/")

    def test_valid_login(self):
        # click login button
        self.driver.find_element_by_css_selector(".btn[onclick='App.showLoginPage();']").click()

        # enter username, password and click login
        self.driver.find_element_by_css_selector("[name='login.username']").send_keys("testuser@example.com")
        self.driver.find_element_by_css_selector("[name='login.password']").send_keys("test123")
        self.driver.find_element_by_css_selector(".button-login[onclick='App.login()']").click()

        # user was login and notes page is displayed
        header = self.driver.find_element_by_css_selector("h2").text
        self.assertEqual("My Notes", header)


    def test_create_note(self):
        # click login button
        self.driver.find_element_by_css_selector(".btn[onclick='App.showLoginPage();']").click()

        # enter username, password and click login
        self.driver.find_element_by_css_selector("[name='login.username']").send_keys("testuser@example.com")
        self.driver.find_element_by_css_selector("[name='login.password']").send_keys("test123")
        self.driver.find_element_by_css_selector(".button-login[onclick='App.login()']").click()

        # user was login and notes page is displayed
        header = self.driver.find_element_by_css_selector("h2").text
        self.assertEqual("My Notes", header)

        # create note
        self.driver.find_element_by_css_selector(".btn[onclick='App.showAddNotePage();']").click()
        self.driver.find_element_by_css_selector("[name='note.title']").send_keys("hello")
        self.driver.find_element_by_css_selector("[name='note.description']").send_keys("test")
        self.driver.find_element_by_css_selector(".btn[onclick='App.addNote()']").click()

        # verify note was created
        title = self.driver.find_elements_by_css_selector("h4.list-group-item-heading")
        description = self.driver.find_elements_by_css_selector("p.list-group-item-text")
        self.assertEqual("hello", title[2].text)
        self.assertEqual("test", description[2].text)

   def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
