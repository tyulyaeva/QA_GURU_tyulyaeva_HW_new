from datetime import date


#1 part_a.
email = {
    "subject": "Homework, lesson 6",
    "from": "admin@admin.com",
    "to": "Tyulyaeva@admin.com",
    "body": "Good morning, colleague!"
}
def normalize_addresses(email: dict) -> dict:
    normalized_email = email.copy()
    normalized_email["from"] = email["from"].strip().lower()
    normalized_email["to"] = email["to"].strip().lower()
    return normalized_email
normalized_email = normalize_addresses(email)
print(normalized_email)

#2 part_a.
def add_short_body(email: dict) -> dict:
    short_email = email.copy()
    short_email["short_body"] = email["body"][:10] + "..."
    return short_email
email_with_short = add_short_body(email)
print(email_with_short)

#3 part_a.
def clean_body_text(body: str) -> str:
    clean_body = " ".join(body.replace("\t", " ").replace("\n", " ").split())
    return clean_body
email["clean_body"] = clean_body_text(email["body"])
print(email)

#4 part_a.
def build_sent_text(email: dict) -> str:
    sent_text = f"""To: {email["to"]}, From {email["from"]}
    Subject: {email["subject"]}, Date {email["date"]} {email["clean_body"]}"""
    return sent_text
email["date"] = "2025-11-16"
email["sent_text"] = build_sent_text(email)
print(email["sent_text"])

#5 part_a.
def check_empty_fields(email: dict) -> tuple[bool, bool]:
    is_subject_empty = not email["subject"].strip()
    is_body_empty = not email["body"].strip()
    return is_subject_empty, is_body_empty
is_subject_empty, is_body_empty = check_empty_fields(email)
print("Empty email subject:", is_subject_empty)
print("Empty email body:", is_body_empty)

#6 part_a.
def mask_sender_email(login: str, domain: str) -> str:
    masked_email_from = login[:2] + "***@" + domain
    return masked_email_from

#7 part_a.
def get_correct_email(email_list: list[str]) -> list[str]:
    valid_email = []
    valid_domain_zones = (".com", ".ru", ".net")
    for email in email_list:
        email_cleaned = email.strip().lower()
        if "@" not in email_cleaned:
            continue
        if not email_cleaned.endswith(valid_domain_zones):
            continue
        if email_cleaned.startswith("@"):
            continue
        has_valid_domain = bool(email_cleaned.split("@")[1].split(".")[0])
        if not has_valid_domain:
            continue
        valid_email.append(email)
    return valid_email

#8 part_a.
def create_email(sender: str, recipient: str, subject: str, body: str) -> dict:
    email = {"sender": sender, "recipient": recipient, "subject": subject, "body": body}
    return email

#9 part_a.
def add_send_date(email: dict) -> dict:
    send_date = date.today().strftime("%Y-%m-%d")
    email["date"] = send_date
    return email
email = {
    "sender": "admin@admin.com",
    "recipient": "Tyulyaeva@admin.com",
    "subject": "Homework, lesson 6",
    "body": "Good morning, colleague!"
}
email = add_send_date(email)
print(email)

#10 part_a.
def extract_login_domain(address: str) -> tuple[str, str]:
    login, domain = address.split("@")
    return login, domain
email = {"from": "admin@admin.com"}  # пример письма
login, domain = extract_login_domain(email["from"])
print("Sender's login:", login)
print("Sender's domain:", domain)

def build_sent_text(email: dict) -> str:
    return f"""Кому: {email['recipient']}, от {email['sender']}
Тема: {email['subject']}, дата {email['date']}
{email['clean_body']}"""


def sender_email(recipient_list: list[str], subject: str, message: str, *, sender="admin@admin.com") -> list[dict]:
#1 part_b.
    if not recipient_list:
        return []

#2 part_b.
    valid_sender = get_correct_email([sender])
    valid_recipients = get_correct_email(recipient_list)
    if not valid_sender or not valid_recipients:
        return []
    sender = valid_sender[0]

#3 part_b.
    is_subject_empty, is_body_empty = check_empty_fields({"subject": subject, "body": message})
    if is_subject_empty or is_body_empty:
        return []

#4 part_b.
    valid_recipients = [r for r in valid_recipients if r != sender]
    if not valid_recipients:
        return []

#5 part_b.
    clean_subject = clean_body_text(subject)
    clean_body = clean_body_text(message)
    emails: list[dict] = []
    for r in valid_recipients:

#6 part_b.
        email = create_email(sender=sender, recipient=r, subject=clean_subject, body=clean_body)

#7 part_b.
        email = add_send_date(email)

#8 part_b.
        login, domain = extract_login_domain(sender)
        email["masked_sender"] = mask_sender_email(login, domain)

#9 part_b.
        email = add_short_body(email)
        email["clean_body"] = clean_body

#10 part_b.
        email["sent_text"] = build_sent_text(email)
        emails.append(email)
    return emails

emails = sender_email(
    recipient_list=["admin@admin.ru", "admin@main.ru", "admin@admin.com"],
    subject="Homework, lesson 6",
    message="Good morning, colleague!",
    sender="admin@admin.com",
)
for e in emails:
    print(e["sent_text"])