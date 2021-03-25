import unittest
from selenium import webdriver
import pages

class Vaccine_Finder_and_Appt_Booker(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("url") 
        self.timeslots = ['09:30 AM - 09:45 AM','10:30 AM - 10:45 AM', '11:00 AM - 11:15 AM']
        self.first = 'Joe'
        self.last = 'Doe'
        self.code = '11749'
        self.number = '000-0000-9911'
        self.address = '1 Test Drive'
        self.email = 'noreply@notrealemailaddie.org'
        self.dob = '01/01/2001'
        self.wait = self.driver.implicitly_wait(2)
        
    def test_vaccine_appt(self):
        
        '''This all has to be done in one single test due to hidden redirection links'''
        #Load the pages classes
        main_page = pages.MainPage(self.driver, self.wait, self.timeslots, self.first, self.last, self.code, self.number, self.address, self.email, self.dob)
        appt_page = pages.PageTwo(self.driver, self.wait, self.timeslots, self.first, self.last, self.code, self.number, self.address, self.email, self.dob)
        info_page = pages.PageThree(self.driver, self.wait, self.timeslots, self.first, self.last, self.code, self.number, self.address, self.email, self.dob)
        remaining_pages = pages.RemainingPages(self.driver, self.wait, self.timeslots, self.first, self.last, self.code, self.number, self.address, self.email, self.dob)
        
        #assert main_page.is_title_matches()
        
        #find appt and click next
        main_page.is_appt_available()
        main_page.click_primary_button()
        
        #find best appt time and click next
        appt_page.get_best_appt_time()
        appt_page.click_next_button()
        #appt_page.did_we_get_appt()
        
        #fill out form page and click next
        info_page.fill_personal_info()
        info_page.click_next_button()
        
        #fill out rest of the pages
        #ethnicity page
        remaining_pages.fill_ethnicity_info()
        remaining_pages.click_next_button()
        #accomodations page
        remaining_pages.fill_accomdations_info()
        remaining_pages.click_next_button()
        #optional 2 pages
        remaining_pages.click_next_button()
        remaining_pages.click_next_button()
        #screening page
        remaining_pages.fill_screening_info()
        remaining_pages.click_next_button()
        #almost done page
        remaining_pages.click_continue_button()
        #registration page
        remaining_pages.click_register_button()
        #save ticket page
        remaining_pages.click_primary_button()

        
    def tearDown(self):
        #print('Ticket Downloaded')
        #print('Tearing Down in T-Minus 30 Seconds...')
        self.driver.implicitly_wait(30)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()