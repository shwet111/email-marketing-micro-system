from personalization import render_template
from rotation import get_next_domain
from db import save_email_status

counter = 0

def send_email(user_data):
    global counter

    domain = get_next_domain(counter)
    counter += 1

    content = render_template(user_data)

    # Simulate email sending
    print("----- EMAIL SENT -----")
    print("To:", user_data["email"])
    print("From:", f"no-reply@{domain}")
    print("Content:", content)
    print("----------------------")

    save_email_status(user_data["email"], "sent")