"""

SEE https://matplotlib.org/users/pyplot_tutorial.html

"""

import requests
import matplotlib.pyplot as plt
from datetime import datetime

# simple plot

response = requests.get("https://api.iextrading.com/1.0/stock/aapl/batch?types=quote,news,chart&range=1m&last=10")

jsondata = response.json()

dates = []
close_values = []
for data in jsondata["chart"]:
    # Need to cover to datetime object see strptime docs
    dates.append(datetime.strptime(data["date"], "%Y-%m-%d"))
    close_values.append(data["close"])

# Plot x vs y
plt.plot(dates, close_values)
plt.ylabel('Close Price')
plt.xlabel('Date')
plt.title("Apple Stock")
plt.show()