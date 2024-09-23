def send_email(message, recipient, *, sender="university.help@gmail.com"):

    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с {sender} на {recipient}\n")
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!\n")
        return

    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с {sender} на {recipient}\n")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с {sender} на {recipient}\n")

def is_valid_email(email):
    return "@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net"))

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')