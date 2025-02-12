from datetime import date , timedelta
today = date.today()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1) 
print("Yesterday:", yesterday.strftime("%A"))
print("Today:" ,today.strftime("%A"))
print("Tomorrow:", tomorrow.strftime("%A"))