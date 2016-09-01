# coding: utf-8

from slackbot.bot import respond_to
from pyquery import PyQuery as pq
from datetime import datetime

def fetch_seminar(month, day):
    d = pq(url='http://research.ipmu.jp/seminar/?mode=seminar_coming')
    for table in d('table'):
        table = pq(table)
        date_text = pq(table('tr')[2])('td').text()
        splited = date_text.split(', ')
        seminar_day = datetime.strptime(', '.join(splited[:-1]), '%a, %b %d, %Y')

        if seminar_day.month == month and seminar_day.day == day:
            title = ' '.join(table.prev().text().split()[:2])
            cont = ', '.join(pq(e).text() for e in table('tr')[:3])
            yield '%s;        %s' % (title, cont)

@respond_to(r'(\d?\d)/(\d?\d)')
def check(message, month, day):
    seminars = list(fetch_seminar(int(month), int(day)))
    
    if seminars:
        message.reply(u'%d件のセミナーが見つかりました' % len(seminars))
        message.reply('\n'.join(seminars))
    else:
        message.reply(u'セミナーはありません')
