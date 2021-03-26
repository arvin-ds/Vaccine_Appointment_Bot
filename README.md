# Vaccine_Appointment_Bot
The Python bot that finds and registers vaccine appointments

## Summary
This python script uses the Unittest library to carry out a Selenium-based scrpit that waits for, and finally registers a vaccine appointment from a specfic registration site. All info about the site was removed before uploading to github.

### main.py
Responsible for defining the necessary patient info and carrying out the Selenium scripts in pages.py on a chrome webdriver

### pages.py
Instructions carried out by the bot on each webpage including a never-end wait for an appointment to become available. Uses a handful of loops and try/excepts to interact with webpages and register appointments (at desired timeslots, if possible) without error(s) (ie. backwards webpage redirection).

### locators.py
HTML button locators that the bot clicks to advance registration pages.
