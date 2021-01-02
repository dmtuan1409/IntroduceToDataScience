import cv2
import numpy as np
import sys,os
import matplotlib.pyplot as plt
import pandas as pd
from time import sleep
import json
import csv

#Đọc file hotelFinish.csv rồi lọc nhưng thứ nhiễu rồi lưu vào file hotelFinish1.csv

hotel = pd.read_csv("../Data/hotelFinish.csv")
link = hotel['Link khách sạn']
soPhong = hotel['Số lượng phòng']
star = hotel['Rate Star']
doSachSe = hotel["Độ sạch sẽ"]
dichVu = hotel["Dịch vụ"]
tienNghi = hotel["Tiện nghi"]
viTri = hotel['Vị trí']
suThoaiMai = hotel['Sự thoải mái và chất lượng phòng']

#Nếu không có thông tin số phòng hoặc số sao thì loại bỏ
arrDrop=[]
for i in range(len(link)):
    if str(soPhong[i])=="nan" or str(star[i])=="nan":
        print(link[i])
        arrDrop.append(i)
for i in arrDrop:
    hotel=hotel.drop(index=i)

#Chuan hoa Star
for i in range(len(link)):
    if star[i]==1.5:
        star[i]=1
    if star[i]==2.5:
        star[i]=2
    if star[i]==3.5:
        star[i]=3
    if star[i]==4.5:
        star[i]=4

#Sủa dấu phảy trong phần chấm điểm thành dấu chấm, phục vụ cho việc chuẩn hóa Float
for i in range(len(suThoaiMai)):
    if str(suThoaiMai[i]).find(",")!=-1:
        suThoaiMai[i]=str(suThoaiMai[i]).replace(",",".")
    if str(doSachSe[i]).find(",")!=-1:
        doSachSe[i]=str(doSachSe[i]).replace(",",".")
    if str(dichVu[i]).find(",")!=-1:
        dichVu[i]=str(dichVu[i]).replace(",",".")
    if str(tienNghi[i]).find(",")!=-1:
        tienNghi[i]=str(tienNghi[i]).replace(",",".")
    if str(viTri[i]).find(",")!=-1:
        viTri[i]=str(viTri[i]).replace(",",".")

hotel.to_csv("../Data/hotelFinish1.csv",index=None)
