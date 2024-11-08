import os
import requests
import smtplib
import lxml
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

smtp_address = os.getenv("SMTP_ADDRESS")
smtp_key = os.getenv("SMTP_PASSWORD")
my_email = os.getenv("MY_EMAIL")
to_email = os.getenv("TO_EMAIL")
url = ("https://www.amazon.com/Home-Edit-Organizing-Realizing-Refrigerator/dp/0525572643/ref=sr_1_1?dib="
       "eyJ2IjoiMSJ9.Zdnl0GMglUevz8q6VcLVcV_e4R9GFmh3momqSDek1q0s73aPi7CStyS0Zl3ITXuGUp7qHOJM9XCVP7wpYUUuny"
       "c3Uq6Ll9X4Hia3QzTj-Xevny05OAHshLexMqVAmwwhO6aO3WdKLCJ9Qw1DDRtID4uedM5cAwC85Lvr0zfr9rNGcaODnjtv7nHp3YA"
       "OjY0q6YB92ob-Pw-MIVYMZ_r2D6d9yqz-PO7uYMVKvMlCY4xBULaDJAGWlm0w-hpd2jYsq1qcW8aFT13y8Iqoxo7fIr5WTkkVQXJB2"
       "Pd3wp38s8w.KrjAEHmqWeSQwbcV252Ur_p0RQ0EygLFyw0kJ13hjPc"
       "&dib_tag=se&keywords=the+home+edit&qid=1731058443&sr=8-1")
max_price = 15

website_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive",
    "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"99\", \"Brave\";v=\"127\", \"Chromium\";v=\"127\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
}

website_response = requests.get(url, headers=website_headers)
website_data = website_response.text

print(website_data)

soup = BeautifulSoup(website_data, "lxml")
whole_price_tag = soup.find(class_="a-price-whole")
decimal_price_tag = soup.find(class_="a-price-fraction")
price = f"{whole_price_tag.getText()}{decimal_price_tag.getText()}"
price_number = float(price)

print(price_number)

product_tag = soup.find(id="productTitle")
product_name = product_tag.getText().split("    ")[0].strip()

if price_number < 15:
    message = (f"Subject: Amazon price alert! \n\n "
               f"{product_name} is now ${price_number}.\n{url}")
    with smtplib.SMTP(smtp_address, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=smtp_key)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)
