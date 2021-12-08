from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import path
from sys import argv
from sqlite3 import connect
from pizza_menu import UiForm


FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"/media/ziad/Turbo/zizo/projects/PYTHON/RESTRAUNT/main_app.ui"))


class mainapp(QMainWindow,FORM_CLASS):
    def __init__(self, parent=None):
        super(mainapp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.cashierlist = []
        self.firstwinsetup()
        self.button_setup()
        self.window2 = QMainWindow()
        self.ui = UiForm()
        self.ui.setupUi(self.window2)
        self.databasesetup()
        self.tableitem = 0
        self.tableprice = 1

    def firstwinsetup(self):
        self.ui = UiForm()
        self.cashier_win.hide()
        self.cashier_button_win.hide()
        self.info_win.hide()
        self.info_button_win.hide()
        self.database_win.hide()
        self.database_button_win.hide()
        self.admin_win.hide()
        self.admin_button_win.hide()

    def button_setup(self):
        self.pizza_menu_setup()
        self.cashier_button.clicked.connect(self.cashierbt)
        self.info_button.clicked.connect(self.infobt)
        self.database_button.clicked.connect(self.databasebt)
        self.admin_button.clicked.connect(self.adminbt)
        self.pizza_button.clicked.connect(self.pizza_menu)
        self.ui.piz_cheese_L.clicked.connect(self.cheeseL)
        self.ui.piz_cheese_M.clicked.connect(self.cheeseM)
        self.ui.piz_cheese_S.clicked.connect(self.cheeseS)
        self.ui.piz_chicken_L.clicked.connect(self.chickenL)
        self.ui.piz_chicken_M.clicked.connect(self.chickenM)
        self.ui.piz_chicken_S.clicked.connect(self.chickenS)
        self.ui.piz_peperoni_L.clicked.connect(self.peperoniL)
        self.ui.piz_extra_cheese.clicked.connect(self.peperoniM)
        self.ui.piz_peperoni_S.clicked.connect(self.peperoniS)
        self.ui.piz_mushroom_L.clicked.connect(self.mushroomL)
        self.ui.piz_mushroom_M.clicked.connect(self.mushroomM)
        self.ui.piz_mushroom_S.clicked.connect(self.mushroomS)
        # self.confirm_button.clicked.connect(self.pizzaingredients)

    def hide_window(self):
        self.cashier_win.hide()
        self.cashier_button_win.hide()
        self.info_win.hide()
        self.info_button_win.hide()
        self.database_win.hide()
        self.database_button_win.hide()
        self.admin_win.hide()
        self.admin_button_win.hide()

    def cashierbt(self):
        self.hide_window()
        self.cashier_win.show()
        self.cashier_button_win.show()
        
    def infobt(self):
        self.hide_window()
        self.info_win.show()
        self.info_button_win.show()

    def databasebt(self):
        self.hide_window()
        self.database_win.show()
        self.database_button_win.show()

    def adminbt(self):
        self.hide_window()
        self.admin_win.show()
        self.admin_button_win.show()

    def pizza_menu_setup(self):
        self.MainWindow = QMainWindow()
        self.ui = UiForm()
        self.ui.setupUi(self.MainWindow)
        
    
    def pizza_menu(self):
        self.MainWindow.show()


    def cheeseL(self):
        self.testtable()
        pizprice = self.getfromdb("pizza_cheese_L")
        self.addtotable(pizprice)

    def cheeseM(self):
        self.testtable()
        pizprice = self.getfromdb("pizza_cheese_M")
        self.addtotable(pizprice)

    def cheeseS(self):
        self.testtable()
        pizprice = self.getfromdb("pizza_cheese_S")
        self.addtotable(pizprice)

    def peperoniL(self):
        self.testtable()
        pizprice = self.getfromdb("pizza_peperoni_L")
        self.addtotable(pizprice)
     
    def peperoniM(self):
        self.testtable()
        pizprice = self.getfromdb("pizza_peperoni_M")
        self.addtotable(pizprice)

    def peperoniS(self):
        self.testtable()
        pizprice = self.getfromdb("pizza_peperoni_S")
        self.addtotable(pizprice)

    def chickenL(self):
        self.testtable()
        pizprice = self.getfromdb("pizza_chicken_L")
        self.addtotable(pizprice)

    def chickenM(self):
        self.testtable()
        pizprice = self.getfromdb("pizza_chicken_M")
        self.addtotable(pizprice)

    def chickenS(self):
        self.testtable()
        pizprice = self.getfromdb("pizza_chicken_S")
        self.addtotable(pizprice)

    def mushroomL(self):
        self.testtable()
        pizprice = self.getfromdb("pizza_mushroom_L")
        self.addtotable(pizprice)

    def mushroomM(self):
        self.testtable()
        pizprice = self.getfromdb("pizza_mushroom_M")
        self.addtotable(pizprice)

    def mushroomS(self):
        self.testtable()
        pizprice = self.getfromdb("pizza_mushroom_S")
        self.addtotable(pizprice)

    def addtotable(self,pizprice):
        rowPosition = self.tableWidget.rowCount()
        ind = self.total_pric.text().index("$")
        currentmon = int(self.total_pric.text()[:ind])
        if str(pizprice[1]) in self.cashierlist:
            indx = self.cashierlist.index(str(pizprice[1]))
            amount = self.tableWidget.item(int(indx), 1)
            price = self.tableWidget.item(int(indx),2)
            moh = price.text()
            self.tableWidget.setItem(int(indx) , 1, QTableWidgetItem(str(int(amount.text())+1)))
            self.tableWidget.setItem(int(indx),2,   QTableWidgetItem(str(int(price.text())+int(pizprice[0]))))
        else:
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition , 0, QTableWidgetItem(str(pizprice[1])))
            self.tableWidget.setItem(rowPosition , 1, QTableWidgetItem("1"))
            self.tableWidget.setItem(rowPosition , 2, QTableWidgetItem(str(pizprice[0])))
            
        self.totalprice(currentmon,pizprice[0])
        # self.data_total(pizprice)
        self.pizzaingredients(pizprice)

    def databasesetup(self):
        self.db = connect("restraunt.db")
        self.cr = self.db.cursor()

    def getfromdb(self, item):
        item = item
        self.cr.execute(f"select * from price WHERE item='{item}'")
        mydata = self.cr.fetchall()
        data = mydata[0][1]
        return data ,item

    def testtable(self):
        a = 0
        self.cashierlist = []
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(a, 0)
            self.cashierlist.append(item.text())
            a+=1
    
    def totalprice(self,current,new):
        added = int(current)+int(new)
        self.total_pric.setText(f"{added}$")

    def data_total(self,piz):
        pizzatotal = piz[1]
        self.cr.execute(f"select * from total WHERE item='{pizzatotal}'")
        coun = self.cr.fetchall()
        count = coun[0][1]
        newcount = int(count)+1
        pri = coun[0][2]
        newpri = int(pri)+int(piz[0])

        self.cr.execute(f"select * from total WHERE item='total'")
        totalval = self.cr.fetchall()
        totalcount = totalval[0][1]
        newtotalcount = int(totalcount)+1
        totalmoney = totalval[0][2]
        newtotalmoney = int(totalmoney)+int(piz[0])


        self.cr.execute(f"UPDATE total set count = '{newtotalcount}' WHERE item='total'")
        self.cr.execute(f"UPDATE total set total = '{newtotalmoney}' WHERE item='total'")

        self.cr.execute(f"UPDATE total set count = '{newcount}' WHERE item='{pizzatotal}'")
        self.cr.execute(f"UPDATE total set total = '{newpri}' WHERE item='{pizzatotal}'")
        self.db.commit()


    def pizzaingredients(self,piz):
        main_ing = ["dough","mozarella","tomato_sauce"]
        pizzaname = piz[1]
        self.cr.execute(f"select * from piz_ing WHERE item = '{pizzaname}'")
        pizing = self.cr.fetchall()
        print(pizing[0])
        for i in pizing[0]:
            if i != "no" and "pizza_" not in i:
                main_ing.append(i)
        print(main_ing)
        for x in main_ing:
            self.cr.execute(f"select amount from ingredients WHERE item='{x}'")
            amount = self.cr.fetchall()
            print(amount)
            new_amount = int(amount[0][0])-1
            print(new_amount)
            self.cr.execute(f"UPDATE ingredients set amount = '{new_amount}' WHERE item='{x}'")
        self.db.commit()



if __name__ == "__main__":
    app = QApplication(argv)
    MainWindow = QMainWindow()
    window = mainapp()
    window.show()
    app.exec()