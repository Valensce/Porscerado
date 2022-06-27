import webbot
import bruteforce
import time
import stayalive
import os
import threading

bot = webbot.Browser()


def follow(user):
    print(f'Following {user}')
    with open('following', 'r') as f:
        following = f.read().split('\n')
    for i in following:
      if user == i:
        bot.go_to(f'https://github.com/{user}?tab=following')
        bot.click('Follow', tag="button", multiple=True)
        bot.go_to(f'https://github.com/{user}?tab=followers')
        bot.click('Follow', tag="button", multiple=True)

        return
    bot.go_to(f'https://github.com/{user}')
    bot.click('Follow', tag="button")
    with open('following', 'a') as f:
        f.write(f"{user}\n")


def start():
    print('Started program')
    bot.go_to('https://github.com')


    bot.driver.add_cookie({'name': 'logged_in', 'value': 'yes'})
    bot.driver.add_cookie({
      'name': 'user_session',
      'value': os.getenv('USER_SESSION')
    })

    i = 2
    a = 0

    while True:
        time.sleep(0.50)
        if a > 50:
            a = 0
            i = i + 1
        username = bruteforce.generate_text(i)
        follow(username)
        a = a + 1

a = threading.Thread(target=start)
a.start()
