import time

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
import glob
import os

from kivy.uix.image import Image
from kivy.uix.widget import Widget



class AnalyseCompost(Widget):
    def selected(self, filename):
        try:

            os.system(
                "python yolov5/detect.py --weights yolov5/weights/best.pt --source {} --name {}".format(filename[0], filename[0].split("\\").pop().split(".")[0]))
            source_img = 'runs/detect/{}/{}'.format(filename[0].split("\\").pop(), filename[0].split("\\").pop())

            self.display_image(source_img)

        except:
            pass

    def display_image(self, source_img):
        im = Image(source=source_img)
        im.reload()
        self.ids.my_image.source = im

    def scan_fruit(self):
        os.system("python yolov5/detect.py --weights yolov5/weights/best.pt --source 0")


class AnalyseCompostApp(App):
    def build(self):
        return AnalyseCompost()

    pass


if __name__ == '__main__':
    AnalyseCompostApp().run()
