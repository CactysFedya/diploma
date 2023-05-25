import cv2
import numpy as np

from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap


class ThreadOpenCV(QThread):
    changePixmap = pyqtSignal(QImage)

    def __init__(self, source):
        super().__init__()

        self.source = source
        # self.time = None
        # self.checkState = None
        # self.arrayStatic = None
        self.color = [(244, 200, 189), (244, 200, 189), (244, 200, 189),(244, 200, 189), (244, 200, 189), (244, 200, 189)]
        # self.countObject = None

        self.running = True
        self.grayscale = False
        self.blur = False

        self.net = cv2.dnn.readNetFromDarknet("Resources/yolov4-tiny.cfg",
                                         "Resources/yolov4-tiny.weights")
        layer_names = self.net.getLayerNames()
        out_layers_indexes = self.net.getUnconnectedOutLayers()
        self.out_layers = [layer_names[index - 1] for index in out_layers_indexes]

        with open("Resources/coco.names.txt") as file:
            self.classes = file.read().split("\n")

        self.classes_to_look_for = ['person', 'bicycle', 'car',
                    'motorbike', 'bus', 'truck']

    def apply_yolo_object_detection(self, image_to_process):
        """
        Распознавание и определение координат объектов на изображении
        на входе: image_to_process - исходное изображение
        на выходе: изображение с отмеченными объектами и подписями к ним
        """

        height, width, _ = image_to_process.shape
        blob = cv2.dnn.blobFromImage(image_to_process, 1 / 255, (608, 608),
                                     (0, 0, 0), swapRB=True, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.out_layers)

        class_indexes, class_scores, boxes = ([] for i in range(3))

        for out in outs:
            for obj in out:
                scores = obj[5:]
                class_index = np.argmax(scores)
                class_score = scores[class_index]
                if class_score > 0:
                    center_x = int(obj[0] * width)
                    center_y = int(obj[1] * height)
                    obj_width = int(obj[2] * width)
                    obj_height = int(obj[3] * height)
                    box = [center_x - obj_width // 2, center_y - obj_height // 2,
                           obj_width, obj_height]
                    boxes.append(box)
                    class_indexes.append(class_index)
                    class_scores.append(float(class_score))

        chosen_boxes = cv2.dnn.NMSBoxes(boxes, class_scores, 0.0, 0.4)
        for box_index in chosen_boxes:
            box_index = box_index
            box = boxes[box_index]
            class_index = class_indexes[box_index]

            if self.classes[class_index] in self.classes_to_look_for:
                index = self.classes_to_look_for.index(self.classes[class_index])
                image_to_process = self.draw_object_bounding_box(image_to_process, index, box)

        return image_to_process

    def draw_object_bounding_box(self, image_to_process, index, box):
        """
        Функция нужна для отрисовки границ и надписей к ним
        на входе: image_to_process - исходное изображение;
                  index - индекс класса объекта
                  box - координаты "рамки" вокруг объекта
        :на выходе: final_image - изображение с отмеченными объектами
        """

        x, y, w, h = box
        start = (x, y)
        end = (x + w, y + h)
        width = 2
        final_image = cv2.rectangle(image_to_process, start, end, self.color[index], width)

        start = (x, y - 10)
        font_size = 1
        font = cv2.FONT_HERSHEY_SIMPLEX
        width = 2
        text = self.classes_to_look_for[index]
        final_image = cv2.putText(final_image, text, start, font,
                                  font_size, (255, 255, 255), width, cv2.LINE_AA)

        return final_image

    def run(self):
        data = cv2.VideoCapture(self.source)
        # frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
        # fps = data.get(cv2.CAP_PROP_FPS)

        # calculate duration of the video
        # self.seconds = round(frames / fps)
        # self.time[2].setText('{:02d}:{:02d}'.format(self.seconds//60, self.seconds % 60))
        # self.time[1].setMinimum(0)
        # self.time[1].setMaximum(self.seconds)
        #
        # self.time[1].setSingleStep(1)
        # self.time_passed = 0

        cap = cv2.VideoCapture(self.source)
        self.running = True

        while self.running:
            ret, frame = cap.read()
            if ret:
                if self.grayscale:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
                else:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                if self.blur:
                    frame = cv2.blur(frame, (15, 15))

                h, w, ch = frame.shape
                bytes_per_line = ch * w  # PEP8: `lower_case_names` for variables
                frame = self.apply_yolo_object_detection(frame)
                image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                image = image.scaled(992, 558, Qt.KeepAspectRatio)
                self.changePixmap.emit(image)

                # self.time_passed += 0.0375
                # self.time[2].setText(
                #     '{:02d}:{:02d}'.format((self.seconds - int(self.time_passed)) // 60,
                #                            (self.seconds - int(self.time_passed)) % 60))
                # self.time[0].setText('{:02d}:{:02d}'.format(int(self.time_passed) // 60, int(self.time_passed) % 60))
                # self.time[1].setValue(int(self.time_passed))

        cap.release()

    def stop(self):
        self.running = False

    def read(self, source):
        self.source = source
    #
    # def setTime(self, time):
    #     self.time = time
    #
    # def setCheckState(self, objects, count):
    #     self.classes_to_look_for = []
    #     self.color = []
    #     self.countObject = []
    #     if objects[0].isChecked():
    #         self.classes_to_look_for.append('person')
    #         self.color.append((244, 200, 189))
    #         self.countObject.append(count[0])
    #
    #     if objects[1].isChecked():
    #         self.classes_to_look_for.append('bicycle')
    #         self.color.append((160, 191, 220))
    #         self.countObject.append(count[1])
    #
    #     if objects[2].isChecked():
    #         self.classes_to_look_for.append('car')
    #         self.color.append((169, 209, 147))
    #         self.countObject.append(count[2])
    #
    #     if objects[3].isChecked():
    #         self.classes_to_look_for.append('motorbike')
    #         self.color.append((181, 153, 193))
    #         self.countObject.append(count[3])
    #
    #     if objects[4].isChecked():
    #         self.classes_to_look_for.append('bus')
    #         self.color.append((249, 238, 174))
    #         self.countObject.append(count[4])
    #
    #     if objects[5].isChecked():
    #         self.classes_to_look_for.append('truck')
    #         self.color.append((245, 190, 107))
    #         self.countObject.append(count[5])

    # def setStatic(self, arrayStatic):
    #     self.arrayStatic = arrayStatic
