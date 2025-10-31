from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ✅ set path to your ChromeDriver
driver = webdriver.Chrome(executable_path="C:\\Users\\Sravani Press\\Downloads\\chromedriver-win64\\chromedriver.exe")

# ✅ open your Laravel login page
driver.get("http://127.0.0.1:8000/login")

# ✅ fill email and password fields
driver.find_element(By.NAME, "email").send_keys("test@example.com")
driver.find_element(By.NAME, "password").send_keys("password123")

# wait for a few seconds (so you can see it)
time.sleep(3)

# ✅ close the browser
driver.quit()
