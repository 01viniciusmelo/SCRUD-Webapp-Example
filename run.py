#!venv/bin/python3

#enter the command below in terminal to start smtp server if debugging is off.
# (flask) Phils-iMac:microblog Phil$ sudo python3 -m smtpd -n -c DebuggingServer localhost:25
from app import app

app.run(host='127.0.0.1', port=5032)
