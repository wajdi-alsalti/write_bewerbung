import sys
import os
import sqlite3
from PySide2 import QtGui
from PySide2.QtCore import QDate, QCoreApplication
from PySide2.QtWidgets import QAction, QApplication, QColorDialog, QCompleter, QDesktopWidget, QFileDialog, \
    QFontDialog,QMainWindow, QMessageBox
from gui import Ui_MainWindow
from writeWordFile import BewerbungDocx
from wordTopdf import pdfMerge as pM, pdfSplitter as pS,convert_to_pdf
from textExamples import arbeitBewerbung,kundigungarbeit,kundigungInernet,kundigungWohnung,kundigungHandy
from languages import *
from programIsOpen import checkIfProgrammeOpen as isOpen


# how to load the gui
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.gui = Ui_MainWindow()  # name of the class
        self.gui.setupUi(self)
        self.docx = BewerbungDocx()

        ########################################
        self.now = QDate.currentDate()
        # set checkable to preview toolbar cause for the function hideLabel
        self.gui.actionPrivew.setCheckable(True)

        self.write = True
        self.answer = True # set true for the answer of dialog question
        self.emptyText = False # for the empty line edit
        self.editLinesNameText = {} # dictionary of line edits text
        self.restyleLineEdit = {} # dictionary of line edits if they empty will colored to red
        #self.names = [] # list for the names to auto complete
        self.names = set() # set for the names to auto complete to not duplicate names when save it

        # call all functions we need when the program start
        #self.toolbar()
        self.centerWindow()
        self.buttonsConnect()
        self.radioButtonsConnect()
        self.menuOptions()
        self.toolTips()
        self.setCurrentTime()
        self.defaultFontColorWriteDocument()
        self.resizeScreenHideWidget(False, 700, 944)
        self.connectDB()
        self.autoComplite()

    #######################################
    """connect to data base and functions"""
    def connectDB(self):
        self.connection = sqlite3.connect('names.db')
        self.namesUser = self.connection.execute("SELECT * FROM userNames")
        self.selectNameDB()

    def selectNameDB(self):
        # loop in list of names from db and add it in set list (set for not duplicate names show)
        for user in self.namesUser:
            self.names.add(user[0]) # return names from db and add in list for auto compiler

    def selectRowDB(self,name):
        # will take the name and give the complete row of the name from db
        self.namesSelect = self.connection.execute("SELECT * FROM userNames WHERE vollName='{}';".format(name))
        for item in self.namesSelect: # return the row of the name
            self.selectedName = item
            return self.selectedName

    def insertUserDataDB(self):
        # add the information user in db after press save
        fullName = self.gui.your1_name_line.text()
        zipCode = self.gui.your_zipcode_line.text()
        city = self.gui.your2_city_line.text()
        street = self.gui.your3_street_line.text()
        email = self.gui.your4_email_line.text()
        tN = self.gui.your5_tn_line.text()

        conn = sqlite3.connect('names.db')
        cur = conn.cursor()
        sql_executeOrder = """INSERT INTO userNames VALUES (?,?,?,?,?,?);"""
        cur.execute(sql_executeOrder, (fullName,zipCode,city,street,email,tN))
        conn.commit()
        conn.close()

    def enterPressed(self):
        # after chose name from auto complete when press enter will insert the data from the user
        # in edit lines
        for name in self.names:
            if self.gui.your1_name_line.text() == name:
                self.gui.your_zipcode_line.setText(str(self.selectRowDB(name)[1]))
                self.gui.your2_city_line.setText(str(self.selectRowDB(name)[2]))
                self.gui.your3_street_line.setText(str(self.selectRowDB(name)[3]))
                self.gui.your4_email_line.setText(str(self.selectRowDB(name)[4]))
                self.gui.your5_tn_line.setText(str(self.selectRowDB(name)[5]))

    #####################################################
    def autoComplite(self):
        # auto complete take the set of names to show in line edit
        completer = QCompleter(self.names)
        self.lineedit = self.gui.your1_name_line
        self.lineedit.setCompleter(completer)

    ####################################################
    def resizeScreenHideWidget(self, visible:bool, width:int, height:int):
        # resize the window and hide/show the right section
        self.gui.widgetform.setVisible(visible)
        self.resize(width, height)

    ########################################
    def defaultFontColorWriteDocument(self):
        # header default style
        self.hFs = 12
        self.hfF = "Arial"
        self.redH = 0
        self.greenH = 0
        self.blueH = 0
        ########################################
        # firma default style
        self.fFs = 12
        self.ffF = "Arial"
        self.redF = 0
        self.greenF = 0
        self.blueF = 0
        ########################################
        # subject default style
        self.sFs = 12
        self.sfF = "Arial"
        self.redS = 0
        self.greenS = 0
        self.blueS = 0
        ########################################

    def setCurrentTime(self):
        self.gui.dateEdit.setDate(self.now)

    def toolTips(self):
        self.gui.your_fontBtn.setToolTip("Font")

        self.gui.your_colorBtn.setToolTip("Color")

        self.gui.f_fontBtn.setToolTip("Font")

        self.gui.f_colorBtn.setToolTip("Color")

        self.gui.s_fontBtn.setToolTip("Font")

        self.gui.s_colorBtn.setToolTip("Color")

    def buttonsConnect(self):
        self.gui.your_fontBtn.clicked.connect(lambda:self.fontDialog_h())
        self.gui.your_colorBtn.clicked.connect(lambda:self.colorDialog_H())

        self.gui.f_fontBtn.clicked.connect(lambda:self.fontDialog_C())
        self.gui.f_colorBtn.clicked.connect(lambda:self.colorDialog_C())

        self.gui.s_fontBtn.clicked.connect(lambda:self.fontDialog_S())
        self.gui.s_colorBtn.clicked.connect(lambda:self.colorDialog_S())

        # this connect the line edit with enter button when it pressed
        self.gui.your1_name_line.returnPressed.connect(lambda:self.enterPressed())

    def radioButtonsConnect(self):
        self.gui.mr_rb.toggled.connect(lambda:self.radioBtn_subject(self.gui.mr_rb))
        self.gui.miss_rb.toggled.connect(lambda:self.radioBtn_subject(self.gui.miss_rb))
        self.gui.plural_rb.toggled.connect(lambda:self.radioBtn_subject(self.gui.plural_rb))

        self.gui.rb_L_your.toggled.connect(lambda:self.radioBtn_yourText())
        self.gui.rb_C_your.toggled.connect(lambda: self.radioBtn_yourText())
        self.gui.rb_R_your.toggled.connect(lambda:self.radioBtn_yourText())

        self.gui.rb_R_firma.toggled.connect(lambda:self.radioBtn_companyText())
        self.gui.rb_C_firma.toggled.connect(lambda:self.radioBtn_companyText())
        self.gui.rb_L_firma.toggled.connect(lambda:self.radioBtn_companyText())

        self.gui.rb_R_your.setChecked(True)
        self.gui.rb_L_firma.setChecked(True)

    def menuOptions(self):
        self.gui.actionSave_as_pdf.triggered.connect(lambda:self.pdfConverter())
        self.gui.actionSave_as_docx.triggered.connect(lambda:self.pressSave())

        self.gui.actionMerge.triggered.connect(lambda:self.pdfMerge())
        self.gui.actionSplit.triggered.connect(lambda:self.pdfSplit())

        self.gui.actionQuit.triggered.connect(lambda:self.closeWindow())
        self.gui.actionQuit.setShortcut("alt+F4")

        self.gui.actionPrivew.triggered.connect(lambda:self.hideLabelWidgets())

        self.gui.actionBewerbung.triggered.connect(lambda:self.insertExample(arbeitBewerbung()))

        self.gui.actioninternt.triggered.connect(lambda:self.insertExample(kundigungInernet()))

        self.gui.actionhandy.triggered.connect(lambda:self.insertExample(kundigungHandy()))

        self.gui.actionwohnung.triggered.connect(lambda:self.insertExample(kundigungWohnung()))

        self.gui.actionarbeit.triggered.connect(lambda:self.insertExample(kundigungarbeit()))

        self.gui.actionEars.triggered.connect(lambda:self.clearLines())

        self.gui.actionGermany.triggered.connect(lambda:self.gLanguage())

        self.gui.actionEnglish.triggered.connect(lambda:self.eLanguage())
        self.gui.actionEnglish.setIcon(QtGui.QIcon('images/rightCheck.png'))

    def changeFontSizeTextEdit(self,size):
        font = QtGui.QFont()
        font.setPointSize(size)
        self.gui.main_text.setFont(font)

    def insertExample(self, text:str):
        self.gui.main_text.setText(text[0])
        self.gui.subject_line.setText(text[1])

    def hideLabelWidgets(self):
        if self.gui.actionPrivew.isChecked():
            self.resizeScreenHideWidget(True, 1010, 944)
        else:
            self.resizeScreenHideWidget(False, 700, 944)

    def closeWindow(self):
        self.close()

    def set_lineEditStyle(self):
        # loop inside dic of line edits and set the style
        for line in self.restyleLineEdit.values():
            line.setStyleSheet(u"QLineEdit{\n"
                               u"	border: 0.3px solid rgb(0, 0, 0);\n"
                               u"	border-radius : 10px;\n"
                               u"	padding-left:5px;\n"
                               u"	height:26px;\n"
                               u"	\n"
                               u"}\n"
                               u"QLineEdit::hover{\n"
                               u"	border:2px solid rgb(0, 255, 255);\n"
                               u"}\n"
                               u"QLineEdit::focus{\n"
                               u"	border:2px solid  rgb(0, 170, 255);\n"
                               u"}\n"
                               "")

    def set_alignedYourLabel(self, position: str):
        self.gui.your_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"{}\">"
                                                                             u"<span >"
                                                                             u"Your Name</span>"
                                                                             u"</p><p "u"align=\"{}\">"
                                                                             u"<span >"
                                                                             u"Your Street</span>"
                                                                             u"</p><p align=\"{}\">"
                                                                             u"<span >"
                                                                             u"Your Email</span></p>"
                                                                             u"<p align=\"{}\">"
                                                                             u"<span >"
                                                                             u"Your TN</span></p></body></html>",
                                                               None).format(position, position,
                                                                            position, position))

    def set_StyleYourLabel(self):
        self.gui.your_label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                          "border:1px solid rgb(195, 194, 193);\n"
                                          "border-radius:10px;\ncolor:rgb({},{},{});\n"
                                          "font:{}pt '{}';".format(self.redH, self.greenH, self.blueH,self.hFs, self.hfF))

    def set_alignedCompanyLabel(self, position):
        self.gui.firma_label.setText(QCoreApplication.translate("MainWindow",
                                                                u"<html><head/><body><p align=\"{}\">"
                                                                u"<span>"
                                                                u"Company Name</span></p><p align=\"{}\">"
                                                                u"<span>"
                                                                u"Company Address</span></p><p align=\"{}\">"
                                                                u"<span>"
                                                                u"Company Street</span></p>"
                                                                u"<p><br/></p></body></html>",
                                                                None).format(position, position, position))

    def set_StyleCompanyLabel(self):
        self.gui.firma_label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                           "border:1px solid rgb(195, 194, 193);\n"
                                           "border-radius:10px;\ncolor:rgb({},{},{});\n"
                                           "font:{}pt '{}';".format(self.redF, self.greenF, self.blueF,self.fFs, self.ffF))

    def set_StyleSubjectLabel(self):
        self.gui.s_label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                       "border:1px solid rgb(195, 194, 193);\n"
                                       "border-radius:10px;\ncolor:rgb({},{},{});\n"
                                       "font:{}pt '{}';".format(self.redS, self.greenS, self.blueS,self.sFs, self.sfF))

    def take_text_from_editLine(self):
        # dic with the text from the line edits used to take the string from them
        self.editLinesNameText['your Name'] = self.gui.your1_name_line.text()
        self.editLinesNameText['Your zipCode'] = self.gui.your_zipcode_line.text()
        self.editLinesNameText['your city'] = self.gui.your2_city_line.text()
        self.editLinesNameText['your street'] = self.gui.your3_street_line.text()
        self.editLinesNameText['your email'] = self.gui.your4_email_line.text()
        self.editLinesNameText['your TN'] = self.gui.your5_tn_line.text()
        self.editLinesNameText['firma Name'] = self.gui.firma_name_line.text()
        self.editLinesNameText['firma address'] = self.gui.firma_address_line.text()
        self.editLinesNameText['firma str'] = self.gui.firma_str_line.text()
        self.editLinesNameText['subject text'] = self.gui.subject_line.text()
        self.editLinesNameText['send to'] = self.gui.sendTo_line.text()

    def lineEditDic(self):
        # dic of lines edit used to restyle the lineEdit if they empty
        self.restyleLineEdit['your Name'] = self.gui.your1_name_line
        self.restyleLineEdit['Your zipCode'] = self.gui.your_zipcode_line
        self.restyleLineEdit['your city'] = self.gui.your2_city_line
        self.restyleLineEdit['your street'] = self.gui.your3_street_line
        self.restyleLineEdit['your email'] = self.gui.your4_email_line
        self.restyleLineEdit['your TN'] = self.gui.your5_tn_line
        self.restyleLineEdit['firma Name'] = self.gui.firma_name_line
        self.restyleLineEdit['firma address'] = self.gui.firma_address_line
        self.restyleLineEdit['firma str'] = self.gui.firma_str_line
        self.restyleLineEdit['subject text'] = self.gui.subject_line
        self.restyleLineEdit['send to'] = self.gui.sendTo_line
        return self.restyleLineEdit

    def emptyLineEditRestyle(self):
        """ loop in dic (editLinesNameText) of lineEdits if the line is empty we pass the key
        to the dic restyleLineEdit they have the same key names and change the empty one  """
        for key,value in self.editLinesNameText.items():
            if value == "":
                self.lineEditDic()[key].setStyleSheet("""border: 0.6px solid red;\n
                border-radius : 10px;\n
                padding-left:5px;\n
                height:26px;""")
                self.emptyText = True

    def saveWordDocument(self, fileName):
        # save the word file if not excite
        if not self.checkFileExcite():
            self.writeWordFile()
            self.docx.document.save('{}.docx'.format(fileName))
            self.popMessage("File Created", 'Done', 'images/done.png')

    def toolbar(self):
        # create an icon in toolbar
        saveAction = QAction("save", self)
        # icon photo
        saveAction.setIcon(QtGui.QIcon("images/save.png"))
        # with which function will be connect if pressed
        #saveAction.triggered.connect(lambda:self.saveWordDocument())

        savePdf = QAction("save a pdf", self)
        savePdf.setIcon(QtGui.QIcon("images/pdf.png"))
        savePdf.triggered.connect(lambda:self.pdfConverter())

        mergeFiles = QAction("merge pdf", self)
        mergeFiles.setIcon(QtGui.QIcon("images/merge.png"))
        mergeFiles.triggered.connect(lambda:self.pdfMerge())

        splitFiles = QAction("split pdf", self)
        splitFiles.setIcon(QtGui.QIcon("images/split.png"))
        splitFiles.triggered.connect(lambda:self.pdfSplitter())

        # not to move
        self.gui.toolBar.setMovable(False)

        # add icon to the tool bar and the connect function
        self.gui.toolBar.addAction(saveAction)
        self.gui.toolBar.addAction(savePdf)

        # add line between icons
        self.gui.toolBar.addSeparator()

        self.gui.toolBar.addAction(mergeFiles)
        self.gui.toolBar.addAction(splitFiles)

    def writeWordFile(self):
        if self.write:
            # create new page if not exist
            self.docx.createPage()
            # header
            self.docx.write_heading(self.header_pos,
                                    "{}\n{} {}\n{}\n{}\nTelefon: {}".format(self.editLinesNameText['your Name'].title(),
                                                                            self.editLinesNameText['Your zipCode'],
                                                                            self.editLinesNameText['your city'].title(),
                                                                            self.editLinesNameText['your street'].title(),
                                                                            self.editLinesNameText['your email'],
                                                                            self.editLinesNameText['your TN']),
                                    self.hFs, self.redH, self.greenH, self.blueH, self.hfF)
            # company
            self.docx.write_paragraph(self.company_pos,
                                      "{}\n{}\n{}".format(self.editLinesNameText['firma Name'].title(),
                                                          self.editLinesNameText['firma address'].title(),
                                                          self.editLinesNameText['firma str'].title()),
                                      self.fFs,
                                      self.redF, self.greenF, self.blueF, self.ffF)
            # time
            self.docx.write_paragraph(self.docx.right, "{},{}".format(self.editLinesNameText['your city'].title(),
                                                                      self.gui.dateEdit.text()), self.sFs, self.redS,
                                      self.greenS, self.blueS, self.sfF)
            # subject

            self.docx.write_paragraph(self.docx.left,"{} ".format(self.editLinesNameText['subject text']), self.sFs,
                                      self.redS,self.greenS, self.blueS, self.sfF)
            # send to
            try:
                self.docx.write_paragraph(self.docx.left,"{} {}".format(self.to,
                                                                        self.editLinesNameText['send to'].title() + ','),
                                          self.sFs, self.redS,self.greenS, self.blueS, self.sfF)
            except Exception:
                pass
            # text edit find about your exp
            find_it = self.gui.main_text
            self.docx.write_paragraph(self.docx.left,"{}".format(find_it.toPlainText()), self.sFs, self.redS,
                                      self.greenS, self.blueS, self.sfF)
            #writer name
            self.docx.write_paragraph(self.docx.left, self.editLinesNameText['your Name'].title(), self.sFs, self.redS,
                                      self.greenS, self.blueS, self.sfF)
            self.docx.page_margin()
        else:
            pass

    # if the file already created will not create another one in the same name
    def checkFileExcite(self):
        file = os.path.isfile("{}.docx".format(self.editLinesNameText['firma Name']))
        if file:
            self.popMessage("The file already created", "Error", "images/error.png")
            self.write = False
            return True
        elif not file:
            self.write = True

    ###################################
    # open dialog file and return the path of the selected file for pdf
    def openDialogFile(self):
        filename = QFileDialog.getOpenFileNames(filter="*.docx",)
        try:
            filename_fix = filename[0][0].replace("/", '\\')
            return filename_fix
        except AttributeError:
            return ""

    # add path to save the file docx
    def saveFileDialog(self):
        self.filename = QFileDialog.getSaveFileName(dir="{}".format(self.gui.firma_name_line.text()))

    def pressSave(self):
        # the function will work when we press the save on gui
        self.take_text_from_editLine() # take text from lines edit
        self.emptyLineEditRestyle() # check if an empty line edit
        if self.emptyText:
            self.questionMessage() # pop a message if want to continue and have an empty line
        if self.answer and self.editLinesNameText['firma Name'] != "": # answer is the yes button in question message
            self.saveFileDialog() # open save file dialog
            self.checkIfNameInSet() # if name in names list will not save it in db
            if self.filename[0] != "": #if the save dialog return path not empty(empty when press cancel in save dialog)
                self.saveWordDocument(self.filename[0])#save file with name we give from company name
            self.set_lineEditStyle() # restyle the line edits after we press yes
        elif self.editLinesNameText['firma Name'] == "": # if the company name empty do not save
            self.popMessage("can not create file without company name","Ops","images/error.png")
            self.set_lineEditStyle()

        self.answer = True
        self.emptyText = False

    def checkIfNameInSet(self):
        # if the name not in names set will add it in db other wise will not save it cause already in db
        if self.gui.your1_name_line.text() not in self.names:
            self.insertUserDataDB()

    ######################################
    # pdf functions split merge and convert from docx
    def pdfConverter(self):
        fileIsOpen = isOpen("WINWORD.EXE")
        try:
            if not fileIsOpen:
                convert_to_pdf(self.openDialogFile())
                self.popMessage("it has successful converted", "converted to pdf", "images/done.png")
            else:
                self.popMessage("Please Close Word application before convert","Error convert","images/error.png")

        except Exception as e:
            print(e)


    def pdfMerge(self):
        try:
            pM()
            self.popMessage("The file  merged successful","Done","images/done.png")
        except Exception:
            pass
        # TODO: create a widget to add files need to merged

    def pdfSplit(self):
        try:
            pS()
            self.popMessage("The file  split successful", "Done", "images/done.png")
        except Exception:
            pass

    #######################################################################
    # fonts dialogs for every font buttons
    def fontDialog_h(self):
        ok, font = QFontDialog.getFont()
        if ok:
            self.hFs = int(font.pointSize())  # give the font size from dialog
            self.hfF = font.family()
            self.set_StyleYourLabel()
            #print(font.toString())

    def fontDialog_C(self):
        ok, font = QFontDialog.getFont()
        if ok:
            self.fFs = int(font.pointSize())  # give the font size from dialog
            self.ffF = font.family()
            self.set_StyleCompanyLabel()

    def fontDialog_S(self):
        ok, font = QFontDialog.getFont()
        if ok:
            self.sFs = int(font.pointSize())  # give the font size from dialog
            self.sfF = font.family()
            self.set_StyleSubjectLabel()
            self.changeFontSizeTextEdit(self.sFs)

    #######################################################################
    # color dialogs for every color buttons
    def colorDialog_H(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.redH = color.red()
            self.greenH = color.green()
            self.blueH = color.blue()
            self.set_StyleYourLabel()

    def colorDialog_C(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.redF = color.red()
            self.greenF = color.green()
            self.blueF = color.blue()
            self.set_StyleCompanyLabel()

    def colorDialog_S(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.redS = color.red()
            self.greenS = color.green()
            self.blueS = color.blue()
            self.set_StyleSubjectLabel()

    #######################################################################
    def radioBtn_subject(self, rb):
        if rb.isChecked() and rb.text() == "Herr":
            self.to = "Sehr geehrter Herr"
            self.gui.sendTo_line.setPlaceholderText("The recipient's name")
            self.gui.sendTo_line.setEnabled(True)

        elif rb.isChecked() and rb.text() == "Frau":
            self.to = "Sehr geehrte Frau"
            self.gui.sendTo_line.setPlaceholderText("The recipient's name")
            self.gui.sendTo_line.setEnabled(True)

        elif rb.isChecked() and rb.text() == "Plural":
            self.gui.sendTo_line.setPlaceholderText("you did not need a name")
            self.gui.sendTo_line.setEnabled(False)
            self.to = "Sehr geehrte Damen und Herren"

    def radioBtn_yourText(self):
        if self.gui.rb_L_your.isChecked():
            self.set_alignedYourLabel("left")
            self.header_pos = self.docx.left

        elif self.gui.rb_C_your.isChecked():
            self.set_alignedYourLabel("center")
            self.header_pos = self.docx.center

        elif self.gui.rb_R_your.isChecked():
            self.set_alignedYourLabel("right")
            self.header_pos = self.docx.right

    def radioBtn_companyText(self):
        if self.gui.rb_L_firma.isChecked():
            self.set_alignedCompanyLabel("left")
            self.company_pos = self.docx.left

        elif self.gui.rb_C_firma.isChecked():
            self.set_alignedCompanyLabel("center")
            self.company_pos = self.docx.center

        elif self.gui.rb_R_firma.isChecked():
            self.set_alignedCompanyLabel("right")
            self.company_pos = self.docx.right

    def popMessage(self, text, head, imagePath: str):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon(imagePath))
        msg.about(msg, head, text)

    def questionMessage(self):
        mes = QMessageBox.question(self,"ops","some fields are empty, do you want to save it",
                                   QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if mes == QMessageBox.Yes:
            self.answer = True
        else:
            self.answer = False

    def centerWindow(self):
        # geometry of the main window
        qr = self.frameGeometry()
        # centerWindow point of screen
        cp = QDesktopWidget().availableGeometry(screen=-1).center()
        # move rectangle's centerWindow point to screen's centerWindow point
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    def clearLines(self):
        for value in self.lineEditDic().values():
            value.setText('')
        self.gui.main_text.setText('')

    def gLanguage(self):
        self.gui.actionEnglish.setIcon(QtGui.QIcon(''))
        # change label language to germany
        self.gui.info_label.setText(y_informationG)
        self.gui.comp_label.setText(companyG)
        self.gui.sub_label.setText(subjectG)
        self.gui.send_label.setText(sendG)
        self.gui.styleInfo_label.setText(styleG)
        self.gui.styleComp_label.setText(styleG)
        self.gui.styleSub_label.setText(styleG)
        self.gui.actionGermany.setIcon(QtGui.QIcon('images/rightCheck.png'))

        # change line edit place holder language
        self.gui.your1_name_line.setPlaceholderText(phNameG)
        self.gui.your_zipcode_line.setPlaceholderText(phZipCodeG)
        self.gui.your2_city_line.setPlaceholderText(phCityG)
        self.gui.your3_street_line.setPlaceholderText(phStreetG)
        self.gui.your5_tn_line.setPlaceholderText(phTnG)

        self.gui.firma_name_line.setPlaceholderText(phCoNameG)
        self.gui.firma_address_line.setPlaceholderText(phCoAddressG)
        self.gui.firma_str_line.setPlaceholderText(phCoStreetG)
        self.gui.sendTo_line.setPlaceholderText(phSendToG)

    def eLanguage(self):
        self.gui.actionGermany.setIcon(QtGui.QIcon(''))
        # change label language to english
        self.gui.info_label.setText(y_informationE)
        self.gui.comp_label.setText(companyE)
        self.gui.sub_label.setText(subjectE)
        self.gui.send_label.setText(sendE)
        self.gui.styleInfo_label.setText(styleE)
        self.gui.styleComp_label.setText(styleE)
        self.gui.styleSub_label.setText(styleE)
        self.gui.actionEnglish.setIcon(QtGui.QIcon('images/rightCheck.png'))

        # change line edit place holder language
        self.gui.your1_name_line.setPlaceholderText(phNameE)
        self.gui.your_zipcode_line.setPlaceholderText(phZipCodeE)
        self.gui.your2_city_line.setPlaceholderText(phCityE)
        self.gui.your3_street_line.setPlaceholderText(phStreetE)
        self.gui.your5_tn_line.setPlaceholderText(phTnE)

        self.gui.firma_name_line.setPlaceholderText(phCoNameE)
        self.gui.firma_address_line.setPlaceholderText(phCoAddressE)
        self.gui.firma_str_line.setPlaceholderText(phCoStreetE)
        self.gui.sendTo_line.setPlaceholderText(phSendToE)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
