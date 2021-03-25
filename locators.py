from selenium.webdriver.common.by import By

class Buttons(object):

    PRIMARY_BUTTON = (By.CLASS_NAME, 'btn.btn-primary')
    #NEXT_BUTTON = (By.CLASS_NAME, 'btn.btn-primary.next-btn')
    REGISTER_BUTTON = (By.CLASS_NAME, 'btn.btn-primary.register-btn')
    
    CONTINUE_BUTTON = (By.XPATH,'//button[contains(text(), "Continue")]')
    NEXT_BUTTON = (By.XPATH, '//button[contains(text(), "Next")]')
    #REGISTER_BUTTON = (By.XPATH, '//button[contains(text(), "Register")]')