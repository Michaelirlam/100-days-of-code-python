import requests
import os
import smtplib

# |-------------------------------------STOCK API---------------------------------|

# Stock API response and data using https://www.alphavantage.co
def get_stock_data(symbol, api_key):
    """performs an api call to the alpha advantage api and returns a dictionary of stock data with dates as keys
    :params: symbol= The name of the equity to pull, api_key= API key to access the API
    """
    url = "https://www.alphavantage.co/query",
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": api_key,
        "outputsize": "compact",
    }
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("Time Series (Daily)", {})

# Calculates the percentage difference of the closing stock for the past two trading days
def calculate_percentage_change(stock_data):
    """Returns the percentage difference for the closin stock for the past two days of trade
    :params: stock_data= dictionary of key/value pairs with dates as keys and a number of trade values
    """
    dates = list(stock_data)
    close = "4. close"
    first_day_close = float(stock_data[dates[0]][close])
    second_day_close = float(stock_data[dates[1]][close])
    return abs(first_day_close - second_day_close) / second_day_close * 100

def check_up_or_down(stock_data):
    dates = list(stock_data)
    close = "4. close"
    first_day_close = float(stock_data[dates[0]][close])
    second_day_close = float(stock_data[dates[1]][close])

    if first_day_close > second_day_close:
        return "🔺"
    else:
        return "🔻"
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# |------------------------------------NEWS API-------------------------------------|

def get_news(company_name, api_key):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": company_name,
        "apiKey": api_key,
        "sortBy": "publishedAt"
    }
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    news_data = response.json()
    return news_data.get("articles", [])[:3]

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def main():
    alpha_vantage_api_key = os.environ["ALPHA_API_KEY"]
    news_api_key = os.environ["NEWS_API_KEY"]
    STOCK = "TSLA"
    COMPANY_NAME = "Tesla Inc"
    sender_email = os.environ["SENDER_EMAIL"]
    sender_password = os.environ["SENDER_PASSWORD"]
    recipient_email = os.environ["RECIPIENT_EMAIL"]

    stock_data = get_stock_data(STOCK, alpha_vantage_api_key)
    if not stock_data:
        print("Stock API error or rate limit reached.")
        return

    percentage_change = calculate_percentage_change(stock_data)
    up_or_down = check_up_or_down(stock_data)
    if percentage_change >= 5:
        articles = get_news(COMPANY_NAME, news_api_key)
        message_body = f"{STOCK}: {up_or_down}{percentage_change:.2f}%\n\n"
        for article in articles:
            message_body += f"Headline: {article['title']}\nBrief: {article['description']}\n\n"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=sender_password)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=recipient_email,
                msg=f"Subject:\n{STOCK} {up_or_down}{percentage_change:.2f}%: \n\n{message_body}"
            )

if __name__ == "__main__":
    main()

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

