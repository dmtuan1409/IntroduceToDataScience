import cv2
import numpy as np
import sys,os
import matplotlib.pyplot as plt
import pandas as pd
from time import sleep
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

#File này sẽ lọc bỏ 1 số dòng không liên quan đến khách sạn trong file hotel.csv rồi lưu vào file hotelNew.csv

hotel = pd.read_csv("../Data/hotel.csv")
link = hotel['link']
arr=[]
for tuan in link:
    arr.append(tuan)
i=0
while i<len(arr):
    if (str)(arr[i]).find("motel")!=-1:
        arr.remove(arr[i])
        continue
    i=i+1
j=0
while j<len(arr):
    if (str)(arr[j]).find("hostel")!=-1:
        arr.remove(arr[j])
        continue
    j=j+1

k=0
while k<len(arr):
    if (str)(arr[k]).find("-room-")!=-1:
        arr.remove(arr[k])
        continue
    k=k+1
k1=0
while k1<len(arr):
    if (str)(arr[k1]).find("nha-nghi")!=-1:
        arr.remove(arr[k1])
        continue
    k1=k1+1
k2=0
while k2<len(arr):
    if (str)(arr[k2]).find("nha-khach")!=-1:
        arr.remove(arr[k2])
        continue
    k2=k2+1
k3=0
while k3<len(arr):
    if (str)(arr[k3]).find("chung-cu")!=-1:
        arr.remove(arr[k3])
        continue
    k3=k3+1
k4=0
while k4<len(arr):
    if (str)(arr[k4]).find("-home-")!=-1:
        arr.remove(arr[k4])
        continue
    k4=k4+1
k5=0
while k5<len(arr):
    if (str)(arr[k5]).find("studio")!=-1:
        arr.remove(arr[k5])
        continue
    k5=k5+1
k6=0
while k6<len(arr):
    if (str)(arr[k6]).find("can-ho")!=-1:
        arr.remove(arr[k6])
        continue
    k6=k6+1
k7=0
while k7<len(arr):
    if (str)(arr[k7]).find("apartment")!=-1:
        arr.remove(arr[k7])
        continue
    k7=k7+1
k8=0
while k8<len(arr):
    if (str)(arr[k8]).find("house")!=-1:
        arr.remove(arr[k8])
        continue
    k8=k8+1
k9=0
while k9<len(arr):
    if (str)(arr[k9]).find("homestay")!=-1:
        arr.remove(arr[k9])
        continue
    k9=k9+1
k10=0
while k10<len(arr):
    if (str)(arr[k10]).find("villa")!=-1:
        arr.remove(arr[k10])
        continue
    k10=k10+1
k11=0
while k11<len(arr):
    if (str)(arr[k11]).find("resort")!=-1:
        arr.remove(arr[k11])
        continue
    k11=k11+1

