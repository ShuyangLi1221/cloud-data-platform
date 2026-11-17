import os
import smtplib
from email.message import EmailMessage

from common.logger import logger


def send_alert(subject, body):
    sender = os.getenv("ALERT_EMAIL_FROM")
    password = os.getenv("ALERT_EMAIL_PASSWORD")
    recipient = os.getenv("ALERT_EMAIL_TO")

    if not (sender and password and recipient):
        logger.warning("Alert email not configured, skipping: %s", subject)
        return

    msg = EmailMessage()
    msg["Subject"] = f"[retail-pipeline] {subject}"
    msg["From"] = sender
    msg["To"] = recipient
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
    except Exception:
        logger.exception("Failed to send alert email")