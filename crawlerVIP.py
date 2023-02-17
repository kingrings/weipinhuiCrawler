import requests
import json
import time
from selenium import webdriver

result=0

driver=webdriver.Chrome()
vip='https://list.vip.com/autolist.html?rule_id=54886020&title=%E7%BA%AF%E8%89%B2%E7%BE%8E%E8%A3%99&refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome'
driver.get(vip)

minPrice=driver.find_element_by_class_name('J_priceMin').send_keys(0)
maxPrice=driver.find_element_by_class_name('J_priceMax').send_keys(50)

above=driver.find_element_by_xpath('//*[@id="J_inputLayout"]/div/span[1]/input')
webdriver.ActionChains(driver).move_to_element(above).perform()
driver.find_element_by_xpath('//*[@id="J_inputLayout"]/div/i[2]').click()

dress=[[['纯色美裙'], ['54886020']], [['高腰美裙'], ['54886032']], [['半截裙'], ['55521161']], [['中长款裙'], ['54886023']], [['碎花美裙'], ['54886027']], [['百褶美裙'], ['54886022']], [['格纹美裙'], ['54886016']], [['吊带美裙'], ['54886031']], [['真丝美裙'], ['54886021']], [['旗袍美裙'], ['54886017']], [['牛仔美裙'], ['54886028']], [['大码裙装'], ['54879403']]]
hot=[[['加厚保暖'], ['62221605']], [['冬季尚新'], ['61971038']], [['针织衫'], ['53986298']], [['唯品独家'], ['61971053']], [['休闲裤'], ['53986312']], [['连衣裙'], ['53986307']], [['女式毛衣'], ['55515022']], [['外套'], ['53986308']], [['牛仔裤'], ['53986316']], [['衬衫'], ['53986299']], [['T恤'], ['53986306']], [['套装'], ['53986294']], [['半截裙'], ['53986314']], [['妈妈装'], ['53986804']]]
coat=[[['衬衫'], ['53986299']], [['T恤'], ['53986306']], [['外套'], ['53986308']], [['针织衫'], ['53986298']], [['风衣'], ['53986296']], [['西服'], ['53986315']], [['卫衣'], ['53986297']], [['马夹'], ['53986639']], [['打底衫'], ['59968549']], [['背心'], ['53986303']], [['大衣'], ['53986305']], [['皮衣和皮草'], ['53986295']], [['毛衣'], ['55515022']], [['羽绒服'], ['53986313']]]
trousers=[[['运动裤'], ['58811183']], [['西裤'], ['55518075']], [['连体裤'], ['58811586']], [['打底裤'], ['53986311']], [['休闲裤'], ['53986312']], [['牛仔裤'], ['53986316']], [['短裤'], ['53986751']], [['直筒裤'], ['55516985']], [['工装裤'], ['55518074']], [['小脚裤'], ['55517801']], [['阔腿裤'], ['55516984']], [['哈伦裤'], ['55517076']], [['半截裙'], ['53986314']]]
underwear=[[['纯棉内裤'], ['59495926']], [['女士家居服'], ['59495911']], [['纯棉家居服'], ['59495921']], [['塑身内衣'], ['59495929']], [['女士睡袍'], ['58325065']], [['美背文胸'], ['59495679']], [['薄杯文胸'], ['59493551']], [['运动文胸'], ['59495397']], [['女士内裤'], ['59450382']], [['无钢圈'], ['59450613']], [['聚拢'], ['59450718']], [['女袜'], ['59450379']], [['裤袜'], ['59450380']], [['女士吊带/打底背心'], ['59450384']], [['文胸套装'], ['59450750']]]



t=time.time()
T=int(round(t*1000))

headers={
    'Cookie':'mars_cid=1676468557909_88ad8e73c54c63fc4d01321aebe6e4aa; mars_sid=6701d9251e97374c36fc94958dd48d4b; user_class=a; VipUINFO=luc%3Aa%7Csuc%3Aa%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A0%7Cul%3A3105; vip_first_visitor=1; vip_address=%257B%2522pid%2522%253A%2522103102%2522%252C%2522cid%2522%253A%2522103102101%2522%252C%2522pname%2522%253A%2522%255Cu6c5f%255Cu82cf%255Cu7701%2522%252C%2522cname%2522%253A%2522%255Cu5357%255Cu4eac%255Cu5e02%2522%257D; vip_province=103102; vip_province_name=%E6%B1%9F%E8%8B%8F%E7%9C%81; vip_city_name=%E5%8D%97%E4%BA%AC%E5%B8%82; vip_city_code=103102101; vip_wh=VIP_SH; vip_ipver=31; vip_access_times=%7B%22list%22%3A1%7D; pg_session_no=1; vip_tracker_source_from=; mars_pid=0; visit_id=0BE76D618274D6F6AF72DFDF2C32BA5D',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
    'Referer': 'https://category.vip.com/suggest.php?keyword=%E6%8A%A4%E8%82%A4&ff=235|12|1|1',
    'Connection':'close'
}


url="https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103102101&client=pc&mobile_platform=1&province_id=103102&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1676471105494_271a305606bc0a0c089bedbc05e5462a&wap_consumer=a&uid=&abtestId=1872&mtmsRuleId=54886020&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=0&pageOffset=0&salePlatform=1&priceRange=-50&_={}".format(T)
html=requests.get(url,headers=headers)
#print(html.text)
start=html.text.index('{')
end=html.text.index('})')+1
json_data=json.loads(html.text[start:end])
print(json_data['data']['products'])
product_ids=json_data['data']['products']
temp=[]
for i in range(len(product_ids)):
    temp.append(int(product_ids[i]['pid']))

n=12
for x in range(0,(n+1)*120,120):
    urlOffset ="https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103102101&client=pc&mobile_platform=1&province_id=103102&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1676115414402_a7342faa478349a4d9384c3962f40178&wap_consumer=a&uid=&abtestId=1872&mtmsRuleId=54886020&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=0&pageOffset={}&salePlatform=1&priceRange=-50&_={}".format(x,T)
    html=requests.get(url,headers=headers)
    startOffset = html.text.index('{')
    endOffset = html.text.index('})') + 1
    json_data_offset=json.loads(html.text[startOffset:endOffset])
    product_ids_offset=json_data_offset['data']['products']
    temp_offset=[]
    #ans=set(product_ids['pid']) ^ set(product_ids_offset['pid'])
    for i in range(len(product_ids_offset)):
        temp_offset.append(int(product_ids_offset[i]['pid']))
    print(temp_offset)
    for y in temp_offset:
        if y not in temp:
            temp.append(y)
    #more=set(temp)^set(temp_offset)
    #temp.append(list(more))


driver.find_element_by_xpath('//*[@id="J-operSales-hd"]').click()
#https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103102101&client=pc&mobile_platform=1&province_id=103102&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1676433695440_a5d1888bd9b0e7922d6b4f886feee5dd&wap_consumer=a&uid=&abtestId=1872&mtmsRuleId=54886020&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=1&pageOffset=0&salePlatform=1&priceRange=-50&_=1676507973599
#https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103102101&client=pc&mobile_platform=1&province_id=103102&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1676433695440_a5d1888bd9b0e7922d6b4f886feee5dd&wap_consumer=a&uid=&abtestId=1872&mtmsRuleId=54886020&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=2&pageOffset=0&salePlatform=1&priceRange=-50&_=1676507973604
for x in range(0,(n+1)*120,120):
    url_sales = f'https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103102101&client=pc&mobile_platform=1&province_id=103102&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1676433695440_a5d1888bd9b0e7922d6b4f886feee5dd&wap_consumer=a&uid=&abtestId=1871&mtmsRuleId=54886020&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=6&pageOffset={x}&salePlatform=1&priceRange=-50&_={T}'
    html = requests.get(url_sales, headers=headers)
    startOffset = html.text.index('{')
    endOffset = html.text.index('})') + 1
    json_data_offset_sales = json.loads(html.text[startOffset:endOffset])
    product_ids_offset_sales = json_data_offset_sales['data']['products']
    temp_offset_sales=[]
    for i in range(len(product_ids_offset_sales)):
        temp_offset_sales.append(int(product_ids_offset_sales[i]['pid']))
    print(temp_offset_sales)
    for y in temp_offset_sales:
        if y not in temp:
            temp.append(y)


driver.find_element_by_xpath('//*[@id="J-operPrice-hd"]').click()
for x in range(0,(n+1)*120,120):
    url_price_low = f'https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103102101&client=pc&mobile_platform=1&province_id=103102&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1676433695440_a5d1888bd9b0e7922d6b4f886feee5dd&wap_consumer=a&uid=&abtestId=1872&mtmsRuleId=54886020&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=1&pageOffset={x}&salePlatform=1&priceRange=-50&_={T}'
    html = requests.get(url_price_low, headers=headers)
    startOffset = html.text.index('{')
    endOffset = html.text.index('})') + 1
    json_data_offset_sales = json.loads(html.text[startOffset:endOffset])
    product_ids_offset_sales = json_data_offset_sales['data']['products']
    temp_offset_sales=[]
    for i in range(len(product_ids_offset_sales)):
        temp_offset_sales.append(int(product_ids_offset_sales[i]['pid']))
    print(temp_offset_sales)
    for y in temp_offset_sales:
        if y not in temp:
            temp.append(y)


driver.find_element_by_xpath('//*[@id="J-operPrice-hd"]').click()
for x in range(0,(n+1)*120,120):
    url_price_high = f'https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103102101&client=pc&mobile_platform=1&province_id=103102&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1676433695440_a5d1888bd9b0e7922d6b4f886feee5dd&wap_consumer=a&uid=&abtestId=1872&mtmsRuleId=54886020&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=2&pageOffset={x}&salePlatform=1&priceRange=-50&_={T}'

    html = requests.get(url_price_high, headers=headers)
    startOffset = html.text.index('{')
    endOffset = html.text.index('})') + 1
    json_data_offset_sales = json.loads(html.text[startOffset:endOffset])
    product_ids_offset_sales = json_data_offset_sales['data']['products']
    temp_offset_sales=[]
    for i in range(len(product_ids_offset_sales)):
        temp_offset_sales.append(int(product_ids_offset_sales[i]['pid']))
    print(temp_offset_sales)
    for y in temp_offset_sales:
        if y not in temp:
            temp.append(y)


driver.find_element_by_xpath('//*[@id="J-operdiscount-hd"]').click()
for x in range(0,(n+1)*120,120):
    url_discount_low = f'https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103102101&client=pc&mobile_platform=1&province_id=103102&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1676433695440_a5d1888bd9b0e7922d6b4f886feee5dd&wap_consumer=a&uid=&abtestId=1872&mtmsRuleId=54886020&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=3&pageOffset={x}&salePlatform=1&priceRange=-50&_={T}'
    html = requests.get(url_discount_low, headers=headers)
    startOffset = html.text.index('{')
    endOffset = html.text.index('})') + 1
    json_data_offset_sales = json.loads(html.text[startOffset:endOffset])
    product_ids_offset_sales = json_data_offset_sales['data']['products']
    temp_offset_sales=[]
    for i in range(len(product_ids_offset_sales)):
        temp_offset_sales.append(int(product_ids_offset_sales[i]['pid']))
    print(temp_offset_sales)
    for y in temp_offset_sales:
        if y not in temp:
            temp.append(y)

driver.find_element_by_xpath('//*[@id="J-operdiscount-hd"]').click()
for x in range(0,(n+1)*120,120):
    url_discount_high = f'https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103102101&client=pc&mobile_platform=1&province_id=103102&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1676433695440_a5d1888bd9b0e7922d6b4f886feee5dd&wap_consumer=a&uid=&abtestId=1872&mtmsRuleId=54886020&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=4&pageOffset={x}&salePlatform=1&priceRange=-50&_={T}'
    html = requests.get(url_discount_high, headers=headers)
    startOffset = html.text.index('{')
    endOffset = html.text.index('})') + 1
    json_data_offset_sales = json.loads(html.text[startOffset:endOffset])
    product_ids_offset_sales = json_data_offset_sales['data']['products']
    temp_offset_sales=[]
    for i in range(len(product_ids_offset_sales)):
        temp_offset_sales.append(int(product_ids_offset_sales[i]['pid']))
    print(temp_offset_sales)
    for y in temp_offset_sales:
        if y not in temp:
            temp.append(y)





result+=len(temp)
print(result)



# urlOffset="https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103102101&client=pc&mobile_platform=1&province_id=103102&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1676200403374_2de062203eaff44a86758f9fa726c0d6&wap_consumer=a&uid=&abtestId=1871&mtmsRuleId=54886020&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=6&pageOffset=120&salePlatform=1&_={}".format(T)
# product_idsOffset=json_data['data']['products']
# if product_idsOffset[0]['pid']==product_ids[0]['pid']:
#     driver.find_element_by_xpath('//*[@id="J-operSales-hd"]').click()
#     htmlSales=requests.get(url,headers=headers)
#     start = html.text.index('{')
#     end = html.text.index('})') + 1
#     json_data = json.loads(html.text[start:end])
#     print(json_data['data']['products'])
#     product_ids = json_data['data']['products']
#     result += len(product_ids)
#
# print(result)
#
# for product_id in product_ids:
#     product_url='https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/module/list/v2?callback=getMerchandiseDroplets1&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103102101&client=pc&mobile_platform=1&province_id=103102&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1676200403374_2de062203eaff44a86758f9fa726c0d6&wap_consumer=a&productIds={}%2C&scene=rule_stream&standby_id=nature&extParams=%7B%22stdSizeVids%22%3A%22%22%2C%22preheatTipsVer%22%3A%223%22%2C%22couponVer%22%3A%22v2%22%2C%22exclusivePrice%22%3A%221%22%2C%22iconSpec%22%3A%222x%22%2C%22ic2label%22%3A1%2C%22superHot%22%3A1%2C%22bigBrand%22%3A%221%22%7D&context=%7B%22615%22%3A%221%22%2C%22872%22%3A%221%22%7D&_=1676204206352'.format(product_id['pid'])
#     product_html = requests.get(product_url, headers=headers)
#     product_start = product_html.text.index('{')
#     product_end = product_html.text.index('})') + 1
#     product_json_data = json.loads(product_html.text[product_start:product_end])
#     product_info_data = product_json_data['data']['products'][0]
#     # print(product_info_data)
#     product_title = product_info_data['title']
#     product_brand = product_info_data['brandShowName']
#     product_price = product_info_data['price']['salePrice']
#     print('商品名称：{}，品牌：{}，折后价格：{}'.format(product_title, product_brand, product_price))