import cv2
import numpy as np
import sys,os
import matplotlib.pyplot as plt
import pandas as pd
from time import sleep
import json
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from helium import *
driver = webdriver.Chrome()

#Link khách sạn,Độ sạch sẽ,Sự thoải mái và chất lượng phòng,Dịch vụ,Vị trí,Tiện nghi,Số lượng phòng,Số lượng nhà hàng,Số quán bar,Thang máy,Tiêu chuẩn về an toàn,Bể bơi, Bồn tắm, Ghế Sofa,Phòng xông hơi, Spa, Mát-xa,Phòng tập,Sân golf, Sân quần vợt, Rate Star

#Hàm này thêm thông tin từng khách sạn sau khi lấy được vào từng dòng của file csv
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def getInfor(link):
    dict = {"Link khách sạn": "nan", "Độ sạch sẽ": "nan", "Sự thoải mái và chất lượng phòng": "nan", "Dịch vụ": "nan",
            "Vị trí": "nan", "Tiện nghi": "nan", "Số lượng phòng": "nan", "Số lượng nhà hàng": "nan",
            "Số quán bar": "nan", "Thang máy": "nan", "Tiêu chuẩn về an toàn": "nan", "Bể bơi": "nan", "Bồn tắm": "nan",
            "Ghế Sofa": "nan", "Phòng xông hơi": "nan", "Spa": "nan", "Mát-xa": "nan", "Phòng tập": "nan",
            "Sân golf": "nan", "Sân quần vợt": "nan", "Rate Star": "nan"}
    driver.get(link)
    sleep(5)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load the page
        sleep(3)
        # Calculate new scroll height and compare with last height.
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        sleep(3)
    sleep(10)
    htmltext = driver.page_source
    soup = BeautifulSoup(htmltext, "html.parser")

    # Lấy phòng
    room = soup.findAll("div", class_="sub-section no-margin padding-top")
    room1 = 0
    if len(room) > 0:
        x = 0
        for i in range(len(room)):
            mm = room[i].text
            if str(mm).find("Về khách sạn") != -1:
                x = i
                break
        room1 = room[x]

    # Lấy tất cả phần đánh giá
    point = soup.find("div", class_="Review-travelerGrade-Cell")

    # Lấy thang máy
    thangMay = soup.findAll("span", class_="feature-with-tooltip")

    # Tiêu chuẩn về an toàn
    anToan = soup.findAll("i", class_="ficon ficon-32 ficon-cleaning-products feature-group-icon")

    # Thư giãn và vui chơi giải trí
    beBoiNgoaiTroi = soup.findAll("i", class_="ficon ficon-18 ficon-outdoor-pool")
    beBoiTrongNha = soup.findAll("i", class_="ficon ficon-18 ficon-indoor-poor")
    xongKho = soup.findAll("i", class_="ficon ficon-18 ficon-sauna")
    xongUot = soup.findAll("i", class_="ficon ficon-18 ficon-steamroom")
    matXa = soup.findAll("i", class_="ficon ficon-18 ficon-massage")
    sanGolf = soup.findAll("i", class_="ficon ficon-18 ficon-golf-course-on-site")
    sanQuanVot = soup.findAll("i", class_="ficon ficon-18 ficon-tennis-courts")
    sPa = soup.findAll("i", class_="ficon ficon-18 ficon-spa-sauna")
    phongTap = soup.findAll("i", class_="ficon ficon-18 ficon-fitness-center")

    # Trang bị trong phòng
    bonTam = soup.findAll("i", class_="ficon ficon-18 ficon-bathtub")
    gheSofa = soup.findAll("i", class_="ficon ficon-18 ficon-sofa")

    # Số sao
    star = soup.findAll("span", class_="HeaderCerebrum__Rating")

    # Điền vào đánh giá

    dict["Link khách sạn"] = link
    try:
        point1 = point.findAll("span")
        if len(point1) > 0:
            i = 0
            while i < len(point1):
                if point1[i].text in dict:
                    dict[point1[i].text] = point1[i + 1].text
                    i = i + 2
                else:
                    i = i + 2
    except: print("Không có phần đánh giá")

    # Điền vào số lượng khách sạn và số nhà hàng, quán bar
    room1 = str(room1)
    print(room1)
    index = room1.find("Số lượng nhà hàng")
    if index != -1:
        sonhahang = ""
        for i in range(index, index+40):
            if room1[i].isdigit() == True:
                sonhahang = sonhahang + room1[i]
        dict["Số lượng nhà hàng"] = (int)(sonhahang)
    index1 = room1.find("Số lượng phòng")
    if index1 != -1:
        soluongphong = ""
        for j in range(index1, index1+40):
            if room1[j].isdigit() == True:
                soluongphong = soluongphong + room1[j]
        dict["Số lượng phòng"] = (int)(soluongphong)
    index2 = room1.find("Số lượng quán bar")
    if index2 != -1:
        soquanbar = ""
        for k in range(index2, index2+40):
            if room1[k].isdigit() == True:
                soquanbar = soquanbar + room1[k]
        dict["Số quán bar"] = (int)(soquanbar)

    # Điền vào thang máy
    if len(thangMay) > 0:
        for i in thangMay:
            if i.text == "Thang máy":
                dict["Thang máy"] = 1

    # Điền vào tiêu chuẩn về an toàn
    if len(anToan) == 1:
        dict["Tiêu chuẩn về an toàn"] = 1

    # Điền vào thư giãn vui chơi giải trí
    if len(beBoiNgoaiTroi) > 0 and len(beBoiTrongNha) > 0:
        dict["Bể bơi"] = 2
    if len(beBoiNgoaiTroi) > 0 or len(beBoiTrongNha) > 0:
        dict["Bể bơi"] = 1
    if len(beBoiNgoaiTroi) == 0 and len(beBoiTrongNha) == 0:
        dict["Bể bơi"] = 0

    if len(xongKho) > 0 and len(xongUot) > 0:
        dict["Phòng xông hơi"] = 2
    if len(xongKho) > 0 or len(xongUot) > 0:
        dict["Phòng xông hơi"] = 1
    if len(xongKho) == 0 and len(xongUot) == 0:
        dict["Phòng xông hơi"] = 0

    if len(matXa) > 0:
        dict["Mát-xa"] = 1
    if len(matXa) == 0:
        dict["Mát-xa"] = 0

    if len(sanGolf) > 0:
        dict["Sân golf"] = 1
    if len(sanGolf) == 0:
        dict["Sân golf"] = 0

    if len(sanQuanVot) > 0:
        dict["Sân quần vợt"] = 1
    if len(sanQuanVot) == 0:
        dict["Sân quần vợt"] = 0

    if len(sPa) > 0:
        dict["Spa"] = 1
    if len(sPa) == 0:
        dict["Spa"] = 0

    if len(phongTap) > 0:
        dict["Phòng tập"] = 1
    if len(phongTap) == 0:
        dict["Phòng tập"] = 0

    # Điền vào trang bị trong phòng
    if len(bonTam) > 0:
        dict["Bồn tắm"] = 1
    if len(bonTam) == 0:
        dict["Bồn tắm"] = 0
    if len(gheSofa) > 0:
        dict["Ghế Sofa"] = 1
    if len(gheSofa) == 0:
        dict["Ghế Sofa"] = 0

    # Điền vào số sao
    if len(star) == 1:
        soSao = ""
        star = (str)(star[0])
        x = star.find("ficon-star-")
        for i in range(x, x + 50):
            if star[i].isdigit() == True:
                soSao = soSao + star[i]
        if len(soSao) == 1:
            dict["Rate Star"] = (float)(soSao)
        if len(soSao) == 2:
            dict["Rate Star"] = (float)(soSao) / 10
    return dict.values()

links = pd.read_csv("../Data/hotelNew.csv")
links = links["link"]
for link in links:
    arr = getInfor(link)
    append_list_as_row("../Data/hotelFinish.csv",arr)


