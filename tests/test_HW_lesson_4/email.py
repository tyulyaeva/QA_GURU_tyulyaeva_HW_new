import math
from datetime import datetime

#1.
email = {
    "subject": "Homework, lesson 4",
    "from": "Inna@admin.com",
    "to": "Tyulyaeva@admin.com",
    "body": "Good morning, colleague!"
}

#2.
send_date = datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date
print(send_date)

#3.
email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()
print(email["from"])
print(email["to"])

#4.
login = email["from"].split("@")[0]
domain = email["from"].split("@")[1]
print(login)
print(domain)

#5.
email["short_body"] = email["body"][0:10] + '...'
print(email["short_body"])

#6.
personal_domains = [
    'gmail.com',
    'list.ru',
    'yahoo.com',
    'outlook.com',
    'hotmail.com',
    'icloud.com',
    'yandex.ru',
    'mail.ru',
    'list.ru',
    'bk.ru',
    'inbox.ru'
]
corporate_domains = [
    'company.ru',
    'corporation.com',
    'university.edu',
    'organization.org',
    'company.org',
    'business.net'
]
personal_domains = list(set(personal_domains))
corporate_domains = list(set(corporate_domains))
print(personal_domains)
print(corporate_domains)

#7.
intersection = set(personal_domains) & set(corporate_domains)
print(intersection)

#8.
sender_domain = email["from"].split("@")[1]
is_corporate = sender_domain in corporate_domains
print(f"is corporate sender: {is_corporate}")

#9.
email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")
print(email["clean_body"])

#10.
email["sent_text"] = f"""To: {email["to"]}, from {email["from"]}
Subject: {email["subject"]}, Date {email["date"]}
{email["clean_body"]}"""
print(email["sent_text"])

#11.
pages = math.ceil(len(email["sent_text"]) / 500)
print("Page count:", pages)

#12.
is_subject_empty = not email["subject"].strip()
is_body_empty = not email["body"].strip()
print("Empty email subject", is_subject_empty)
print("Empty email body", is_body_empty)

#13.
sender = email["from"]
email["masked_from"] = login[:2] + "***@" + domain
print("Sender's mask:", email["masked_from"])

#14.
if "list.ru" in personal_domains: personal_domains.remove("list.ru")
if "bk.ru" in personal_domains: personal_domains.remove("bk.ru")
print(personal_domains)