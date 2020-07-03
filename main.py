import XlsxToCsvFilter
from selenium import webdriver
import os
import pandas as pd
import time
address = "users/excel/examples.xlsx"
destination = "users/csv/examples.csv"
df = XlsxToCsvFilter.filter_columns(XlsxToCsvFilter.to_csv(address, destination))





# -----------------------------------
# FF def filling...
#



project_folder_path = os.getcwd()
driver_path = os.path.join(project_folder_path, r"Chrome_Drivers\chromedriver.exe")


driver = webdriver.Chrome(driver_path)
driver.maximize_window()





# df = pd.read_csv("users/csv/examples.csv")

start_url = "https://www.points.homeoffice.gov.uk/gui-sponsor-jsf/SponsorHome.faces"
driver.get(start_url)

loginformbp = "/html/body/div/div/div[6]/div[1]/div/form/ul/li[3]/a"

# huy = "/html/body/div/div/div[6]/div[1]/div"
# in_huy = "form/ul/li[3]/a"
#
# element = driver.find_element_by_xpath(huy)
# element.find_element_by_xpath(in_huy).click()

driver.find_element_by_xpath(loginformbp).click()
user = df.iloc[0]["UserId"]
userp = "/html/body/div/div/div[6]/div[2]/div[1]/form[2]/div/div[2]/span[2]/input"
password = df.iloc[0]["Password"]
passwordp = "/html/body/div/div/div[6]/div[2]/div[1]/form[2]/div/div[3]/span[2]/input"
driver.find_element_by_xpath(userp).send_keys(user)
driver.find_element_by_xpath(passwordp).send_keys(password)
loginbp = "/html/body/div/div/div[6]/div[2]/div[1]/form[2]/span/input"

driver.find_element_by_xpath(loginbp).click()

time.sleep(0.3)

apply_licbp = "/html/body/div/div/div[6]/div[2]/div[1]/form/div[1]/p[2]/b/a"

driver.find_element_by_xpath(apply_licbp).click()

# -----------------------------------
# First page
time.sleep(0.5)

tier2n = (list(df.iloc[0]["Tier2":"Tier4"]))
tier2 = tier2n[1:len(tier2n)-1]
tier4n =(list(df.iloc[0]["Tier4":"Tier5"]))
tier4 = tier4n[1:len(tier4n)-1]
tier5n =(list(df.iloc[0]["Tier5":"SLN"]))
tier5 = tier5n[1:len(tier5n)-1]

all_names = list(df.columns)
tier2_names = all_names[all_names.index("Tier2")+1:all_names.index("Tier4")]
tier4_names = all_names[all_names.index("Tier4")+1:all_names.index("Tier5")]
tier5_names = all_names[all_names.index("Tier5")+1:all_names.index("SLN")]
tier4_names = list(map(lambda x: x if x.find(".1")==-1 else x[:x.find(".1")], tier4_names))

# e = driver.find_elements_by_xpath("//*[contains(text(),'"+ "General"+ "')]")
# e[1].click()
# e[0].click()

for i in range(len(tier2)):
    if tier2[i] == 1:
        x = tier2_names[i]
        driver.find_element_by_xpath("//*[contains(text(),'"+ x+ "')]").click()
for i in range(len(tier5)):
    if tier5[i] == 1:
        x = tier5_names[i]
        click_list = driver.find_element_by_xpath("//*[contains(text(),'"+ x+ "')]").click()

for i in range(len(tier4)):
    if tier4[i] == 1:
        x = tier4_names[i]
        click_list = driver.find_elements_by_xpath("//*[contains(text(),'"+ x+ "')]")
        if len(click_list)==1:
            click_list[0].click()
        elif len(click_list)==2:
            click_list[1].click()

sln = df.iloc[0]["SLN"]
if sln==0:
    nobp = "/html/body/div/div/div[6]/div[2]/div[1]/form/div[20]/span[2]/table/tbody/tr[2]/td/label"
    driver.find_element_by_xpath(nobp).click()
else:
    yesbp = "/html/body/div/div/div[6]/div[2]/div[1]/form/div[20]/span[2]/table/tbody/tr[1]/td/label"
    driver.find_element_by_xpath(yesbp).click()
    slnp = "/html/body/div/div/div[6]/div[2]/div[1]/form/div[21]/span[2]/input"
    driver.find_element_by_xpath(slnp).send_keys(str(sln))


next_pageb = "/html/body/div/div/div[6]/div[2]/div[1]/form/div[23]/span/input[1]"
driver.find_element_by_xpath(next_pageb).click()


# --------------------------------------
# Second page

names_secp = all_names[all_names.index("SLN")+1:]

# for i in range(len(names_secp)):
#     fillf = names_secp[i]
#     info = df.iloc[0][fillf]
#     fillfp = driver.find_element_by_xpath("//div[//*[contains(text(),'"+ fillf+ "')]]")
#     fillfp.find_elements_by_class_name("fieldInput")[0].send_keys(info)


# forms_place = "/html/body/div/div/div[6]/div[2]/div[1]"
# block = driver.find_element_by_xpath(forms_place)
# elements = block.find_elements_by_tag_name("input")
# elements = elements[1:]
# # elements[8].send_keys("wsferhjofew")
# for i in range(len(names_secp)):
#     elements[i].send_keys(df.iloc[0][names_secp[i]])



# 1
# for i in range(len(names_secp)):
#     elements = driver.find_elements_by_tag_name("input")
#     # elements[i].send_keys(df.iloc[0][names_secp[i]])
#     # elements[i].send_keys(df.iloc[0][names_secp[i]])
#     print(len(elements))
#
# #  3
#
# WTF
#
#
# ttt = "/html/body/div/div/div[6]/div[2]/div[1]/form/div[1]/div[2]/span[2]/input"
# driver.find_element_by_xpath(ttt).send_keys("huy")


org = "/html/body/div/div/div[6]/div[2]/div[1]/form/div[1]/div[2]/span[2]/input"
add = "/html/body/div/div/div[6]/div[2]/div[1]/form/div[1]/div[3]/span[2]/input"
cit = "/html/body/div/div/div[6]/div[2]/div[1]/form/div[1]/div[6]/span[2]/input"
con = "/html/body/div/div/div[6]/div[2]/div[1]/form/div[1]/div[7]/span[2]/input"
pos = "/html/body/div/div/div[6]/div[2]/div[1]/form/div[1]/div[8]/span[2]/input"
tel = "/html/body/div/div/div[6]/div[2]/div[1]/form/div[1]/div[10]/span[2]/input"

paths = [org,add,cit,con,pos,tel]

for i in range(len(names_secp)):
    driver.find_element_by_xpath(paths[i]).send_keys(str(df.iloc[0][names_secp[i]]))
    # elements[i].send_keys(df.iloc[0][names_secp[i]])
    # elements[i].send_keys(df.iloc[0][names_secp[i]])


next_pageb2p = "/html/body/div/div/div[6]/div[2]/div[1]/form/div[5]/span/input[1]"
driver.find_element_by_xpath(next_pageb2p).click()

# ---------------------------------
