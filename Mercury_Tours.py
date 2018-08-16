from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import xlrd
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
url = 'http://newtours.demoaut.com/'
driver.get(url)
driver.implicitly_wait(15)
driver.maximize_window()
path = "C:\\Users\\priya.singh\\Desktop\\Book1.xlsx"
driver.implicitly_wait(5)

def login():
    uname = driver.find_element_by_xpath("//input[@id='userNameInput']")
    uname.send_keys('priya.singh@ihsmarkit.com')
    pwd = driver.find_element_by_xpath("//input[@id='passwordInput']")
    pwd.send_keys('P@ssw0rd')
    btnSub = driver.find_element_by_xpath("//span[@id='submitButton']")
    btnSub.text
    btnSub.submit()

login()

im = driver.find_element_by_xpath("//img[@alt='Mercury Tours']")
if im:
    print("Image exists")

def register():
    reg = driver.find_element_by_link_text('REGISTER')
    reg.click()
    wb = xlrd.open_workbook(path)
    sheet = wb.sheet_by_index(0)
    fname = driver.find_element_by_xpath("//input[@name='firstName']")
    fname.send_keys(sheet.cell_value(1, 0))
    lname = driver.find_element_by_xpath("//*[contains(@name,'lastName')]")
    lname.send_keys(sheet.cell_value(1, 1))
    phn = driver.find_element_by_xpath("//input[@name='phone']")
    phn.send_keys(int(sheet.cell_value(1, 2)))
    email = driver.find_element_by_xpath("//input[@name='userName']")
    email.send_keys(sheet.cell_value(1, 3))
    add1 = driver.find_element_by_xpath("//input[@name='address1']")
    add1.send_keys(sheet.cell_value(1, 4))
    add2 = driver.find_element_by_xpath("//input[@name='address2']")
    add2.send_keys(sheet.cell_value(1, 5))
    uid = driver.find_element_by_xpath("//input[@id='email']")
    uid.send_keys(sheet.cell_value(1, 10))
    pwd2 = driver.find_element_by_xpath("//input[@name='password']")
    pwd2.send_keys(sheet.cell_value(1, 11))
    cpwd2 = driver.find_element_by_xpath("//input[@name='confirmPassword']")
    cpwd2.send_keys(sheet.cell_value(1, 12))
    btnS = driver.find_element_by_xpath("//input[@name='register']")
    btnS.submit()
    signIn = driver.find_element_by_xpath("//a[@href='mercurysignon.php']")
    signIn.click()

register()
#60
txt = driver.find_element_by_tag_name('body').text
if "Welcome" in txt:
    print("text exists in page")
else:
    raise AssertionError

def click_link():
    '''window_before = driver.window_handles[0]
    print(window_before)
    driver.find_element_by_link_text('Flights').click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    print(window_after)'''
    url1 = driver.current_url
    driver.get(url1)
    #open a link in a new window
    actions = ActionChains(driver)
    flight = driver.find_element_by_link_text('Flights')
    #open a new tab
    actions.key_down(Keys.CONTROL).click(flight).key_up(Keys.CONTROL).perform()
    #switch to new tab
    driver.switch_to_window(driver.window_handles[-1])
    print(driver.window_handles)
    '''driver.get(url)
    driver.switch_to_window(driver.window_handles[0])
    cruise = driver.find_element_by_link_text('Cruises')
    actions.key_down(Keys.CONTROL).click(cruise).key_up(Keys.CONTROL).perform()
    driver.switch_to_window(driver.window_handles[1])
    driver.close()
    driver.switch_to_window(driver.window_handles[0])'''

click_link()
'''element = driver.find_elements_by_xpath("//input[type='radio']")
s = getattr("element", "type")
#handling radio button and dropdown under flight module
#def assert_element_is_radio(element):
if s != 'radio':
    raise BaseException("Elwement passed is not a radio button")
else:
    print("it is a radio element")'''

elem = driver.find_element_by_name('tripType')
if elem.is_selected():
    print("roundtrip is selected")
    elem.click()
    #assert elem.text=='Round Trip'
else:
    print("Element not selected.")

elem2 = driver.find_element_by_xpath("//input[@type='radio'][@value='oneway']")
elem2.click()
if elem2.is_selected():
    print("one way selected")
    print(elem2.text)
else:
    print("not selected")

'''passenger = driver.find_element_by_xpath("//select[@name='passCount']")
all_optn = passenger.find_element_by_tag_name('option')
for op in all_optn:
    print("value is"+op.get_attribute('value'))
    op.click()
#assert_element_is_radio(element)'''

passenger = Select(driver.find_element_by_name('passCount'))
i = passenger.select_by_visible_text('4')

'''if passenger.is_multiple():
    passenger.select_by_index('0')
    passenger.select_by_index('1')
else:
    print("you can only select one option")'''

#is_active = "checked" in roundt.__getattribute__("")
#oneway = driver.find_element_by_css_selector("input#tripType[value='oneway']").click()
#port = driver.find_elements_by_xpath("//select[@name='fromPort']")[0].get_attribute('value')

#list all elements in dropdown
port = driver.find_element_by_name('fromPort')
options = [a for a in port.find_elements_by_tag_name('option')]
for element in options:
    print(element.get_attribute('value'))

portp = Select(driver.find_element_by_name('fromPort'))
i = portp.select_by_visible_text('Portland')

fromMonth = Select(driver.find_element_by_name('fromMonth'))
m = fromMonth.select_by_visible_text('September')
fromDate = Select(driver.find_element_by_name('fromDay'))
d = fromDate.select_by_visible_text('14')
arriveIn = Select(driver.find_element_by_name('toPort'))
a = arriveIn.select_by_visible_text('Seattle')
tomonth = Select(driver.find_element_by_name("toMonth"))
tm = tomonth.select_by_visible_text('November')
today =Select(driver.find_element_by_name("toDay"))
td = today.select_by_visible_text('30')
serviceClass = driver.find_element_by_xpath("//input[@type='radio'][@value='Business']")
airline = Select(driver.find_element_by_name("airline"))
ai = airline.select_by_visible_text("Unified Airlines")
cont = driver.find_element_by_xpath("//input[@type='image'][@name='findFlights']")
cont.submit()

#depart details
unified_radio = driver.find_elements_by_xpath("//input[@type='radio'][@value='Unified Airlines$563$125$11:24']")
unified_radio.click()

#return details
return_details = driver.find_elements_by_xpath("//input[@type='radio'][@value='Blue Skies Airlines$651$99$14:30']")
return_details.click()
