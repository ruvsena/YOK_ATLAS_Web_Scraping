import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import pandas as pd
from pk_2019 import iki_yıllık
#from pk_2019 import lisans
from pk_2021 import lisans
user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
driver_path = r"C:\\Users\\pc\\Desktop\\chromedriver.exe"
chrome_service = Service(driver_path)
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
browser =webdriver.Chrome(service=chrome_service, options=chrome_options)

original_df = pd.DataFrame()
for p in range(1,5):
    try:
        program_kodu=lisans[p]
        browser.get("https://yokatlas.yok.gov.tr/2021/lisans.php?y="+str(program_kodu))

        wait = WebDriverWait(browser,4)
        wait1 = WebDriverWait(browser,4)

        try:
            reklamı_kapat=wait.until(EC.presence_of_all_elements_located(
                       (By.XPATH, "/html/body/div[3]/div/span")))
        except:
            pass

        first_column=[]
        iki=[]
        uc=[]

        b1=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[2]/div[1]/a/h4")
        b1.click()

        for sayi in range(1,7):
           tablo = wait.until(EC.presence_of_all_elements_located(
                   (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[1]/tbody/tr["+str(sayi)+"]/td[1]")))
           tablo1 = wait.until(EC.presence_of_all_elements_located(
                   (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[1]/tbody/tr["+str(sayi)+"]/td[2]")))
           iki.append(str([i.text for i in tablo]))
           uc.append(str([i.text for i in tablo1]))


        for sayi in range(1, 11):
           tablo2 = wait.until(EC.presence_of_all_elements_located(
               (By.XPATH,
                "/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[2]/tbody/tr["+str(sayi)+"]/td[1]")))
           tablo21 = wait.until(EC.presence_of_all_elements_located(
               (By.XPATH,
                "/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[2]/tbody/tr["+str(sayi)+"]/td[2]")))
           iki.append(str([i.text for i in tablo2]))
           uc.append(str([i.text for i in tablo21]))

        for sayi in range(1, 10):
            tablo3 = wait.until(EC.presence_of_all_elements_located(
               (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[3]/tbody/tr["+str(sayi)+"]/td[1]")))
            tablo31 = wait.until(EC.presence_of_all_elements_located(
               (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[3]/tbody/tr["+str(sayi)+"]/td[2]")))
            iki.append(str([i.text for i in tablo3]))
            uc.append(str([i.text for i in tablo31]))
        ######

        b2=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[3]/div[1]/a")
        b2.click()

        s3=1
        s4=1

        t21=[]
        t22=[]
        t23=[]
        t24=[]
        t25=[]
        t26=[]
        for k in range(1,7):
            t1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[3]/div[2]/div/div/table/thead/tr[1]/th["+str(k)+"]")))

            t2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[3]/div[2]/div/div/table/tbody/tr[1]/td["+str(k)+"]")))
            t3,t4=[],[]
            if s3==1 or s3== 2:
                t3 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[3]/div[2]/div/div/table/tbody/tr[2]/td["+str(s3)+"]")))
                t4 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[3]/div[2]/div/div/table/tbody/tr[3]/td["+str(s3)+"]")))

            s3=s3+0.5
            if s3>=3:
                s3=3

            t5,t6 = [],[]
            if s4 == 1or s4 ==2 or s4 ==3:
                t5 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[3]/div[2]/div/div/table/tbody/tr[4]/td["+str(s4)+"]")))
                t6 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[3]/div[2]/div/div/table/tbody/tr[5]/td["+str(s4)+"]")))
            s4=s4+1
            if s4 >= 4:
                s4=4
            t21.append(str([i.text for i in t1]))
            t22.append(str([i.text for i in t2]))
            t23.append(str([i.text for i in t3]))
            t24.append(str([i.text for i in t4]))
            t25.append(str([i.text for i in t5]))
            t26.append(str([i.text for i in t6]))
        ####

        b3=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[4]/div[1]/a/h4")
        b3.click()
        t31=[]
        t32=[]
        t33=[]
        for c in range(1,4):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[4]/div[2]/div/div/table/thead/tr/th["+str(c)+"]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[4]/div[2]/div/div/table/tbody/tr[1]/td["+str(c)+"]")))
            c3 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[4]/div[2]/div/div/table/tbody/tr[2]/td["+str(c)+"]")))
            t31.append(str([i.text for i in c1]))
            t32.append(str([i.text for i in c2]))
            t33.append(str([i.text for i in c3]))

        #####

        b4=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[1]/a/h4")
        b4.click()
        t41=[]
        t42=[]
        t43=[]
        t44=[]
        for c in range(1,5):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[1]/thead/tr/th["+str(c)+"]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[1]/tbody/tr[1]/td["+str(c)+"]")))
            c3 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[1]/tbody/tr[2]/td["+str(c)+"]")))
            c4 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[1]/tbody/tr[3]/td["+str(c)+"]")))
            t41.append(str([i.text for i in c1]))
            t42.append(str([i.text for i in c2]))
            t43.append(str([i.text for i in c3]))
            t44.append(str([i.text for i in c4]))

        t41_2=[]
        t42_2=[]
        t43_2=[]

        c14 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[2]/thead/tr/th[1]")))
        c24 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[2]/thead/tr/th[2]")))
        c34 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[2]/thead/tr/th[3]")))
        t41_2.append(str([i.text for i in c14]))
        t42_2.append(str([i.text for i in c24]))
        t43_2.append(str([i.text for i in c34]))

        for c in range(1,10):
            try:
                c1 = wait1.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[2]/tbody/tr["+str(c)+"]/td[1]")))
                c2 = wait1.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[2]/tbody/tr["+str(c)+"]/td[2]")))
                c3 = wait1.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[2]/tbody/tr["+str(c)+"]/td[3]")))
                t41_2.append(str([i.text for i in c1]))
                t42_2.append(str([i.text for i in c2]))
                t43_2.append(str([i.text for i in c3]))
            except:
                break
    #######

        b5=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[6]/div[1]/a/h4")
        b5.click()

        t51=[]
        t52=[]
        t53=[]
        c15 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[6]/div[2]/div/div/table/thead/tr/th[1]")))
        c25 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[6]/div[2]/div/div/table/thead/tr/th[2]")))
        c35 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[6]/div[2]/div/div/table/thead/tr/th[3]")))
        t51.append(str([i.text for i in c15]))
        t52.append(str([i.text for i in c25]))
        t53.append(str([i.text for i in c35]))

        for c in range(1,82):
            try:
                c1 = wait1.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[6]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
                c2 = wait1.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[6]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
                c3 = wait1.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[6]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[3]")))
                t51.append(str([i.text for i in c1]))
                t52.append(str([i.text for i in c2]))
                t53.append(str([i.text for i in c3]))
            except:
                break

        ######
        b6=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[7]/div[1]/a/h4")
        b6.click()

        t61=[]
        t62=[]
        t63=[]

        c16 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/thead/tr/th[1]")))
        c26 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/thead/tr/th[2]")))
        c36 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/thead/tr/th[3]")))
        t61.append(str([i.text for i in c16]))
        t62.append(str([i.text for i in c26]))
        t63.append(str([i.text for i in c36]))


        for c in range(1,7):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
            c3 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[3]")))
            t61.append(str([i.text for i in c1]))
            t62.append(str([i.text for i in c2]))
            t63.append(str([i.text for i in c3]))

        ######
        b7=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[8]/div[1]/a/h4")
        b7.click()
        t71 = []
        t72 = []
        t73 = []
        c1 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/thead/tr/th[1]")))
        c2 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/thead/tr/th[2]")))
        c3 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/thead/tr/th[3]")))
        t71.append(str([i.text for i in c1]))
        t72.append(str([i.text for i in c2]))
        t73.append(str([i.text for i in c3]))
        for c in range(1,21):
            try:
                c1 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
                c2 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
                c3 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[3]")))
                t71.append(str([i.text for i in c1]))
                t72.append(str([i.text for i in c2]))
                t73.append(str([i.text for i in c3]))
            except:
                break


        ######
        b8=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[9]/div[1]/a/h4")
        b8.click()
        t81 = []
        t82 = []
        t83 = []

        c1 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/thead/tr/th[1]")))
        c2 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/thead/tr/th[1]")))
        c3 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/thead/tr/th[1]")))
        t81.append(str([i.text for i in c1]))
        t82.append(str([i.text for i in c2]))
        t83.append(str([i.text for i in c3]))


        for c in range(1,21):
            try:
                c1 = wait.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
                c2 = wait.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
                c3 = wait.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[3]")))
                t81.append(str([i.text for i in c1]))
                t82.append(str([i.text for i in c2]))
                t83.append(str([i.text for i in c3]))
            except:
                break
        ###

        b9=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[10]/div[1]/a/h4")
        b9.click()

        t911 = []
        t921 = []
        t931 = []
        try:
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table/thead/tr[2]/th[1]")))
            c2 = wait1.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table/thead/tr[2]/th[2]")))
            c3 = wait1.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table/thead/tr[2]/th[3]")))
            t911.append(str([i.text for i in c1]))
            t921.append(str([i.text for i in c2]))
            t931.append(str([i.text for i in c3]))
        except:
            pass


        for c in range(1,10):
            try:
                try:
                    c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table/tbody/tr/td[1]")))
                    c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table/tbody/tr/td[2]")))
                    c3 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table/tbody/tr/td[3]")))
                    t911.append(str([i.text for i in c1]))
                    t921.append(str([i.text for i in c2]))
                    t931.append(str([i.text for i in c3]))
                except:
                    c1 = wait.until(EC.presence_of_all_elements_located(
                                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
                    c2 = wait1.until(EC.presence_of_all_elements_located(
                                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
                    c3 = wait1.until(EC.presence_of_all_elements_located(
                                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[3]")))
                    t911.append(str([i.text for i in c1]))
                    t921.append(str([i.text for i in c2]))
                    t931.append(str([i.text for i in c3]))
            except:
                pass
        t912=[]
        t922=[]
        t932=[]

        try:
            c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[2]/thead/tr[2]/th[1]")))
            c2 = wait1.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[2]/thead/tr[2]/th[2]")))
            c3 = wait1.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[2]/thead/tr[2]/th[3]")))

            t912.append(str([i.text for i in c1]))
            t922.append(str([i.text for i in c2]))
            t932.append(str([i.text for i in c3]))
        except:
            pass
        for c in range(1,4):
            try:
                try:
                    c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[2]/tbody/tr/td[1]")))
                    c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[2]/tbody/tr/td[2]")))
                    c3 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[2]/tbody/tr/td[3]")))
                    t912.append(str([i.text for i in c1]))
                    t922.append(str([i.text for i in c2]))
                    t932.append(str([i.text for i in c3]))
                except:
                    c1 = wait.until(EC.presence_of_all_elements_located(
                                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[2]/tbody/tr["+str(c)+"]/td[1]")))
                    c2 = wait1.until(EC.presence_of_all_elements_located(
                                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[2]/tbody/tr["+str(c)+"]/td[2]")))
                    c3 = wait1.until(EC.presence_of_all_elements_located(
                                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[2]/tbody/tr["+str(c)+"]/td[3]")))
                    t912.append(str([i.text for i in c1]))
                    t922.append(str([i.text for i in c2]))
                    t932.append(str([i.text for i in c3]))
            except:
                pass
        t913 = []
        t923 = []
        t933 = []
        try:
            c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[3]/thead/tr[2]/th[1]")))
            c2 = wait1.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[3]/thead/tr[2]/th[2]")))
            c3 = wait1.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[3]/thead/tr[2]/th[3]")))
            t913.append(str([i.text for i in c1]))
            t923.append(str([i.text for i in c2]))
            t933.append(str([i.text for i in c3]))
        except:
            pass

        try:
            c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[3]/tbody/tr/td[1]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[3]/tbody/tr/td[2]")))
            c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[3]/tbody/tr/td[3]")))

            t913.append(str([i.text for i in c1]))
            t923.append(str([i.text for i in c2]))
            t933.append(str([i.text for i in c3]))

        except:
            pass

        #########

        b10=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[11]/div[1]/a/h4")
        b10.click()

        t101=[]
        t102=[]
        t103=[]
        t104=[]

        c11 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[11]/div[2]/div/div/table/thead/tr[2]/th[1]")))
        c21 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[11]/div[2]/div/div/table/thead/tr[2]/th[2]")))
        c31 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[11]/div[2]/div/div/table/thead/tr[2]/th[3]")))
        c41 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[11]/div[2]/div/div/table/thead/tr[2]/th[4]")))

        t101.append(str([i.text for i in c11]))
        t102.append(str([i.text for i in c21]))
        t103.append(str([i.text for i in c31]))
        t104.append(str([i.text for i in c41]))

        for c in range(1,120):
            try:
                c1 = wait.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[11]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
                c2 = wait1.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[11]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
                c3 = wait1.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[11]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[3]")))
                c4 = wait1.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[11]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[4]")))
                t101.append(str([i.text for i in c1]))
                t102.append(str([i.text for i in c2]))
                t103.append(str([i.text for i in c3]))
                t104.append(str([i.text for i in c4]))
            except:
                break
        #######

        b11=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[12]/div[1]/a/h4")
        b11.click()

        t111=[]
        t112=[]
        t113=[]
        t114=[]

        for c in range(1,3):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[12]/div[2]/div/div/table/thead/tr/th["+str(c)+"]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[12]/div[2]/div/div/table/tbody/tr[1]/td["+str(c)+"]")))
            c3 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[12]/div[2]/div/div/table/tbody/tr[2]/td["+str(c)+"]")))
            c4 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[12]/div[2]/div/div/table/tbody/tr[3]/td["+str(c)+"]")))
            t111.append(str([i.text for i in c1]))
            t112.append(str([i.text for i in c2]))
            t113.append(str([i.text for i in c3]))
            t114.append(str([i.text for i in c4]))

        ########

        b12=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[13]/div[1]/a/h4")
        b12.click()

        t121=[]
        t122=[]
        t123=[]
        for c in range(1,5):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[13]/div[2]/div/div/table[1]/thead/tr/th["+str(c)+"]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[13]/div[2]/div/div/table[1]/tbody/tr[1]/td["+str(c)+"]")))
            c3 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[13]/div[2]/div/div/table[1]/tbody/tr[2]/td["+str(c)+"]")))
            t121.append(str([i.text for i in c1]))
            t122.append(str([i.text for i in c2]))
            t123.append(str([i.text for i in c3]))

        #########

        #yukarı çık
        yuk_cık=browser.find_element(By.XPATH,"/html/body/span/a").click()
        sleep(5)
        #########

        b13=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[1]/div[1]/a/h4")
        b13.click()

        t131=[]
        t132=[]
        for c in range(1,11):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[1]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[1]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
            t131.append(str([i.text for i in c1]))
            t132.append(str([i.text for i in c2]))

        ######yerleşenlerin net ortalamaları

        b14=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[2]/div[1]/a/h4")
        b14.click()

        t141=[]
        t142=[]
        t143=[]

        c1 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/thead/tr/th[1]")))
        c2 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/thead/tr/th[2]")))
        c3 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/thead/tr/th[3]")))

        t141.append(str([i.text for i in c1]))
        t142.append(str([i.text for i in c2]))
        t143.append(str([i.text for i in c3]))


        for c in range(1,11):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
            c3 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[3]")))
            t141.append(str([i.text for i in c1]))
            t142.append(str([i.text for i in c2]))
            t143.append(str([i.text for i in c3]))

        ######

        b15=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[3]/div[1]/a/h4")
        b15.click()

        t151=[]
        t152=[]
        t153=[]
        t154=[]
        for c in range(1,4):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[3]/div[2]/div/div/table/thead/tr/th["+str(c)+"]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[3]/div[2]/div/div/table/tbody/tr[1]/td["+str(c)+"]")))
            c3 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[3]/div[2]/div/div/table/tbody/tr[2]/td["+str(c)+"]")))
            c4 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[3]/div[2]/div/div/table/tbody/tr[3]/td["+str(c)+"]")))

            t151.append(str([i.text for i in c1]))
            t152.append(str([i.text for i in c2]))
            t153.append(str([i.text for i in c3]))
            t154.append(str([i.text for i in c4]))

        t151_1=[]
        t152_1=[]
        t153_1=[]
        t154_1=[]
        for c in range(1,4):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[3]/div[2]/div/div/div[2]/table/thead/tr/th["+str(c)+"]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[3]/div[2]/div/div/div[2]/table/tbody/tr[1]/td["+str(c)+"]")))
            c3 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[3]/div[2]/div/div/div[2]/table/tbody/tr[2]/td["+str(c)+"]")))
            c4 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[3]/div[2]/div/div/div[2]/table/tbody/tr[3]/td["+str(c)+"]")))
            t151_1.append(str([i.text for i in c1]))
            t152_1.append(str([i.text for i in c2]))
            t153_1.append(str([i.text for i in c3]))
            t154_1.append(str([i.text for i in c4]))

        #######

        b16=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[4]/div[1]/a/h4")
        b16.click()

        t161=[]
        t162=[]
        t163=[]
        for c in range(1,4):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/table/thead/tr/th["+str(c)+"]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/table/tbody/tr[1]/td["+str(c)+"]")))
            c3 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/table/tbody/tr[2]/td["+str(c)+"]")))
            t161.append(str([i.text for i in c1]))
            t162.append(str([i.text for i in c2]))
            t163.append(str([i.text for i in c3]))

        t161_1=[]
        t162_1=[]
        t163_1=[]
        for c in range(1,4):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/div[2]/table/thead/tr/th["+str(c)+"]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/div[2]/table/tbody/tr[1]/td["+str(c)+"]")))
            c3 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/div[2]/table/tbody/tr[2]/td["+str(c)+"]")))
            t161_1.append(str([i.text for i in c1]))
            t162_1.append(str([i.text for i in c2]))
            t163_1.append(str([i.text for i in c3]))

        ######

        b17=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[5]/div[1]/a/h4")
        b17.click()

        t1711=[]
        t1721=[]
        for c in range(1,4):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[1]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[2]")))
            t1711.append(str([i.text for i in c1]))
            t1721.append(str([i.text for i in c2]))

        t1712=[]
        t1722=[]
        t1732=[]
        for c in range(4,7):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[1]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[2]")))
            c3 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[3]")))
            t1712.append(str([i.text for i in c1]))
            t1722.append(str([i.text for i in c2]))
            t1732.append(str([i.text for i in c3]))


        t1713=[]
        t1723=[]

        c1 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[2]/thead/tr/th[1]")))
        c2 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[2]/thead/tr/th[2]")))

        t1713.append(str([i.text for i in c1]))
        t1723.append(str([i.text for i in c2]))


        for c in range(1,11):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[2]/tbody/tr["+str(c)+"]/td[1]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[2]/tbody/tr["+str(c)+"]/td[2]")))

            t1713.append(str([i.text for i in c1]))
            t1723.append(str([i.text for i in c2]))

        #########

        b18=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[6]/div[1]/a/h4")
        b18.click()


        t181=[]
        t182=[]
        for c in range(1,6):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[1]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[2]")))
            t181.append(str([i.text for i in c1]))
            t182.append(str([i.text for i in c2]))


        t181_2=[]
        t182_2=[]
        c1 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table[2]/tbody/tr/td[1]/table/thead/tr/th[1]")))
        c2 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table[2]/tbody/tr/td[1]/table/thead/tr/th[2]")))
        t181_2.append(str([i.text for i in c1]))
        t182_2.append(str([i.text for i in c2]))

        for cc in range(1,3):
            for c in range(1,13):
                c1 = wait.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table[2]/tbody/tr/td["+str(cc)+"]/table/tbody/tr["+str(c)+"]/td[1]")))
                c2 = wait.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table[2]/tbody/tr/td["+str(cc)+"]/table/tbody/tr["+str(c)+"]/td[2]")))
                t181_2.append(str([i.text for i in c1]))
                t182_2.append(str([i.text for i in c2]))


        ##########
        b19=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[7]/div[1]/a/h4")
        b19.click()

        t191=[]
        t192=[]
        for c in range(1,6):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[7]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[7]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
            t191.append(str([i.text for i in c1]))
            t192.append(str([i.text for i in c2]))
        #########

        b20=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[8]/div[1]/a/h4")
        b20.click()

        t201=[]
        t202=[]
        for c in range(1,5):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[8]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[8]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
            t201.append(str([i.text for i in c1]))
            t202.append(str([i.text for i in c2]))
        ###########

        b21=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[1]/a/h4")
        b21.click()

        t2111=[]
        t2121=[]
        c1 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table[1]/thead/tr[2]/th[1]")))
        c2 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table[1]/thead/tr[2]/th[2]")))

        t2111.append(str([i.text for i in c1]))
        t2121.append(str([i.text for i in c2]))


        for c in range(1,150):
            try:
                c1 = wait.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[1]")))
                c2 = wait1.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[2]")))
                t2111.append(str([i.text for i in c1]))
                t2121.append(str([i.text for i in c2]))
            except:
                break

        t2112=[]
        t2122=[]

        c1 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table[2]/thead/tr[2]/th[1]")))
        c2 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table[2]/thead/tr[2]/th[2]")))
        t2112.append(str([i.text for i in c1]))
        t2122.append(str([i.text for i in c2]))

        for c in range(1,100):
            try:
                c1 = wait.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table[2]/tbody/tr["+str(c)+"]/td[1]")))
                c2 = wait1.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table[2]/tbody/tr["+str(c)+"]/td[2]")))
                t2112.append(str([i.text for i in c1]))
                t2122.append(str([i.text for i in c2]))
            except:
                break
        ##########

        b22=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[10]/div[1]/a/h4")
        b22.click()

        t221=[]
        t222=[]
        c1 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/thead/tr/th[1]")))
        c2 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/thead/tr/th[2]")))

        t221.append(str([i.text for i in c1]))
        t222.append(str([i.text for i in c2]))

        for c in range(1,82):
            try:
                c1 = wait.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
                c2 = wait1.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
                t221.append(str([i.text for i in c1]))
                t222.append(str([i.text for i in c2]))
            except:
                break

        ##############

        b23=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[11]/div[1]/a/h4")
        b23.click()

        t231=[]
        t232=[]
        ac23_3 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[11]/div[2]/div/div/table/thead/tr/th[1]")))
        ac23_4 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[11]/div[2]/div/div/table/thead/tr/th[2]")))

        t231.append(str([i.text for i in ac23_3]))
        t232.append(str([i.text for i in ac23_4]))


        for c in range(1,8):
            try:
                c1 = wait.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[11]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
                c2 = wait.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[11]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
                t231.append(str([i.text for i in c1]))
                t232.append(str([i.text for i in c2]))
            except:
                break
        ###########
        b24=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[12]/div[1]/a/h4")
        b24.click()

        t241=[]
        t242=[]
        c1 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[12]/div[2]/div/div/table/thead/tr/th[1]")))
        c2 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[12]/div[2]/div/div/table/thead/tr/th[2]")))
        t241.append(str([i.text for i in c1]))
        t242.append(str([i.text for i in c2]))

        for c in range(1,82):
            try:
                c1 = wait.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[12]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
                c2 = wait1.until(EC.presence_of_all_elements_located(
                            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[12]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
                t241.append(str([i.text for i in c1]))
                t242.append(str([i.text for i in c2]))
            except:
               break

        ##############
        b25=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[13]/div[1]/a/h4")
        b25.click()

        t251=[]
        t252=[]
        c1 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,
                     "/html/body/div[2]/div[1]/div[8]/div/div[13]/div[2]/div/div/table/thead/tr/th[1]")))
        c2 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,
                     "/html/body/div[2]/div[1]/div[8]/div/div[13]/div[2]/div/div/table/thead/tr/th[2]")))
        t251.append(str([i.text for i in c1]))
        t252.append(str([i.text for i in c2]))

        for c in range(1,10):
            try:
                c1 = wait.until(EC.presence_of_all_elements_located(
                            (By.XPATH,
                             "/html/body/div[2]/div[1]/div[8]/div/div[13]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
                c2 = wait1.until(EC.presence_of_all_elements_located(
                            (By.XPATH,
                             "/html/body/div[2]/div[1]/div[8]/div/div[13]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
                t251.append(str([i.text for i in c1]))
                t252.append(str([i.text for i in c2]))
            except:
                break

        #####burdan sonrakiler yeşil alanda olanlar


        y1=browser.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[1]/div[1]/a/h4")
        y1.click()

        yt1=[]
        yt2=[]
        c1 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/table/thead/tr/th[1]")))
        c2 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/table/thead/tr/th[2]")))
        yt1.append(str([i.text for i in c1]))
        yt2.append(str([i.text for i in c2]))


        for c in range(1,5):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
            yt1.append(str([i.text for i in c1]))
            yt2.append(str([i.text for i in c2]))
        #######
        y4 = browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div[1]/div[1]/a/h4")
        y4.click()

        yt41 = []
        yt42 = []
        yt43 = []
        try:
            c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div/table/thead/tr/th[1]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div/table/thead/tr/th[2]")))
            c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div/table/thead/tr/th[3]")))
            yt41.append(str([i.text for i in c1]))
            yt42.append(str([i.text for i in c2]))
            yt43.append(str([i.text for i in c3]))
        except:
            pass
        for c in range(1, 4):
            try:
                try:
                    c1 = wait1.until(EC.presence_of_all_elements_located(
                        (By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div/table/tbody/tr/td[1]")))
                    c2 = wait1.until(EC.presence_of_all_elements_located(
                        (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr/td[2]")))
                    c3 = wait1.until(EC.presence_of_all_elements_located(
                        (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr/td[3]")))
                except:
                    c1 = wait1.until(EC.presence_of_all_elements_located(
                        (By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div/table/tbody/tr[" + str(
                            c) + "]/td[1]")))
                    c2 = wait1.until(EC.presence_of_all_elements_located(
                        (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[" + str(
                            c) + "]/td[2]")))
                    c3 = wait1.until(EC.presence_of_all_elements_located(
                        (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[" + str(
                            c) + "]/td[3]")))
                yt41.append(str([i.text for i in c1]))
                yt42.append(str([i.text for i in c2]))
                yt43.append(str([i.text for i in c3]))
            except:
                break
        ##########
        y2=browser.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[1]/a/h4")
        y2.click()

        yt21=[]
        yt22=[]
        yt23=[]
        c1 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/table/thead/tr/th[1]")))
        c2 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/table/thead/tr/th[2]")))
        c3 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/table/thead/tr/th[3]")))
        yt21.append(str([i.text for i in c1]))
        yt22.append(str([i.text for i in c2]))
        yt23.append(str([i.text for i in c3]))

        for c in range(1,4):
            c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
            c3 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[3]")))
            yt21.append(str([i.text for i in c1]))
            yt22.append(str([i.text for i in c2]))
            yt23.append(str([i.text for i in c3]))

        ######

        ####


        y5=browser.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[1]/a/h4")
        y5.click()

        yt51=[]
        yt52=[]
        yt53=[]
        c1 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/div/table[1]/thead/tr[2]/th[1]")))
        c2 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/div/table[1]/thead/tr[2]/th[2]")))
        c3 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/div/table[1]/thead/tr[2]/th[3]")))
        yt51.append(str([i.text for i in c1]))
        yt52.append(str([i.text for i in c2]))
        yt53.append(str([i.text for i in c3]))

        for c in range(1,3):
            try:
                try:
                    c1 = wait1.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/div/table[1]/tbody/tr/td[1]")))
                    c2 = wait1.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/div/table[1]/tbody/tr/td[2]")))
                    c3 = wait1.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/div/table[1]/tbody/tr/td[3]")))
                    yt51.append(str([i.text for i in c1]))
                    yt52.append(str([i.text for i in c2]))
                    yt53.append(str([i.text for i in c3]))
                except:
                    c1 = wait1.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[1]")))
                    c2 = wait1.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[2]")))
                    c3 = wait1.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[3]")))
                    yt51.append(str([i.text for i in c1]))
                    yt52.append(str([i.text for i in c2]))
                    yt53.append(str([i.text for i in c3]))
            except:
                break




        yt511=[]
        yt521=[]
        yt531=[]
        c1 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/div/table[2]/thead/tr[2]/th[1]")))
        c2 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/div/table[2]/thead/tr[2]/th[2]")))
        c3 = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/div/table[2]/thead/tr[2]/th[3]")))
        yt511.append(str([i.text for i in c1]))
        yt521.append(str([i.text for i in c2]))
        yt531.append(str([i.text for i in c3]))

        for c in range(1,3):
            try:
                try:
                    c1 = wait1.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/div/table[2]/tbody/tr/td[1]")))
                    c2 = wait1.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/div/table[2]/tbody/tr/td[2]")))
                    c3 = wait1.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/div/table[2]/tbody/tr/td[3]")))
                    yt511.append(str([i.text for i in c1]))
                    yt521.append(str([i.text for i in c2]))
                    yt531.append(str([i.text for i in c3]))
                except:
                    c1 = wait1.until(EC.presence_of_all_elements_located(
                                (By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/div/table[2]/tbody/tr["+str(c)+"]/td[1]")))
                    c2 = wait.until(EC.presence_of_all_elements_located(
                                (By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/div/table[2]/tbody/tr["+str(c)+"]/td[2]")))
                    c3 = wait1.until(EC.presence_of_all_elements_located(
                                (By.XPATH,"/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/div/table[2]/tbody/tr["+str(c)+"]/td[3]")))
                    yt511.append(str([i.text for i in c1]))
                    yt521.append(str([i.text for i in c2]))
                    yt531.append(str([i.text for i in c3]))
            except:
                break
        ##############
        y3 = browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[1]/a/h4")
        y3.click()

        yt31 = []
        yt32 = []
        yt33 = []
        yt34 = []
        try:
            c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/table/thead/tr/th[1]")))
            c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/table/thead/tr/th[2]")))
            c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/table/thead/tr/th[3]")))
            c4 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/table/thead/tr/th[3]")))
            yt31.append(str([i.text for i in c1]))
            yt32.append(str([i.text for i in c2]))
            yt33.append(str([i.text for i in c3]))
            yt34.append(str([i.text for i in c4]))
        except:
            pass
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        for c in range(1, 3):
            try:
                try:
                    c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))
                    c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[2]")))
                    c3 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[3]")))
                    c4 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[4]")))
                    yt31.append(str([i.text for i in c1]))
                    yt32.append(str([i.text for i in c2]))
                    yt33.append(str([i.text for i in c3]))
                    yt34.append(str([i.text for i in c4]))
                except:
                    c1 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
                    c2 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
                    c3 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[3]")))
                    c4 = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[4]")))
                    yt31.append(str([i.text for i in c1]))
                    yt32.append(str([i.text for i in c2]))
                    yt33.append(str([i.text for i in c3]))
                    yt34.append(str([i.text for i in c4]))
            except:
                break
        ########
        temp =pd.DataFrame({"Program Kodu:":(([[program_kodu]])),
                            "Genel Bilgiler":(([[iki,uc]])),
                            "Kontenjan, Yerleşme ve Kayıt İstatistikleri ":(([[t21,t22,t23,t24,t25,t26]])),
                            "Yerleşenlerin Cinsiyet Dağılımı":(([[t31,t32,t33]])),
                            "Yerleşenlerin Geldikleri Coğrafi Bölgeler --tbl1":(([[t41,t42,t43,t44]])),
                            "Yerleşenlerin Geldikleri Coğrafi Bölgeler --tbl2":(([[t41_2,t42_2,t43_2]])),
                            "Yerleşenlerin Geldikleri İller":(([[t51,t52,t53]])),
                            "yerleşenlerin Öğrenim durumu":(([[t61,t62,t63]])),
                            "Yerleşenlerin Liseden Mezuniyet Yılları":(([[t71,t72,t73]])),
                            "Yerleşenlerin Mezun Oldukları Lise Alanları":(([[t81,t82]])),
                            "Yerleşenlerin Mezun Oldukları Lise Grubu / Tipleri--tablo1 genel liseler grubu--":(([[t911,t921,t931]])),
                            "Yerleşenlerin Mezun Oldukları Lise Grubu / Tipleri--tablo2 meslek lisesi grubu--":(([[t912,t922,t932]])),
                            "Yerleşenlerin Mezun Oldukları Lise Grubu / Tipleri--tablo3 belli değil--"        :(([[t913,t923,t933]])),
                            "Yerleşenlerin Mezun Oldukları Liseler ":(([[t101,t102,t103,t104]])),
                            "Yerleşen Okul Birincileri":(([[t111,t112,t113,t114]])),
                            "Taban Puan ve Başarı Sırası İstatistikleri":(([[t121,t122,t123]])),
                            "Yerleşen Son Kişinin Profili":(([[t131,t132]])),
                            "Yerleşenlerin YKS Net Ortalamaları":(([[t141,t142,t143]])),
                            "Yerleşenlerin YKS Puanları-- tablo1 ortalama":(([[t151,t152,t153,t154]])),
                            "Yerleşenlerin YKS Puanları-- tablo2 en düşük puan":(([[t151_1,t152_1,t153_1,t154_1]])),
                            "Yerleşenlerin YKS Başarı Sıraları-- tablo1 ortalama":(([[t161,t162,t163]])),
                            "Yerleşenlerin YKS Başarı Sıraları-- tablo2 en düşük":(([[t161_1,t162_1,t163_1]])),
                            "Ülke Genelinde Tercih Edilme İstatistikleri --tbl1 ":(([[t1711,t1721]])),
                            "Ülke Genelinde Tercih Edilme İstatistikleri --tbl2 ":(([[t1712,t1722,t1732]])),
                            "Ülke Genelinde Tercih Edilme İstatistikleri --tbl3":(([[t1713,t1723]])),
                            "Yerleşenler Ortalama Kaçıncı Tercihlerine Yerleşti?--tbl1":(([[t181,t182]])),
                            "Yerleşenler Ortalama Kaçıncı Tercihlerine Yerleşti?--tbl2":(([[t181_2,t182_2]])),
                            "Yerleşenlerin Tercih Eğilimleri - Genel ":(([[t191,t192]])),
                            "Yerleşenlerin Tercih Eğilimleri - Üniversite Türleri":(([[t201,t202]])),
                            "Yerleşenlerin Tercih Eğilimleri - Üniversiteler --tbl1 devlet":(([[t2111,t2121]])),
                            "Yerleşenlerin Tercih Eğilimleri - Üniversiteler --tbl2 vakıf":(([[t2112,t2122]])),
                            "Yerleşenlerin Tercih Eğilimleri - İller ":(([[t221,t222]])),
                            "Yerleşenlerin Tercih Eğilimleri - Aynı/Farklı Program":(([[t231,t232]])),
                            "Yerleşenlerin Tercih Eğilimleri - Programlar (Meslekler)":(([[t241,t242]])),
                            "Yerleşme Koşulları ":(([[t251,t252]])),
                            "Öğretim Üyesi Sayısı ve Unvan Dağılımı":(([[yt1,yt2]])),
                            "Kayıtlı Öğrenci Sayısı":(([[yt21,yt22,yt23]])),
                            "Programdan Mezun Olan Öğrenci Sayıları":(([[yt31,yt32,yt33,yt34]])),
                            "Değişim Programı ile Giden/Gelen Öğrenci Sayıları":(([[yt41,yt42,yt43]])),
                            "Yatay Geçiş ile Gelen/Giden Öğrenci Sayıları--tbl1 gelen öğrenci":(([[yt51,yt52,yt53]])),
                            "Yatay Geçiş ile Gelen/Giden Öğrenci Sayıları--tbl1 giden öğrenci":(([[yt511,yt521,yt531]])),
                            })


        #original_df.to_pickle("./dummy.pkl")
        #unpickled_df = pd.read_pickle("./dummy.pkl")
        print(temp.to_string())
        original_df = pd.concat([original_df, temp])

    except:
        print(str(program_kodu) +" bulunamadı")



print(original_df.to_string())
