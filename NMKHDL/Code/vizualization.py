import cv2
import numpy as np
import sys,os
import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd
from time import sleep
from collections import Counter
import json
import csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report,r2_score,mean_squared_error
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn import svm
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.neighbors import KNeighborsClassifier

#Khai bao bien va chuan hoa string thanh float
hotel = pd.read_csv("../Data/hotelFinish1.csv")
columns_data=['Độ sạch sẽ', 'Sự thoải mái và chất lượng phòng', 'Dịch vụ', 'Vị trí', 'Tiện nghi', 'Số lượng phòng', 'Số lượng nhà hàng', 'Số quán bar', 'Thang máy', 'Tiêu chuẩn về an toàn', 'Bể bơi', 'Bồn tắm', 'Ghế Sofa', 'Phòng xông hơi', 'Spa', 'Mát-xa', 'Phòng tập', 'Sân golf', 'Sân quần vợt',"Rate Star"]
Star = hotel["Rate Star"]
data_train = pd.DataFrame(hotel,columns=columns_data)
label_train = hotel['Rate Star']
data_train=data_train.replace('','NaN')
data_train = data_train[data_train!="NaN"].astype("float")

#Ve Correlation Matrix
#Xử lý giá trị trống của tiêu chuẩn an toàn là 0 nếu như không có
for i in range(len(data_train)):
    if str(data_train["Tiêu chuẩn về an toàn"][i])=="nan":
        data_train["Tiêu chuẩn về an toàn"][i]=0

#Xử lý giá trị của số nhà hàng và quán bar là 0 nếu như không có
for i in range(len(data_train)):
    if str(data_train["Số lượng nhà hàng"][i])=="nan":
        data_train["Số lượng nhà hàng"][i]=0
    if str(data_train["Số quán bar"][i])=="nan":
        data_train["Số quán bar"][i]=0
imputer = KNNImputer(n_neighbors=10)
imputer = imputer.fit(data_train)
data_train = imputer.transform(data_train)
print(data_train)
data_train=pd.DataFrame(data_train,columns=columns_data)
corrMatrix =data_train.corr()
sn.heatmap(corrMatrix, annot=True)
plt.show()
#Ve bieu do phan bo Rate Star
countStar = dict(Counter(Star))
countStar = countStar.items()
countStar=dict(sorted(countStar))
countStarKey = list(countStar.keys())
arr = []
for i in countStarKey:
    i = str(i)
    arr.append(i)
print(arr)
countStarValue = list(countStar.values())
print(countStarValue)
plt.figure(figsize=(20,10))
plt.bar(arr,countStarValue,color="green")
plt.title("Biểu đồ Rate Star")
plt.xlabel("Star")
plt.ylabel("So luong")
plt.show()

Explode=[0,0.1,0,0,0]
plt.pie(countStarValue,explode=Explode,labels=arr,shadow=True,startangle=45)
plt.axis('equal')
plt.legend(title="Biểu đồ Rate Star")
plt.show()

