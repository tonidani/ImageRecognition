from PyQt5 import QtCore, QtGui, QtWidgets
from collections import defaultdict
import colorsys as cs
import sys
import math
import helpers as lol
import numpy as arx


class MainAppWindow:
    def __init__(self, MainWindowToni):
        self.MainWindowToni = MainWindowToni
        self.MainWindowToni.setObjectName("MainWindowToni")
        self.width = 1024
        self.height = 728
        self.MainWindowToni.resize(self.width, self.height)
        self.central_widget = QtWidgets.QWidget(MainWindowToni)
        self.central_widget.setObjectName("central_widget")
        self.image = QtWidgets.QLabel(self.central_widget)
        self.image.setGeometry(QtCore.QRect(0, 0, MainWindowToni.width(), MainWindowToni.height()))
        self.image.setText("")
        self.image.setScaledContents(False)
        self.image.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.image.setWordWrap(False)
        self.image.setObjectName("image")
        self.MainWindowToni.setCentralWidget(self.central_widget)

        self.menubar = QtWidgets.QMenuBar(self.MainWindowToni)
        self.menubar.setGeometry(QtCore.QRect(0, 0, self.width, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuFilters = QtWidgets.QMenu(self.menubar)
        self.menuFilters.setObjectName("menuFilters")

        self.menuContrast = QtWidgets.QMenu(self.menuFilters)
        self.menuContrast.setObjectName("menuContrast")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.MainWindowToni.setMenuBar(self.menubar)

        self.menuEdgeDetection = QtWidgets.QMenu(self.menuFilters)
        self.menuEdgeDetection.setObjectName("menuEdgeDetection")

        self.menuCornerDet = QtWidgets.QMenu(self.menuFilters)
        self.menuCornerDet.setObjectName("menuCornerDetectors")

        self.statusbar = QtWidgets.QStatusBar(self.MainWindowToni)
        self.pixmap = None

        self.statusbar.setObjectName("statusbar")
        self.MainWindowToni.setStatusBar(self.statusbar)

        self.actionOpen = QtWidgets.QAction(self.MainWindowToni)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_As = QtWidgets.QAction(self.MainWindowToni)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExit = QtWidgets.QAction(self.MainWindowToni)
        self.actionExit.setObjectName("actionExit")
        self.actionCopy = QtWidgets.QAction(self.MainWindowToni)
        self.actionCopy.setObjectName("actionCopy")

        self.actionPaste = QtWidgets.QAction(self.MainWindowToni)
        self.actionPaste.setObjectName("actionPaste")

        self.actionZoom_In_25 = QtWidgets.QAction(self.MainWindowToni)
        self.actionZoom_In_25.setObjectName("actionZoom_In_25")

        self.actionZoom_Out_25 = QtWidgets.QAction(self.MainWindowToni)
        self.actionZoom_Out_25.setObjectName("actionZoom_Out_25")

        self.actionNormal_Size = QtWidgets.QAction(self.MainWindowToni)
        self.actionNormal_Size.setObjectName("actionNormal_Size")

        self.actionFit_to_Window = QtWidgets.QAction(self.MainWindowToni)
        self.actionFit_to_Window.setObjectName("actionFit_to_Window")

        self.actionFilterDesaturate = QtWidgets.QAction(self.MainWindowToni)
        self.actionFilterDesaturate.setObjectName("actionFilterDesaturate")

        self.actionFilterInvert = QtWidgets.QAction(self.MainWindowToni)
        self.actionFilterInvert.setObjectName("actionFilterInvert")

        self.actionFilterNegative = QtWidgets.QAction(self.MainWindowToni)
        self.actionFilterNegative.setObjectName("actionFilterNegative")

        self.actionLinearContrast = QtWidgets.QAction(self.MainWindowToni)
        self.actionLinearContrast.setObjectName("actionLinearContrast")

        self.actionFilterMonochromatic = QtWidgets.QAction(self.MainWindowToni)
        self.actionFilterMonochromatic.setObjectName("actionFilterMonochromatic")

        self.actionFilterBrightness = QtWidgets.QAction(self.MainWindowToni)
        self.actionFilterBrightness.setObjectName("actionFilterBrightness")

        self.actionLogarithmicContrast = QtWidgets.QAction(self.MainWindowToni)
        self.actionLogarithmicContrast.setObjectName("actionLogarithmicContrast")

        self.actionPowerContrast = QtWidgets.QAction(self.MainWindowToni)
        self.actionPowerContrast.setObjectName("actionPowerContrast")

        self.actionCompareImgSum = QtWidgets.QAction(self.MainWindowToni)
        self.actionCompareImgSum.setObjectName("actionCompareImgSum")
        self.actionCompareImgDiff = QtWidgets.QAction(self.MainWindowToni)
        self.actionCompareImgDiff.setObjectName("actionCompareImgDiff")

        self.actionAbout = QtWidgets.QAction(self.MainWindowToni)
        self.actionAbout.setObjectName("actionAbout")

        # GAUSS
        self.actionGaussFilter = QtWidgets.QAction(self.MainWindowToni)
        self.actionGaussFilter.setObjectName("actionGaussFilter")

        # OTSU

        self.actionOtsuAlgorithm = QtWidgets.QAction(self.MainWindowToni)
        self.actionOtsuAlgorithm.setObjectName("actionOtsuAlgorithm")

        # MORAVEC

        self.actionMoravecAlgorithm = QtWidgets.QAction(self.MainWindowToni)
        self.actionMoravecAlgorithm.setObjectName("actionMoravecAlgorithm")

        self.actionHarris = QtWidgets.QAction(self.MainWindowToni)
        self.actionHarris.setObjectName("actionHarris")

        self.actionEdgePrewit = QtWidgets.QAction(self.MainWindowToni)
        self.actionEdgePrewit.setObjectName("actionEdgePrewit")

        self.actionEdgeSobel = QtWidgets.QAction(self.MainWindowToni)
        self.actionEdgeSobel.setObjectName("actionEdgeSobel")

        self.actionEdgeRoberts = QtWidgets.QAction(self.MainWindowToni)
        self.actionEdgeRoberts.setObjectName("actionEdgeRoberts")

        self.actionEdgeLaplace = QtWidgets.QAction(self.MainWindowToni)
        self.actionEdgeLaplace.setObjectName("actionEdgeLaplace")

        self.actionEdgeLogarithmic = QtWidgets.QAction(self.MainWindowToni)
        self.actionEdgeLogarithmic.setObjectName("actionEdgeLogarithmic")

        self.actionEdgeSharpening = QtWidgets.QAction(self.MainWindowToni)
        self.actionEdgeSharpening.setObjectName("actionEdgeSharpening")

        self.actionEdgeKirsch = QtWidgets.QAction(self.MainWindowToni)
        self.actionEdgeKirsch.setObjectName("actionEdgeKirsch")

        #

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuView.addAction(self.actionZoom_In_25)
        self.menuView.addAction(self.actionZoom_Out_25)
        self.menuView.addAction(self.actionNormal_Size)
        self.menuView.addAction(self.actionFit_to_Window)

        self.menuFilters.addAction(self.actionFilterDesaturate)
        self.menuFilters.addAction(self.actionFilterNegative)
        self.menuFilters.addAction(self.actionFilterInvert)
        self.menuFilters.addAction(self.actionFilterMonochromatic)
        self.menuFilters.addAction(self.actionFilterBrightness)
        self.menuFilters.addAction(self.actionGaussFilter)

        self.menuContrast.addAction(self.actionLinearContrast)
        self.menuContrast.addAction(self.actionLogarithmicContrast)
        self.menuContrast.addAction(self.actionPowerContrast)

        self.menuFilters.addAction(self.actionCompareImgSum)
        self.menuFilters.addAction(self.actionCompareImgDiff)

        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuFilters.menuAction())
        self.menuFilters.addAction(self.menuContrast.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        #
        self.menuFilters.addAction(self.menuEdgeDetection.menuAction())
        self.menuEdgeDetection.addAction(self.actionEdgeRoberts)
        self.menuEdgeDetection.addAction(self.actionEdgePrewit)
        self.menuEdgeDetection.addAction(self.actionEdgeKirsch)
        self.menuEdgeDetection.addAction(self.actionEdgeSobel)
        self.menuEdgeDetection.addAction(self.actionEdgeLaplace)
        self.menuEdgeDetection.addAction(self.actionEdgeLogarithmic)
        self.menuEdgeDetection.addAction(self.actionOtsuAlgorithm)

        #
        self.menuFilters.addAction(self.menuEdgeDetection.menuAction())
        self.menuFilters.addAction(self.actionEdgeSharpening)
        #

        self.menuFilters.addAction(self.menuCornerDet.menuAction())
        self.menuCornerDet.addAction(self.actionMoravecAlgorithm)
        self.menuCornerDet.addAction(self.actionHarris)

        self.translate_ui()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindowToni)

        self.actionOpen.triggered.connect(lambda: self.loadImage())
        self.actionZoom_In_25.triggered.connect(lambda: self.changeSize(1.20))
        self.actionZoom_Out_25.triggered.connect(lambda: self.changeSize(0.80))
        self.actionFit_to_Window.triggered.connect(lambda: self.autoFit())
        self.actionExit.triggered.connect(lambda: self.exit())

        self.actionFilterDesaturate.triggered.connect(lambda: self.desaturate())
        self.actionFilterNegative.triggered.connect(lambda: self.negative())
        self.actionLinearContrast.triggered.connect(lambda: self.linearContrast())
        self.actionLogarithmicContrast.triggered.connect(lambda: self.logContrast())
        self.actionPowerContrast.triggered.connect(lambda: self.powContrast())
        self.actionFilterInvert.triggered.connect(lambda: self.invert())
        self.actionFilterMonochromatic.triggered.connect(lambda: self.monoCanal())
        self.actionFilterBrightness.triggered.connect(lambda: self.brightness())
        self.actionCompareImgSum.triggered.connect(lambda: self.compareImg(1))
        self.actionCompareImgDiff.triggered.connect(lambda: self.compareImg(0))

        self.actionGaussFilter.triggered.connect(lambda: self.gausseFilter())

        self.actionEdgeKirsch.triggered.connect(lambda: self.edgeKirsch())
        self.actionEdgeLaplace.triggered.connect(lambda: self.edgeLaplace())
        self.actionEdgePrewit.triggered.connect(lambda: self.edgePrewitSobel(1))
        self.actionEdgeSobel.triggered.connect(lambda: self.edgePrewitSobel(0))
        self.actionEdgeLogarithmic.triggered.connect(lambda: self.edgeLogarithmic())
        self.actionEdgeRoberts.triggered.connect(lambda: self.edgeRoberts())

        self.actionOtsuAlgorithm.triggered.connect(lambda: self.otsu())
        self.actionMoravecAlgorithm.triggered.connect(lambda: self.moravec())
        self.actionHarris.triggered.connect(lambda: self.harris())

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindowToni.setWindowTitle(_translate("MainWindowToni", "MainWindowToni"))
        self.menuFile.setTitle(_translate("MainWindowToni", "File"))
        self.menuEdit.setTitle(_translate("MainWindowToni", "Edit"))
        self.menuView.setTitle(_translate("MainWindowToni", "View"))
        self.menuFilters.setTitle(_translate("MainWindowToni", "Filters"))
        self.menuHelp.setTitle(_translate("MainWindowToni", "Help"))
        self.actionOpen.setText(_translate("MainWindowToni", "Open ..."))
        self.actionSave_As.setText(_translate("MainWindowToni", "Save As ..."))
        self.actionExit.setText(_translate("MainWindowToni", "Exit"))
        self.actionCopy.setText(_translate("MainWindowToni", "Copy"))
        self.actionPaste.setText(_translate("MainWindowToni", "Paste"))

        self.actionFit_to_Window.setText(_translate("MainWindowToni", "Fit to Window"))
        self.actionZoom_In_25.setText(_translate("MainWindowToni", "Zoom In + (20%)"))
        self.actionZoom_Out_25.setText(_translate("MainWindowToni", "Zoom Out - (20%)"))
        self.actionNormal_Size.setText(_translate("MainWindowToni", "Normal Size"))

        self.actionFilterDesaturate.setText(_translate("MainWindowToni", "Desaturate"))
        self.actionFilterNegative.setText(_translate("MainWindowToni", "Negative"))
        self.menuContrast.setTitle(_translate("MainWindowToni", "Contrast"))
        self.actionLinearContrast.setText(_translate("MainWindowToni", "Linear"))
        self.actionLogarithmicContrast.setText(_translate("MainWindowToni", "Logarithmic"))
        self.actionPowerContrast.setText(_translate("MainWindowToni", "Power"))
        self.actionFilterInvert.setText(_translate("MainWindowToni", "Invert"))
        self.actionFilterMonochromatic.setText(_translate("MainWindowToni", "Monochromatic Canal"))
        self.actionFilterBrightness.setText(_translate("MainWindowToni", "Brightness"))
        self.actionCompareImgSum.setText(_translate("MainWindowToni", "Compare Img (Sum)"))
        self.actionCompareImgDiff.setText(_translate("MainWindowToni", "Compare Img (Difference)"))
        self.actionAbout.setText(_translate("MainWindowToni", "About"))

        self.actionGaussFilter.setText(_translate("MainWindowToni", "Gausse filter"))

        self.actionEdgePrewit.setText(_translate("MainWindowToni", "Prewit"))
        self.actionEdgeKirsch.setText(_translate("MainWindowToni", "Kirsch"))
        self.actionEdgeSobel.setText(_translate("MainWindowToni", "Sobel"))
        self.menuEdgeDetection.setTitle(_translate("MainWindowToni", "Edges"))
        self.actionEdgeRoberts.setText(_translate("MainWindowToni", "Roberts"))
        self.actionEdgeLaplace.setText(_translate("MainWindowToni", "Laplace"))
        self.actionEdgeLogarithmic.setText(_translate("MainWindowToni", "Logharitmic"))

        self.menuCornerDet.setTitle(_translate("MainWindowToni", "Corners"))
        self.actionOtsuAlgorithm.setText(_translate("mainWindowToni", "Otsu"))
        self.menuCornerDet.setTitle(_translate("MainWindowToni", "Corners"))
        self.actionMoravecAlgorithm.setText(_translate("MainWindowToni", "Moravec Algotithm"))
        self.actionHarris.setText(_translate("MainWindowToni", "Harris Algotithm"))

    def loadImage(self):

        filename = QtWidgets.QFileDialog.getOpenFileName(self.central_widget, 'Open file', './',
                                                         "Image files (*.pgm *.pbm *.ppm)")
        self.pixmap = QtGui.QPixmap(filename[0])
        self.setPixmap()

    def setPixmap(self):

        self.image.setPixmap(self.pixmap)
        print(self.image)

    def changeSize(self, factor):

        self.pixmap = self.pixmap.scaled(int(self.pixmap.width() * factor), int(self.pixmap.height() * factor))
        self.setPixmap()

    def autoFit(self):

        self.image.resize(self.MainWindowToni.width(), self.MainWindowToni.height())
        self.pixmap = self.pixmap.scaled(self.MainWindowToni.width(), self.MainWindowToni.height())
        self.setPixmap()

    def exit(self):

        sys.exit()

    colors_in_rgb = (0, 0, 0)  ## GLOBALS SCOPE

    def negative(self):

        image = self.pixmap.toImage()
        width = self.pixmap.width()
        height = self.pixmap.height()

        for x in range(width):
            for y in range(height):
                c = image.pixel(x, y)

                colors_in_rgb = QtGui.QColor(c).getRgb()
                colors_in_rgb2 = (255 - colors_in_rgb[0], 255 - colors_in_rgb[1], 255 - colors_in_rgb[2])

                image.setPixel(x, y, QtGui.qRgb(*colors_in_rgb2))

        self.pixmap = QtGui.QPixmap.fromImage(image)
        self.setPixmap()

    def invert(self):  ##### testowy filtr
        image = self.pixmap.toImage()
        image.invertPixels()
        self.pixmap = QtGui.QPixmap.fromImage(image)
        self.setPixmap()

    def compareImg(self, value):

        self.autoFit()
        image = self.pixmap.toImage()
        width = self.pixmap.width()
        height = self.pixmap.height()
        filename = QtWidgets.QFileDialog.getOpenFileName(self.central_widget, 'Open file', './',
                                                         "Image files (*.pgm *.pbm *.ppm)")
        other_image = QtGui.QPixmap(filename[0])
        other_image = other_image.scaled(self.width, self.height)
        image_2 = other_image.toImage()

        for x in range(width):
            for y in range(height):
                color_image_1 = image.pixel(x, y)
                color_image_2 = image_2.pixel(x, y)
                set_image_color_1 = QtGui.QColor(color_image_1).getRgb()
                set_image_color_2 = QtGui.QColor(color_image_2).getRgb()

                if value == 1:
                    color_red = set_image_color_1[0] + set_image_color_2[0]
                    color_green = set_image_color_1[1] + set_image_color_2[1]
                    color_blue = set_image_color_1[2] + set_image_color_2[2]

                    if color_red <= 255:
                        c_r = color_red
                    else:
                        c_r = 255

                    if color_green <= 255:
                        c_g = color_green
                    else:
                        c_g = 255

                    if color_blue <= 255:
                        c_b = color_blue
                    else:
                        c_b = 255

                    colors_in_rgb2 = (c_r, c_g, c_b)

                else:
                    color_red = set_image_color_1[0] - set_image_color_2[0]
                    color_green = set_image_color_1[1] - set_image_color_2[1]
                    color_blue = set_image_color_1[2] - set_image_color_2[2]

                    if color_red <= 255:
                        c_r = color_red
                    else:
                        c_r = 255

                    if color_green <= 255:
                        c_g = color_green
                    else:
                        c_g = 255

                    if color_blue <= 255:
                        c_b = color_blue
                    else:
                        c_b = 255

                    colors_in_rgb2 = (c_r, c_g, c_b)

                image.setPixel(x, y, QtGui.qRgb(*colors_in_rgb2))

        self.pixmap = QtGui.QPixmap.fromImage(image)
        self.setPixmap()

    def desaturate(self):

        image = self.pixmap.toImage()
        width = self.pixmap.width()
        height = self.pixmap.height()

        for x in range(width):
            for y in range(height):
                c = image.pixel(x, y)

                colors_in_rgb = QtGui.QColor(c).getRgb()
                colors_in_rgb2 = (colors_in_rgb[0] + colors_in_rgb[1] + colors_in_rgb[2]) / 3
                colors_in_rgb3 = (0, 0, 0)

                colors_in_rgb3 = (colors_in_rgb2, colors_in_rgb2, colors_in_rgb2)
                image.setPixel(x, y, QtGui.qRgb(*colors_in_rgb3))

        self.pixmap = QtGui.QPixmap.fromImage(image)
        self.setPixmap()

    def linearContrast(self):

        image = self.pixmap.toImage()
        counter_float = 1.5
        width = self.pixmap.width()
        height = self.pixmap.height()

        for x in range(width):
            for y in range(height):
                c = image.pixel(x, y)

                colors_in_rgb = QtGui.QColor(c).getRgb()

                color_red = int(colors_in_rgb[0] * counter_float)
                color_green = int(colors_in_rgb[1] * counter_float)
                color_blue = int(colors_in_rgb[2] * counter_float)

                if color_red <= 255:
                    c_r = color_red
                else:
                    c_r = 255

                if color_green <= 255:
                    c_g = color_green
                else:
                    c_g = 255

                if color_blue <= 255:
                    c_b = color_blue
                else:
                    c_b = 255

                colors_in_rgb2 = (c_r, c_g, c_b)
                image.setPixel(x, y, QtGui.qRgb(*colors_in_rgb2))
        self.pixmap = QtGui.QPixmap.fromImage(image)
        self.setPixmap()

    def logContrast(self):

        image = self.pixmap.toImage()
        width = self.pixmap.width()
        height = self.pixmap.height()

        for x in range(width):
            for y in range(height):
                c = image.pixel(x, y)
                colors_in_rgb = QtGui.QColor(c).getRgb()

                color_red = 10 * int(math.log(colors_in_rgb[0] + 1))
                color_green = 10 * int(math.log(colors_in_rgb[1] + 1))
                color_blue = 10 * int(math.log(colors_in_rgb[2] + 1))

                if color_red <= 255:
                    c_r = color_red
                else:
                    c_r = 255

                if color_green <= 255:
                    c_g = color_green
                else:
                    c_g = 255

                if color_blue <= 255:
                    c_b = color_blue
                else:
                    c_b = 255

                colors_in_rgb2 = (c_r, c_g, c_b)
                image.setPixel(x, y, QtGui.qRgb(*colors_in_rgb2))
        self.pixmap = QtGui.QPixmap.fromImage(image)
        self.setPixmap()

    def powContrast(self):

        image = self.pixmap.toImage()
        width = self.pixmap.width()
        height = self.pixmap.height()
        counter_float = 10

        for x in range(width):
            for y in range(height):
                c = image.pixel(x, y)
                colors_in_rgb = QtGui.QColor(c).getRgb()

                color_red = int(math.pow(2, colors_in_rgb[0] / counter_float) - 1)
                color_green = int(math.pow(2, colors_in_rgb[1] / counter_float) - 1)
                color_blue = int(math.pow(2, colors_in_rgb[2] / counter_float) - 1)

                if color_red <= 255:
                    c_r = color_red
                else:
                    c_r = 255
                if color_green <= 255:
                    c_g = color_green
                else:
                    c_g = 255
                if color_blue <= 255:
                    c_b = color_blue
                else:
                    c_b = 255

                colors_in_rgb2 = (c_r, c_g, c_b)

                image.setPixel(x, y, QtGui.qRgb(*colors_in_rgb2))
        self.pixmap = QtGui.QPixmap.fromImage(image)
        self.setPixmap()

    def monoCanal(self):

        image = self.pixmap.toImage()
        width = self.pixmap.width()
        height = self.pixmap.height()

        for x in range(width):
            for y in range(height):
                colors_in_rgb = list(QtGui.QColor(image.pixel(x, y)).getRgb())
                canal = QtGui.QColor(255 - colors_in_rgb[0], colors_in_rgb[1], colors_in_rgb[2], colors_in_rgb[3]).rgb()
                image.setPixel(x, y, canal)

        self.pixmap = self.pixmap.fromImage(image)
        self.setPixmap()

    def modal(self, z):
        if z > 1:
            z = 1
        elif z < 0:
            z = 0
        return z

    def shelper(self, flag):
        image = self.pixmap.toImage()
        width = self.pixmap.width()
        height = self.pixmap.height()
        shocker = arx.zeros((width, height), arx.float32)
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                shocker[x][y] = lol.c_ar(lol.ar3(image, x, y), flag)
        return shocker

    def brightness(self):

        value, control = QtWidgets.QInputDialog.getInt(self.central_widget, "Set brightness (0.1)", "Value:", 0.0, -255,
                                                       255, 2)
        if control:

            image = self.pixmap.toImage()
            width = self.pixmap.width()
            height = self.pixmap.height()
            counter_float = float(value / 100)

            for x in range(width):
                for y in range(height):
                    c = image.pixel(x, y)
                    colors_in_rgb = QtGui.QColor(c).getRgb()
                    color_r, color_g, color_b = [x / 255.0 for x in
                                                 [colors_in_rgb[0], colors_in_rgb[1], colors_in_rgb[2]]]
                    color_h, color_l, color_s = cs.rgb_to_hls(color_r, color_g, color_b)
                    color_l += counter_float
                    lol = self.modal(color_l)
                    color_r, color_g, color_b = cs.hls_to_rgb(color_h, lol, color_s)
                    color_r, color_g, color_b = [x * 255.0 for x in [color_r, color_g, color_b]]
                    colors_in_rgb2 = color_r, color_g, color_b
                    image.setPixel(x, y, QtGui.qRgb(*colors_in_rgb2))

            self.pixmap = QtGui.QPixmap.fromImage(image)
            self.setPixmap()

    # EDGES

    def edgeRoberts(self):
        self.desaturate()
        image = self.pixmap.toImage()
        width = self.pixmap.width() - 1
        height = self.pixmap.height() - 1
        image2 = self.pixmap.toImage()

        for x in range(0, width):
            for y in range(0, height):
                img_pix0 = QtGui.QColor(image.pixel(x, y)).getRgb()[0]
                img_pix1 = QtGui.QColor(image.pixel(x + 1, y)).getRgb()[0]
                img_pix2 = QtGui.QColor(image.pixel(x, y + 1)).getRgb()[0]
                img_pix3 = QtGui.QColor(image.pixel(x + 1, y + 1)).getRgb()[0]
                r_gx = img_pix3 * -1
                r_gy = img_pix2 * -1
                z_gx = img_pix0 + r_gx
                z_gy = img_pix1 + r_gy
                powed_gx = pow(z_gx, 2)
                powed_gy = pow(z_gy, 2)
                value = round(math.sqrt(powed_gx + powed_gy))
                image2.setPixel(x, y, QtGui.qRgb(value, value, value))

        self.pixmap = QtGui.QPixmap.fromImage(image2)
        self.setPixmap()

    def edgeLaplace(self):
        self.desaturate()
        ar = lol.ARR2
        image = self.pixmap.toImage()
        image2 = self.pixmap.toImage()
        width = self.pixmap.width() - 1
        height = self.pixmap.height() - 1
        for x in range(1, width):
            for y in range(1, height):
                arr = lol.ar3(image, x, y)
                value = lol.nor(lol.c_ar(arr, ar))
                image2.setPixel(x, y, QtGui.qRgb(value, value, value))
        self.pixmap = QtGui.QPixmap.fromImage(image2)
        self.setPixmap()

    def edgePrewitSobel(self, flag):
        self.desaturate()
        image = self.pixmap.toImage()
        width = self.pixmap.width() - 1
        height = self.pixmap.height() - 1
        image2 = self.pixmap.toImage()
        h, v = lol.c_f(flag)
        for x in range(1, width):
            for y in range(1, height):
                array = lol.ar3(image, x, y)
                z_gy = lol.c_ar(array, v)
                z_gx = lol.c_ar(array, h)
                powed_gx = pow(z_gx, 2)
                powed_gy = pow(z_gy, 2)
                value = lol.nor(round(math.sqrt(powed_gx + powed_gy)))
                image2.setPixel(x, y, QtGui.qRgb(value, value, value))
        self.pixmap = QtGui.QPixmap.fromImage(image2)
        self.setPixmap()

    def edgeKirsch(self):
        self.desaturate()
        image = self.pixmap.toImage()
        width = self.pixmap.width() - 1
        height = self.pixmap.height() - 1
        image2 = self.pixmap.toImage()
        power = lol.ARR
        power_arr = []
        for x in range(1, width):
            for y in range(1, height):
                power_arr.clear()
                array = lol.ar3(image, x, y)
                for z in power:
                    power_arr.append(lol.c_ar(array, z))
                value = lol.nor(max(power_arr))
                image2.setPixel(x, y, QtGui.qRgb(value, value, value))
        self.pixmap = QtGui.QPixmap.fromImage(image2)
        self.setPixmap()

    def edgeLogarithmic(self):
        self.desaturate()
        arr3 = lol.ARR3
        image = self.pixmap.toImage()
        image2 = self.pixmap.toImage()
        width = self.pixmap.width() - 4
        height = self.pixmap.height() - 4

        for x in range(3, width):
            for y in range(3, height):
                ar = lol.ar3(image, x, y)
                val = lol.nor(lol.c_ar(ar, arr3))
                image2.setPixel(x, y, QtGui.qRgb(val, val, val))

        self.pixmap = QtGui.QPixmap.fromImage(image2)
        self.setPixmap()

    def gausseFilter(self):
        image = self.pixmap.toImage()

        width = self.pixmap.width() - 2
        height = self.pixmap.height() - 2

        for x in range(2, width):
            for y in range(2, height):
                c = image.pixel(x, y)
                f_c = lol.cor_5x5(image, c, x, y)
                n_color = lol.gausser(f_c, lol.g_filter)
                image.setPixel(x, y, QtGui.qRgb(*n_color))
        self.pixmap = QtGui.QPixmap.fromImage(image)
        self.setPixmap()

    def setZero(self):
        self.monoCanal()

    def otsu(self):

        self.setZero()
        image = self.pixmap.toImage()
        width = image.width()
        height = image.height()
        highK, highF = 0, 0

        color_hi = defaultdict(lambda: 0)
        for x in range(width):
            for y in range(height):
                c = image.pixel(x, y)
                colors = QtGui.QColor(c).getRgb()

                color_r = colors[0] / 255
                color_g = colors[1] / 255
                color_b = colors[2] / 255

                color_h, color_l, color_s = cs.rgb_to_hls(color_r, color_g, color_b)
                color_hi[int(color_l * 255)] += 1

        for n in range(1, 255):
            bp, op, bpp, opb, awp = lol.gpixel(width, height, n, color_hi)

            some_lumin = bp / (bpp if bpp != 0 else 0.0001)
            second_lumin = op / (opb if opb != 0 else 0.00001)

            powed_l = pow(some_lumin - awp, 2)
            powed_s = pow(second_lumin - awp, 2)
            varI = (powed_l * bpp) + (powed_s * opb)

            highK = n if varI > highF else highK
            highF = varI if varI > highF else highF

        print('Binarization: {} {} {} {} {} '.format(bp, op, bpp, opb, awp))

        for x in range(width):
            for y in range(height):
                c = image.pixel(x, y)
                colors = QtGui.QColor(c).getRgb()

                color_r = colors[0] / 255
                color_g = colors[1] / 255
                color_b = colors[2] / 255

                color_h, color_l, color_s = cs.rgb_to_hls(color_r, color_g, color_b)

                if color_l < round(highK / 255, 3):
                    color_after_change = (0, 0, 0)
                else:
                    color_after_change = (255, 255, 255)
                image.setPixel(x, y, QtGui.qRgb(*color_after_change))

        self.pixmap = QtGui.QPixmap.fromImage(image)
        self.setPixmap()

    def moravec(self):
        image = self.pixmap.toImage()
        width = self.pixmap.width() - 1
        height = self.pixmap.height() - 1
        results = []
        colex = 400

        for x in range(1, width):
            for y in range(1, height):
                l_m = 1000
                c = image.pixel(x, y)
                colors = QtGui.QColor(c).getRgb()
                r, g, b = [x for x in [colors[0], colors[1], colors[2]]]
                limes = r * 299 / 1000 + g * 587 / 1000 + b * 114 / 1000
                for bj in [image.pixel(x - 1, y), image.pixel(x + 1, y), image.pixel(x, y - 1), image.pixel(x, y + 1)]:
                    colors = QtGui.QColor(bj).getRgb()
                    r, g, b = [x for x in [colors[0], colors[1], colors[2]]]
                    pix_l = r * 299 / 1000 + g * 587 / 1000 + b * 114 / 1000
                    elis = pow(abs(limes - pix_l), 2)
                    if elis < l_m:
                        l_m = elis
                if l_m > colex:
                    results.append((x, y))

        for dot in results:
            x, y = dot
            cgrey = QtGui.qRgb(105, 105, 105)
            for a in range(x - 2, x + 2):
                for b in range(y - 2, y + 2):
                    image.setPixel(a, b, cgrey)

        self.pixmap = QtGui.QPixmap.fromImage(image)
        self.setPixmap()

    def harris(self):
        self.desaturate()
        image = self.pixmap.toImage()
        width = self.pixmap.width()
        height = self.pixmap.height()
        iX = self.shelper(lol.slX)
        iY = self.shelper(lol.slY)

        for x in range(1, width - 1):
            for y in range(1, height - 1):
                if iX[x][y] < 0:
                    iX[x][y] *= -1
                if iY[x][y] < 0:
                    iY[x][y] *= -1

        resultX = arx.square(iX)
        resultY = arx.square(iY)
        bowe = arx.multiply(iX, iY)
        bowee = arx.multiply(iY, iX)
        artarax = arx.zeros((width, height), arx.float32)

        for x in range(width):
            for y in range(height):
                martarax = arx.array([[resultX[x][y], bowe[x][y]], [bowee[x][y], resultY[x][y]]])
                det = (resultX[x][y] * bowe[x][y]) - (bowee[x][y] * resultY[x][y])
                artarax[x][y] = det - (0.04 * arx.square(arx.trace(martarax)))

        for x in range(2, width - 2):
            for y in range(2, height - 2):
                if artarax[x][y] > 60000:
                    l_m = artarax[x][y]
                    xd = True
                    for z in range(x - 3, x + 3):
                        for q in range(y - 3, y + 3):
                            if artarax[z][q] > l_m:
                                xd = False
                    if xd:
                        image.setPixel(x, y, QtGui.qRgb(255, 0, 0))
                        image.setPixel(x + 1, y, QtGui.qRgb(255, 0, 0))
                        image.setPixel(x, y + 1, QtGui.qRgb(255, 0, 0))
                        image.setPixel(x - 1, y, QtGui.qRgb(255, 0, 0))
                        image.setPixel(x, y - 1, QtGui.qRgb(255, 0, 0))

        self.pixmap = QtGui.QPixmap.fromImage(image)
        self.setPixmap()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    AppWindow = MainAppWindow(QtWidgets.QMainWindow())
    AppWindow.MainWindowToni.show()
    sys.exit(app.exec_())
