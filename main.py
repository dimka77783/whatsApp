import pywhatkit
import os

def send_message_inst():
    #  mobile = os.getenv('MOBILE')
    message = input('Введите текст сообщения: ')
    mobile = input('Введите номер получателя: ')
    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message)

def send_message():
    #  mobile = os.getenv('MOBILE')
    message = input('Введите текст сообщения: ')
    mobile = input('Введите номер получателя: ')
    hour = int(input('Веедите часы: '))
    minutes = int(input('Введите минуты: '))

    pywhatkit.sendwhatmsg(phone_no=mobile, message=message, time_hour=hour, time_min=minutes)


def main():
    # send_message_inst()
    send_message()

if __name__ == '__main__':
    main()