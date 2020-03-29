# generate a paypal payment link to the user identified by "email" for "sum" amount
def CreatePayPalLink(sum, email):
    BaseUrl = "https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=EMAIL&amount=SUM&currency_code=ILS&item_name=test"
    return BaseUrl.replace("SUM", sum).replace("EMAIL", email)


#print(CreatePayPalLink("20", "oblivic90@gmail.com"))