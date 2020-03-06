import config
import os
from PIL import Image

if __name__ == '__main__':
    if not os.path.isdir(config.img_out_dir):
        print("[ERROR] Directory {} not exist".format(config.img_out_dir))
        exit()

    fp = open('out_data.txt', 'w')
    if not fp:
        print("Create file out_data.txt failed")
        exit()

    def _get_rgb_symbol(rgb):
        t = sum(rgb) / 3
        if t < 64:
            return 'MM'
        elif t < 128:
            return 'OO'
        elif t < 192:
            return '^^'
        else:
            return '  '

    for file in os.listdir(config.img_out_dir):
        img_path = "{}/{}".format(config.img_out_dir, file)
        img = Image.open(img_path)
        w, h = img.size

        for y in range(h):
            for x in range(w):
                rgb = img.getpixel((x, y))
                symbol = _get_rgb_symbol(rgb)
                fp.write(symbol)
            fp.write(os.linesep)

        print('{} OK'.format(file))

        fp.write(os.linesep)
    fp.close()
