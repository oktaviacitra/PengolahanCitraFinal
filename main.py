# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PIL import Image
import io
import random

class Ui_MainWindow(QtWidgets.QMainWindow):
    image_name = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(560, 40, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(560, 70, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 110, 351, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(325, 160, 391, 281))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(740, 160, 391, 281))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.chartview = QtChart.QChartView(self.centralwidget)
        self.chartview.setGeometry(QtCore.QRect(310, 470, 831, 331))
        self.chartview.setObjectName("chartview")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFlip = QtWidgets.QMenu(self.menuEdit)
        self.menuFlip.setObjectName("menuFlip")
        self.menuLayer = QtWidgets.QMenu(self.menuEdit)
        self.menuLayer.setObjectName("menuLayer")
        self.menuBlack_White = QtWidgets.QMenu(self.menuEdit)
        self.menuBlack_White.setObjectName("menuBlack_White")
        self.menuThreshold = QtWidgets.QMenu(self.menuBlack_White)
        self.menuThreshold.setObjectName("menuThreshold")
        self.menuDetection = QtWidgets.QMenu(self.menuEdit)
        self.menuDetection.setObjectName("menuDetection")
        self.menuLine = QtWidgets.QMenu(self.menuDetection)
        self.menuLine.setObjectName("menuLine")
        self.menuGrayscale = QtWidgets.QMenu(self.menuEdit)
        self.menuGrayscale.setObjectName("menuGrayscale")
        self.menuGrayscale_2 = QtWidgets.QMenu(self.menuGrayscale)
        self.menuGrayscale_2.setObjectName("menuGrayscale_2")
        self.menuQuantization_grayscale = QtWidgets.QMenu(self.menuGrayscale)
        self.menuQuantization_grayscale.setObjectName("menuQuantization_grayscale")
        self.menuBrightness_grayscale = QtWidgets.QMenu(self.menuGrayscale)
        self.menuBrightness_grayscale.setObjectName("menuBrightness_grayscale")
        self.menuContrast_grayscale = QtWidgets.QMenu(self.menuGrayscale)
        self.menuContrast_grayscale.setObjectName("menuContrast_grayscale")
        self.menuFilter_grayscale = QtWidgets.QMenu(self.menuGrayscale)
        self.menuFilter_grayscale.setObjectName("menuFilter_grayscale")
        self.menuNode = QtWidgets.QMenu(self.menuFilter_grayscale)
        self.menuNode.setObjectName("menuNode")
        self.menu4_grayscale = QtWidgets.QMenu(self.menuNode)
        self.menu4_grayscale.setObjectName("menu4_grayscale")
        self.menu8_grayscale = QtWidgets.QMenu(self.menuNode)
        self.menu8_grayscale.setObjectName("menu8_grayscale")
        self.menuNoise_grayscale = QtWidgets.QMenu(self.menuGrayscale)
        self.menuNoise_grayscale.setObjectName("menuNoise_grayscale")
        self.menuGaussian = QtWidgets.QMenu(self.menuNoise_grayscale)
        self.menuGaussian.setObjectName("menuGaussian")
        self.menuProbability = QtWidgets.QMenu(self.menuGaussian)
        self.menuProbability.setObjectName("menuProbability")
        self.menuSpeckle = QtWidgets.QMenu(self.menuNoise_grayscale)
        self.menuSpeckle.setObjectName("menuSpeckle")
        self.menuProbability_2 = QtWidgets.QMenu(self.menuSpeckle)
        self.menuProbability_2.setObjectName("menuProbability_2")
        self.menuSalt_and_Pepper = QtWidgets.QMenu(self.menuNoise_grayscale)
        self.menuSalt_and_Pepper.setObjectName("menuSalt_and_Pepper")
        self.menuProbabilty = QtWidgets.QMenu(self.menuSalt_and_Pepper)
        self.menuProbabilty.setObjectName("menuProbabilty")
        self.menuMethod_grayscale = QtWidgets.QMenu(self.menuGrayscale)
        self.menuMethod_grayscale.setObjectName("menuMethod_grayscale")
        self.menuSharpness = QtWidgets.QMenu(self.menuGrayscale)
        self.menuSharpness.setObjectName("menuSharpness")
        self.menuFull_Color = QtWidgets.QMenu(self.menuEdit)
        self.menuFull_Color.setObjectName("menuFull_Color")
        self.menuQuantization_full_color = QtWidgets.QMenu(self.menuFull_Color)
        self.menuQuantization_full_color.setObjectName("menuQuantization_full_color")
        self.menuBrightness__full_color = QtWidgets.QMenu(self.menuFull_Color)
        self.menuBrightness__full_color.setObjectName("menuBrightness__full_color")
        self.menuContrast__full_color = QtWidgets.QMenu(self.menuFull_Color)
        self.menuContrast__full_color.setObjectName("menuContrast__full_color")
        self.menuFilter_full_color = QtWidgets.QMenu(self.menuFull_Color)
        self.menuFilter_full_color.setObjectName("menuFilter_full_color")
        self.menuNode__full_color = QtWidgets.QMenu(self.menuFilter_full_color)
        self.menuNode__full_color.setObjectName("menuNode__full_color")
        self.menu4__full_color_filter = QtWidgets.QMenu(self.menuNode__full_color)
        self.menu4__full_color_filter.setObjectName("menu4__full_color_filter")
        self.menu8__full_color_filter = QtWidgets.QMenu(self.menuNode__full_color)
        self.menu8__full_color_filter.setObjectName("menu8__full_color_filter")
        self.menuNoise = QtWidgets.QMenu(self.menuFull_Color)
        self.menuNoise.setObjectName("menuNoise")
        self.menuGaussian_2 = QtWidgets.QMenu(self.menuNoise)
        self.menuGaussian_2.setObjectName("menuGaussian_2")
        self.menuProbability_3 = QtWidgets.QMenu(self.menuGaussian_2)
        self.menuProbability_3.setObjectName("menuProbability_3")
        self.menuSpeckle_2 = QtWidgets.QMenu(self.menuNoise)
        self.menuSpeckle_2.setObjectName("menuSpeckle_2")
        self.menuProbability_4 = QtWidgets.QMenu(self.menuSpeckle_2)
        self.menuProbability_4.setObjectName("menuProbability_4")
        self.menuSalt_and_Pepper_2 = QtWidgets.QMenu(self.menuNoise)
        self.menuSalt_and_Pepper_2.setObjectName("menuSalt_and_Pepper_2")
        self.menuProbability_5 = QtWidgets.QMenu(self.menuSalt_and_Pepper_2)
        self.menuProbability_5.setObjectName("menuProbability_5")
        self.menuMethod = QtWidgets.QMenu(self.menuFull_Color)
        self.menuMethod.setObjectName("menuMethod")
        self.menuSharpness_2 = QtWidgets.QMenu(self.menuFull_Color)
        self.menuSharpness_2.setObjectName("menuSharpness_2")
        self.menuRotate = QtWidgets.QMenu(self.menuEdit)
        self.menuRotate.setObjectName("menuRotate")
        self.menuChart = QtWidgets.QMenu(self.menubar)
        self.menuChart.setObjectName("menuChart")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.open_image)

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.save_image)

        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCopy.triggered.connect(self.copy_image)

        self.actionHorizontal_flip = QtWidgets.QAction(MainWindow)
        self.actionHorizontal_flip.setObjectName("actionHorizontal_flip")
        self.actionHorizontal_flip.triggered.connect(lambda: self.flip_image(-1, 1))

        self.actionVertical_flip = QtWidgets.QAction(MainWindow)
        self.actionVertical_flip.setObjectName("actionVertical_flip")
        self.actionVertical_flip.triggered.connect(lambda: self.flip_image(1, -1))

        self.actionRGB_layer = QtWidgets.QAction(MainWindow)
        self.actionRGB_layer.setObjectName("actionRGB_layer")
        self.actionRGB_layer.triggered.connect(lambda: self.layer_image(1))

        self.actionRed_layer = QtWidgets.QAction(MainWindow)
        self.actionRed_layer.setObjectName("actionRed_layer")
        self.actionRed_layer.triggered.connect(lambda: self.layer_image(2))

        self.actionGreen_layer = QtWidgets.QAction(MainWindow)
        self.actionGreen_layer.setObjectName("actionGreen_layer")
        self.actionGreen_layer.triggered.connect(lambda: self.layer_image(3))

        self.actionBlue_layer = QtWidgets.QAction(MainWindow)
        self.actionBlue_layer.setObjectName("actionBlue_layer")
        self.actionBlue_layer.triggered.connect(lambda: self.layer_image(4))

        self.actionBlack_white_black_white = QtWidgets.QAction(MainWindow)
        self.actionBlack_white_black_white.setObjectName("actionBlack_white_black_white")
        self.actionBlack_white_black_white.triggered.connect(lambda: self.black_white_image(1))

        self.action100_blackWhite = QtWidgets.QAction(MainWindow)
        self.action100_blackWhite.setObjectName("action100_blackWhite")
        self.action100_blackWhite.triggered.connect(lambda: self.black_white_image(2))

        self.action200_blackWhite = QtWidgets.QAction(MainWindow)
        self.action200_blackWhite.setObjectName("action200_blackWhite")
        self.action200_blackWhite.triggered.connect(lambda: self.black_white_image(3))

        self.actionAverage_threshold_black_white = QtWidgets.QAction(MainWindow)
        self.actionAverage_threshold_black_white.setObjectName("actionAverage_threshold_black_white")
        self.actionAverage_threshold_black_white.triggered.connect(lambda: self.black_white_image(4))

        self.actionEdge_detection = QtWidgets.QAction(MainWindow)
        self.actionEdge_detection.setObjectName("actionEdge_detection")
        self.actionEdge_detection.triggered.connect(self.detection_edge)

        self.actionHorizontal_line_detection = QtWidgets.QAction(MainWindow)
        self.actionHorizontal_line_detection.setObjectName("actionHorizontal_line_detection")
        self.actionHorizontal_line_detection.triggered.connect(lambda: self.detection_image(2))

        self.actionVertical_line_detection = QtWidgets.QAction(MainWindow)
        self.actionVertical_line_detection.setObjectName("actionVertical_line_detection")
        self.actionVertical_line_detection.triggered.connect(lambda: self.detection_image(3))

        self.actionNode_detection = QtWidgets.QAction(MainWindow)
        self.actionNode_detection.setObjectName("actionNode_detection")
        self.actionNode_detection.triggered.connect(lambda: self.detection_image(1))

        self.actionRGB_grayscale = QtWidgets.QAction(MainWindow)
        self.actionRGB_grayscale.setObjectName("actionRGB_grayscale")
        self.actionRGB_grayscale.triggered.connect(lambda: self.grayscale_image(1))

        self.actionRed_grayscale = QtWidgets.QAction(MainWindow)
        self.actionRed_grayscale.setObjectName("actionRed_grayscale")
        self.actionRed_grayscale.triggered.connect(lambda: self.grayscale_image(2))

        self.actionGreen_grayscale = QtWidgets.QAction(MainWindow)
        self.actionGreen_grayscale.setObjectName("actionGreen_grayscale")
        self.actionGreen_grayscale.triggered.connect(lambda: self.grayscale_image(3))

        self.actionBlue_grayscale = QtWidgets.QAction(MainWindow)
        self.actionBlue_grayscale.setObjectName("actionBlue_grayscale")
        self.actionBlue_grayscale.triggered.connect(lambda: self.grayscale_image(4))

        self.action8_grayscale_quantization = QtWidgets.QAction(MainWindow)
        self.action8_grayscale_quantization.setObjectName("action8_grayscale_quantization")
        self.action8_grayscale_quantization.triggered.connect(lambda: self.quantization_grayscale_image(8))

        self.action16_grayscale_quantization = QtWidgets.QAction(MainWindow)
        self.action16_grayscale_quantization.setObjectName("action16_grayscale_quantization")
        self.action16_grayscale_quantization.triggered.connect(lambda: self.quantization_grayscale_image(16))

        self.action32_grayscale_quantization = QtWidgets.QAction(MainWindow)
        self.action32_grayscale_quantization.setObjectName("action32_grayscale_quantization")
        self.action32_grayscale_quantization.triggered.connect(lambda: self.quantization_grayscale_image(32))

        self.action64_grayscale_quantization = QtWidgets.QAction(MainWindow)
        self.action64_grayscale_quantization.setObjectName("action64_grayscale_quantization")
        self.action64_grayscale_quantization.triggered.connect(lambda: self.quantization_grayscale_image(64))

        self.actionLow_grayscale_brightness = QtWidgets.QAction(MainWindow)
        self.actionLow_grayscale_brightness.setObjectName("actionLow_grayscale_brightness")
        self.actionLow_grayscale_brightness.triggered.connect(lambda: self.brightness_image(1, 10))

        self.actionMedium_grayscale_brightness = QtWidgets.QAction(MainWindow)
        self.actionMedium_grayscale_brightness.setObjectName("actionMedium_grayscale_brightness")
        self.actionMedium_grayscale_brightness.triggered.connect(lambda: self.brightness_image(1, 20))

        self.actionHigh_grayscale_brightness = QtWidgets.QAction(MainWindow)
        self.actionHigh_grayscale_brightness.setObjectName("actionHigh_grayscale_brightness")
        self.actionHigh_grayscale_brightness.triggered.connect(lambda: self.brightness_image(1, 20))

        self.actionLow_grayscale_contrast = QtWidgets.QAction(MainWindow)
        self.actionLow_grayscale_contrast.setObjectName("actionLow_grayscale_contrast")
        self.actionLow_grayscale_contrast.triggered.connect(lambda: self.contrast_image(1, 5))

        self.actionMedium_grayscale_contrast = QtWidgets.QAction(MainWindow)
        self.actionMedium_grayscale_contrast.setObjectName("actionMedium_grayscale_contrast")
        self.actionMedium_grayscale_contrast.triggered.connect(lambda: self.contrast_image(1, 10))

        self.actionHigh_grayscale_contrast = QtWidgets.QAction(MainWindow)
        self.actionHigh_grayscale_contrast.setObjectName("actionHigh_grayscale_contrast")
        self.actionHigh_grayscale_contrast.triggered.connect(lambda: self.contrast_image(1, 15))

        self.actionInvers_grayscale = QtWidgets.QAction(MainWindow)
        self.actionInvers_grayscale.setObjectName("actionInvers_grayscale")
        self.actionInvers_grayscale.triggered.connect(lambda: self.invers_image(1))

        self.actionAutolevel_grayscale = QtWidgets.QAction(MainWindow)
        self.actionAutolevel_grayscale.setObjectName("actionAutolevel_grayscale")
        self.actionAutolevel_grayscale.triggered.connect(lambda: self.auto_level_image(1))

        self.actionSharpness_grayscale_sharpness = QtWidgets.QAction(MainWindow)
        self.actionSharpness_grayscale_sharpness.setObjectName("actionSharpness_grayscale_sharpness")
        self.actionSharpness_grayscale_sharpness.triggered.connect(lambda: self.sharpness_grayscale_image(1))

        self.actionLPF_grayscale_sharpness = QtWidgets.QAction(MainWindow)
        self.actionLPF_grayscale_sharpness.setObjectName("actionLPF_grayscale_sharpness")
        self.actionLPF_grayscale_sharpness.triggered.connect(lambda: self.sharpness_grayscale_image(2))

        self.actionHPF_grayscale_sharpness = QtWidgets.QAction(MainWindow)
        self.actionHPF_grayscale_sharpness.setObjectName("actionHPF_grayscale_sharpness")
        self.actionHPF_grayscale_sharpness.triggered.connect(lambda: self.sharpness_grayscale_image(3))

        self.actionConvolution_1_grayscale_filter4node = QtWidgets.QAction(MainWindow)
        self.actionConvolution_1_grayscale_filter4node.setObjectName("actionConvolution_1_grayscale_filter4node")
        self.actionConvolution_1_grayscale_filter4node.triggered.connect(lambda: self.filter_4_node_image(1, 1))

        self.actionConvolution_2_grayscale_filter4node = QtWidgets.QAction(MainWindow)
        self.actionConvolution_2_grayscale_filter4node.setObjectName("actionConvolution_2_grayscale_filter4node")
        self.actionConvolution_2_grayscale_filter4node.triggered.connect(lambda: self.filter_4_node_image(1, 2))

        self.actionConvolution_3_grayscale_filter4node = QtWidgets.QAction(MainWindow)
        self.actionConvolution_3_grayscale_filter4node.setObjectName("actionConvolution_3_grayscale_filter4node")
        self.actionConvolution_3_grayscale_filter4node.triggered.connect(lambda: self.filter_4_node_image(1, 3))

        self.actionConvolution_1_grayscale_filter8node = QtWidgets.QAction(MainWindow)
        self.actionConvolution_1_grayscale_filter8node.setObjectName("actionConvolution_1_grayscale_filter8node")
        self.actionConvolution_1_grayscale_filter8node.triggered.connect(lambda: self.filter_8_node_image(1, 1))

        self.actionConvolution_2_grayscale_filter8node = QtWidgets.QAction(MainWindow)
        self.actionConvolution_2_grayscale_filter8node.setObjectName("actionConvolution_2_grayscale_filter8node")
        self.actionConvolution_2_grayscale_filter8node.triggered.connect(lambda: self.filter_8_node_image(1, 2))

        self.actionConvolution_3_grayscale_filter8node = QtWidgets.QAction(MainWindow)
        self.actionConvolution_3_grayscale_filter8node.setObjectName("actionConvolution_3_grayscale_filter8node")
        self.actionConvolution_3_grayscale_filter8node.triggered.connect(lambda: self.filter_8_node_image(1, 3))

        self.actionAverage_grayscale_filter = QtWidgets.QAction(MainWindow)
        self.actionAverage_grayscale_filter.setObjectName("actionAverage_grayscale_filter")
        self.actionAverage_grayscale_filter.triggered.connect(lambda: self.average_filter_image(1))

        self.actionGaussian_grayscale_filter = QtWidgets.QAction(MainWindow)
        self.actionGaussian_grayscale_filter.setObjectName("actionGaussian_grayscale_filter")
        self.actionGaussian_grayscale_filter.triggered.connect(lambda: self.gaussian_filter_image(1))

        self.actionMedian_grayscale_filter = QtWidgets.QAction(MainWindow)
        self.actionMedian_grayscale_filter.setObjectName("actionMedian_grayscale_filter")
        self.actionMedian_grayscale_filter.triggered.connect(lambda: self.median_filter_image(1))

        self.actionRobert_grayscale_method = QtWidgets.QAction(MainWindow)
        self.actionRobert_grayscale_method.setObjectName("actionRobert_grayscale_method")
        self.actionRobert_grayscale_method.triggered.connect(lambda: self.robert_method_image(1))

        self.actionPrewitt_grayscale_method = QtWidgets.QAction(MainWindow)
        self.actionPrewitt_grayscale_method.setObjectName("actionPrewitt_grayscale_method")
        self.actionPrewitt_grayscale_method.triggered.connect(lambda: self.prewitt_method_image(1))

        self.actionSobel_grayscale_method = QtWidgets.QAction(MainWindow)
        self.actionSobel_grayscale_method.setObjectName("actionSobel_grayscale_method")
        self.actionSobel_grayscale_method.triggered.connect(lambda: self.sobel_method_image(1))

        self.actionLaplacian_grayscale_method = QtWidgets.QAction(MainWindow)
        self.actionLaplacian_grayscale_method.setObjectName("actionLaplacian_grayscale_method")
        self.actionLaplacian_grayscale_method.triggered.connect(lambda: self.laplacian_method_image(1))

        self.actionGaussian_grayscale_noise_gaussian = QtWidgets.QAction(MainWindow)
        self.actionGaussian_grayscale_noise_gaussian.setObjectName("actionGaussian_grayscale_noise_gaussian")
        self.actionGaussian_grayscale_noise_gaussian.triggered.connect(lambda: self.gaussian_noise_image(1, 20))

        self.action5_grayscale_noise_gaussian = QtWidgets.QAction(MainWindow)
        self.action5_grayscale_noise_gaussian.setObjectName("action5_grayscale_noise_gaussian")
        self.action5_grayscale_noise_gaussian.triggered.connect(lambda: self.gaussian_noise_image(1, 5))

        self.action10_grayscale_noise_gaussian = QtWidgets.QAction(MainWindow)
        self.action10_grayscale_noise_gaussian.setObjectName("action10_grayscale_noise_gaussian")
        self.action10_grayscale_noise_gaussian.triggered.connect(lambda: self.gaussian_noise_image(1, 10))

        self.action20_grayscale_noise_gaussian = QtWidgets.QAction(MainWindow)
        self.action20_grayscale_noise_gaussian.setObjectName("action20_grayscale_noise_gaussian")
        self.action20_grayscale_noise_gaussian.triggered.connect(lambda: self.gaussian_noise_image(1, 20))

        self.action30_grayscale_noise_gaussian = QtWidgets.QAction(MainWindow)
        self.action30_grayscale_noise_gaussian.setObjectName("action30_grayscale_noise_gaussian")
        self.action30_grayscale_noise_gaussian.triggered.connect(lambda: self.gaussian_noise_image(1, 30))

        self.action40_grayscale_noise_gaussian = QtWidgets.QAction(MainWindow)
        self.action40_grayscale_noise_gaussian.setObjectName("action40_grayscale_noise_gaussian")
        self.action40_grayscale_noise_gaussian.triggered.connect(lambda: self.gaussian_noise_image(1, 40))

        self.actionSpeckle_grayscale_noise_speckle = QtWidgets.QAction(MainWindow)
        self.actionSpeckle_grayscale_noise_speckle.setObjectName("actionSpeckle_grayscale_noise_speckle")
        self.actionSpeckle_grayscale_noise_speckle.triggered.connect(lambda: self.speckle_noise_image(1, 20))

        self.action5_grayscale_noise_speckle = QtWidgets.QAction(MainWindow)
        self.action5_grayscale_noise_speckle.setObjectName("action5_grayscale_noise_speckle")
        self.action5_grayscale_noise_speckle.triggered.connect(lambda: self.speckle_noise_image(1, 5))

        self.action10_grayscale_noise_speckle = QtWidgets.QAction(MainWindow)
        self.action10_grayscale_noise_speckle.setObjectName("action10_grayscale_noise_speckle")
        self.action10_grayscale_noise_speckle.triggered.connect(lambda: self.speckle_noise_image(1, 10))

        self.action20_grayscale_noise_speckle = QtWidgets.QAction(MainWindow)
        self.action20_grayscale_noise_speckle.setObjectName("action20_grayscale_noise_speckle")
        self.action20_grayscale_noise_speckle.triggered.connect(lambda: self.speckle_noise_image(1, 20))

        self.action30_grayscale_noise_speckle = QtWidgets.QAction(MainWindow)
        self.action30_grayscale_noise_speckle.setObjectName("action30_grayscale_noise_speckle")
        self.action30_grayscale_noise_speckle.triggered.connect(lambda: self.speckle_noise_image(1, 30))

        self.action40_grayscale_noise_speckle = QtWidgets.QAction(MainWindow)
        self.action40_grayscale_noise_speckle.setObjectName("action40_grayscale_noise_speckle")
        self.action40_grayscale_noise_speckle.triggered.connect(lambda: self.speckle_noise_image(1, 40))

        self.actionSalt_and_Pepper_grayscale_noise_saltnpepper = QtWidgets.QAction(MainWindow)
        self.actionSalt_and_Pepper_grayscale_noise_saltnpepper.setObjectName("actionSalt_and_Pepper_grayscale_noise_saltnpepper")
        self.actionSalt_and_Pepper_grayscale_noise_saltnpepper.triggered.connect(lambda: self.salt_pepper_noise_image(1, 20))

        self.action5_noise_saltnpepper = QtWidgets.QAction(MainWindow)
        self.action5_noise_saltnpepper.setObjectName("action5_noise_saltnpepper")
        self.action5_noise_saltnpepper.triggered.connect(lambda: self.salt_pepper_noise_image(1, 5))

        self.action10_noise_saltnpepper = QtWidgets.QAction(MainWindow)
        self.action10_noise_saltnpepper.setObjectName("action10_noise_saltnpepper")
        self.action10_noise_saltnpepper.triggered.connect(lambda: self.salt_pepper_noise_image(1, 10))

        self.action20_noise_saltnpepper = QtWidgets.QAction(MainWindow)
        self.action20_noise_saltnpepper.setObjectName("action20_noise_saltnpepper")
        self.action20_noise_saltnpepper.triggered.connect(lambda: self.salt_pepper_noise_image(1, 20))

        self.action30_noise_saltnpepper = QtWidgets.QAction(MainWindow)
        self.action30_noise_saltnpepper.setObjectName("action30_noise_saltnpepper")
        self.action30_noise_saltnpepper.triggered.connect(lambda: self.salt_pepper_noise_image(1, 30))

        self.action40_noise_saltnpepper = QtWidgets.QAction(MainWindow)
        self.action40_noise_saltnpepper.setObjectName("action40_noise_saltnpepper")
        self.action40_noise_saltnpepper.triggered.connect(lambda: self.salt_pepper_noise_image(1, 40))

        self.action8_full_color_quantization = QtWidgets.QAction(MainWindow)
        self.action8_full_color_quantization.setObjectName("action8_full_color_quantization")
        self.action8_full_color_quantization.triggered.connect(lambda: self.quantization_full_color_image(8))

        self.action16_full_color_quantization = QtWidgets.QAction(MainWindow)
        self.action16_full_color_quantization.setObjectName("action16_full_color_quantization")
        self.action16_full_color_quantization.triggered.connect(lambda: self.quantization_full_color_image(16))

        self.action32_full_color_quantization = QtWidgets.QAction(MainWindow)
        self.action32_full_color_quantization.setObjectName("action32_full_color_quantization")
        self.action32_full_color_quantization.triggered.connect(lambda: self.quantization_full_color_image(32))

        self.action64_full_color_quantization = QtWidgets.QAction(MainWindow)
        self.action64_full_color_quantization.setObjectName("action64_full_color_quantization")
        self.action64_full_color_quantization.triggered.connect(lambda: self.quantization_full_color_image(64))

        self.actionLow_full_color_brightness = QtWidgets.QAction(MainWindow)
        self.actionLow_full_color_brightness.setObjectName("actionLow_full_color_brightness")
        self.actionLow_full_color_brightness.triggered.connect(lambda: self.brightness_image(2, 10))

        self.actionMedium_full_color_brightness = QtWidgets.QAction(MainWindow)
        self.actionMedium_full_color_brightness.setObjectName("actionMedium_full_color_brightness")
        self.actionMedium_full_color_brightness.triggered.connect(lambda: self.brightness_image(2, 20))

        self.actionHigh_full_color_brightness = QtWidgets.QAction(MainWindow)
        self.actionHigh_full_color_brightness.setObjectName("actionHigh_full_color_brightness")
        self.actionHigh_full_color_brightness.triggered.connect(lambda: self.brightness_image(2, 30))

        self.actionLow_full_color_contrast = QtWidgets.QAction(MainWindow)
        self.actionLow_full_color_contrast.setObjectName("actionLow_full_color_contrast")
        self.actionLow_full_color_contrast.triggered.connect(lambda: self.contrast_image(2, 5))

        self.actionMedium_full_color_contrast = QtWidgets.QAction(MainWindow)
        self.actionMedium_full_color_contrast.setObjectName("actionMedium_full_color_contrast")
        self.actionMedium_full_color_contrast.triggered.connect(lambda: self.contrast_image(2, 10))

        self.actionHigh_full_color_contrast = QtWidgets.QAction(MainWindow)
        self.actionHigh_full_color_contrast.setObjectName("actionHigh_full_color_contrast")
        self.actionHigh_full_color_contrast.triggered.connect(lambda: self.contrast_image(2, 20))

        self.actionInvers_full_color = QtWidgets.QAction(MainWindow)
        self.actionInvers_full_color.setObjectName("actionInvers_full_color")
        self.actionInvers_full_color.triggered.connect(lambda: self.invers_image(2))

        self.actionAutolevel_full_color = QtWidgets.QAction(MainWindow)
        self.actionAutolevel_full_color.setObjectName("actionAutolevel_full_color")
        self.actionAutolevel_full_color.triggered.connect(lambda: self.auto_level_image(2))

        self.actionSharpness_full_color_sharpness = QtWidgets.QAction(MainWindow)
        self.actionSharpness_full_color_sharpness.setObjectName("actionSharpness_full_color_sharpness")
        self.actionSharpness_full_color_sharpness.triggered.connect(lambda: self.sharpness_full_color_image(1))

        self.actionLPF_full_color_sharpness = QtWidgets.QAction(MainWindow)
        self.actionLPF_full_color_sharpness.setObjectName("actionLPF_full_color_sharpness")
        self.actionLPF_full_color_sharpness.triggered.connect(lambda: self.sharpness_full_color_image(2))

        self.actionHPF_full_color_sharpness = QtWidgets.QAction(MainWindow)
        self.actionHPF_full_color_sharpness.setObjectName("actionHPF_full_color_sharpness")
        self.actionHPF_full_color_sharpness.triggered.connect(lambda: self.sharpness_full_color_image(3))

        self.actionAverage_full_color_filter = QtWidgets.QAction(MainWindow)
        self.actionAverage_full_color_filter.setObjectName("actionAverage_full_color_filter")
        self.actionAverage_full_color_filter.triggered.connect(lambda: self.average_filter_image(2))

        self.actionGaussian_full_color_filter = QtWidgets.QAction(MainWindow)
        self.actionGaussian_full_color_filter.setObjectName("actionGaussian_full_color_filter")
        self.actionGaussian_full_color_filter.triggered.connect(lambda: self.gaussian_filter_image(2))
        
        self.actionMedian_full_color_filter = QtWidgets.QAction(MainWindow)
        self.actionMedian_full_color_filter.setObjectName("actionMedian_full_color_filter")
        self.actionMedian_full_color_filter.triggered.connect(lambda: self.median_filter_image(2))

        self.actionConvolution_1_full_color_filter4node = QtWidgets.QAction(MainWindow)
        self.actionConvolution_1_full_color_filter4node.setObjectName("actionConvolution_1_full_color_filter4node")
        self.actionConvolution_1_full_color_filter4node.triggered.connect(lambda: self.filter_4_node_image(2, 1))

        self.actionConvolution_2_full_color_filter4node = QtWidgets.QAction(MainWindow)
        self.actionConvolution_2_full_color_filter4node.setObjectName("actionConvolution_2_full_color_filter4node")
        self.actionConvolution_2_full_color_filter4node.triggered.connect(lambda: self.filter_4_node_image(2, 2))

        self.actionConvolution_3_full_color_filter4node = QtWidgets.QAction(MainWindow)
        self.actionConvolution_3_full_color_filter4node.setObjectName("actionConvolution_3_full_color_filter4node")
        self.actionConvolution_3_full_color_filter4node.triggered.connect(lambda: self.filter_4_node_image(2, 3))

        self.actionConvolution_1_full_color_filter8node = QtWidgets.QAction(MainWindow)
        self.actionConvolution_1_full_color_filter8node.setObjectName("actionConvolution_1_full_color_filter8node")
        self.actionConvolution_1_full_color_filter8node.triggered.connect(lambda: self.filter_4_node_image(2, 1))

        self.actionConvolution_2_full_color_filter8node = QtWidgets.QAction(MainWindow)
        self.actionConvolution_2_full_color_filter8node.setObjectName("actionConvolution_2_full_color_filter8node")
        self.actionConvolution_2_full_color_filter8node.triggered.connect(lambda: self.filter_4_node_image(2, 2))

        self.actionConvolution_3_full_color_filter8node = QtWidgets.QAction(MainWindow)
        self.actionConvolution_3_full_color_filter8node.setObjectName("actionConvolution_3_full_color_filter8node")
        self.actionConvolution_3_full_color_filter8node.triggered.connect(lambda: self.filter_4_node_image(2, 3))

        self.actionGaussian_full_color_method = QtWidgets.QAction(MainWindow)
        self.actionGaussian_full_color_method.setObjectName("actionGaussian_full_color_method")
        self.actionGaussian_full_color_method.triggered.connect(lambda: self.gaussian_noise_image(2, 20))

        self.actionGaussian_full_color_gaussian = QtWidgets.QAction(MainWindow)
        self.actionGaussian_full_color_gaussian.setObjectName("actionGaussian_full_color_gaussian")
        self.actionGaussian_full_color_gaussian.triggered.connect(lambda: self.gaussian_noise_image(2, 20))

        self.action5_full_color_noise_gaussian = QtWidgets.QAction(MainWindow)
        self.action5_full_color_noise_gaussian.setObjectName("action5_full_color_noise_gaussian")
        self.action5_full_color_noise_gaussian.triggered.connect(lambda: self.gaussian_noise_image(2, 5))

        self.action10_full_color_noise_gaussian = QtWidgets.QAction(MainWindow)
        self.action10_full_color_noise_gaussian.setObjectName("action10_full_color_noise_gaussian")
        self.action10_full_color_noise_gaussian.triggered.connect(lambda: self.gaussian_noise_image(2, 10))

        self.action20_full_color_noise_gaussian = QtWidgets.QAction(MainWindow)
        self.action20_full_color_noise_gaussian.setObjectName("action20_full_color_noise_gaussian")
        self.action20_full_color_noise_gaussian.triggered.connect(lambda: self.gaussian_noise_image(2, 20))

        self.action30_full_color_noise_gaussian = QtWidgets.QAction(MainWindow)
        self.action30_full_color_noise_gaussian.setObjectName("action30_full_color_noise_gaussian")
        self.action30_full_color_noise_gaussian.triggered.connect(lambda: self.gaussian_noise_image(2, 30))

        self.action40_full_color_noise_gaussian = QtWidgets.QAction(MainWindow)
        self.action40_full_color_noise_gaussian.setObjectName("action40_full_color_noise_gaussian")
        self.action40_full_color_noise_gaussian.triggered.connect(lambda: self.gaussian_noise_image(2, 40))

        self.actionSpeckle_full_color_noise = QtWidgets.QAction(MainWindow)
        self.actionSpeckle_full_color_noise.setObjectName("actionSpeckle_full_color_noise")
        self.actionSpeckle_full_color_noise.triggered.connect(lambda: self.speckle_noise_image(2, 20))

        self.action5_full_color_noise_speckle = QtWidgets.QAction(MainWindow)
        self.action5_full_color_noise_speckle.setObjectName("action5_full_color_noise_speckle")
        self.action5_full_color_noise_speckle.triggered.connect(lambda: self.speckle_noise_image(2, 5))

        self.action10_full_color_noise_speckle = QtWidgets.QAction(MainWindow)
        self.action10_full_color_noise_speckle.setObjectName("action10_full_color_noise_speckle")
        self.action10_full_color_noise_speckle.triggered.connect(lambda: self.speckle_noise_image(2, 10))

        self.action20_full_color_noise_speckle = QtWidgets.QAction(MainWindow)
        self.action20_full_color_noise_speckle.setObjectName("action20_full_color_noise_speckle")
        self.action20_full_color_noise_speckle.triggered.connect(lambda: self.speckle_noise_image(2, 20))

        self.action30_full_color_noise_speckle = QtWidgets.QAction(MainWindow)
        self.action30_full_color_noise_speckle.setObjectName("action30_full_color_noise_speckle")
        self.action30_full_color_noise_speckle.triggered.connect(lambda: self.speckle_noise_image(2, 30))

        self.action40_full_color_noise_speckle = QtWidgets.QAction(MainWindow)
        self.action40_full_color_noise_speckle.setObjectName("action40_full_color_noise_speckle")
        self.action40_full_color_noise_speckle.triggered.connect(lambda: self.speckle_noise_image(1, 40))

        self.actionSalt_and_Pepper_noise_full_color = QtWidgets.QAction(MainWindow)
        self.actionSalt_and_Pepper_noise_full_color.setObjectName("actionSalt_and_Pepper_noise_full_color")
        self.actionSalt_and_Pepper_noise_full_color.triggered.connect(lambda: self.salt_pepper_noise_image(2, 20))

        self.action5_full_color_salt_pepper = QtWidgets.QAction(MainWindow)
        self.action5_full_color_salt_pepper.setObjectName("action5_full_color_salt_pepper")
        self.action5_full_color_salt_pepper.triggered.connect(lambda: self.salt_pepper_noise_image(2, 5))

        self.action10_full_color_salt_pepper = QtWidgets.QAction(MainWindow)
        self.action10_full_color_salt_pepper.setObjectName("action10_full_color_salt_pepper")
        self.action10_full_color_salt_pepper.triggered.connect(lambda: self.salt_pepper_noise_image(2, 10))

        self.action20_full_color_salt_pepper = QtWidgets.QAction(MainWindow)
        self.action20_full_color_salt_pepper.setObjectName("action20_full_color_salt_pepper")
        self.action20_full_color_salt_pepper.triggered.connect(lambda: self.salt_pepper_noise_image(2, 20))

        self.action30_full_color_salt_pepper = QtWidgets.QAction(MainWindow)
        self.action30_full_color_salt_pepper.setObjectName("action30_full_color_salt_pepper")
        self.action30_full_color_salt_pepper.triggered.connect(lambda: self.salt_pepper_noise_image(2, 30))

        self.action40_full_color_salt_pepper = QtWidgets.QAction(MainWindow)
        self.action40_full_color_salt_pepper.setObjectName("action40_full_color_salt_pepper")
        self.action40_full_color_salt_pepper.triggered.connect(lambda: self.salt_pepper_noise_image(2, 20))

        self.actionRobert_full_color_method = QtWidgets.QAction(MainWindow)
        self.actionRobert_full_color_method.setObjectName("actionRobert_full_color_method")
        self.actionRobert_full_color_method.triggered.connect(lambda: self.robert_method_image(2))

        self.actionPrewitt_full_color_method = QtWidgets.QAction(MainWindow)
        self.actionPrewitt_full_color_method.setObjectName("actionPrewitt_full_color_method")
        self.actionPrewitt_full_color_method.triggered.connect(lambda: self.prewitt_method_image(2))

        self.actionSobel_full_color_method = QtWidgets.QAction(MainWindow)
        self.actionSobel_full_color_method.setObjectName("actionSobel_full_color_method")
        self.actionSobel_full_color_method.triggered.connect(lambda: self.sobel_method_image(2))

        self.actionLaplacian_full_color_method = QtWidgets.QAction(MainWindow)
        self.actionLaplacian_full_color_method.setObjectName("actionLaplacian_full_color_method")
        self.actionLaplacian_full_color_method.triggered.connect(lambda: self.laplacian_method_image(2))

        self.actionHistogram = QtWidgets.QAction(MainWindow)
        self.actionHistogram.setObjectName("actionHistogram")
        self.actionHistogram.triggered.connect(self.set_histogram)

        self.actionCDF = QtWidgets.QAction(MainWindow)
        self.actionCDF.setObjectName("actionCDF")
        self.actionCDF.triggered.connect(self.set_cdf)
        
        self.actionPDF = QtWidgets.QAction(MainWindow)
        self.actionPDF.setObjectName("actionPDF")
        self.actionPDF.triggered.connect(self.set_pdf)

        self.actionPDF_to_CDF = QtWidgets.QAction(MainWindow)
        self.actionPDF_to_CDF.setObjectName("actionPDF_to_CDF")
        self.actionPDF_to_CDF.triggered.connect(self.convert_pdf_to_cdf)

        self.action90_rotate = QtWidgets.QAction(MainWindow)
        self.action90_rotate.setObjectName("action90_rotate")
        self.action90_rotate.triggered.connect(lambda: self.rotate_image(90))

        self.action180_rotate = QtWidgets.QAction(MainWindow)
        self.action180_rotate.setObjectName("action180_rotate")
        self.action180_rotate.triggered.connect(lambda: self.rotate_image(180))

        self.action270_rotate = QtWidgets.QAction(MainWindow)
        self.action270_rotate.setObjectName("action270_rotate")
        self.action270_rotate.triggered.connect(lambda: self.rotate_image(270))

        self.action360_rotate = QtWidgets.QAction(MainWindow)
        self.action360_rotate.setObjectName("action360_rotate")
        self.action360_rotate.triggered.connect(lambda: self.rotate_image(360))

        self.actionEqualization_grayscale = QtWidgets.QAction(MainWindow)
        self.actionEqualization_grayscale.setObjectName("actionEqualization_grayscale")
        self.actionEqualization_grayscale.triggered.connect(lambda: self.equalization_image(1))

        self.actionEqualization_full_color = QtWidgets.QAction(MainWindow)
        self.actionEqualization_full_color.setObjectName("actionEqualization_full_color")
        self.actionEqualization_full_color.triggered.connect(lambda: self.equalization_image(2))

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionCopy)
        self.menuFlip.addAction(self.actionHorizontal_flip)
        self.menuFlip.addAction(self.actionVertical_flip)
        self.menuLayer.addAction(self.actionRGB_layer)
        self.menuLayer.addAction(self.actionRed_layer)
        self.menuLayer.addAction(self.actionGreen_layer)
        self.menuLayer.addAction(self.actionBlue_layer)
        self.menuThreshold.addAction(self.action100_blackWhite)
        self.menuThreshold.addAction(self.action200_blackWhite)
        self.menuThreshold.addAction(self.actionAverage_threshold_black_white)
        self.menuBlack_White.addAction(self.actionBlack_white_black_white)
        self.menuBlack_White.addAction(self.menuThreshold.menuAction())
        self.menuLine.addAction(self.actionHorizontal_line_detection)
        self.menuLine.addAction(self.actionVertical_line_detection)
        self.menuDetection.addAction(self.actionEdge_detection)
        self.menuDetection.addAction(self.menuLine.menuAction())
        self.menuDetection.addAction(self.actionNode_detection)
        self.menuGrayscale_2.addAction(self.actionRGB_grayscale)
        self.menuGrayscale_2.addAction(self.actionRed_grayscale)
        self.menuGrayscale_2.addAction(self.actionGreen_grayscale)
        self.menuGrayscale_2.addAction(self.actionBlue_grayscale)
        self.menuQuantization_grayscale.addAction(self.action8_grayscale_quantization)
        self.menuQuantization_grayscale.addAction(self.action16_grayscale_quantization)
        self.menuQuantization_grayscale.addAction(self.action32_grayscale_quantization)
        self.menuQuantization_grayscale.addAction(self.action64_grayscale_quantization)
        self.menuBrightness_grayscale.addAction(self.actionLow_grayscale_brightness)
        self.menuBrightness_grayscale.addAction(self.actionMedium_grayscale_brightness)
        self.menuBrightness_grayscale.addAction(self.actionHigh_grayscale_brightness)
        self.menuContrast_grayscale.addAction(self.actionLow_grayscale_contrast)
        self.menuContrast_grayscale.addAction(self.actionMedium_grayscale_contrast)
        self.menuContrast_grayscale.addAction(self.actionHigh_grayscale_contrast)
        self.menu4_grayscale.addAction(self.actionConvolution_1_grayscale_filter4node)
        self.menu4_grayscale.addAction(self.actionConvolution_2_grayscale_filter4node)
        self.menu4_grayscale.addAction(self.actionConvolution_3_grayscale_filter4node)
        self.menu8_grayscale.addAction(self.actionConvolution_1_grayscale_filter8node)
        self.menu8_grayscale.addAction(self.actionConvolution_2_grayscale_filter8node)
        self.menu8_grayscale.addAction(self.actionConvolution_3_grayscale_filter8node)
        self.menuNode.addAction(self.menu4_grayscale.menuAction())
        self.menuNode.addAction(self.menu8_grayscale.menuAction())
        self.menuFilter_grayscale.addAction(self.menuNode.menuAction())
        self.menuFilter_grayscale.addAction(self.actionAverage_grayscale_filter)
        self.menuFilter_grayscale.addAction(self.actionGaussian_grayscale_filter)
        self.menuFilter_grayscale.addAction(self.actionMedian_grayscale_filter)
        self.menuProbability.addAction(self.action5_grayscale_noise_gaussian)
        self.menuProbability.addAction(self.action10_grayscale_noise_gaussian)
        self.menuProbability.addAction(self.action20_grayscale_noise_gaussian)
        self.menuProbability.addAction(self.action30_grayscale_noise_gaussian)
        self.menuProbability.addAction(self.action40_grayscale_noise_gaussian)
        self.menuGaussian.addAction(self.actionGaussian_grayscale_noise_gaussian)
        self.menuGaussian.addAction(self.menuProbability.menuAction())
        self.menuProbability_2.addAction(self.action5_grayscale_noise_speckle)
        self.menuProbability_2.addAction(self.action10_grayscale_noise_speckle)
        self.menuProbability_2.addAction(self.action20_grayscale_noise_speckle)
        self.menuProbability_2.addAction(self.action30_grayscale_noise_speckle)
        self.menuProbability_2.addAction(self.action40_grayscale_noise_speckle)
        self.menuSpeckle.addAction(self.actionSpeckle_grayscale_noise_speckle)
        self.menuSpeckle.addAction(self.menuProbability_2.menuAction())
        self.menuProbabilty.addAction(self.action5_noise_saltnpepper)
        self.menuProbabilty.addAction(self.action10_noise_saltnpepper)
        self.menuProbabilty.addAction(self.action20_noise_saltnpepper)
        self.menuProbabilty.addAction(self.action30_noise_saltnpepper)
        self.menuProbabilty.addAction(self.action40_noise_saltnpepper)
        self.menuSalt_and_Pepper.addAction(self.actionSalt_and_Pepper_grayscale_noise_saltnpepper)
        self.menuSalt_and_Pepper.addAction(self.menuProbabilty.menuAction())
        self.menuNoise_grayscale.addAction(self.menuGaussian.menuAction())
        self.menuNoise_grayscale.addAction(self.menuSpeckle.menuAction())
        self.menuNoise_grayscale.addAction(self.menuSalt_and_Pepper.menuAction())
        self.menuMethod_grayscale.addAction(self.actionRobert_grayscale_method)
        self.menuMethod_grayscale.addAction(self.actionPrewitt_grayscale_method)
        self.menuMethod_grayscale.addAction(self.actionSobel_grayscale_method)
        self.menuMethod_grayscale.addAction(self.actionLaplacian_grayscale_method)
        self.menuSharpness.addAction(self.actionLPF_grayscale_sharpness)
        self.menuSharpness.addAction(self.actionHPF_grayscale_sharpness)
        self.menuSharpness.addAction(self.actionSharpness_grayscale_sharpness)
        self.menuGrayscale.addAction(self.menuGrayscale_2.menuAction())
        self.menuGrayscale.addAction(self.menuQuantization_grayscale.menuAction())
        self.menuGrayscale.addAction(self.menuBrightness_grayscale.menuAction())
        self.menuGrayscale.addAction(self.menuContrast_grayscale.menuAction())
        self.menuGrayscale.addAction(self.actionInvers_grayscale)
        self.menuGrayscale.addAction(self.actionAutolevel_grayscale)
        self.menuGrayscale.addAction(self.menuFilter_grayscale.menuAction())
        self.menuGrayscale.addAction(self.menuNoise_grayscale.menuAction())
        self.menuGrayscale.addAction(self.menuMethod_grayscale.menuAction())
        self.menuGrayscale.addAction(self.menuSharpness.menuAction())
        self.menuGrayscale.addAction(self.actionEqualization_grayscale)
        self.menuQuantization_full_color.addAction(self.action8_full_color_quantization)
        self.menuQuantization_full_color.addAction(self.action16_full_color_quantization)
        self.menuQuantization_full_color.addAction(self.action32_full_color_quantization)
        self.menuQuantization_full_color.addAction(self.action64_full_color_quantization)
        self.menuBrightness__full_color.addAction(self.actionLow_full_color_brightness)
        self.menuBrightness__full_color.addAction(self.actionMedium_full_color_brightness)
        self.menuBrightness__full_color.addAction(self.actionHigh_full_color_brightness)
        self.menuContrast__full_color.addAction(self.actionLow_full_color_contrast)
        self.menuContrast__full_color.addAction(self.actionMedium_full_color_contrast)
        self.menuContrast__full_color.addAction(self.actionHigh_full_color_contrast)
        self.menu4__full_color_filter.addAction(self.actionConvolution_1_full_color_filter4node)
        self.menu4__full_color_filter.addAction(self.actionConvolution_2_full_color_filter4node)
        self.menu4__full_color_filter.addAction(self.actionConvolution_3_full_color_filter4node)
        self.menu8__full_color_filter.addAction(self.actionConvolution_1_full_color_filter8node)
        self.menu8__full_color_filter.addAction(self.actionConvolution_2_full_color_filter8node)
        self.menu8__full_color_filter.addAction(self.actionConvolution_3_full_color_filter8node)
        self.menuNode__full_color.addAction(self.menu4__full_color_filter.menuAction())
        self.menuNode__full_color.addAction(self.menu8__full_color_filter.menuAction())
        self.menuFilter_full_color.addAction(self.menuNode__full_color.menuAction())
        self.menuFilter_full_color.addAction(self.actionAverage_full_color_filter)
        self.menuFilter_full_color.addAction(self.actionGaussian_full_color_filter)
        self.menuFilter_full_color.addAction(self.actionMedian_full_color_filter)
        self.menuProbability_3.addAction(self.action5_full_color_noise_gaussian)
        self.menuProbability_3.addAction(self.action10_full_color_noise_gaussian)
        self.menuProbability_3.addAction(self.action20_full_color_noise_gaussian)
        self.menuProbability_3.addAction(self.action30_full_color_noise_gaussian)
        self.menuProbability_3.addAction(self.action40_full_color_noise_gaussian)
        self.menuGaussian_2.addAction(self.actionGaussian_full_color_gaussian)
        self.menuGaussian_2.addAction(self.menuProbability_3.menuAction())
        self.menuProbability_4.addAction(self.action5_full_color_noise_speckle)
        self.menuProbability_4.addAction(self.action10_full_color_noise_speckle)
        self.menuProbability_4.addAction(self.action20_full_color_noise_speckle)
        self.menuProbability_4.addAction(self.action30_full_color_noise_speckle)
        self.menuProbability_4.addAction(self.action40_full_color_noise_speckle)
        self.menuSpeckle_2.addAction(self.actionSpeckle_full_color_noise)
        self.menuSpeckle_2.addAction(self.menuProbability_4.menuAction())
        self.menuProbability_5.addAction(self.action5_full_color_salt_pepper)
        self.menuProbability_5.addAction(self.action10_full_color_salt_pepper)
        self.menuProbability_5.addAction(self.action20_full_color_salt_pepper)
        self.menuProbability_5.addAction(self.action30_full_color_salt_pepper)
        self.menuProbability_5.addAction(self.action40_full_color_salt_pepper)
        self.menuSalt_and_Pepper_2.addAction(self.actionSalt_and_Pepper_noise_full_color)
        self.menuSalt_and_Pepper_2.addAction(self.menuProbability_5.menuAction())
        self.menuNoise.addAction(self.menuGaussian_2.menuAction())
        self.menuNoise.addAction(self.menuSpeckle_2.menuAction())
        self.menuNoise.addAction(self.menuSalt_and_Pepper_2.menuAction())
        self.menuMethod.addAction(self.actionRobert_full_color_method)
        self.menuMethod.addAction(self.actionPrewitt_full_color_method)
        self.menuMethod.addAction(self.actionSobel_full_color_method)
        self.menuMethod.addAction(self.actionLaplacian_full_color_method)
        self.menuSharpness_2.addAction(self.actionLPF_full_color_sharpness)
        self.menuSharpness_2.addAction(self.actionHPF_full_color_sharpness)
        self.menuSharpness_2.addAction(self.actionSharpness_full_color_sharpness)
        self.menuFull_Color.addAction(self.menuQuantization_full_color.menuAction())
        self.menuFull_Color.addAction(self.menuBrightness__full_color.menuAction())
        self.menuFull_Color.addAction(self.menuContrast__full_color.menuAction())
        self.menuFull_Color.addAction(self.actionInvers_full_color)
        self.menuFull_Color.addAction(self.actionAutolevel_full_color)
        self.menuFull_Color.addAction(self.menuFilter_full_color.menuAction())
        self.menuFull_Color.addAction(self.menuNoise.menuAction())
        self.menuFull_Color.addAction(self.menuMethod.menuAction())
        self.menuFull_Color.addAction(self.menuSharpness_2.menuAction())
        self.menuFull_Color.addAction(self.actionEqualization_full_color)
        self.menuRotate.addAction(self.action90_rotate)
        self.menuRotate.addAction(self.action180_rotate)
        self.menuRotate.addAction(self.action270_rotate)
        self.menuRotate.addAction(self.action360_rotate)
        self.menuEdit.addAction(self.menuFlip.menuAction())
        self.menuEdit.addAction(self.menuRotate.menuAction())
        self.menuEdit.addAction(self.menuLayer.menuAction())
        self.menuEdit.addAction(self.menuBlack_White.menuAction())
        self.menuEdit.addAction(self.menuDetection.menuAction())
        self.menuEdit.addAction(self.menuGrayscale.menuAction())
        self.menuEdit.addAction(self.menuFull_Color.menuAction())
        self.menuChart.addAction(self.actionHistogram)
        self.menuChart.addAction(self.actionCDF)
        self.menuChart.addAction(self.actionPDF)
        self.menuChart.addAction(self.actionPDF_to_CDF)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuChart.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "IMAGE PROCESSING"))
        self.label.setText(_translate("MainWindow", "D E V E L O P   U S I N G   P Y T H O N 3"))
        self.label_2.setText(_translate("MainWindow", "g u i   b y    P y Q t 5    and   l i b r a r y   by   P i l l o w"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuFlip.setTitle(_translate("MainWindow", "Flip"))
        self.menuLayer.setTitle(_translate("MainWindow", "Layer"))
        self.menuBlack_White.setTitle(_translate("MainWindow", "Black White"))
        self.menuThreshold.setTitle(_translate("MainWindow", "Threshold"))
        self.menuDetection.setTitle(_translate("MainWindow", "Detection"))
        self.menuLine.setTitle(_translate("MainWindow", "Line"))
        self.menuGrayscale.setTitle(_translate("MainWindow", "Grayscale"))
        self.menuGrayscale_2.setTitle(_translate("MainWindow", "Grayscale"))
        self.menuQuantization_grayscale.setTitle(_translate("MainWindow", "Quantization"))
        self.menuBrightness_grayscale.setTitle(_translate("MainWindow", "Brightness"))
        self.menuContrast_grayscale.setTitle(_translate("MainWindow", "Contrast"))
        self.menuFilter_grayscale.setTitle(_translate("MainWindow", "Filter"))
        self.menuNode.setTitle(_translate("MainWindow", "Node"))
        self.menu4_grayscale.setTitle(_translate("MainWindow", "4"))
        self.menu8_grayscale.setTitle(_translate("MainWindow", "8"))
        self.menuNoise_grayscale.setTitle(_translate("MainWindow", "Noise"))
        self.menuGaussian.setTitle(_translate("MainWindow", "Gaussian"))
        self.menuProbability.setTitle(_translate("MainWindow", "Probability"))
        self.menuSpeckle.setTitle(_translate("MainWindow", "Speckle"))
        self.menuProbability_2.setTitle(_translate("MainWindow", "Probability"))
        self.menuSalt_and_Pepper.setTitle(_translate("MainWindow", "Salt and Pepper"))
        self.menuProbabilty.setTitle(_translate("MainWindow", "Probabilty"))
        self.menuMethod_grayscale.setTitle(_translate("MainWindow", "Method"))
        self.menuSharpness.setTitle(_translate("MainWindow", "Sharpness"))
        self.menuFull_Color.setTitle(_translate("MainWindow", "Full Color"))
        self.menuQuantization_full_color.setTitle(_translate("MainWindow", "Quantization"))
        self.menuBrightness__full_color.setTitle(_translate("MainWindow", "Brightness"))
        self.menuContrast__full_color.setTitle(_translate("MainWindow", "Contrast"))
        self.menuFilter_full_color.setTitle(_translate("MainWindow", "Filter"))
        self.menuNode__full_color.setTitle(_translate("MainWindow", "Node"))
        self.menu4__full_color_filter.setTitle(_translate("MainWindow", "4"))
        self.menu8__full_color_filter.setTitle(_translate("MainWindow", "8"))
        self.menuNoise.setTitle(_translate("MainWindow", "Noise"))
        self.menuGaussian_2.setTitle(_translate("MainWindow", "Gaussian"))
        self.menuProbability_3.setTitle(_translate("MainWindow", "Probability"))
        self.menuSpeckle_2.setTitle(_translate("MainWindow", "Speckle"))
        self.menuProbability_4.setTitle(_translate("MainWindow", "Probability"))
        self.menuSalt_and_Pepper_2.setTitle(_translate("MainWindow", "Salt and Pepper"))
        self.menuProbability_5.setTitle(_translate("MainWindow", "Probability"))
        self.menuMethod.setTitle(_translate("MainWindow", "Method"))
        self.menuSharpness_2.setTitle(_translate("MainWindow", "Sharpness"))
        self.menuRotate.setTitle(_translate("MainWindow", "Rotate"))
        self.menuChart.setTitle(_translate("MainWindow", "Chart"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionHorizontal_flip.setText(_translate("MainWindow", "Horizontal"))
        self.actionVertical_flip.setText(_translate("MainWindow", "Vertical"))
        self.actionRGB_layer.setText(_translate("MainWindow", "RGB"))
        self.actionRed_layer.setText(_translate("MainWindow", "Red"))
        self.actionGreen_layer.setText(_translate("MainWindow", "Green"))
        self.actionBlue_layer.setText(_translate("MainWindow", "Blue"))
        self.actionBlack_white_black_white.setText(_translate("MainWindow", "Black White"))
        self.action100_blackWhite.setText(_translate("MainWindow", "100"))
        self.action200_blackWhite.setText(_translate("MainWindow", "200"))
        self.actionEdge_detection.setText(_translate("MainWindow", "Edge"))
        self.actionHorizontal_line_detection.setText(_translate("MainWindow", "Horizontal"))
        self.actionVertical_line_detection.setText(_translate("MainWindow", "Vertical"))
        self.actionNode_detection.setText(_translate("MainWindow", "Node"))
        self.actionRGB_grayscale.setText(_translate("MainWindow", "RGB"))
        self.actionRed_grayscale.setText(_translate("MainWindow", "Red"))
        self.actionGreen_grayscale.setText(_translate("MainWindow", "Green"))
        self.actionBlue_grayscale.setText(_translate("MainWindow", "Blue"))
        self.action8_grayscale_quantization.setText(_translate("MainWindow", "8"))
        self.action16_grayscale_quantization.setText(_translate("MainWindow", "16"))
        self.action32_grayscale_quantization.setText(_translate("MainWindow", "32"))
        self.action64_grayscale_quantization.setText(_translate("MainWindow", "64"))
        self.actionLow_grayscale_brightness.setText(_translate("MainWindow", "Low"))
        self.actionMedium_grayscale_brightness.setText(_translate("MainWindow", "Medium"))
        self.actionHigh_grayscale_brightness.setText(_translate("MainWindow", "High"))
        self.actionLow_grayscale_contrast.setText(_translate("MainWindow", "Low"))
        self.actionMedium_grayscale_contrast.setText(_translate("MainWindow", "Medium"))
        self.actionHigh_grayscale_contrast.setText(_translate("MainWindow", "High"))
        self.actionInvers_grayscale.setText(_translate("MainWindow", "Invers"))
        self.actionAutolevel_grayscale.setText(_translate("MainWindow", "Autolevel"))
        self.actionConvolution_1_grayscale_filter4node.setText(_translate("MainWindow", "Convolution 1"))
        self.actionConvolution_2_grayscale_filter4node.setText(_translate("MainWindow", "Convolution 2"))
        self.actionConvolution_3_grayscale_filter4node.setText(_translate("MainWindow", "Convolution 3"))
        self.actionConvolution_1_grayscale_filter8node.setText(_translate("MainWindow", "Convolution 1"))
        self.actionConvolution_2_grayscale_filter8node.setText(_translate("MainWindow", "Convolution 2"))
        self.actionConvolution_3_grayscale_filter8node.setText(_translate("MainWindow", "Convolution 3"))
        self.actionAverage_grayscale_filter.setText(_translate("MainWindow", "Average"))
        self.actionGaussian_grayscale_filter.setText(_translate("MainWindow", "Gaussian"))
        self.actionMedian_grayscale_filter.setText(_translate("MainWindow", "Median"))
        self.actionGaussian_grayscale_noise_gaussian.setText(_translate("MainWindow", "Gaussian"))
        self.actionRobert_grayscale_method.setText(_translate("MainWindow", "Robert"))
        self.actionPrewitt_grayscale_method.setText(_translate("MainWindow", "Prewitt"))
        self.actionSobel_grayscale_method.setText(_translate("MainWindow", "Sobel"))
        self.actionLaplacian_grayscale_method.setText(_translate("MainWindow", "Laplacian"))
        self.action5_grayscale_noise_gaussian.setText(_translate("MainWindow", "5%"))
        self.action10_grayscale_noise_gaussian.setText(_translate("MainWindow", "10%"))
        self.action20_grayscale_noise_gaussian.setText(_translate("MainWindow", "20%"))
        self.action30_grayscale_noise_gaussian.setText(_translate("MainWindow", "30%"))
        self.action40_grayscale_noise_gaussian.setText(_translate("MainWindow", "40%"))
        self.actionSpeckle_grayscale_noise_speckle.setText(_translate("MainWindow", "Speckle"))
        self.action5_grayscale_noise_speckle.setText(_translate("MainWindow", "5%"))
        self.action10_grayscale_noise_speckle.setText(_translate("MainWindow", "10%"))
        self.action20_grayscale_noise_speckle.setText(_translate("MainWindow", "20%"))
        self.action30_grayscale_noise_speckle.setText(_translate("MainWindow", "30%"))
        self.action40_grayscale_noise_speckle.setText(_translate("MainWindow", "40%"))
        self.actionSalt_and_Pepper_grayscale_noise_saltnpepper.setText(_translate("MainWindow", "Salt and Pepper"))
        self.action5_noise_saltnpepper.setText(_translate("MainWindow", "5%"))
        self.action10_noise_saltnpepper.setText(_translate("MainWindow", "10%"))
        self.action20_noise_saltnpepper.setText(_translate("MainWindow", "20%"))
        self.action30_noise_saltnpepper.setText(_translate("MainWindow", "30%"))
        self.action40_noise_saltnpepper.setText(_translate("MainWindow", "40%"))
        self.action8_full_color_quantization.setText(_translate("MainWindow", "8"))
        self.action16_full_color_quantization.setText(_translate("MainWindow", "16"))
        self.action32_full_color_quantization.setText(_translate("MainWindow", "32"))
        self.action64_full_color_quantization.setText(_translate("MainWindow", "64"))
        self.actionLow_full_color_brightness.setText(_translate("MainWindow", "Low"))
        self.actionMedium_full_color_brightness.setText(_translate("MainWindow", "Medium"))
        self.actionHigh_full_color_brightness.setText(_translate("MainWindow", "High"))
        self.actionLow_full_color_contrast.setText(_translate("MainWindow", "Low"))
        self.actionMedium_full_color_contrast.setText(_translate("MainWindow", "Medium"))
        self.actionHigh_full_color_contrast.setText(_translate("MainWindow", "High"))
        self.actionInvers_full_color.setText(_translate("MainWindow", "Invers"))
        self.actionAutolevel_full_color.setText(_translate("MainWindow", "Autolevel"))
        self.actionAverage_full_color_filter.setText(_translate("MainWindow", "Average"))
        self.actionGaussian_full_color_filter.setText(_translate("MainWindow", "Gaussian"))
        self.actionMedian_full_color_filter.setText(_translate("MainWindow", "Median"))
        self.actionConvolution_1_full_color_filter4node.setText(_translate("MainWindow", "Convolution 1"))
        self.actionConvolution_2_full_color_filter4node.setText(_translate("MainWindow", "Convolution 2"))
        self.actionConvolution_3_full_color_filter4node.setText(_translate("MainWindow", "Convolution 3"))
        self.actionConvolution_1_full_color_filter8node.setText(_translate("MainWindow", "Convolution 1"))
        self.actionConvolution_2_full_color_filter8node.setText(_translate("MainWindow", "Convolution 2"))
        self.actionConvolution_3_full_color_filter8node.setText(_translate("MainWindow", "Convolution 3"))
        self.actionGaussian_full_color_gaussian.setText(_translate("MainWindow", "Gaussian"))
        self.action5_full_color_noise_gaussian.setText(_translate("MainWindow", "5%"))
        self.action10_full_color_noise_gaussian.setText(_translate("MainWindow", "10%"))
        self.action20_full_color_noise_gaussian.setText(_translate("MainWindow", "20%"))
        self.action30_full_color_noise_gaussian.setText(_translate("MainWindow", "30%"))
        self.action40_full_color_noise_gaussian.setText(_translate("MainWindow", "40%"))
        self.actionSpeckle_full_color_noise.setText(_translate("MainWindow", "Speckle"))
        self.action5_full_color_noise_speckle.setText(_translate("MainWindow", "5%"))
        self.action10_full_color_noise_speckle.setText(_translate("MainWindow", "10%"))
        self.action20_full_color_noise_speckle.setText(_translate("MainWindow", "20%"))
        self.action30_full_color_noise_speckle.setText(_translate("MainWindow", "30%"))
        self.action40_full_color_noise_speckle.setText(_translate("MainWindow", "40%"))
        self.actionRobert_full_color_method.setText(_translate("MainWindow", "Robert"))
        self.actionPrewitt_full_color_method.setText(_translate("MainWindow", "Prewitt"))
        self.actionSobel_full_color_method.setText(_translate("MainWindow", "Sobel"))
        self.actionLaplacian_full_color_method.setText(_translate("MainWindow", "Laplacian"))
        self.actionHistogram.setText(_translate("MainWindow", "Histogram"))
        self.actionCDF.setText(_translate("MainWindow", "CDF"))
        self.actionPDF.setText(_translate("MainWindow", "PDF"))
        self.actionAverage_threshold_black_white.setText(_translate("MainWindow", "Average"))
        self.action90_rotate.setText(_translate("MainWindow", "90"))
        self.action180_rotate.setText(_translate("MainWindow", "180"))
        self.action270_rotate.setText(_translate("MainWindow", "270"))
        self.action360_rotate.setText(_translate("MainWindow", "360"))
        self.actionLPF_grayscale_sharpness.setText(_translate("MainWindow", "LPF"))
        self.actionHPF_grayscale_sharpness.setText(_translate("MainWindow", "HPF"))
        self.actionLPF_full_color_sharpness.setText(_translate("MainWindow", "LPF"))
        self.actionHPF_full_color_sharpness.setText(_translate("MainWindow", "HPF"))
        self.actionSharpness_grayscale_sharpness.setText(_translate("MainWindow", "Sharpness"))
        self.actionSharpness_full_color_sharpness.setText(_translate("MainWindow", "Sharpness"))
        self.actionSalt_and_Pepper_noise_full_color.setText(_translate("MainWindow", "Salt and Pepper"))
        self.action5_full_color_salt_pepper.setText(_translate("MainWindow", "5%"))
        self.action10_full_color_salt_pepper.setText(_translate("MainWindow", "10%"))
        self.action20_full_color_salt_pepper.setText(_translate("MainWindow", "20%"))
        self.action30_full_color_salt_pepper.setText(_translate("MainWindow", "30%"))
        self.action40_full_color_salt_pepper.setText(_translate("MainWindow", "40%"))
        self.actionEqualization_grayscale.setText(_translate("MainWindow", "Equalization"))
        self.actionEqualization_full_color.setText(_translate("MainWindow", "Equalization"))
        self.actionPDF_to_CDF.setText(_translate("MainWindow", "PDF to CDF"))

    def open_image(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/Users/oktaviacitra/ImageProcessing/bismillah')[0]
        self.scene = QtWidgets.QGraphicsScene()
        self.image_name = QtGui.QImage(file_name)
        self.scene.addPixmap(QtGui.QPixmap.fromImage(self.image_name))
        self.graphicsView.setScene(self.scene)
        self.graphicsView.fitInView(self.scene.itemsBoundingRect())

    def save_image(self):
        file_name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save file', '/Users/oktaviacitra/ImageProcessing/bismillah')[0]
        QtGui.QPixmap.save(self.image_name, file_name, 'jpg', 100)

    def copy_image(self):
        self.show_image(QtGui.QPixmap.fromImage(self.image_name))
    
    def flip_image(self, x, y):
        self.image_name = self.image_name.transformed(QtGui.QTransform().scale(x, y))
        self.show_image(QtGui.QPixmap.fromImage(self.image_name))
    
    def rotate_image(self, angle):
        self.image_name = self.image_name.transformed(QtGui.QTransform().rotate(angle))
        self.show_image(QtGui.QPixmap.fromImage(self.image_name))

    def show_image(self, pixmap):
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(pixmap)
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(self.scene.itemsBoundingRect())

    def buffer_image(self):
        image = self.image_name
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        pil_im.convert('RGB')
        width, height = pil_im.size
        return image, width, height

    def layer_image(self, choice):
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i ,j)).getRgb()
                result_r, result_g, result_b = self.layer_choice(choice, r, g, b)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))

    def layer_choice(self, choice, r, g, b):
        if choice == 1:
            pass
        elif choice == 2:
            g = 0
            b = 0
        elif choice == 3:
            r = 0
            b = 0
        elif choice == 4:
            r = 0
            g = 0
        return r, g, b
    
    def black_white_image(self, choice):
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i ,j)).getRgb()
                result_r, result_g, result_b = self.black_white_choice(choice, r, g, b)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def black_white_choice(self, choice, r, g, b):
        xg = int((r + g + b)/3)
        xbw = 0
        if choice == 1:
            if xg >= 128:
                xbw = 255
        elif choice == 2:
            if xg >= 100:
                xbw = 255
        elif choice == 3:
            if xg >= 200:
                xbw = 255
        elif choice == 4:
            if xg >= self.get_average_pixel():
                xbw = 255
        r = xbw
        g = xbw
        b = xbw
        return r, g, b

    def grayscale_image(self, choice):
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i ,j)).getRgb()
                result_r, result_g, result_b = self.grayscale_choice(choice, r, g, b)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))

    def grayscale_choice(self, choice, r, g, b):
        if choice == 1:
            xg = (r + g + b)/3
            r = xg
            g = xg
            b = xg
        elif choice == 2:
            g = r
            b = r
        elif choice == 3:
            r = g
            b = g
        elif choice == 4:
            r = b
            g = b
        return r, g, b

    def get_average_pixel(self):
        image, width, height = self.buffer_image()
        sum_r = 0
        sum_g = 0
        sum_b = 0
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i ,j)).getRgb()
                sum_r += r
                sum_g += g
                sum_b += b
        average = int(((sum_r + sum_g + sum_b)/(width * height)) / 3)
        return average

    def quantization_grayscale_image(self, value,):
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i ,j)).getRgb()
                result_r, result_g, result_b = self.quantization_grayscale_value(value, r, g, b)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def quantization_grayscale_value(self, value, r, g, b):
        result = value * int((int((r + g + b) / 3) / value))
        return self.get_result(result)
    
    def quantization_full_color_image(self, value):
        image = self.image_name
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        im = pil_im.convert("P", palette=Image.ADAPTIVE, colors=value)
        data = im.convert("RGBA").tobytes("raw", "RGBA")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
        result = QtGui.QPixmap.fromImage(qim)
        self.show_image(result)
    
    def brightness_image(self, choice, value):
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i ,j)).getRgb()
                result_r, result_g, result_b = self.brightness_value(choice, value, r, g, b)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def brightness_value(self, choice, value, r, g, b):
        r = r + value
        b = b + value
        g = g + value
        if r < 0:
            r = 0
        if r > 255:
            r = 255
        if choice == 1:
            r, g, b = self.get_result(r)
        elif choice == 2:
            if g < 0:
                g = 0
            if g > 255:
                g = 255
            if b < 0:
                b = 0
            if b > 255:
                b = 255
        return r, g, b
    
    def get_result(self, result):
        r = result
        g = result
        b = result
        return r, g, b
    
    def contrast_image(self, choice, value):
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                result_r, result_g, result_b = self.contrast_value(choice, value, r, g, b)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def contrast_value(self,choice, value, r, g, b):
        result_r = self.decision_result_0(int(value * r))
        result_g = 0
        result_b = 0
        if choice == 1:
            result_r, result_g, result_b = self.get_result(result_r)
        elif choice == 2:
            result_g = self.decision_result_0(int(value * g))
            result_b = self.decision_result_0(int(value * b))
        return result_r, result_g, result_b
    
    def robert_method_image(self, choice):
        r = [0, 0, 0]
        g = [0, 0, 0]
        b = [0, 0, 0]
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r[0], g[0], b[0], a = QtGui.QColor(image.pixel(i - 1, j)).getRgb()
                r[1], g[1], b[1], a = QtGui.QColor(image.pixel(i, j)).getRgb()
                r[2], g[2], b[2], a = QtGui.QColor(image.pixel(i, j - 1)).getRgb()
                result_r, result_g, result_b = self.robert_method_list(r, g, b, choice)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))

    def robert_method_list(self, list_r, list_g, list_b, choice):
        r = int((list_r[1] - list_r[0]) + (list_r[1] - list_r[2]))
        result_r = self.decision_result(r)
        if choice == 1:
            result_g = result_r
            result_b = result_r
        elif choice == 2:
            g = int((list_g[1] - list_g[0]) + (list_g[1] - list_g[2]))
            result_g = self.decision_result(g)
            b = int((list_b[1] - list_b[0]) + (list_b[1] - list_b[2]))
            result_b = self.decision_result(b)
        return result_r, result_g, result_b
    
    def decision_result(self, xb):
        result = xb
        if xb < 0:
            result = xb * (-1)
        if xb > 255:
            result = 255
        return result
    
    def decision_result_0(self, xb):
        result = xb
        if xb < 0:
            result = 0
        if xb > 255:
            result = 255
        return result

    def prewitt_method_image(self, choice):
        r = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        g = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        b = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r[0], g[0], b[0], a = QtGui.QColor(image.pixel(i - 1, j - 1)).getRgb()
                r[1], g[1], b[1], a = QtGui.QColor(image.pixel(i - 1, j)).getRgb()
                r[2], g[2], b[2], a = QtGui.QColor(image.pixel(i - 1, j + 1)).getRgb()
                r[3], g[3], b[3], a = QtGui.QColor(image.pixel(i, j - 1)).getRgb()
                r[4], g[4], b[4], a = QtGui.QColor(image.pixel(i, j)).getRgb()
                r[5], g[5], b[5], a = QtGui.QColor(image.pixel(i, j + 1)).getRgb()
                r[6], g[6], b[6], a = QtGui.QColor(image.pixel(i + 1, j - 1)).getRgb()
                r[7], g[7], b[7], a = QtGui.QColor(image.pixel(i + 1, j)).getRgb()
                r[8], g[8], b[8], a = QtGui.QColor(image.pixel(i + 1, j + 1)).getRgb()
                result_r, result_g, result_b = self.prewitt_method_list(r, g, b, choice)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def prewitt_method_list(self, list_r, list_g, list_b, choice):
        r = int((-list_r[0] - list_r[3] - list_r[6] + list_r[2] + list_r[5] + list_r[8]) + (-list_r[0] - list_r[1] - list_r[2] + list_r[6] + list_r[7] + list_r[8]))
        result_r = self.decision_result(r)
        if choice == 1:
            result_g = result_r
            result_b = result_r
        elif choice == 2:
            g = int((-list_g[0] - list_g[3] - list_g[6] + list_g[2] + list_g[5] + list_g[8]) + (-list_g[0] - list_g[1] - list_g[2] + list_g[6] + list_g[7] + list_g[8]))
            result_g = self.decision_result(g)
            b = int((-list_b[0] - list_b[3] - list_b[6] + list_b[2] + list_b[5] + list_b[8]) + (-list_b[0] - list_b[1] - list_b[2] + list_b[6] + list_b[7] + list_b[8]))
            result_b = self.decision_result(b)
        return result_r, result_g, result_b
    
    def sobel_method_image(self, choice):
        r = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        g = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        b = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r[0], g[0], b[0], a = QtGui.QColor(image.pixel(i - 1, j - 1)).getRgb()
                r[1], g[1], b[1], a = QtGui.QColor(image.pixel(i - 1, j)).getRgb()
                r[2], g[2], b[2], a = QtGui.QColor(image.pixel(i - 1, j + 1)).getRgb()
                r[3], g[3], b[3], a = QtGui.QColor(image.pixel(i, j - 1)).getRgb()
                r[4], g[4], b[4], a = QtGui.QColor(image.pixel(i, j)).getRgb()
                r[5], g[5], b[5], a = QtGui.QColor(image.pixel(i, j + 1)).getRgb()
                r[6], g[6], b[6], a = QtGui.QColor(image.pixel(i + 1, j - 1)).getRgb()
                r[7], g[7], b[7], a = QtGui.QColor(image.pixel(i + 1, j)).getRgb()
                r[8], g[8], b[8], a = QtGui.QColor(image.pixel(i + 1, j + 1)).getRgb()
                result_r, result_g, result_b = self.sobel_method_list(r, g, b, choice)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def sobel_method_list(self, list_r, list_g, list_b, choice):
        r = int((-list_r[0] - 2 * list_r[3] - list_r[6] + list_r[2] + 2 * list_r[5] + list_r[8]) + (-list_r[0] - 2 * list_r[1] - list_r[2] + list_r[6] + 2 * list_r[7] + list_r[8]))
        result_r = self.decision_result(r)
        if choice == 1:
            result_g = result_r
            result_b = result_r
        elif choice == 2:
            g = int((-list_g[0] - 2 * list_g[3] - list_g[6] + list_g[2] + 2 * list_g[5] + list_g[8]) + (-list_g[0] - 2 * list_g[1] - list_g[2] + list_g[6] + 2 * list_g[7] + list_g[8]))
            result_g = self.decision_result(g)
            b = int((-list_b[0] - 2 * list_b[3] - list_b[6] + list_b[2] + 2 * list_b[5] + list_b[8]) + (-list_b[0] - 2 * list_b[1] - list_b[2] + list_b[6] + 2 * list_b[7] + list_b[8]))
            result_b = self.decision_result(b)
        return result_r, result_g, result_b
    
    def laplacian_method_image(self, choice):
        r = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        g = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        b = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r[0], g[0], b[0], a = QtGui.QColor(image.pixel(i - 1, j - 1)).getRgb()
                r[1], g[1], b[1], a = QtGui.QColor(image.pixel(i - 1, j)).getRgb()
                r[2], g[2], b[2], a = QtGui.QColor(image.pixel(i - 1, j + 1)).getRgb()
                r[3], g[3], b[3], a = QtGui.QColor(image.pixel(i, j - 1)).getRgb()
                r[4], g[4], b[4], a = QtGui.QColor(image.pixel(i, j)).getRgb()
                r[5], g[5], b[5], a = QtGui.QColor(image.pixel(i, j + 1)).getRgb()
                r[6], g[6], b[6], a = QtGui.QColor(image.pixel(i + 1, j - 1)).getRgb()
                r[7], g[7], b[7], a = QtGui.QColor(image.pixel(i + 1, j)).getRgb()
                r[8], g[8], b[8], a = QtGui.QColor(image.pixel(i + 1, j + 1)).getRgb()
                result_r, result_g, result_b = self.laplacian_method_list(r, g, b, choice)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def laplacian_method_list(self, list_r, list_g, list_b, choice):
        r = int(list_r[0] - 2 * list_r[1] + list_r[2] - 2 * list_r[3] + 4 * list_r[4] - 2 * list_r[5] + list_r[6] - 2 * list_r[7] + list_r[8])
        result_r = self.decision_result(r)
        if choice == 1:
            result_g = result_r
            result_b = result_r
        elif choice == 2:
            g = int(list_g[0] - 2 * list_g[1] + list_g[2] - 2 * list_g[3] + 4 * list_g[4] - 2 * list_g[5] + list_g[6] - 2 * list_g[7] + list_g[8])
            result_g = self.decision_result(g)
            b = int(list_b[0] - 2 * list_b[1] + list_b[2] - 2 * list_b[3] + 4 * list_b[4] - 2 * list_b[5] + list_b[6] - 2 * list_b[7] + list_b[8])
            result_b = self.decision_result(b)
        return result_r, result_g, result_b
    
    def sharpness_grayscale_image(self, choice):
        r = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r[0], g, b, a = QtGui.QColor(image.pixel(i - 1, j - 1)).getRgb()
                r[1], g, b, a = QtGui.QColor(image.pixel(i - 1, j)).getRgb()
                r[2], g, b, a = QtGui.QColor(image.pixel(i - 1, j + 1)).getRgb()
                r[3], g, b, a = QtGui.QColor(image.pixel(i, j - 1)).getRgb()
                r[4], g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                r[5], g, b, a = QtGui.QColor(image.pixel(i, j + 1)).getRgb()
                r[6], g, b, a = QtGui.QColor(image.pixel(i + 1, j - 1)).getRgb()
                r[7], g, b, a = QtGui.QColor(image.pixel(i + 1, j)).getRgb()
                r[8], g, b, a = QtGui.QColor(image.pixel(i + 1, j + 1)).getRgb()
                result_r, result_g, result_b = self.sharpness_list(r, choice)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def sharpness_grayscale_list(self, list_r, choice):
        xt = [0, 0, 0]
        xt[0] = int((list_r[0] + list_r[1] + list_r[2] + list_r[3] + list_r[4] + list_r[5] + list_r[6] + list_r[7] + list_r[8])/9)
        xt[1] = int(-list_r[0] - 2 * list_r[1] - list_r[2] + list_r[6] + 2 * list_r[7] + list_r[8])
        xt[2] = int(-list_r[0] - 2 * list_r[3] - list_r[6] + list_r[2] + 2 * list_r[5] + list_r[8])
        if choice == 1:
            xb = int(xt[0] + xt[1] + xt[2])
        elif choice == 2:
            xb = int((2 * xt[0] + xt[1] + xt[2]) / 2)
        elif choice == 3:
            xb = int((xt[0] + 2 * xt[1] + 2 * xt[2]) / 3)
        return self.get_result(self.decision_result(xb))
    
    def sharpness_full_color_image(self, choice):
        r = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        g = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        b = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r[0], g[0], b[0], a = QtGui.QColor(image.pixel(i - 1, j - 1)).getRgb()
                r[1], g[1], b[1], a = QtGui.QColor(image.pixel(i - 1, j)).getRgb()
                r[2], g[2], b[2], a = QtGui.QColor(image.pixel(i - 1, j + 1)).getRgb()
                r[3], g[3], b[3], a = QtGui.QColor(image.pixel(i, j - 1)).getRgb()
                r[4], g[4], b[4], a = QtGui.QColor(image.pixel(i, j)).getRgb()
                r[5], g[5], b[5], a = QtGui.QColor(image.pixel(i, j + 1)).getRgb()
                r[6], g[6], b[6], a = QtGui.QColor(image.pixel(i + 1, j - 1)).getRgb()
                r[7], g[7], b[7], a = QtGui.QColor(image.pixel(i + 1, j)).getRgb()
                r[8], g[8], b[8], a = QtGui.QColor(image.pixel(i + 1, j + 1)).getRgb()
                result_r, result_g, result_b = self.sharpness_full_color_list(r, g,b, choice)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def sharpness_full_color_list(self, list_r, list_g, list_b, choice):
        r = [0, 0, 0]
        g = [0, 0, 0]
        b = [0, 0, 0]
        r[0] = int(-list_r[0] - list_r[3] - list_r[6] + list_r[2] + list_r[5] + list_r[8])
        g[0] = int(-list_g[0] - list_g[3] - list_g[6] + list_g[2] + list_g[5] + list_g[8])
        b[0] = int(-list_b[0] - list_b[3] - list_b[6] + list_b[2] + list_b[5] + list_b[8])
        r[1] = int(-list_r[0] - list_r[1] - list_r[2] + list_r[6] + list_r[7] + list_r[8])
        g[1] = int(-list_g[0] - list_g[1] - list_g[2] + list_g[6] + list_g[7] + list_g[8])
        b[1] = int(-list_b[0] - list_b[1] - list_b[2] + list_b[6] + list_b[7] + list_b[8])
        r[2] = int((list_r[0] + list_r[1] + list_r[2] + list_r[3] + list_r[4] + list_r[5] + list_r[6] + list_r[7] + list_r[8]) / 9)
        g[2] = int((list_g[0] + list_g[1] + list_g[2] + list_g[3] + list_g[4] + list_g[5] + list_g[6] + list_g[7] + list_g[8]) / 9)
        b[2] = int((list_b[0] + list_b[1] + list_b[2] + list_b[3] + list_b[4] + list_b[5] + list_b[6] + list_b[7] + list_b[8]) / 9)
        if choice == 1:
            sum_r = r[0] + r[1] + r[2]
            sum_g = g[0] + g[1] + g[2]
            sum_b = b[0] + b[1] + b[2]
            result_r = self.decision_result(sum_r)
            result_g = self.decision_result(sum_g)
            result_b = self.decision_result(sum_b)
        elif choice == 2:
            sum_r = (2 * r[0] + r[1] + r[2])/2
            sum_g = (2 * g[0] + g[1] + g[2])/2
            sum_b = (2 * b[0] + b[1] + b[2])/2
            result_r = self.decision_result(sum_r)
            result_g = self.decision_result(sum_g)
            result_b = self.decision_result(sum_b)
        elif choice == 3:
            sum_r = (r[0] + 2 * r[2] + 2 * r[1])/2
            sum_g = (r[0] + 2 * r[2] + 2 * r[1])/2
            sum_b = (r[0] + 2 * r[2] + 2 * r[1])/2
            result_r = self.decision_result(sum_r)
            result_g = self.decision_result(sum_g)
            result_b = self.decision_result(sum_b)
        return result_r, result_g, result_b
    
    def invers_image(self, choice):
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                result_r, result_g, result_b = self.invers_choice(choice, r, g, b)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def invers_choice(self, choice, r, g, b):
        r = 255 - r
        if choice == 1:
            r, g, b = self.get_result(r)
        elif choice == 2:
            g = 255 - g
            b = 255 - b
        return r, g, b
    
    def get_max_min_rgb(self):
        image, width, height = self.buffer_image()
        list_r = []
        list_g = []
        list_b = []
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                list_r.append(r)
                list_b.append(b)
                list_g.append(g)
        return max(list_r), max(list_g), max(list_b), min(list_r), min(list_g), min(list_b)
    
    def auto_level_image(self, choice):
        image, width, height = self.buffer_image()
        max_r, max_g, max_b, min_r, min_g, min_b = self.get_max_min_rgb()
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                result_r, result_g, result_b = self.auto_level_choice(choice, r, g, b, max_r, max_g, max_b, min_r, min_g, min_b )
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def auto_level_choice(self, choice, r, g, b, max_r, max_g, max_b, min_r, min_g, min_b):
        r = int(255 * (r - min_r) / (max_r - min_r))
        if choice == 1:
            r, g, b = self.get_result(r)
        elif choice == 2:
            b = int(255 * (b - min_b) / (max_b - min_b))
            g = int(255 * (g - min_g) / (max_g - min_g))
        return r, g, b
    
    def detection_image(self, choice):
        image, width, height = self.buffer_image()
        k = []
        if choice == 1:
            k = [-1, -1, -1, -1, 8, -1, -1, -1, -1]
        elif choice == 2:
            k = [-1, -1, -1, 2, 2, 2, -1, -1, -1]
        elif choice == 3:
            k = [-1, 2, -1, -1, 2, -1, -1, 2, -1]
        for x in range(width):
            for y in range(height):
                sum_wr = 0
                sum_wg = 0
                sum_wb = 0
                aa = 0
                if (x > 0 and y> 0) and (x < width and y < height):
                    count = 0
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            r, g, b, a = QtGui.QColor(image.pixel(x + i , y + j)).getRgb()
                            wr = k[count] * r
                            wg = k[count] * g
                            wb = k[count] * b
                            sum_wr += wr
                            sum_wg += wg
                            sum_wb + wb
                            aa = a
                            count += 1
                rr = sum_wr
                gg = sum_wg
                bb = sum_wb
                if rr > 255:
                    rr = 255
                if rr < 0 :
                    rr = 0
                if gg > 255:
                    gg = 255
                if gg < 0:
                    gg = 0
                if bb > 255:
                    bb = 255
                if bb < 0:
                    bb = 0
                image.setPixel(x, y, QtGui.QColor(rr, gg, bb, aa).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def detection_edge(self):
        r = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        g = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        b = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r[0], g[0], b[0], a = QtGui.QColor(image.pixel(i - 1, j - 1)).getRgb()
                r[1], g[1], b[1], a = QtGui.QColor(image.pixel(i - 1, j)).getRgb()
                r[2], g[2], b[2], a = QtGui.QColor(image.pixel(i - 1, j + 1)).getRgb()
                r[3], g[3], b[3], a = QtGui.QColor(image.pixel(i, j - 1)).getRgb()
                r[4], g[4], b[4], a = QtGui.QColor(image.pixel(i, j)).getRgb()
                r[5], g[5], b[5], a = QtGui.QColor(image.pixel(i, j + 1)).getRgb()
                r[6], g[6], b[6], a = QtGui.QColor(image.pixel(i + 1, j - 1)).getRgb()
                r[7], g[7], b[7], a = QtGui.QColor(image.pixel(i + 1, j)).getRgb()
                r[8], g[8], b[8], a = QtGui.QColor(image.pixel(i + 1, j + 1)).getRgb()
                result_r, result_g, result_b = self.detection_edge_list(r, g,b)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def detection_edge_list(self, list_r, list_g, list_b):
        r = int((-list_r[0] - list_r[3] - list_r[6] + list_r[2] + list_r[5] + list_r[8]) + (-list_r[0] - list_r[1] - list_r[2] + list_r[6] + list_r[7] + list_r[8]))
        result_r = self.decision_result(r)
        g = int((-list_g[0] - list_g[3] - list_g[6] + list_g[2] + list_g[5] + list_g[8]) + (-list_g[0] - list_g[1] - list_g[2] + list_g[6] + list_g[7] + list_g[8]))
        result_g = self.decision_result(g)
        b = int((-list_b[0] - list_b[3] - list_b[6] + list_b[2] + list_b[5] + list_b[8]) + (-list_b[0] - list_b[1] - list_b[2] + list_b[6] + list_b[7] + list_b[8]))
        result_b = self.decision_result(b)
        return r, g, b
    
    def average_filter_image(self, choice):
        r = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        g = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        b = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r[0], g[0], b[0], a = QtGui.QColor(image.pixel(i - 1, j - 1)).getRgb()
                r[1], g[1], b[1], a = QtGui.QColor(image.pixel(i - 1, j)).getRgb()
                r[2], g[2], b[2], a = QtGui.QColor(image.pixel(i - 1, j + 1)).getRgb()
                r[3], g[3], b[3], a = QtGui.QColor(image.pixel(i, j - 1)).getRgb()
                r[4], g[4], b[4], a = QtGui.QColor(image.pixel(i, j)).getRgb()
                r[5], g[5], b[5], a = QtGui.QColor(image.pixel(i, j + 1)).getRgb()
                r[6], g[6], b[6], a = QtGui.QColor(image.pixel(i + 1, j - 1)).getRgb()
                r[7], g[7], b[7], a = QtGui.QColor(image.pixel(i + 1, j)).getRgb()
                r[8], g[8], b[8], a = QtGui.QColor(image.pixel(i + 1, j + 1)).getRgb()
                result_r, result_g, result_b = self.average_filter_list(r, g, b, choice)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def average_filter_list(self, list_r, list_g, list_b, choice):
        r = int((list_r[0] + list_r[1] + list_r[2] + list_r[3] + list_r[4] + list_r[5] + list_r[6] + list_r[8]) / 9)
        result_r = self.decision_result_0(r)
        if choice == 1:
            result_g = result_r
            result_b = result_r
        elif choice == 2:
            g = int((list_g[0] + list_g[1] + list_g[2] + list_g[3] + list_g[4] + list_g[5] + list_g[6] + list_g[8]) / 9)
            result_g = self.decision_result_0(g)
            b = int((list_b[0] + list_b[1] + list_b[2] + list_b[3] + list_b[4] + list_b[5] + list_b[6] + list_b[8]) / 9)
            result_b = self.decision_result_0(b)
        return result_r, result_g, result_b
    
    def median_filter_image(self, choice):
        r = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        g = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        b = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r[0], g[0], b[0], a = QtGui.QColor(image.pixel(i - 1, j - 1)).getRgb()
                r[1], g[1], b[1], a = QtGui.QColor(image.pixel(i - 1, j)).getRgb()
                r[2], g[2], b[2], a = QtGui.QColor(image.pixel(i - 1, j + 1)).getRgb()
                r[3], g[3], b[3], a = QtGui.QColor(image.pixel(i, j - 1)).getRgb()
                r[4], g[4], b[4], a = QtGui.QColor(image.pixel(i, j)).getRgb()
                r[5], g[5], b[5], a = QtGui.QColor(image.pixel(i, j + 1)).getRgb()
                r[6], g[6], b[6], a = QtGui.QColor(image.pixel(i + 1, j - 1)).getRgb()
                r[7], g[7], b[7], a = QtGui.QColor(image.pixel(i + 1, j)).getRgb()
                r[8], g[8], b[8], a = QtGui.QColor(image.pixel(i + 1, j + 1)).getRgb()
                result_r, result_g, result_b = self.median_filter_list(r, g, b, choice)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def median_filter_list(self, list_r, list_g, list_b, choice):
        result_r = self.get_median(list_r)
        if choice == 1:
            result_g = result_r
            result_b = result_r
        elif choice == 2:
            result_g = self.get_median(list_g)
            result_b = self.get_median(list_b)
        return result_r, result_g, result_b
        
    def get_median(self, list_rgb):
        temp = 0
        for i in range(len(list_rgb)):
            for j in range(len(list_rgb)):
                if list_rgb[j] == list_rgb[j+1]:
                    temp = list_rgb[j]
                    list_rgb[j] = list_rgb[j + 1]
                    list_rgb[j + 1] = temp
        return list_rgb[(int(len(list_rgb)/2))]
    
    def gaussian_filter_image(self, choice):
        r = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        g = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        b = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r[0], g[0], b[0], a = QtGui.QColor(image.pixel(i - 1, j - 1)).getRgb()
                r[1], g[1], b[1], a = QtGui.QColor(image.pixel(i - 1, j)).getRgb()
                r[2], g[2], b[2], a = QtGui.QColor(image.pixel(i - 1, j + 1)).getRgb()
                r[3], g[3], b[3], a = QtGui.QColor(image.pixel(i, j - 1)).getRgb()
                r[4], g[4], b[4], a = QtGui.QColor(image.pixel(i, j)).getRgb()
                r[5], g[5], b[5], a = QtGui.QColor(image.pixel(i, j + 1)).getRgb()
                r[6], g[6], b[6], a = QtGui.QColor(image.pixel(i + 1, j - 1)).getRgb()
                r[7], g[7], b[7], a = QtGui.QColor(image.pixel(i + 1, j)).getRgb()
                r[8], g[8], b[8], a = QtGui.QColor(image.pixel(i + 1, j + 1)).getRgb()
                result_r, result_g, result_b = self.get_gaussian_list(r, g, b, choice)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def get_gaussian_list(self, list_r, list_g, list_b, choice):
        r = int((list_r[0] + list_r[1] + list_r[2] + list_r[3] + 4 * list_r[4] + list_r[5] + list_r[6] + list_r[7] + list_r[8]) / 13)
        result_r = self.decision_result_0(r)
        if choice == 1:
            result_g = result_r
            result_b = result_r
        elif choice == 2:
            g = int((list_g[0] + list_g[1] + list_g[2] + list_g[3] + 4 * list_g[4] + list_g[5] + list_g[6] + list_g[7] + list_g[8]) / 13)
            result_g = self.decision_result_0(g)
            b = int((list_b[0] + list_b[1] + list_b[2] + list_b[3] + 4 * list_b[4] + list_b[5] + list_b[6] + list_b[7] + list_b[8]) / 13)
            result_b = self.decision_result_0(b)
        return result_r, result_g, result_b
    
    def gaussian_noise_image(self, choice, value):
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                result_r, result_g, result_b = self.gaussian_noise_choice(r, g, b, choice, value)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def gaussian_noise_choice(self, r, g, b, choice, value):
        random_number = random.randint(0, 100)
        result_r = 0
        result_g = 0
        result_b = 0
        if random_number < value:
            value_random = random.randint(0, 256)
            result_r = self.decision_result(r + value_random)
            if choice == 1:
                result_g = result_r
                result_b = result_r
            elif choice == 2:
                result_g = self.decision_result(g + value_random)
                result_b = self.decision_result(b + value_random)
        return result_r, result_g, result_b
    
    def speckle_noise_image(self, choice, value):
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                result_r, result_g, result_b = self.speckle_noise_choice(r, g, b, choice, value)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def speckle_noise_choice(self, r, g, b, choice, value):
        random_number = random.randint(0, 100)
        result_r = r
        result_g = g
        result_b = b
        if random_number < value:
            result_r = 0
            result_g = 0
            result_b = 0
        if choice == 1:
            result_r, result_g, result_b = self.get_result(result_r)
        elif choice == 2:
            result_r, result_g, result_b = result_r, result_g, result_b
        return result_r, result_g, result_b
    
    def salt_pepper_noise_image(self, choice, value):
        image, width, height = self.buffer_image()
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                result_r, result_g, result_b = self.salt_pepper_noise_choice(r, g, b, choice, value)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def salt_pepper_noise_choice(self, r, g, b, choice, value):
        random_number = random.randint(0, 100)
        result_r = r
        result_g = g
        result_b = b
        if random_number < value:
            result_r = 255
            result_g = 255
            result_b = 255
        if choice == 1:
            result_r, result_g, result_b = self.get_result(result_r)
        elif choice == 2:
            result_r, result_g, result_b = result_r, result_g, result_b
        return result_r, result_g, result_b
    
    def filter_4_node_image(self, choice, value):
        image, width, height = self.buffer_image()
        r = [0, 0, 0, 0, 0]
        g = [0, 0, 0, 0, 0]
        b = [0, 0, 0, 0, 0]
        matrix = []
        if value == 1:
            matrix = [0.2, 0.2, 0.2, 0.2, 0.2]
        elif value == 2:
            matrix = [-0.5, -0.5, 0, 0.5, 0.5]
        elif value == 3:
            matrix = [-0.5, -0.5, 1, 0.5, 0.5]
        for i in range(width):
            for j in range(height):
                r[0], g[0], b[0], a = QtGui.QColor(image.pixel(i, j)).getRgb()
                r[2], g[2], b[2], a = QtGui.QColor(image.pixel(i + 1, j)).getRgb()
                r[4], g[4], b[4], a = QtGui.QColor(image.pixel(i, j + 1)).getRgb()
                r[3], g[3], b[3], a = QtGui.QColor(image.pixel(i, j - 1)).getRgb()
                r[1], g[1], b[1], a = QtGui.QColor(image.pixel(i - 1, j)).getRgb()
                result_r, result_g, result_b = self.filter_node_list(choice, matrix, r, g, b)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def filter_node_list(self, choice, matrix, list_r, list_g, list_b):
        sum_r = 0.0
        sum_g = 0.0
        sum_b = 0.0
        for k in range(len(matrix)):
            sum_r += matrix[k] * list_r[k]
            sum_g += matrix[k] * list_g[k]
            sum_b += matrix[k] * list_b[k]
        result_r = self.decision_result(int(sum_r))
        if choice == 1:
            result_g = result_r
            result_b = result_r
        elif choice == 2:
            result_g = self.decision_result(int(sum_g))
            result_b = self.decision_result(int(sum_b))
        return result_r, result_g, result_b
    
    def filter_8_node_image(self, choice, value):
        image, width, height = self.buffer_image()
        r = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        g = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        b = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        matrix = []
        if value == 1:
            matrix = [0.1, 0.1, 0.1, 0.1, 0.2, 0.1, 0.1, 0.1, 0.1]
        elif value == 2:
            matrix = [-1, -0.5, 0, -0.5, 0, 0.5, 0, 0.5, 1]
        elif value == 3:
            matrix = [-1, -0.5, 0, -0.5, 1, 0.5, 0, 0.5, 1]
        for i in range(width):
            for j in range(height):
                r[0], g[0], b[0], a = QtGui.QColor(image.pixel(i - 1, j - 1)).getRgb()
                r[1], g[1], b[1], a = QtGui.QColor(image.pixel(i - 1, j)).getRgb()
                r[2], g[2], b[2], a = QtGui.QColor(image.pixel(i - 1, j + 1)).getRgb()
                r[3], g[3], b[3], a = QtGui.QColor(image.pixel(i, j - 1)).getRgb()
                r[4], g[4], b[4], a = QtGui.QColor(image.pixel(i, j)).getRgb()
                r[5], g[5], b[5], a = QtGui.QColor(image.pixel(i, j + 1)).getRgb()
                r[6], g[6], b[6], a = QtGui.QColor(image.pixel(i + 1, j - 1)).getRgb()
                r[7], g[7], b[7], a = QtGui.QColor(image.pixel(i + 1, j)).getRgb()
                r[8], g[8], b[8], a = QtGui.QColor(image.pixel(i + 1, j + 1)).getRgb()
                result_r, result_g, result_b = self.filter_node_list(choice, matrix, r, g, b)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def set_histogram(self):
        image, width, height = self.buffer_image()
        data = []
        for i in range(256):
            data.append(0)
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                data[r] += 1
        dataChart = QtChart.QBarSet("Count")
        dataChart.setColor(QtCore.Qt.black)
        for i in range(256):
            dataChart << data[i]
        self.get_histogram(dataChart)
    
    def get_histogram(self, dataChart):
        series = QtChart.QBarSeries()
        series.append(dataChart)
        chart = QtChart.QChart()
        chart.addSeries(series)
        chart.setTitle("Histogram")
        chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)
        chart.setTheme(QtChart.QChart.ChartThemeBlueCerulean)
        axis = QtChart.QValueAxis()
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
        chart.axisY(series)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(QtCore.Qt.AlignBottom)
        self.chartview.setChart(chart)
        self.chartview.setRenderHint(QtGui.QPainter.Antialiasing)
    
    def set_cdf(self):
        image, width, height = self.buffer_image()
        data = []
        result = []
        for i in range(256):
            data.append(0)
            result.append(0)
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                data[r] += 1
        result[0] = data[0]
        for i in range(256):
            result[i] = result[i - 1] + data[i]
        dataChart = QtChart.QBarSet("Count")
        dataChart.setColor(QtCore.Qt.black)
        for i in range(256):
            dataChart << result[i]
        self.get_histogram(dataChart)
    
    def set_pdf(self):
        image, width, height = self.buffer_image()
        data = []
        total = 0
        for i in range(256):
            data.append(0)
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                data[r] += 1
                total = total + r
        average = total / (width * height)
        dataChart = QtChart.QBarSet("Count")
        dataChart.setColor(QtCore.Qt.black)
        for i in range(256):
            dataChart << (data[i] / average)
        self.get_histogram(dataChart)
    
    def convert_pdf_to_cdf(self):
        image, width, height = self.buffer_image()
        data = []
        result = []
        total = 0
        for i in range(256):
            data.append(0)
            result.append(0)
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                data[r] += 1
                total = total + r
        average = total / (width * height)
        result[0] = data[0]
        for i in range(256):
            result[i] = result[i - 1] + ( data[i] / average)
        dataChart = QtChart.QBarSet("Count")
        dataChart.setColor(QtCore.Qt.black)
        for i in range(256):
            dataChart << result[i]
        self.get_histogram(dataChart)

    def equalization_image(self, choice):
        image, width, height = self.buffer_image()
        data = []
        result = []
        for i in range(256):
            data.append(0)
            result.append(0)
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                data[r] += 1
        result[0] = data[0]
        for i in range(256):
            result[i] = result[i - 1] + data[i]
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                result_r, result_g, result_b = self.equalization_choice(choice, r, g, b, width, height, data)
                image.setPixel(i, j, QtGui.QColor(result_r, result_g, result_b, a).rgb())
        self.show_image(QtGui.QPixmap.fromImage(image))
    
    def equalization_choice(self, choice, r, g, b, width, height, data):
        result_r = int(255 * data[r] / width / height)
        result_g = 0
        result_b = 0
        if choice == 1:
            result_g = result_r
            result_b = result_r
        elif choice == 2:
            result_g = int(255 * data[g] / width / height)
            result_b = int(255 * data[b] / width / height)
        return result_r, result_g, result_b

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
