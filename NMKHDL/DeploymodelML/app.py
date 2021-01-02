import flask
import pandas as pd
from joblib import dump, load


with open('model/random_forest.joblib', 'rb') as f:
    model = load(f)

app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('main.html'))

    if flask.request.method == 'POST':
        name = flask.request.form['name']
        do_sach_se = flask.request.form['do_sach_se']
        su_thoai_mai = flask.request.form['su_thoai_mai']
        dich_vu = flask.request.form['dich_vu']
        vi_tri = flask.request.form['vi_tri']
        tien_nghi = flask.request.form['tien_nghi']
        so_luong_phong = flask.request.form['so_luong_phong']
        so_luong_nha_hang = flask.request.form['so_luong_nha_hang']
        so_quan_bar = flask.request.form['so_quan_bar']
        thang_may = flask.request.form['thang_may']
        an_toan = flask.request.form['an_toan']
        be_boi = flask.request.form['be_boi']
        bon_tam = flask.request.form['bon_tam']
        ghe_sofa = flask.request.form['ghe_sofa']
        xong_hoi = flask.request.form['xong_hoi']
        spa = flask.request.form['spa']
        mat_xa = flask.request.form['mat_xa']
        phong_tap = flask.request.form['phong_tap']
        san_golf = flask.request.form['san_golf']
        san_quan_vot = flask.request.form['san_quan_vot']



        input_variables = pd.DataFrame([[do_sach_se, su_thoai_mai, dich_vu, vi_tri, tien_nghi, so_luong_phong, so_luong_nha_hang, so_quan_bar, thang_may,an_toan,be_boi,bon_tam,ghe_sofa,xong_hoi,spa,mat_xa,phong_tap,san_golf,san_quan_vot]],
                                       columns=['Độ sạch sẽ', 'Sự thoải mái và chất lượng phòng', 'Dịch vụ', 'Vị trí', 'Tiện nghi', 'Số lượng phòng', 'Số lượng nhà hàng', 'Số quán bar', 'Thang máy', 'Tiêu chuẩn về an toàn', 'Bể bơi', 'Bồn tắm', 'Ghế Sofa', 'Phòng xông hơi', 'Spa', 'Mát-xa', 'Phòng tập', 'Sân golf', 'Sân quần vợt'],
                                       dtype='float',
                                       index=['input'])

        predictions = (int)(model.predict(input_variables)[0])
        print(predictions)

        return flask.render_template('main.html',original_input={'Tên khách sạn': name, 'Độ sạch sẽ': do_sach_se, 'Sự thoải mái': su_thoai_mai, 'Dịch vụ': dich_vu, 'Vị trí': vi_tri, 'Tiện nghi': tien_nghi, 'Số lượng phòng': so_luong_phong, 'Số nhà hàng': so_luong_nha_hang, 'Số quán bar': so_quan_bar, 'Thang máy': thang_may, "Tiêu chuẩn an toàn":an_toan,"Bể bơi":be_boi,"Bồn tắm":bon_tam,"Ghế sofa":ghe_sofa,"Phòng xông hơi":xong_hoi,"Spa":spa,"Mát-xa":mat_xa,"Phòng tập":phong_tap,"Sân golf":san_golf,"Sân quần vợt":san_quan_vot},
result=predictions)


if __name__ == '__main__':
    app.run(debug=True)
