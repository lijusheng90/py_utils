import qrcode
from util import data_structure
from PIL import Image
import os


def get_qr_img(white_base_img, qr_str):
    qr_img = qrcode.make(qr_str)
    # 二维码图片 截取时去掉的边框
    padding = 28
    qr_img = qr_img.crop((padding, padding, qr_img.size[0] - padding, qr_img.size[1] - padding))
    # 二维码图片 缩放
    qr_img = qr_img.resize((300, 300))
    # 底图开始坐标
    base_start_point = [50, 80]
    # 底图背景是圆角 设置一个边距
    padding = 0
    white_base_img.paste(qr_img, (base_start_point[0] + padding, base_start_point[1] + padding,
                            base_start_point[0] + padding + qr_img.size[0],
                            base_start_point[1] + padding + qr_img.size[1]))
    return white_base_img


def into_one_page(qr_str_list, source_path, out_path):
    # 一页的数量
    horizontal_size, vertical_size = 3, 5
    # 一张图片的 右下边距
    padding_right, padding_bottom = 5, 5

    qr_base_img = Image.open(source_path)
    page_w = (qr_base_img.size[0]+padding_right) * horizontal_size
    page_h = (qr_base_img.size[1]+padding_bottom) * vertical_size
    white_base_img = Image.new('RGBA', (qr_base_img.size[0] + padding_right,
                                        qr_base_img.size[1] + padding_bottom), (255, 255, 255, 255))
    white_base_img.paste(qr_base_img, (0, 0))
    for page in data_structure.list_split(qr_str_list, horizontal_size*vertical_size):
        page_img = Image.new('RGBA', (page_w, page_h), (255, 255, 255, 255))
        for i, temp_qr_str in enumerate(page, 0):
            index_y, index_x = divmod(i, horizontal_size)
            one_img = get_qr_img(white_base_img, temp_qr_str)
            page_img.paste(one_img, (one_img.size[0]*index_x, one_img.size[1]*index_y))
        name = '_'.join(page)

        page_img.save(os.path.join(out_path, name+'.png'))


if __name__ == "__main__":
    # 需要批量打印的二维码
    qr_str_list = ['xxxxxxxxxxxxx']
    # 二维码的底图
    source_path = "xxxxxxxx.png"
    # 输出路径
    out_path = './xxxxx'
    into_one_page(qr_str_list, source_path, out_path)

