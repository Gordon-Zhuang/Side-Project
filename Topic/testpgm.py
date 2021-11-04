from PIL import Image

def read_img():
    im = Image.open("C:/Users/gordon_zhuang/Downloads/map4.pgm")    # 讀取檔案
    im.show()    # 展示圖片
    print(im.size)   # 輸出圖片大小

if __name__ == "__main__":
    read_img()     # 呼叫read_img()