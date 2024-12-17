def send_email(message, recipient, *, sender="university.help@gmail.com"):
    desired_endings = [".com", ".ru", ".net"]
    if "@" not in recipient or not any(recipient.endswith(endings) for endings in desired_endings):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}. Сообщение: {message}")
        return
    if "@" not in sender or not any(sender.endswith(endings) for endings in desired_endings):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}. Сообщение: {message}")
        return
    if sender == recipient:
        print(f"Нельзя отправить письмо самому себе! Сообщение: {message}")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}. Сообщение: {message}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}. Сообщение: {message}")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
