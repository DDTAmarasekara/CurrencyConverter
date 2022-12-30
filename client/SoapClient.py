import tkinter as tk
from Conversion import Conversion



conversionService = Conversion()


def convert():
    amount = float(souresCurrencyAmount.get())
    source = sourceData.get()
    target = targetData.get()
    
    response = conversionService.convert(source,amount,target)
    targetAount = '%.5f' % response
    targetCurrencyAmount.delete(0,tk.END)
    targetCurrencyAmount.insert(0,targetAount)

r = tk.Tk()
r.title('Currency converter')
r.geometry('400x400')
r.resizable(False,False)

options = ["FJD","MXN","STD","SCR","CDF","BBD","GTQ","CLP","HNL","UGX","ZAR","TND","STN",
                "CUC","BSD","SLL","SDG","IQD","CUP","GMD","TWD","RSD","DOP","KMF","MYR","FKP","XOF",
                "GEL","BTC","UYU","MAD","CVE","TOP","AZN","OMR","PGK","KES","SEK","CNH","BTN","UAH",
                "GNF","ERN","MZN","SVC","ARS","QAR","IRR","MRO","XPD","CNY","THB","UZS","XPF","MRU",
                "BDT","LYD","BMD","KWD","PHP","XPT","RUB","PYG","ISK","JMD","COP","MKD","USD","DZD",
                "PAB","GGP","SGD","ETB","JEP","KGS","SOS","VEF","VUV","LAK","BND","XAF","LRD","XAG",
                "CHF","HRK","ALL","DJF","VES","ZMW","TZS","VND","XAU","AUD","ILS","GHS","GYD","KPW",
                "BOB","KHR","MDL","IDR","KYD","AMD","BWP","SHP","TRY","LBP","TJS","JOD","AED","HKD",
                "RWF","EUR","LSL","DKK","CAD","BGN","MMK","MUR","NOK","SYP","IMP","ZWL","GIP","RON",
                "LKR","NGN","CRC","CZK","PKR","XCD","ANG","HTG","BHD","KZT","SRD","SZL","SAR","TTD",
                "YER","MVR","AFN","INR","AWG","KRW","NPR","JPY","MNT","AOA","PLN","GBP","SBD","BYN",
                "HUF","BIF","MWK","MGA","XDR","BZD","BAM","EGP","MOP","NAD","SSP","NIO","PEN","NZD",
                "WST","TMT","CLF","BRL"]


sourceData = tk.StringVar()
sourceData.set("LKR")

targetData = tk.StringVar()
targetData.set("USD")

souresCurrencyAmount = tk.Entry(r,width = 25, font= 20)
souresCurrencyAmount.place(x=20,y=100)
# souresCurrencyAmount.pack()

souresDrop = tk.OptionMenu(r,sourceData,*options)
souresDrop.place(x=310,y=98)

targetCurrencyAmount = tk.Entry(r,width = 25, font = 20)
targetCurrencyAmount.place(x=20,y=150)
# targetCurrencyAmount.pack()

targetDrop = tk.OptionMenu(r,targetData,*options)
targetDrop.place(x=310,y=148)


button = tk.Button(r, text='Convert', width=25, command=convert)
button.place(x=108,y=280)
# button.pack()


r.mainloop()