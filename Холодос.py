import datetime as dt
from decimal import Decimal

DATE_FORMAT='%Y-%m-%d'
goods={}

def add(items,title,amount,expiration_date=None):
    if title not in items:
        items[title]=[]
    if expiration_date:
        expiration_date=dt.datetime.strptime(expiration_date,DATE_FORMAT).date()
    else:
        expiration_date=None
    list.append(items[title],{'amount':amount,'expiration_date':expiration_date})

def add_by_note(items,note):
    parts=str.split(note,' ')
    if len(str.split(parts[-1],'-'))==3:
        expiration_date=parts[-1]
        amount=Decimal(parts[-2])
        title=str.join(' ',parts[0:-2])
    else:
        expiration_date=None
        amount=Decimal(parts[-1])
        title=str.join(' ',parts[0:-1])
    add(items,title,amount,expiration_date)

def find(items,needle):
    result=[]
    for title in items:
        if needle.lower() in title.lower():
            result.append(title)
    return result

def get_amount(items,needle):
    product_amount=Decimal('0')
    for title in find(items,needle):
        for product in items[title]:
            product_amount+=product['amount']
    return product_amount

def get_expired(items,in_advance_days=0):
    result=[]
    today=dt.date.today()
    for title,parts in items.items():
        amount=Decimal('0')
        for part in parts:
            if part['expiration_date'] is not None:
                if part['expiration_date']<=today+dt.timedelta(days=in_advance_days):
                    amount+=part['amount']
        if amount>0:
            list.append(result,(title,amount))
    return result
