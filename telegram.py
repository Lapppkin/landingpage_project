import requests

token = '1917377132:AAHX9W3TCLTzJLsMpUbfcWT_gYz_me1c0zI'
method = 'sendMessage'
chat_id = -543392334
text = 'Проверка связи!'

response = requests.post(
    url=f'https://api.telegram.org/bot{token}/{method}',
    data={'chat_id': chat_id, 'text': text}
).json()

print('Сообщение отправлено')