import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from playsound import playsound

# Set up the WebDriver (ensure you have the correct path)
driver = webdriver.Chrome()  # Use webdriver.Firefox() if using Firefox

url = "https://medium.com/"

def check_for_available_tests():
    """Check if 'available tests' text is present on the page."""
    try:
        if "available tests" in driver.page_source.lower():
            return True
    except NoSuchElementException:
        pass
    return False

try:
    while True:
        driver.get(url)  # Open the webpage
        print(f"Page refreshed at {time.strftime('%Y-%m-%d %H:%M:%S')}")

        if check_for_available_tests():
            print("🎉 Available test slot found! Stopping refresh.")
            playsound("alert.mp3")  # Play alert sound
            break  # Stop the script

        time.sleep(300)  # Wait for 5 minutes (300 seconds) before refreshing
except KeyboardInterrupt:
    print("Stopped by user.")
finally:
    driver.quit()  # Ensure WebDriver quits properly
