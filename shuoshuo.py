# coding:utf-8
from selenium import webdriver
from xlwt import Workbook
import time

# 登录QQ空间
def get_shuoshuo(select_qq,qq,password,path):
    driver = webdriver.PhantomJS(executable_path=path)
    driver.maximize_window()
    driver.get('http://user.qzone.qq.com/{}/311'.format("查询的QQ号码"))
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
        driver.find_element_by_id('u').send_keys("登录的QQ号")
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys("登录的QQ号密码")
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
        if int(driver.find_element_by_css_selector('.feed_num > .c_tx.goProfile').text) > 20:

            items = driver.find_elements_by_css_selector('.mod_pagenav_main > .c_tx')
            page = int(items[len(items) - 2].text)
        book = Workbook()
        sheet1 = book.add_sheet('Sheet 1')
        sheet1.write(0, 0, '时间')
        sheet1.col(0).width = 15 * 256
        sheet1.col(1).width = 255 * 256
        sheet1.write(0, 1, '内容')
        while i <= page:
            time.sleep(5)
            # 说说的获取格式
            content = driver.find_elements_by_css_selector('.box.bgr3')
            stime = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
            for con, sti, in zip(content, stime):
                sheet1.write(j, 0, sti.text)
                sheet1.write(j, 1, con.find_element_by_css_selector('.content').text)
                j += 1
            i += 1
            if i > page:
                continue
            orders = driver.find_elements_by_css_selector('.mod_pagenav_main > .c_tx')
            orders[len(orders) - 1].click()
            print("已写入" + str(i - 1) + "页数据,还剩" + str(page - i + 1) + "页数据未爬取")
        name = str(select_qq) + "说说.xls"
        book.save(name)
        print("Excel已写入" + str(j - 1) + "条数据")
        print("==========完成================")
        driver.close()
        driver.quit()