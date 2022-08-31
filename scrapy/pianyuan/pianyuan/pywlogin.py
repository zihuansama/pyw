
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from time import sleep


from chaojiying import Chaojiying_Client
driver=webdriver.Chrome()

chaojiying=Chaojiying_Client('zihuansama', '11111', '938191')

if __name__ == '__main__':
    driver.get('https://www.pianyuan.org/User/login.html')
    driver.maximize_window()
    login_button1 = driver.find_element(By.CLASS_NAME, "header-login-entry")
    login_button1.click()
    # 此处记得sleep一下等登录界面加载出来，不然find_elements会找不到结果
    sleep(5)
    # bilibili登录页面的input没有class也没有id，只能用find_elements把所有input都找出来再取出
    # 也不知道为什么find_elements找出来的input有三个，返回一个列表，三个元素分别是主页搜索框，账号和密码输入框
    input_box = driver.find_elements(By.XPATH, '//input')
    input_box[0].send_keys("loginplz")
    input_box[1].send_keys("15377001677")
    input_box[2].send_keys("w526079.")
    # 去除特征码
    script = 'Object.defineProperty(navigator, "webdriver", {get: () => false,});'
    driver.execute_script(script)
    # 找到登陆按键(元素如下)
    # <div data-v-f69d8714="" class="universal-btn login-btn"> 登录 </div>
    login_button2 = driver.find_element(By.CLASS_NAME, "universal-btn.login-btn")
    login_button2.click()

    # 分析验证码
    sleep(3)
    # <div class="geetest_panel_box geetest_no_logo geetest_panelshowclick"
    # 直接获取图片有点麻烦，直接一个截图
    # 使用截图方法,并将当前页面的截图保存
    driver.save_screenshot("./aaa.png")


    # （先确认验证码图片左上和右下的坐标）
    # get_pic方法，分析验证码图片并点击
    def get_pic(classname):
        img1 = driver.find_element(By.CLASS_NAME, classname)
        # 验证码图片左上角坐标↓(返回字典，x为x值，y为y值)
        location_top1 = img1.location
        print(location_top1)
        # 图片的长和宽↓(返回一个字典，height为高，width为宽)
        size1 = img1.size
        print(size1)
        # 将图片长和宽加到location上获取location_bottom的坐标
        location_bottom1 = {}
        location_bottom1["x"] = location_top1["x"] + size1["width"]
        location_bottom1["y"] = location_top1["y"] + size1["height"]
        print(location_bottom1)
        # 建立元组储存图片坐标(*笔记本电脑的浏览器一般会缩放1.25倍，在rangle中的每个元素都要*1.25(ps:也可以在计算机设置里把显示缩放尺寸调成100%
        rangle = (
        int(location_top1["x"]), int(location_top1["y"]), int(location_bottom1["x"]), int(location_bottom1["y"]))
        print(rangle)
        # 打开图片(实例化一个Image对象
        i = Image.open("./aaa.png")
        name1 = "./result.png"
        # 使用Image的crop功能裁剪图像(报错tile cannot extend outside image超出范围)
        frame = i.crop(rangle)
        # 用save方法存储
        frame.save(name1)
        # 超级鹰用法cjy=chaojiying.Chaojiying_Client('', '', '')
        # cjy.Postpic(图片，图片类型码)['pic_str']
        pic1 = open("./result.png", "rb").read()
        # 结果中'pic_str': '235,144|79,154'
        print("————————————————————————————————————————————————————")
        location_words = cjy.PostPic(pic1, 9004)["pic_str"]
        print(location_words, type(location_words))
        # 对目标进行一个处理
        # 以"|"为分隔生成一个列表
        li1 = location_words.split("|")
        print("li1", li1)
        li2 = []
        for a in li1:
            li2.append(a.split(","))
        print(li2)

        # 点击目标点的坐标(
        action1 = ActionChains(driver)
        # move_to_element_with_offset(传入一个元素，到元素左上角坐标的x距离，y距离)
        img2 = driver.find_element(By.CLASS_NAME, "geetest_holder.geetest_silver")
        for li3 in li2:
            # 移动到该点并点击(为什么点不到？
            # 浏览器缩放问题？
            x = int(int(li3[0]))
            y = int(int(li3[1]))
            print("click", int(int(li3[0])), "and", int(int(li3[1])))
            # 此处的bug干掉我几百题分...Actionchains的动作是以上一步的动作为参照系进行动作的，因此如果下一个movebyoffset动作依然要以0，0坐标为起点，就要reset_actions
            # 下面这条代码不起作用，原因不明，把x,y分别除5测试发现似乎是参照系被识别成了元素中央，不懂
            # 改成了下下条，以0，0坐标为参照执行动作，成功
            # action1.move_to_element_with_offset(img1,x,y).click().perform()
            action1.move_by_offset(location_top1["x"] + x, location_top1["y"] + y).click().perform()
            action1.reset_actions()


    # 执行方法处理验证码
    get_pic("geetest_panel_next")
    # 找到验证码的确认按钮
    # <div class="geetest_commit_tip">确认</div>
    login_button3 = driver.find_element(By.CLASS_NAME, "geetest_commit_tip")
    login_button3.click()

    sleep(5)
    driver.quit()


