from element import BasePageElement
from locators import Buttons
from selenium.common.exceptions import NoSuchElementException
import time


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
   
    
    def __init__(self, driver, wait, timeslots,first,last,code,number,address,email,dob):
        self.driver = driver
        self.wait = wait
        self.timeslots = timeslots
        self.first = first
        self.last = last
        self.code = code
        self.number = number
        self.address = address
        self.email = email
        self.dob = dob
        
    def click_primary_button(self):
        element = self.driver.find_element(*Buttons.PRIMARY_BUTTON)
        element.click()
        
    def click_next_button(self):
        element = self.driver.find_element(*Buttons.NEXT_BUTTON)
        element.click()
        self.wait
        
    def click_register_button(self):
        element = self.driver.find_element(*Buttons.REGISTER_BUTTON)
        element.click()
        print('Regsistration Complete!.......',time.strftime("%H:%M:%S",time.localtime()))
        
    def click_continue_button(self):
        element = self.driver.find_element(*Buttons.CONTINUE_BUTTON)
        element.click()
        print('Almost Done Page Complete!.......',time.strftime("%H:%M:%S",time.localtime()))

class MainPage(BasePage):
    
    def is_title_matches(self):
        """Verifies that the hardcoded text "Welcome" appears in page title"""
        return "Welcome" in self.driver.title
    
    def is_appt_available(self):
            while True:
                try:
                    self.driver.find_element(*Buttons.PRIMARY_BUTTON)
                    
                except NoSuchElementException:
                    print('Appointment Not Found Yet.......',time.strftime("%H:%M:%S",time.localtime()))
                    self.wait
                    self.driver.refresh()
                    
                else:
                    print('APPOINTMENT FOUND!.......',time.strftime("%H:%M:%S",time.localtime()))
                    #return 'No Appointment Available' not in self.driver.page_source
                    break

        
class PageTwo(BasePage):
        
    def get_best_appt_time(self):
        #the following loop is to combat the scenario where a timeslot is taken before bot takes it and we are redirected to same page again.
        self.text = self.driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[2]/div/div/table/tbody/tr[1]/th[3]').text
        while 'Select Time' in self.text:
            for i in range(len(self.timeslots)): #lets look at all our desired timeslots
                try: # and try to get one of them if available
                    self.driver.find_element_by_xpath('//input[@value="'+self.timeslots[i]+'"]/./following-sibling::td[@class = "remove123"]/input[@class = "confirmationseconddoseapptsremove"]').click()
                    break #break out of for loop when i'th desired appointment is chosen
                
                except NoSuchElementException: #if desires timeslots are all unavailable, just take the earliest one available
                    self.driver.find_element_by_css_selector("input[name='preRegTimeSlotID']").click() #select time
            try:
                self.click_next_button()
                self.wait
                self.driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[2]/div/div/table/tbody/tr[1]/th[3]') #are we still on the same page? if yes, then while loop will continue because 'text' is still the same
            
            except NoSuchElementException:
                self.text = 'Appointment Time Successfully Secured!'
                print(self.text+'.......',time.strftime("%H:%M:%S",time.localtime())) #changing text will break the while loop - this means we successfully changed pages

class PageThree(BasePage):
    
    def fill_personal_info(self):

        firstinput =  self.driver.find_element_by_xpath('//*[@id="firstName"]')
        firstinput.send_keys(self.first)
        lastinput =  self.driver.find_element_by_xpath('//*[@id="lastName"]')
        lastinput.send_keys(self.last)
        addressinput =  self.driver.find_element_by_xpath('//*[@id="address"]')
        addressinput.send_keys(self.address)
        codeinput =  self.driver.find_element_by_xpath('//*[@id="addrZip"]')
        codeinput.send_keys(self.code)
        numberinput =  self.driver.find_element_by_xpath('//*[@id="phone"]')
        numberinput2 =  self.driver.find_element_by_xpath('//*[@id="phoneConfirm"]')
        numberinput.send_keys(self.number)
        numberinput2.send_keys(self.number)
        emailinput =  self.driver.find_element_by_xpath('//*[@id="emailAddress"]')
        emailinput2 =  self.driver.find_element_by_xpath('//*[@id="emailAddressConfirm"]')
        emailinput.send_keys(self.email)
        emailinput2.send_keys(self.email)
        dateinput = self.driver.find_element_by_xpath('//*[@id="datepicker"]')
        dateinput.send_keys(self.dob)
        gender = self.driver.find_element_by_xpath('//*[@id="gender"]/option[2]')
        gender.click()
        print('Personal Info Page Complete.......',time.strftime("%H:%M:%S",time.localtime()))
        self.wait #wait before next function is called
        
class RemainingPages(BasePage):
    
    def fill_ethnicity_info(self):
        #selects 'no response' as answers
        race = self.driver.find_element_by_xpath('//*[@id="raceID"]/option[9]') 
        race.click()
        ethnicity = self.driver.find_element_by_xpath('//*[@id="ethnicityID"]/option[5]') 
        ethnicity.click()
        print('Ethnicity Info Page Complete.......',time.strftime("%H:%M:%S",time.localtime()))
        self.wait
    
    def fill_accomdations_info(self):
        transport = self.driver.find_element_by_xpath('//*[@id="transportationID"]/option[2]')
        transport.click()
        handicap = self.driver.find_element_by_xpath('//*[@id="needHandicapAccessID"]/option[2]')
        handicap.click()
        langassist = self.driver.find_element_by_xpath('//*[@id="needLanguageAssistanceID"]/option[2]')
        langassist.click()
        print('Accomodations Info Page Complete.......',time.strftime("%H:%M:%S",time.localtime()))
        self.wait
        
    def fill_screening_info(self):
        self.driver.find_element_by_xpath('//*[@id="0Y"]').click()
        print('Screening Info Page Complete.......',time.strftime("%H:%M:%S",time.localtime()))
        self.wait