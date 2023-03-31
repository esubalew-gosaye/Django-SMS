## Django-SMS

Django-SMS provides a way to send SMS, OTP or some verification code to the users through your device by using as a gateway.

Inorder to achive this you need to have follow the instruction.

## Installation

1. clone the repo
- `git clone https://github.com/esubalew-gosaye/Django-SMS.git`
2. Create Virtual Environment
3. install requirements.txt file
- `pip install -r requirements.txt`
4. Download the SMS Gateway app, install and keep it active.
- [SMS-Gateway](https://drive.google.com/file/d/17odd60zAtkAZiUMvfrqK3rlyHMwHxvGw/view?usp=sharing)
- [Gateway-Manager] (https://drive.google.com/file/d/1BSwb2TTGYjdpxhfP_52bU4GN8WupqEXb/view?usp=sharing)
5. Create user on the second app
6. Modify the setting on `sms\views.py`
```
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
to = 'RECIEVER_NUMBER'
message = 'This is a test message'
```