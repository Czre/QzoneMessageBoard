# coding:utf-8
from selenium import webdriver
from xlwt import Workbook

import time


# 登录QQ空间
def get_liuyanban(select_qq, qq, password, path):
    driver = webdriver.PhantomJS(executable_path=path)
    driver.maximize_window()
    driver.get('http://user.qzone.qq.com/{}/334'.format(select_qq))
    time.sleep(5)
    try:
        driver.find_element_by_id('login_div')
        a = True
    except:
        a = False
    if a == True:
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()  # 选择用户名框
        driver.find_element_by_id('u').send_keys(qq)
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys(password)
        driver.find_element_by_id('login_button').click()
        time.sleep(3)
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
        b = True
    except:
        b = False
    if b == True:
        driver.switch_to.frame('app_canvas_frame')
        page = i = j = 1
        if int(driver.find_element_by_id('cnt').text) > 10:
            # 留言板10条分一页,拿取留言板标签的留言板数目
            items = driver.find_elements_by_css_selector('.mod_pagenav_count > .c_tx')
            # 拿到页码数组
            page = int(items[len(items) - 1].text)
            # 拿到总页数
        book = Workbook()
        sheet1 = book.add_sheet('Sheet 1')
        sheet1.write(0, 0, '楼层')
        sheet1.write(0, 1, 'QQ')
        sheet1.write(0, 2, '昵称')
        sheet1.write(0, 3, '时间')
        sheet1.write(0, 4, '内容')
        sheet1.col(0).width = 10 * 256
        sheet1.col(1).width = 11 * 256
        sheet1.col(2).width = 20 * 256
        sheet1.col(3).width = 18 * 256
        sheet1.col(4).width = 255 * 256
        while i <= page:
            time.sleep(5)
            # 留言板的获取格式
            content = driver.find_elements_by_css_selector('.cont')
            stime = driver.find_elements_by_css_selector('.reply_wrap')
            name = driver.find_elements_by_css_selector('.c_tx.q_namecard')
            number = driver.find_elements_by_css_selector('.c_tx3.floor')
            for t, c, n, num in zip(stime, content, name, number):
                sheet1.write(j, 0, num.text)
                sheet1.write(j, 1, n.get_attribute('uin'))
                sheet1.write(j, 2, n.text)
                sheet1.write(j, 3, t.find_element_by_tag_name('span').text)
                sheet1.write(j, 4, c.find_element_by_xpath(".//table/tbody/tr[1]/td[1]").text)
                j += 1
            i += 1
            if i > page:
                continue
            orders = driver.find_elements_by_css_selector('.mod_pagenav_main > .c_tx')
            orders[len(orders) - 1].click()
            print("已写入" + str(i - 1) + "页数据,还剩" + str(page - i + 1) + "页数据未爬取")
        name = str(select_qq) + "留言板.xls"
        book.save(name)
        print("Excel已写入" + str(j - 1) + "条数据")
        print("==========完成================")
        driver.close()
        driver.quit()
