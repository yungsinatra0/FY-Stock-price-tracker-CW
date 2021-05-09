import yahoo_fin.stock_info as si
from datetime import date
from csv import writer
import schedule
import time

def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

list = []

def job():
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    list.append(d1)

    price_azn = si.get_live_price("azn.l") / 100
    list.append(price_azn)
    price_jet = si.get_live_price("jet.l") / 100
    list.append(price_jet)
    price_ocdo = si.get_live_price("ocdo.l") / 100
    list.append(price_ocdo)
    price_tsco = si.get_live_price("tsco.l") / 100
    list.append(price_tsco)
    price_barc = si.get_live_price("barc.l") / 100 
    list.append(price_barc)
    price_ftse = si.get_live_price("^FTSE")
    list.append(price_ftse)

    append_list_as_row("stock_price.csv", list)
    list.clear()

schedule.every().monday.at("17:00").do(job)
schedule.every().tuesday.at("17:00").do(job)
schedule.every().wednesday.at("17:00").do(job)
schedule.every().thursday.at("17:00").do(job)
schedule.every().friday.at("17:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
