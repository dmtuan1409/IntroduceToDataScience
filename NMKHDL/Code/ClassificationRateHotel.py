import numpy as np
import sys,os
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report
import joblib
from sklearn.metrics import plot_confusion_matrix


#Khai bao bien va chuan hoa string thanh float
hotel = pd.read_csv("../Data/hotelFinish1.csv")
columns_data=['Độ sạch sẽ', 'Sự thoải mái và chất lượng phòng', 'Dịch vụ', 'Vị trí', 'Tiện nghi', 'Số lượng phòng', 'Số lượng nhà hàng', 'Số quán bar', 'Thang máy', 'Tiêu chuẩn về an toàn', 'Bể bơi', 'Bồn tắm', 'Ghế Sofa', 'Phòng xông hơi', 'Spa', 'Mát-xa', 'Phòng tập', 'Sân golf', 'Sân quần vợt']
doSachSe = hotel["Độ sạch sẽ"]
dichVu = hotel["Dịch vụ"]
tienNghi = hotel["Tiện nghi"]
viTri = hotel['Vị trí']
soPhong=hotel['Số lượng phòng']
Star = hotel["Rate Star"]
suThoaiMai = hotel['Sự thoải mái và chất lượng phòng']
thangMay=hotel["Thang máy"]
anToan = hotel['Tiêu chuẩn về an toàn']
data_train = pd.DataFrame(hotel,columns=columns_data)
label_train = hotel['Rate Star']
data_train=data_train.replace('','NaN')
data_train = data_train[data_train!="NaN"].astype("float")

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

#Xem những trường nào có giá trị missing value
for i in columns_data:
    for j in range(len(data_train)):
        if str(data_train[i][j])=="nan":
            print(i)
            break

#In thông tin từng đặc trưng
for i in columns_data:
    tuan = data_train[i]
    print(tuan.describe())

#Sử dụng Knn để xử lý missingvalue
imputer = KNNImputer(n_neighbors=10)
imputer = imputer.fit(data_train)
data_train = imputer.transform(data_train)
print(data_train)
# Chia train test
X_train, X_test, y_train, y_test = train_test_split(data_train, label_train, test_size=0.25)

# Phân loại bằng mô hình
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

importance = clf.feature_importances_
# summarize feature importance
for i, v in enumerate(importance):
    print('Feature: %0d, Score: %.5f' % (i, v))
# plot feature importance
plt.figure(figsize=(35, 10))
plt.bar(columns_data, importance)
plt.show()

print(str(metrics.accuracy_score(y_test, y_pred)))
print(str(classification_report(y_test, y_pred)))
plot_confusion_matrix(clf, X_test, y_test)
plt.show()


#Lưu và load mô hình dự báo
joblib.dump(clf, "random_forest.joblib")
loaded_rf = joblib.load("../DeploymodelML/model/random_forest.joblib")









