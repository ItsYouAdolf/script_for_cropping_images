import cv2
import glob
from os import path


#обрезка
def cut():
    for name in glob.glob("images/**.jpg"):
        img = cv2.imread(name)
        m = img[190:, :1100]
        outfile = path.join("transform_foto", path.split(name)[1])
        cv2.imwrite(outfile, m)


def test():
    for name in glob.glob("labels/**.txt"):
        reader = open(name, 'r')
        lines = reader.readlines()
        reader.close()
        out_label = path.join("transform_label", path.split(name)[1])
        writer = open(out_label, 'w')

        for i in lines:
            dh, dw, = 720, 1280
            class_id, x_center, y_center, w, h = i.strip().split()
            x_center, y_center, w, h = float(x_center), float(y_center), float(w), float(h)
            x_center = round(x_center * dw)
            y_center = round(y_center * dh)
            w = round(w * (dw))
            h = round(h * (dh))


            # конверт
            dw2 = 1100
            dh2 = 530


            w2 = (w / dw2)
            h2 = (h / dh2)
            x_center2 = (x_center / dw2)
            y_center2 = ((y_center - 190) / dh2)

            str_k = f'{class_id} {x_center2} {y_center2} {w2} {h2}'

            writer.write(str_k + '\n')
        writer.close()




def main():
    cut()
    test()


if __name__ == '__main__':
    main()

