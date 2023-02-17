#https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103102101&client=pc&mobile_platform=1&province_id=103102&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1676200403374_2de062203eaff44a86758f9fa726c0d6&wap_consumer=a&uid=&abtestId=1872&mtmsRuleId=54886020&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=0&pageOffset=0&salePlatform=1&_=1676200443456
#https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103102101&client=pc&mobile_platform=1&province_id=103102&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1676200403374_2de062203eaff44a86758f9fa726c0d6&wap_consumer=a&uid=&abtestId=1871&mtmsRuleId=54886020&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=6&pageOffset=0&salePlatform=1&_=1676200443458
#/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103102101&client=pc&mobile_platform=1&province_id=103102&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1676200403374_2de062203eaff44a86758f9fa726c0d6&wap_consumer=a&uid=&abtestId=1872&mtmsRuleId=54886020&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=0&pageOffset=0&salePlatform=1&_=1676200443456
#/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103102101&client=pc&mobile_platform=1&province_id=103102&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1676200403374_2de062203eaff44a86758f9fa726c0d6&wap_consumer=a&uid=&abtestId=1871&mtmsRuleId=54886020&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=6&pageOffset=0&salePlatform=1&_=1676200443458
import time
from selenium import webdriver
t=time.time()
print(int(round(t*1000)))
#-6003018852883328690
#-6003018649296998595
#-6003018348883310067
#-6003018348883310067
#-6003018880153380875
#-6003018649296998595   1355
#-6003018360648719649
#

driver=webdriver.Chrome()
vip='https://list.vip.com/autolist.html?rule_id=54886020&title=%E7%BA%AF%E8%89%B2%E7%BE%8E%E8%A3%99&refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome'
driver.get(vip)
sustain=driver.find_element_by_xpath('//*[@id="J-operPrice-hd"]')

#webdriver.ActionChains(driver).move_to_element(sustain).perform()

driver.find_element_by_xpath('//*[@id="J-operPrice-hd"]').click()

num = driver.find_element_by_xpath('//*[@id="J_wrap_pro_add"]/div[1]/a/div[2]/div[1]/div[1]/div[2]/text()')
print(num.text)