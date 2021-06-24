from PySide2 import QtGui

from merge import Ui_Form
import sys
from PySide2.QtWidgets import QApplication,QWidget,QDialogButtonBox,QFileDialog,QMessageBox
from PyPDF2 import PdfFileMerger


class Open(QWidget):
	def __init__(self):
		super(Open,self).__init__()
		self.gui = Ui_Form()
		self.gui.setupUi(self)

		self.buttonConnect()

	def buttonConnect(self):
		self.gui.add_btn.clicked.connect(lambda: self.addFiles())
		self.gui.remove_btn.clicked.connect(lambda: self.removeFile())

		# QDialogButtonBox.Ok mean when we press just ok cause dialog box dose not like pushbutton
		self.gui.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(lambda: self.okPressed())
		self.gui.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(lambda:self.cancelPressed())

		self.gui.up_btn.clicked.connect(lambda: self.upArrow())
		self.gui.down_btn.clicked.connect(lambda: self.downArrow())

	def addFiles(self):
		fileDialog = QFileDialog.getOpenFileNames(filter="*.pdf")

		item = fileDialog[0][0]
		filepath_fix = item.replace("/",'\\')

		self.gui.listWidget.addItem(filepath_fix)

	def removeFile(self):
		for SelectedItem in self.gui.listWidget.selectedItems():
			self.gui.listWidget.takeItem(self.gui.listWidget.row(SelectedItem))

	def okPressed(self):
		fileList = []
		merger = PdfFileMerger(strict=False)
		for file in range(self.gui.listWidget.count()): # loop in all files name
			filesPath = self.gui.listWidget.item(file).text()
			fileList.append(filesPath) # add files path name in list to merge them later

		filenamePath = QFileDialog.getSaveFileName(dir="merged") # save dialog to locate the save location
		for pdfFile in fileList: # loop in file list
			merger.append(pdfFile) # add the pdf files in merger function to merge
		merger.write("{}.pdf".format(filenamePath[0])) # save the file in location from save dialog
		merger.close()

		self.popMessage("The file  merged successful","Done","images/done.png")
		self.close()

	def cancelPressed(self):
		self.close()

	def upArrow(self):
		currentRow = self.gui.listWidget.currentRow()
		currentItem = self.gui.listWidget.takeItem(currentRow)
		self.gui.listWidget.insertItem(currentRow - 1,currentItem)

	def downArrow(self):
		currentRow = self.gui.listWidget.currentRow()
		currentItem = self.gui.listWidget.takeItem(currentRow)
		self.gui.listWidget.insertItem(currentRow + 1,currentItem)

	def popMessage(self,text,head,imagePath: str):
		msg = QMessageBox()
		msg.setWindowIcon(QtGui.QIcon(imagePath))
		msg.about(msg,head,text)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyle("Fusion")
	window = Open()
	window.show()
	sys.exit(app.exec_())
