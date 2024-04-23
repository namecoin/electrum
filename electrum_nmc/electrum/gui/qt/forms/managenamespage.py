# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'electrum_nmc/electrum/gui/qt/forms/managenamespage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ManageNamesPage(object):
    def setupUi(self, ManageNamesPage):
        ManageNamesPage.setObjectName("ManageNamesPage")
        ManageNamesPage.resize(776, 364)
        self.verticalLayout = QtWidgets.QVBoxLayout(ManageNamesPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(ManageNamesPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.tableView = QtWidgets.QTableView(ManageNamesPage)
        self.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView.setTabKeyNavigation(False)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.countLabel = QtWidgets.QLabel(ManageNamesPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.countLabel.sizePolicy().hasHeightForWidth())
        self.countLabel.setSizePolicy(sizePolicy)
        self.countLabel.setText("")
        self.countLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.countLabel.setObjectName("countLabel")
        self.horizontalLayout_3.addWidget(self.countLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.configureNameButton = QtWidgets.QPushButton(ManageNamesPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configureNameButton.sizePolicy().hasHeightForWidth())
        self.configureNameButton.setSizePolicy(sizePolicy)
        self.configureNameButton.setMinimumSize(QtCore.QSize(150, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/edit"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.configureNameButton.setIcon(icon)
        self.configureNameButton.setDefault(False)
        self.configureNameButton.setObjectName("configureNameButton")
        self.horizontalLayout_3.addWidget(self.configureNameButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.renewNameButton = QtWidgets.QPushButton(ManageNamesPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.renewNameButton.sizePolicy().hasHeightForWidth())
        self.renewNameButton.setSizePolicy(sizePolicy)
        self.renewNameButton.setMinimumSize(QtCore.QSize(150, 0))
        self.renewNameButton.setDefault(False)
        self.renewNameButton.setObjectName("renewNameButton")
        self.horizontalLayout_3.addWidget(self.renewNameButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(ManageNamesPage)
        QtCore.QMetaObject.connectSlotsByName(ManageNamesPage)

    def retranslateUi(self, ManageNamesPage):
        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("ManageNamesPage", "Your registered names (pending and unconfirmed names have blank expiration):"))
        self.tableView.setToolTip(_translate("ManageNamesPage", "Double-click name to configure"))
        self.configureNameButton.setToolTip(_translate("ManageNamesPage", "Configure name and submit update operation"))
        self.configureNameButton.setText(_translate("ManageNamesPage", "&Configure Name…"))
        self.renewNameButton.setToolTip(_translate("ManageNamesPage", "Renew the names with their current values"))
        self.renewNameButton.setText(_translate("ManageNamesPage", "&Renew Names"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManageNamesPage = QtWidgets.QWidget()
    ui = Ui_ManageNamesPage()
    ui.setupUi(ManageNamesPage)
    ManageNamesPage.show()
    sys.exit(app.exec_())
