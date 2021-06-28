#Created By : Mohamed Gamal
#WB:+201016017092
from selenium import webdriver
import geckodriver_autoinstaller
from fake_useragent import UserAgent, UserAgentError
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import  random
import platform
OSNAME = platform.system()
print(OSNAME)
count =  7
sa=0
def sub():
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    print(bcolors.OKBLUE + """
    Jimmy<
    Yb  dP  dP"Yb  88   88 888888 88   88 88""Yb 888888
     YbdP  dP   Yb 88   88   88   88   88 88__dP 88__
      8P   Yb   dP Y8   8P   88   Y8   8P 88""Yb 88""
     dP     YbodP  `YbodP'   88   `YbodP' 88oodP 888888
    """ + bcolors.ENDC)

    global count ,sa
    file = open('Datas.txt','r')
    emails = file.readlines()
    emailw = emails[sa]
    email = emailw.split(':')[0]
    passw = emailw.split(':')[1]
    agensy = open('useragents.txt', 'r')
    agens = agensy.readlines()
    agent = agens[sa].replace('\n','')
    print(agent)

    profile =webdriver.FirefoxProfile()
    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('useAutomationExtension', False)
    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference("intl.accept_languages", "en-us")
    profile.set_preference("browser.download.folderList",2)
    profile.set_preference("browser.download.manager.showWhenStarting",False)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv,application/pdf,application/csv,application/vnd.ms-excel")
    profile.set_preference("browser.download.manager.showAlertOnComplete",False)
    profile.set_preference("browser.download.manager.showAlertOnComplete",False)
    profile.set_preference("browser.download.manager.showWhenStartinge",False)
    profile.set_preference("browser.download.panel.shown",False)
    profile.set_preference("browser.download.useToolkitUI",True)
    profile.set_preference("pdfjs.disabled", True)
    profile.set_preference("pdfjs.firstRun", False)
    profile.set_preference("browser.privatebrowsing.autostart", True)
    profile.set_preference("media.autoplay.default", 0)
    profile.set_preference("media.volume_scale", "0.0")
    profile.set_preference("excludeSwitches", "enable-automation")
    profile.set_preference("excludeSwitches", "enable-logging")
    profile.set_preference('useAutomationExtension', False)
    profile.set_preference('disable_capture', True)
    profile.set_preference("webdriver.firefox.marionette", False)
    profile.set_preference('javascript.enabled', False)
    profile.set_preference("general.useragent.override", str(agent))
    viewport = ['2560,1440', '1920,1080', '1440,900',
                '1536,864', '1366,768', '1280,1024', '1024,768']
    profile.set_preference("--window-size=", str(viewport))

    width = ['2560','1920','1440','1536','1336','1366','1280','1242','1024']
    higth = ['1440','1080','1090','900','800','864','765','896','1024']


    profile.update_preferences()

    list = ['youtube','facebook','eviletour','egypt','paris','suez','amrica','greec','germany','netflix','kwit','football','worldwide','instgram']
    search = random.choice(list)
    proxies=  open('Proxe.txt','r')
    proxie = proxies.readlines()
    proxs = proxie[count]
    ip = proxs.split(':')[0]
    port = proxs.split(':')[1].replace('\n','')
    print(port)
    print(ip)


    desired = webdriver.DesiredCapabilities.FIREFOX
    #desired['marionette'] = Falsex

    desired['proxy'] = {
        "proxyType": "MANUAL",
        "httpProxy": proxs,
        "ftpProxy": proxs,
        "sslProxy": proxs
    }
    print(proxs)
    driver = webdriver.Firefox(firefox_profile=profile,desired_capabilities=desired)

    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    driver.get('https://www.youtube.com/results?search_query='+search)
    time.sleep(5)
    try:
        try:
            driver.find_element_by_xpath('//button[@aria-label="Agree to the use of cookies and other data for the purposes described"]').click()
        except:
            driver.find_element_by_xpath('//input[@aria-label="Agree to the use of cookies and other data for the purposes described"]').click()
    except:
        pass

    try:
        try:
            driver.find_element_by_xpath('//button[@value="I agree"]').click()
        except:
            driver.find_element_by_xpath('//input[@value="I agree"]').click()
    except:
        pass




    time.sleep(3)
    driver.get('https://www.google.com')
    try:
        driver.find_element_by_xpath('//input[@role="combobox"]').click()
        driver.find_element_by_xpath('//input[@role="combobox"]').send_keys(search)
        driver.find_element_by_xpath('//input[@role="combobox"]').send_keys(Keys.ENTER)
        driver.find_element_by_xpath('//input[@role="combobox"]').click()
        driver.find_element_by_xpath('//input[@role="combobox"]').send_keys(Keys.ENTER)
    except:
        driver.get('https://www.google.com/search?q='+search)
        pass
    time.sleep(5)
    try:
        driver.find_element_by_xpath('//a[@target="_top"]').click()
    except:
        driver.get('https://accounts.google.com/signin')

    time.sleep(4)
    try:
        try:
            driver.find_element_by_id('identifierId').send_keys(email)
            time.sleep(4)
            driver.find_element_by_id('identifierNext').click()
            time.sleep(3)
        except:
            driver.find_element_by_id('Email').send_keys(email)
            time.sleep(4)
            driver.find_element_by_id('next').click()
            time.sleep(3)
        try:
            ps = driver.find_element_by_name('password')
            time.sleep(3)
            ps.send_keys(passw)
            time.sleep(3)
        except:
            driver.find_element_by_id('password').send_keys(passw)
            time.sleep(3)
            driver.find_element_by_id('submit').click()
            time.sleep(6)

        try:
            driver.find_element_by_id('passwordNext').click()
            time.sleep(6)

        except:
            pass
    except:
        try:
            ps.send_keys(Keys.ENTER)
        except:
            pass

    print('here')

    sits = ['https://web.telegram.org/', 'https://web.whatsapp.com/',
            'https://blog.whatsapp.com/whats-app-web/?lang=en',
            'https://faq.whatsapp.com/web/download-and-installation/about-whatsapp-web-and-desktop/?lang=en',
            'https://www.facebook.com/', 'https://www.sits.eu/', 'https://www.thefreedictionary.com/sits',
            'https://www.thefreedictionary.com/sits',
            'https://www.tribalgroup.com/solutions/student-information-systems/sits-vision', 'https://sits.lk/',
            'https://sits.lk/', 'https://www.sits.eu/en/typy-mebli/sofas', 'https://www.sits.eu/en/typy-mebli/sofas',
            'https://www.sits-group.ch/', 'https://www.sits-group.ch/', 'https://www.servicedeskshow.com/',
            'https://acronyms.thefreedictionary.com/SITS', 'https://acronyms.thefreedictionary.com/SITS',
            'https://acronyms.thefreedictionary.com/SITS', 'https://www.sits-group.ch/', 'https://www.sits-group.ch/',
            'https://sits.ceu.edu/urd/sits.urd/run/siw_lgn', 'https://sits.ceu.edu/urd/sits.urd/run/siw_lgn',
            'https://www.taskers.com/brands/sits', 'https://www.taskers.com/brands/sits',
            'https://www.taskers.com/brands/sits', 'https://sits.london/', 'https://sits.london/']
    site = random.choice(sits)

    driver.get('https://accounts.google.com/ServiceLogin?service=youtube')


    url = 'https://www.youtube.com/results?search_query=%D8%B4%D8%B1%D8%AD+%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D8%AC.+IFb+%D9%82%D8%B3%D8%A7%D8%A6%D9%85+Facebook'
    driver.get(url)
    timesf= [9,10,11,12,13,14,15,16]
    time.sleep(random.choice(timesf))
    driver.execute_script('document.querySelectorAll(\'[title="شرح برنامج. IFb قسائم Facebook"]\')[0].click();')
    time.sleep(random.choice(timesf))

    times = [50,30,60,40,20,80,120]
    timer = random.choice(times)
    print(timer)
    time.sleep(timer)

    try:
        driver.execute_script('document.querySelectorAll(\'[aria-label="يمكنك الاشتراك في قناة Mohamed Gamal."]\')[2].click();')
        print('yeahoo')
    except:
        try:
            driver.execute_script('document.querySelectorAll(\'[aria-label="Subscribe to Mohamed Gamal."]\')[2].click();')
        except:
            pass

        pass
    time.sleep(4)

    driver.quit()
    timesf = [4, 6, 1, 2, 3, 4, 5, 5]
    time.sleep(random.choice(timesf))
    count = count+1
    sa =sa +1
    sub()


sub()



