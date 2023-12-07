from PyQt5 import QtWidgets, QtCore


class Popup(QtWidgets.QWidget):
    def __init__(self, num):
        super().__init__()
        self.initUI(num)

    def initUI(self, plate_num):
        self.setWindowTitle("Alert")
        self.setGeometry(100, 100, 600, 400)  # Adjust the size as needed

        # Styling
        self.setStyleSheet("background-color: #f0f0f0; font-size: 14px;")
        layout = QtWidgets.QVBoxLayout()
        title_label = None
        name_label = None
        id_label = None
        end_label = None
        # Title Label
        if isinstance(plate_num, str):
            title_label = QtWidgets.QLabel(" ".join(('Car with Plate Number: "', plate_num, '" is not allowed to be parked here')), self)
            layout.addWidget(title_label)

        else:
            title_label = QtWidgets.QLabel(" ".join(('Plate Number: ', plate_num[0])), self)
            name_label = QtWidgets.QLabel(" ".join(('Owner Name: ', plate_num[1])), self)
            id_label = QtWidgets.QLabel(" ".join(('Fl Tech ID: ', str(plate_num[2]))), self)
            end_label = QtWidgets.QLabel('is not allowed to be parked here', self)
            name_label.setAlignment(QtCore.Qt.AlignCenter)
            id_label.setAlignment(QtCore.Qt.AlignCenter)
            end_label.setAlignment(QtCore.Qt.AlignCenter)
            layout.addWidget(title_label)

            name_label.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px;")
            id_label.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px;")
            end_label.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px;")
            layout.addWidget(name_label)
            layout.addWidget(id_label)
            layout.addWidget(end_label)

        title_label.setAlignment(QtCore.Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px;")


        # Start Button
        start_button = QtWidgets.QPushButton("Exit", self)
        start_button.setStyleSheet(
            "QPushButton { background-color: #990000; color: white; padding: 10px; font-size: 18px; border: none; border-radius: 4px; }")
        start_button.setFixedSize(200, 40)
        start_button.clicked.connect(self.close)

        # Layout
        layout.addWidget(start_button, 0, QtCore.Qt.AlignCenter)
        self.setLayout(layout)



