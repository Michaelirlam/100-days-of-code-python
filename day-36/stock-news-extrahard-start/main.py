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
    """checks to see if closing stock has gone up or down and returns the correct symbol
    for use in text or message
    :params: stock_data= dictionary of key/value pairs with dates as keys and a number of trade values
    """
    dates = list(stock_data)
    close = "4. close"
    first_day_close = float(stock_data[dates[0]][close])
    second_day_close = float(stock_data[dates[1]][close])

    if first_day_close > second_day_close:
        return "🔺"
    else:
        return "🔻"

# |------------------------------------NEWS API-------------------------------------|

def get_news(company_name, api_key):
    """Fetches the latest news articles related to a company using the News API.
    :params: company_name= The name of the company to search for, api_key= API key to access the News API
    """
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

# |--------------------------------------MAIN SCRIPT-------------------------------------|

def main():
    """Main function to execute the stock news alert script."""
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