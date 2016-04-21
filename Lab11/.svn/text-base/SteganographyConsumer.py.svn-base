#! /usr/bin/env python3

import sys
from scipy.misc import imread
from Steganography import *

from PySide.QtGui import *
from SteganographyGUI import *
from PySide.QtCore import QRectF
from PySide.QtCore import Qt, QSize
from functools import partial
from os.path import splitext
from PIL import ImageQt


class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        # Get the views that are required to have the drag-and-drop enabled.
        views = [self.viewPayload1, self.viewCarrier1, self.viewCarrier2]
        accept = lambda e: e.accept()

        for view in views:
            # We need to accept the drag event to be able to accept the drop.
            view.dragEnterEvent = accept
            view.dragMoveEvent = accept
            view.dragLeaveEvent = accept

            # Assign an event handler (a method,) to be invoked when a drop is performed.
            view.dropEvent = partial(self.processDrop, view)
        # Member Variables
        self.compressionLevel = None
        self.p1 = None
        self.p1scene = QGraphicsScene(self.grpPayload1)
        self.p1size = None
        self.c1 = None
        self.c1scene = QGraphicsScene()
        self.c1size = None

        self.c2fpath = None
        self.p2 = None
        self.p2scene = QGraphicsScene()
        self.c2 = None
        self.c2scene = QGraphicsScene()
        self.c2size = None
        # onEvent Connections
        self.chkApplyCompression.setEnabled(False)
        self.chkApplyCompression.stateChanged.connect(self.onCompress)
        self.slideCompression.valueChanged.connect(self.onSlide)
        self.chkOverride.stateChanged.connect(self.onOverride)
        self.btnSave.clicked.connect(self.onSave)

        self.btnExtract.clicked.connect(self.onExtract)
        self.btnClean.clicked.connect(self.onClean)
    def processDrop(self, view, e):
        """
        Process a drop event when it occurs on the views.
        """
        mime = e.mimeData()

        # Guard against types of drops that are not pertinent to this app.
        if not mime.hasUrls():
            return

        # Obtain the file path using the OS format.
        filePath = mime.urls()[0].toLocalFile()
        _, ext = splitext(filePath)

        if not ext == ".png":
            return

        if view == self.viewPayload1: self.setp1(filePath)
        if view == self.viewCarrier1: self.setc1(filePath)
        if view == self.viewCarrier2: self.setc2(filePath)

    def onSlide(self):
        self.compressionLevel = self.slideCompression.value()
        self.txtCompression.setText(str(self.compressionLevel))
        self.p1sizeCalc()
    def onCompress(self):
        if self.chkApplyCompression.isChecked():
            self.slideCompression.setEnabled(True)
            self.compressionLevel = self.slideCompression.value()
            self.txtCompression.setEnabled(True)
            self.lblLevel.setEnabled(True)
            self.p1sizeCalc()

        else:
            self.slideCompression.setEnabled(False)
            self.txtCompression.setEnabled(False)
            self.lblLevel.setEnabled(False)
            self.compressionLevel = -1
            self.p1sizeCalc()
    def onOverride(self):
        self.checkEmbed()
    def onSave(self):
        if not self.checkEmbed():return
        override = self.chkOverride.isChecked()
        filePath, _ = QFileDialog.getSaveFileName(self, caption='Provide target file Location ...', filter="PNG files (*.png)")

        if not filePath:
            return
        image = Image.fromarray(self.c1.embedPayload(payload=self.p1, override=override))
        image.save(filePath, format="PNG")
    def checkEmbed(self):
        valid = True
        if not self.c1 or not self.p1: valid = False
        elif self.c1size < self.p1size: valid = False
        elif self.chkOverride.isEnabled() and self.chkOverride.isChecked() == False: valid = False
        self.btnSave.setEnabled(valid)
        return valid
    def p1sizeCalc(self):
        """
        Updates p1 with payload compressionLevel, calculates and sets payloadSize(p1size), call checkEmbed
        """
        self.p1 = Payload(img=self.p1.img, compressionLevel=self.compressionLevel)
        self.p1size = len(self.p1.xml)
        self.txtPayloadSize.setText(str(self.p1size))
        self.checkEmbed()
    def setp1(self, path):
        self.chkApplyCompression.setEnabled(True)
        self.chkApplyCompression.setChecked(False)
        self.txtCompression.setEnabled(False)
        self.slideCompression.setEnabled(False)
        self.slideCompression.setValue(0)
        self.lblLevel.setEnabled(False)
        self.compressionLevel = -1


        self.p1scene.clear()
        self.p1 = Payload(img=imread(path))
        self.p1sizeCalc()
        w, h = int(self.viewPayload1.geometry().width()), int(self.viewPayload1.geometry().height())
        pixMap = QPixmap(path)
        self.p1scene.addPixmap(pixMap.scaled(QSize(w,h), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.viewPayload1.setScene(self.p1scene)
        self.viewPayload1.fitInView(QRectF(0, 0, w, h), Qt.KeepAspectRatio)
    def setc1(self, path):
        self.c1scene.clear()
        self.c1 = Carrier(img=imread(path))
        size = len(self.c1.pixelData)
        if self.c1.img.ndim == 3:
            size *= 3
        size /= 8
        self.c1size = int(size)
        self.txtCarrierSize.setText(str(self.c1size))
        if self.c1.payloadExists():
            self.lblPayloadFound.setText(">>>>Payload Found<<<<")
            self.chkOverride.setEnabled(True)
        else:
            self.lblPayloadFound.setText("")
            self.chkOverride.setChecked(False)
            self.chkOverride.setEnabled(False)
        w, h = int(self.viewCarrier1.geometry().width()), int(self.viewCarrier1.geometry().height())
        pixMap = QPixmap(path)
        self.c1scene.addPixmap(pixMap.scaled(QSize(w,h), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.viewCarrier1.setScene(self.c1scene)
        self.viewCarrier1.fitInView(QRectF(0, 0, w, h), Qt.KeepAspectRatio)
        self.checkEmbed()

    def onExtract(self):
        payload = self.c2.extractPayload()
        image = ImageQt.ImageQt(Image.fromarray(payload.img[:-1]))
        pixMap = QPixmap.fromImage(image)
        w, h = int(self.viewPayload2.geometry().width()), int(self.viewPayload2.geometry().height())
        self.p2scene.clear()
        self.p2scene.addPixmap(pixMap.scaled(QSize(w,h), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.viewPayload2.setScene(self.p2scene)
        self.viewPayload2.fitInView(QRectF(0, 0, w, h), Qt.KeepAspectRatio)
        self.btnExtract.setEnabled(False)
    def onClean(self):
        image = (Image.fromarray(self.c2.clean()))
        image.save(self.c2fpath)
        self.setc2(self.c2fpath)
    def setc2(self, path):
        self.c2fpath = path
        self.c2scene.clear()
        self.c2 = Carrier(img=imread(path))
        w, h = int(self.viewCarrier2.geometry().width()), int(self.viewCarrier2.geometry().height())
        pixMap = QPixmap(path)
        self.c2scene.addPixmap(pixMap.scaled(QSize(w,h), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.viewCarrier2.setScene(self.c2scene)
        self.viewCarrier2.fitInView(QRectF(0, 0, w, h), Qt.KeepAspectRatio)
        if self.c2.payloadExists():
            self.lblCarrierEmpty.setText("")
            self.btnExtract.setEnabled(True)
            self.btnClean.setEnabled(True)
        else:
            self.lblCarrierEmpty.setText(">>>>Carrier Empty<<<<")
            self.btnExtract.setEnabled(False)
            self.btnClean.setEnabled(False)
        self.p2scene.clear()
        self.viewPayload2.setScene(self.p2scene)



if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
