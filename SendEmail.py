import smtplib
import ssl

def SendEmail(subject, body, sender_email, receiver_email, password):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    
    # Create a default SSL context
    context = ssl.create_default_context()

    # Establish a connection to the SMTP server
    with smtplib.SMTP(smtp_server, port) as server:
        # Start TLS using the created context
        server.starttls(context=context)

        # Log in to the email account
        server.login(sender_email, password)

        # Compose the email message
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        server.sendmail(sender_email, receiver_email, message)