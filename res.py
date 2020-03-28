from Tkinter import *
from time import *
from PIL import ImageTK, Image
import random
import time
import datetime
from Tkinter import Tk, StringVar
import ttk

root = Tk ()
root.geometry ("1600x800+0+0")
root.title ("Food Management")
root.configure (background='Black')

img1=ImageTk.PhotoImage(Image.open("b1.jpg"))
label = Label (root,image=img1,height=800,width=1600)
#label.image = img1
#label.grid ()

Top = Frame (root, width=1350, height=100, bd=12, relief="raise")
Top.pack (side=TOP)
lblTitle = Label (Top, font=('arial', 50, 'bold'), text="\t\tALL IN ONE\t\t\t")
lblTitle.grid (row=0, column=0)

BottomMainFrame = Frame (root, width=1350, height=100, bd=12, relief="raise")
BottomMainFrame.pack (side=BOTTOM)

f1 = Frame (BottomMainFrame, width=450, height=650, bd=12, relief="raise")
f1.pack (side=LEFT)
f2 = Frame (BottomMainFrame, width=450, height=650, bd=12, relief="raise")
f2.pack (side=LEFT)
f2TOP = Frame (f2, width=450, height=350, bd=4, relief="raise")
f2TOP.pack (side=TOP)
f2BOTTOM = Frame (f2, width=450, height=300, bd=4, relief="raise")
f2BOTTOM.pack (side=BOTTOM)

f3 = Frame (BottomMainFrame, width=450, height=650, bd=12, relief="raise")
f3.pack (side=RIGHT)

Top.configure (background='red')
BottomMainFrame.configure (background='green')
# f1.configure(background='Black')
# f2TOP.configure(background='Black')
# f2BOTTOM.configure(background='Black')
# f3.configure(background='Black')

var1 = IntVar ()
var2 = IntVar ()
var3 = IntVar ()
var4 = IntVar ()
var5 = IntVar ()
var6 = IntVar ()
var7 = IntVar ()
var8 = IntVar ()
var9 = IntVar ()
var10 = IntVar ()
var11 = IntVar ()
var12 = IntVar ()
var13 = IntVar ()
var14 = IntVar ()
var15 = IntVar ()
var16 = IntVar ()
var17 = IntVar ()
var18 = IntVar ()
var19 = IntVar ()
var20 = IntVar ()
var21 = IntVar ()
var22 = StringVar ()
var23 = IntVar ()

var1.set (0)
var2.set (0)
var3.set (0)
var4.set (0)
var5.set (0)
var6.set (0)
var7.set (0)
var8.set (0)
var9.set (0)
var10.set (0)
var11.set (0)
var12.set (0)
var13.set (0)
var14.set (0)
var15.set (0)
var16.set (0)
var17.set (0)
var18.set (0)
var19.set (0)
var20.set (0)
var21.set (0)
var22.set ("")
var23.set (0)

varFries = StringVar ()
varVegNoodles = StringVar ()
varVegManchurian = StringVar ()
varChickenManchurian = StringVar ()
varFishSandwich = StringVar ()
varCheeseSandwich = StringVar ()
varChickenSandwich = StringVar ()
varChickenNoodles = StringVar ()
varTAX = StringVar ()
varSubTotal = StringVar ()
varTotal = StringVar ()
varCheeseCake = StringVar ()
varBrownie = StringVar ()
varPudding = StringVar ()
varWaffle = StringVar ()
varSundae = StringVar ()
varColdDrinks = StringVar ()
varCaffeine = StringVar ()
varMocktail = StringVar ()
varJuices = StringVar ()
varWaterBottle = StringVar ()
varChocolateSwirl = StringVar ()
varButterscotch = StringVar ()
varBerryShakes = StringVar ()

varFries.set ("0")
varVegNoodles.set ("0")
varVegManchurian.set ("0")
varChickenManchurian.set ("0")
varFishSandwich.set ("0")
varCheeseSandwich.set ("0")
varChickenSandwich.set ("0")
varChickenNoodles.set ("0")
varTotal.set ("0")
varTAX.set ("0")
varSubTotal.set ("0")
varCheeseCake.set ("0")
varBrownie.set ("0")
varPudding.set ("0")
varWaffle.set ("0")
varSundae.set ("0")
varColdDrinks.set ("0")
varCaffeine.set ("0")
varMocktail.set ("0")
varJuices.set ("0")
varWaterBottle.set ("0")
varChocolateSwirl.set ("0")
varButterscotch.set ("0")
varBerryShakes.set ("0")


def qExit():
    root.destroy ()


def Reset():
    var1.set (0)
    var2.set (0)
    var3.set (0)
    var4.set (0)
    var5.set (0)
    var6.set (0)
    var7.set (0)
    var8.set (0)
    var9.set (0)
    var10.set (0)
    var11.set (0)
    var12.set (0)
    var13.set (0)
    var14.set (0)
    var15.set (0)
    var16.set (0)
    var17.set (0)
    var18.set (0)
    var19.set (0)
    var20.set (0)
    var21.set (0)
    var22.set (0)
    var23.set (0)

    varFries.set ("0")
    varVegNoodles.set ("0")
    varVegManchurian.set ("0")
    varChickenManchurian.set ("0")
    varChickenNoodles.set ("0")

    varFishSandwich.set ("0")
    varCheeseSandwich.set ("0")
    varChickenSandwich.set ("0")

    varTotal.set ("0")
    varTAX.set ("0")
    varSubTotal.set ("0")

    varCheeseCake.set ("0")
    varBrownie.set ("0")
    varPudding.set ("0")
    varWaffle.set ("0")
    varSundae.set ("0")

    varColdDrinks.set ("0")
    varCaffeine.set ("0")
    varMocktail.set ("0")
    varJuices.set ("0")
    varWaterBottle.set ("0")

    varChocolateSwirl.set ("0")
    varButterscotch.set ("0")
    varBerryShakes.set ("0")

    txtFries.configure (state=DISABLED)
    txtVegNoodles.configure (state=DISABLED)
    txtVegManchurian.configure (state=DISABLED)
    txtChickenNoodles.configure (state=DISABLED)
    txtChickenManchurian.configure (state=DISABLED)

    txtFishSandwich.configure (state=DISABLED)
    txtCheeseSandwich.configure (state=DISABLED)
    txtChickenSandwich.configure (state=DISABLED)

    txtTax.configure (state=DISABLED)
    txtTotal.configure (state=DISABLED)
    txtSubTotal.configure (state=DISABLED)

    txtCheeseCake.configure (state=DISABLED)
    txtBrownie.configure (state=DISABLED)
    txtSundae.configure (state=DISABLED)
    txtWaffle.configure (state=DISABLED)
    txtPudding.configure (state=DISABLED)

    txtColdDrinks.configure (state=DISABLED)
    txtCaffeine.configure (state=DISABLED)
    txtJuices.configure (state=DISABLED)
    txtMocktail.configure (state=DISABLED)
    txtWaterBottle.configure (state=DISABLED)

    txtChocolateSwirl.configure (state=DISABLED)
    txtButterscotch.configure (state=DISABLED)
    txtBerryShakes.configure (state=DISABLED)


def chkbutton_value():
    if (var1.get () == 1):
        txtFries.configure (state=NORMAL)
        varFries.set ("")
    elif (var1.get () == 0):
        txtFries.configure (state=DISABLED)
        varFries.set ("0")

    if (var2.get () == 1):
        txtVegNoodles.configure (state=NORMAL)
        varVegNoodles.set ("")
    elif (var2.get () == 0):
        txtVegNoodles.configure (state=DISABLED)
        varVegNoodles.set ("0")

    if (var3.get () == 1):
        txtChickenNoodles.configure (state=NORMAL)
        varChickenNoodles.set ("")
    elif (var3.get () == 0):
        txtChickenNoodles.configure (state=DISABLED)
        varChickenNoodles.set ("0")

    if (var4.get () == 1):
        txtVegManchurian.configure (state=NORMAL)
        varVegManchurian.set ("")
    elif (var4.get () == 0):
        txtVegManchurian.configure (state=DISABLED)
        varVegManchurian.set ("0")

    if (var5.get () == 1):
        txtChickenManchurian.configure (state=NORMAL)
        varChickenManchurian.set ("")
    elif (var5.get () == 0):
        txtChickenManchurian.configure (state=DISABLED)
        varChickenManchurian.set ("0")

    if (var6.get () == 1):
        txtFishSandwich.configure (state=NORMAL)
        varFishSandwich.set ("")
    elif (var6.get () == 0):
        txtFishSandwich.configure (state=DISABLED)
        varFishSandwich.set ("0")

    if (var7.get () == 1):
        txtCheeseSandwich.configure (state=NORMAL)
        varCheeseSandwich.set ("")
    elif (var7.get () == 0):
        txtCheeseSandwich.configure (state=DISABLED)
        varCheeseSandwich.set ("0")

    if (var8.get () == 1):
        txtChickenSandwich.configure (state=NORMAL)
        varChickenSandwich.set ("")
    elif (var8.get () == 0):
        txtChickenSandwich.configure (state=DISABLED)
        varChickenSandwich.set ("0")

    #       

    if (var9.get () == 1):
        txtCheeseCake.configure (state=NORMAL)
        varCheeseCake.set ("")
    elif (var9.get () == 0):
        txtCheeseCake.configure (state=DISABLED)
        varCheeseCake.set ("0")

    if (var10.get () == 1):
        txtBrownie.configure (state=NORMAL)
        varBrownie.set ("")
    elif (var10.get () == 0):
        txtBrownie.configure (state=DISABLED)
        varBrownie.set ("0")

    if (var11.get () == 1):
        txtPudding.configure (state=NORMAL)
        varPudding.set ("")
    elif (var11.get () == 0):
        txtPudding.configure (state=DISABLED)
        varPudding.set ("0")

    if (var12.get () == 1):
        txtWaffle.configure (state=NORMAL)
        varWaffle.set ("")
    elif (var12.get () == 0):
        txtWaffle.configure (state=DISABLED)
        varWaffle.set ("0")

    if (var13.get () == 1):
        txtSundae.configure (state=NORMAL)
        varSundae.set ("")
    elif (var13.get () == 0):
        txtSundae.configure (state=DISABLED)
        varSundae.set ("0")

    #

    if (var14.get () == 1):
        txtColdDrinks.configure (state=NORMAL)
        varColdDrinks.set ("")
    elif (var14.get () == 0):
        txtColdDrinks.configure (state=DISABLED)
        varColdDrinks.set ("0")

    if (var15.get () == 1):
        txtCaffeine.configure (state=NORMAL)
        varCaffeine.set ("")
    elif (var15.get () == 0):
        txtCaffeine.configure (state=DISABLED)
        varCaffeine.set ("0")

    if (var16.get () == 1):
        txtMocktail.configure (state=NORMAL)
        varMocktail.set ("")
    elif (var16.get () == 0):
        txtMocktail.configure (state=DISABLED)
        varMocktail.set ("0")

    if (var17.get () == 1):
        txtJuices.configure (state=NORMAL)
        varJuices.set ("")
    elif (var17.get () == 0):
        txtJuices.configure (state=DISABLED)
        varJuices.set ("0")

    if (var18.get () == 1):
        txtWaterBottle.configure (state=NORMAL)
        varWaterBottle.set ("")
    elif (var18.get () == 0):
        txtWaterBottle.configure (state=DISABLED)
        varFries.set ("0")

    if (var19.get () == 1):
        txtChocolateSwirl.configure (state=NORMAL)
        varChocolateSwirl.set ("")
    elif (var19.get () == 0):
        txtChocolateSwirl.configure (state=DISABLED)
        varChocolateSwirl.set ("0")

    if (var20.get () == 1):
        txtButterscotch.configure (state=NORMAL)
        varButterscotch.set ("")
    elif (var20.get () == 0):
        txtButterscotch.configure (state=DISABLED)
        varButterscotch.set ("0")

    if (var21.get () == 1):
        txtBerryShakes.configure (state=NORMAL)
        varBerryShakes.set ("")
    elif (var21.get () == 0):
        txtBerryShakes.configure (state=DISABLED)
        varBerryShakes.set ("0")


def costofmeal():
    meal1 = int (varFries.get ())
    meal2 = int (varVegNoodles.get ())
    meal3 = int (varChickenNoodles.get ())
    meal4 = int (varVegManchurian.get ())
    meal5 = int (varChickenManchurian.get ())
    meal6 = int (varFishSandwich.get ())
    meal7 = int (varCheeseSandwich.get ())
    meal8 = int (varChickenSandwich.get ())

    meal9 = int (varCheeseCake.get ())
    meal10 = int (varBrownie.get ())
    meal11 = int (varPudding.get ())
    meal12 = int (varWaffle.get ())
    meal13 = int (varSundae.get ())

    meal14 = int (varColdDrinks.get ())
    meal15 = int (varCaffeine.get ())
    meal16 = int (varMocktail.get ())
    meal17 = int (varJuices.get ())
    meal18 = int (varWaterBottle.get ())
    meal19 = int (varChocolateSwirl.get ())
    meal20 = int (varButterscotch.get ())
    meal21 = int (varBerryShakes.get ())

    Total1 = ((meal1 * 100) + (meal2 * 120) + (meal3 * 150) + (meal4 * 120))
    Total2 = ((meal5 * 150) + (meal6 * 200) + (meal7 * 180) + (meal8 * 200))
    Total3 = ((meal9 * 250) + (meal10 * 180) + (meal11 * 150) + (meal12 * 200))
    Total4 = ((meal13 * 200) + (meal14 * 80) + (meal5 * 100) + (meal6 * 200))
    Total5 = ((meal17 * 150) + (meal18 * 50) + (meal19 * 350) + (meal20 * 300) + (meal21 * 300))
    totalcost = Total1 + Total2 + Total3 + Total4 + Total5

    if (var22.get () == "Cash"):
        SubTotal = totalcost
        varSubTotal.set (SubTotal)
        # tt=SubTotal+t1
        Tax = 30
        varTAX.set (Tax)
        tt = SubTotal + Tax
        iTotalq = "Rs.", ('%d' % tt)
        varTotal.set (iTotalq)

    elif (var22.get () == "Master Card" or var22.get () == "Debit Card" or var22.get () == "Visa Card"):
        SubTotal = totalcost
        varSubTotal.set (SubTotal)
        # tt=SubTotal+t2
        Tax = 50
        varTAX.set (Tax)
        tt = SubTotal + Tax
        iTotalq = "Rs.", ('%d' % tt)
        varTotal.set (iTotalq)


###########################f1

lblMeal = Label (f1, font=('arial', 24, 'bold'), text="\n\nFAST FOOD MEAL\t\n")
lblMeal.grid (row=0, column=0)

Fries = Checkbutton (f1, text="Fries\t\t\t\t\t\t\tRs.100", variable=var1, onvalue=1, offvalue=0,
                     font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=1, column=0, sticky=W)
txtFries = Entry (f1, font=('arial', 18, 'bold'), textvariable=varFries, width=6, justify='right', state=DISABLED)
txtFries.grid (row=1, column=1)

VegNoodles = Checkbutton (f1, text="VegNoodles\t\t\t\t\tRs.120", variable=var2, onvalue=1, offvalue=0,
                          font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=2, column=0, sticky=W)
txtVegNoodles = Entry (f1, font=('arial', 18, 'bold'), textvariable=varVegNoodles, width=6, justify='right',
                       state=DISABLED)
txtVegNoodles.grid (row=2, column=1)

ChickenNoodles = Checkbutton (f1, text="ChickenNoodles\t\t\tRs.150", variable=var3, onvalue=1, offvalue=0,
                              font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=3, column=0, sticky=W)
txtChickenNoodles = Entry (f1, font=('arial', 18, 'bold'), textvariable=varChickenNoodles, width=6, justify='right',
                           state=DISABLED)
txtChickenNoodles.grid (row=3, column=1)

VegManchurian = Checkbutton (f1, text="VegManchurian\t\t\t\tRs.120", variable=var4, onvalue=1, offvalue=0,
                             font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=4, column=0, sticky=W)
txtVegManchurian = Entry (f1, font=('arial', 18, 'bold'), textvariable=varVegManchurian, width=6, justify='right',
                          state=DISABLED)
txtVegManchurian.grid (row=4, column=1)

ChickenManchurian = Checkbutton (f1, text="ChickenManchurian\t\tRs.150", variable=var5, onvalue=1, offvalue=0,
                                 font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=5, column=0, sticky=W)
txtChickenManchurian = Entry (f1, font=('arial', 18, 'bold'), textvariable=varChickenManchurian, width=6,
                              justify='right', state=DISABLED)
txtChickenManchurian.grid (row=5, column=1)

lblSandwich = Label (f1, font=('arial', 24, 'bold'), text="\n\nSANDWICH\n")
lblSandwich.grid (row=6, column=0)

FishSandwich = Checkbutton (f1, text="FishSandwich\t\t\t\tRs.200", variable=var6, onvalue=1, offvalue=0,
                            font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=7, column=0, sticky=W)
txtFishSandwich = Entry (f1, font=('arial', 18, 'bold'), textvariable=varFishSandwich, width=6, justify='right',
                         state=DISABLED)
txtFishSandwich.grid (row=7, column=1)

CheeseSandwich = Checkbutton (f1, text="CheeseSandwich\t\t\tRs.180", variable=var7, onvalue=1, offvalue=0,
                              font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=8, column=0, sticky=W)
txtCheeseSandwich = Entry (f1, font=('arial', 18, 'bold'), textvariable=varCheeseSandwich, width=6, justify='right',
                           state=DISABLED)
txtCheeseSandwich.grid (row=8, column=1)

ChickenSandwich = Checkbutton (f1, text="ChickenSandwich\t\t\tRs.200", variable=var8, onvalue=1, offvalue=0,
                               font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=9, column=0, sticky=W)
txtChickenSandwich = Entry (f1, font=('arial', 18, 'bold'), textvariable=varChickenSandwich, width=6, justify='right',
                            state=DISABLED)
txtChickenSandwich.grid (row=9, column=1)

lblSpace = Label (f1, text="\n\n\n\n\n")
lblSpace.grid (row=10, column=0)

############################f2top

lblMeal = Label (f2TOP, font=('arial', 24, 'bold'), text="\nDESSERTS\n\n")
lblMeal.grid (row=0, column=0)

CheeseCake = Checkbutton (f2TOP, text="CheeseCake\t\tRs.250", variable=var9, onvalue=1, offvalue=0,
                          font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=1, column=0, sticky=W)
txtCheeseCake = Entry (f2TOP, font=('arial', 18, 'bold'), textvariable=varCheeseCake, width=6, justify='right',
                       state=DISABLED)
txtCheeseCake.grid (row=1, column=1)

Brownie = Checkbutton (f2TOP, text="Brownie\t\t\tRs.180", variable=var10, onvalue=1, offvalue=0,
                       font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=2, column=0, sticky=W)
txtBrownie = Entry (f2TOP, font=('arial', 18, 'bold'), textvariable=varBrownie, width=6, justify='right',
                    state=DISABLED)
txtBrownie.grid (row=2, column=1)

Pudding = Checkbutton (f2TOP, text="Pudding\t\t\tRs.150", variable=var11, onvalue=1, offvalue=0,
                       font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=3, column=0, sticky=W)
txtPudding = Entry (f2TOP, font=('arial', 18, 'bold'), textvariable=varPudding, width=6, justify='right',
                    state=DISABLED)
txtPudding.grid (row=3, column=1)
Waffle = Checkbutton (f2TOP, text="waffle\t\t\t\tRs.200", variable=var12, onvalue=1, offvalue=0,
                      font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=4, column=0, sticky=W)
txtWaffle = Entry (f2TOP, font=('arial', 18, 'bold'), textvariable=varWaffle, width=6, justify='right', state=DISABLED)
txtWaffle.grid (row=4, column=1)

Sundae = Checkbutton (f2TOP, text="sundae\t\t\tRs.200", variable=var13, onvalue=1, offvalue=0,
                      font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=5, column=0, sticky=W)
txtSundae = Entry (f2TOP, font=('arial', 18, 'bold'), textvariable=varSundae, width=6, justify='right', state=DISABLED)
txtSundae.grid (row=5, column=1)

#####################f2bottom

lblPaymemntMethod = Label (f2BOTTOM, font=('arial', 15, 'bold'), text="\n\nPAYMENT METHOD ", bd=10, width=16,
                           anchor='w')
lblPaymemntMethod.grid (row=0, column=0)

cmbPaymentMethod = ttk.Combobox (f2BOTTOM, textvariable=var22, state='readonly', font=('arial', 10, 'bold'), width=20)
cmbPaymentMethod['value'] = ('None', 'Cash', 'Master Card', 'Visa Card', 'Debit Card')
cmbPaymentMethod.current (0)
cmbPaymentMethod.grid (row=1, column=0)

lblTax = Label (f2BOTTOM, font=('arial', 14, 'bold'), text="Tax", bd=10, anchor='w')
lblTax.grid (row=1, column=1)
txtTax = Entry (f2BOTTOM, font=('arial', 18, 'bold'), textvariable=varTAX, width=6, justify='right', state=DISABLED)
txtTax.grid (row=1, column=2)

lblSubTotal = Label (f2BOTTOM, font=('arial', 14, 'bold'), text="SubTotal", bd=10, width=8, anchor='w')
lblSubTotal.grid (row=2, column=1)
txtSubTotal = Entry (f2BOTTOM, font=('arial', 18, 'bold'), textvariable=varSubTotal, width=6, justify='right',
                     state=DISABLED)
txtSubTotal.grid (row=2, column=2)

lblTotal = Label (f2BOTTOM, font=('arial', 14, 'bold'), text="TOTAL", bd=10, width=6, anchor='w')
lblTotal.grid (row=3, column=1)
txtTotal = Entry (f2BOTTOM, font=('arial', 18, 'bold'), textvariable=varTotal, width=6, justify='right', state=DISABLED)
txtTotal.grid (row=3, column=2)

###################button

btnTotal = Button (f2BOTTOM, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                   text="Total", command=costofmeal).grid (row=4, column=0)

btnReset = Button (f2BOTTOM, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                   text="Reset", command=Reset).grid (row=4, column=1)

btnExit = Button (f2BOTTOM, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                  text="Exit", command=qExit).grid (row=4, column=2)

lblspace = Label (f2BOTTOM, text="\n\n\n\n\n\n")
lblspace.grid (row=6, column=0)

######################f3


lblMeal = Label (f3, font=('arial', 24, 'bold'), text="\n\nDRINKS\n")
lblMeal.grid (row=0, column=0)

ColdDrinks = Checkbutton (f3, text="ColdDrinks\t\t\tRs.  80", variable=var14, onvalue=1, offvalue=0,
                          font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=1, column=0, sticky=W)
txtColdDrinks = Entry (f3, font=('arial', 18, 'bold'), textvariable=varColdDrinks, width=6, justify='right',
                       state=DISABLED)
txtColdDrinks.grid (row=1, column=1)

Caffeine = Checkbutton (f3, text="Caffeine\t\t\t\tRs.100", variable=var15, onvalue=1, offvalue=0,
                        font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=2, column=0, sticky=W)
txtCaffeine = Entry (f3, font=('arial', 18, 'bold'), textvariable=varCaffeine, width=6, justify='right', state=DISABLED)
txtCaffeine.grid (row=2, column=1)

Mocktail = Checkbutton (f3, text="Mocktail\t\t\t\tRs.200", variable=var16, onvalue=1, offvalue=0,
                        font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=3, column=0, sticky=W)
txtMocktail = Entry (f3, font=('arial', 18, 'bold'), textvariable=varMocktail, width=6, justify='right', state=DISABLED)
txtMocktail.grid (row=3, column=1)

Juices = Checkbutton (f3, text="Juices\t\t\t\tRs.150", variable=var17, onvalue=1, offvalue=0,
                      font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=4, column=0, sticky=W)
txtJuices = Entry (f3, font=('arial', 18, 'bold'), textvariable=varJuices, width=6, justify='right', state=DISABLED)
txtJuices.grid (row=4, column=1)

WaterBottle = Checkbutton (f3, text="WaterBottle\t\t\tRs.  50", variable=var18, onvalue=1, offvalue=0,
                           font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=5, column=0, sticky=W)
txtWaterBottle = Entry (f3, font=('arial', 18, 'bold'), textvariable=varWaterBottle, width=6, justify='right',
                        state=DISABLED)
txtWaterBottle.grid (row=5, column=1)

lblShakes = Label (f3, font=('arial', 24, 'bold'), text="\n\nSHAKES\n")
lblShakes.grid (row=6, column=0)

ChocolateSwirl = Checkbutton (f3, text="ChocolateSwirl\t\tRs.350", variable=var19, onvalue=1, offvalue=0,
                              font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=7, column=0, sticky=W)
txtChocolateSwirl = Entry (f3, font=('arial', 18, 'bold'), textvariable=varChocolateSwirl, width=6, justify='right',
                           state=DISABLED)
txtChocolateSwirl.grid (row=7, column=1)

Butterscotch = Checkbutton (f3, text="ButterScotch\t\tRs.300", variable=var20, onvalue=1, offvalue=0,
                            font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=8, column=0, sticky=W)
txtButterscotch = Entry (f3, font=('arial', 18, 'bold'), textvariable=varButterscotch, width=6, justify='right',
                         state=DISABLED)
txtButterscotch.grid (row=8, column=1)

BerryShakes = Checkbutton (f3, text="BerryShakes\t\t\tRs.300", variable=var21, onvalue=1, offvalue=0,
                           font=('arial', 18, 'bold'), command=chkbutton_value).grid (row=9, column=0, sticky=W)
txtBerryShakes = Entry (f3, font=('arial', 18, 'bold'), textvariable=varBerryShakes, width=6, justify='right',
                        state=DISABLED)
txtBerryShakes.grid (row=9, column=1)

lblSpace = Label (f3, text="\n\n\n\n\n")
lblSpace.grid (row=10, column=0)

root.mainloop ()           
