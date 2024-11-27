from selenium import webdriver

# Open Chrome browser
driver = webdriver.Chrome()
# Keep the browser open
driver.get(" https://youtu.be/iTmlw3vQPSs")


# Keep the browser open until user closes it manually
input("Press Enter to close the browser...")
# Close the browser
driver.quit()
