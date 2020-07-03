# from selenium import webdriver
# import os
#
#
#
#
#
# project_folder_path = os.getcwd()
# driver_path = os.path.join(project_folder_path, r"Chrome_Drivers\chromedriver.exe")
#
#
# driver = webdriver.Chrome(driver_path)
# driver.maximize_window()
#
# def filling(user_info):
#     start_url = "https://www.points.homeoffice.gov.uk/gui-sponsor-jsf/SponsorHome.faces"
#     driver.get(start_url)
#
#     loginb = "/html/body/div/div/div[6]/div[1]/div/form/ul/li[3]/a"
#     driver.find_element_by_xpath(loginb).click()
#     login = df.iloc[0]["UserId"]
#     password = df.iloc[0]["Password"]
#
