# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task_load_dialog_base.ui'
#
# Created: Mon Mar 16 15:07:55 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_task_loadDialogBase(object):
    def setupUi(self, task_loadDialogBase):
        task_loadDialogBase.setObjectName(_fromUtf8("task_loadDialogBase"))
        task_loadDialogBase.resize(400, 300)
        self.pushButton = QtGui.QPushButton(task_loadDialogBase)
        self.pushButton.setGeometry(QtCore.QRect(150, 70, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.status_label = QtGui.QLabel(task_loadDialogBase)
        self.status_label.setGeometry(QtCore.QRect(110, 140, 211, 51))
        self.status_label.setText(_fromUtf8(""))
        self.status_label.setObjectName(_fromUtf8("status_label"))
        self.ok_button = QtGui.QPushButton(task_loadDialogBase)
        self.ok_button.setGeometry(QtCore.QRect(250, 240, 98, 27))
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.cancel_button = QtGui.QPushButton(task_loadDialogBase)
        self.cancel_button.setGeometry(QtCore.QRect(110, 240, 98, 27))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))

        self.retranslateUi(task_loadDialogBase)
        QtCore.QMetaObject.connectSlotsByName(task_loadDialogBase)

    def retranslateUi(self, task_loadDialogBase):
        task_loadDialogBase.setWindowTitle(_translate("task_loadDialogBase", "Load task", None))
        self.pushButton.setText(_translate("task_loadDialogBase", "PushButton", None))
        self.ok_button.setText(_translate("task_loadDialogBase", "ok", None))
        self.cancel_button.setText(_translate("task_loadDialogBase", "cancel", None))

