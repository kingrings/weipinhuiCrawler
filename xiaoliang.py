import requests
import json
import time

headers={
    'Cookie':'vip_cps_cuid=CU1676200402334c3488c38ae95dc889; vip_cps_cid=1676200402336_094ce28b0a8c625541c6f2d09ff71417; cps_share=cps_share; cps=adp%3A486g033v%3A%40_%401676200402335%3Amig_code%3A3d66c414ede3d2a96c2eb0f90dba93f3%3Aac014miuvs0000ycoeqjtcpkooawh854; PAPVisitorId=f07b580f8137d52bca5caa4f2e18e2a7; vip_new_old_user=1; vip_city_name=%E5%B9%BF%E5%B7%9E%E5%B8%82; user_class=a; mars_cid=1676200403374_2de062203eaff44a86758f9fa726c0d6; mars_sid=2f7f53f1735a4cbe0741907bbadd27f7; mars_pid=0; visit_id=B856FBF17A7FFB07AB77B59FE94EDBAD; VipUINFO=luc%3Aa%7Csuc%3Aa%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A0%7Cul%3A3105; vip_address=%257B%2522pname%2522%253A%2522%255Cu6c5f%255Cu82cf%255Cu7701%2522%252C%2522pid%2522%253A%2522103102%2522%252C%2522cname%2522%253A%2522%255Cu5e7f%255Cu5dde%255Cu5e02%2522%252C%2522cid%2522%253A%2522103102101%2522%257D; vip_province=103102; vip_province_name=%E6%B1%9F%E8%8B%8F%E7%9C%81; vip_city_code=103102101; vip_wh=VIP_SH; vip_ipver=31; vip_tracker_source_from=; VipDFT=0; pg_session_no=9; vip_access_times=%7B%22list%22%3A5%2C%22detail%22%3A1%7D',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
    'Referer': 'https://category.vip.com/suggest.php?keyword=%E6%8A%A4%E8%82%A4&ff=235|12|1|1',
    'Connection':'close'
}
url="https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103102101&client=pc&mobile_platform=1&province_id=103102&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1676200403374_2de062203eaff44a86758f9fa726c0d6&wap_consumer=a&uid=&abtestId=1871&mtmsRuleId=54886020&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=6&pageOffset=0&salePlatform=1&_=1676204206351"
html=requests.get(url,headers=headers)
#print(html.text)
start=html.text.index('{')
end=html.text.index('})')+1
json_data=json.loads(html.text[start:end])
#print(json_data['data']['products'])
product_ids=json_data['data']['products']
for product_id in product_ids:
    product_url='https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/module/list/v2?callback=getMerchandiseDroplets1&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103102101&client=pc&mobile_platform=1&province_id=103102&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1676200403374_2de062203eaff44a86758f9fa726c0d6&wap_consumer=a&productIds={}%2C&scene=rule_stream&standby_id=nature&extParams=%7B%22stdSizeVids%22%3A%22%22%2C%22preheatTipsVer%22%3A%223%22%2C%22couponVer%22%3A%22v2%22%2C%22exclusivePrice%22%3A%221%22%2C%22iconSpec%22%3A%222x%22%2C%22ic2label%22%3A1%2C%22superHot%22%3A1%2C%22bigBrand%22%3A%221%22%7D&context=%7B%22615%22%3A%221%22%2C%22872%22%3A%221%22%7D&_=1676204206352'.format(product_id['pid'])
    product_html = requests.get(product_url, headers=headers)
    product_start = product_html.text.index('{')
    product_end = product_html.text.index('})') + 1
    product_json_data = json.loads(product_html.text[product_start:product_end])
    product_info_data = product_json_data['data']['products'][0]
    # print(product_info_data)
    product_title = product_info_data['title']
    product_brand = product_info_data['brandShowName']
    product_price = product_info_data['price']['salePrice']
    print('商品名称：{}，品牌：{}，折后价格：{}'.format(product_title, product_brand, product_price))