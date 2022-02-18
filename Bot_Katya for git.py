#Подключение необходимых модулей
import sys
import random
import datetime
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


#Ввод актуального токена и id группы для авторизации (желательно подключить файл с данными)
token = token
group = group


#Авторизация "Вконтакте" как сообщество
vk_session=vk_api.VkApi(token=token)
print('vk_session')
vk_session._auth_token()
print('auth_token()')
# Работа с сообщениями
longpoll=VkBotLongPoll(vk_session, group)
print('longpoll')
vk=vk_session.get_api()
print('get_api()')


#Переменные для счётчика сообщений (желательно сделать функцией)
i=random.randint(1, 10)
n=0


#Функция определения учебной недели
def whatWeek():
    now=datetime.datetime.now()
    sep=datetime.date(now.year,9,1)
    ye,we,dow=sep.isocalendar()
    if (we%2)==0:
        now2=datetime.datetime.now()
        ye2,we2,dow2=now2.isocalendar()
        if dow==7:
            if (we2%2)==0:
                vk.messages.send(chat_id=chat_id, message='Нижняя', random_id=random_id)
            else:
                vk.messages.send(chat_id=chat_id, message='Верхняя', random_id=random_id)
        else:
            if (we2%2)==0:
                vk.messages.send(chat_id=chat_id, message='Верхняя', random_id=random_id)
            else:
                vk.messages.send(chat_id=chat_id, message='Нижняя', random_id=random_id)
    else:
        now2=datetime.datetime.now()
        ye2,we2,dow2=now2.isocalendar()
        if dow==7:
            if (we2%2)==0:
                vk.messages.send(chat_id=chat_id, message='Верхняя', random_id=random_id)
            else:
                vk.messages.send(chat_id=chat_id, message='Нижняя', random_id=random_id)
        else:
            if (we2%2)==0:
                vk.messages.send(chat_id=chat_id, message='Нижняя', random_id=random_id)
            else:
                vk.messages.send(chat_id=chat_id, message='Верхняя', random_id=random_id)


#Основной цикл
while True:
    for event in longpoll.listen():
        if event.type==VkBotEventType.MESSAGE_NEW:
            #Работа с чатами
            if event.from_chat:
                print(event.object)
                print('\nНовое сообщение')
                print(datetime.datetime.date(datetime.datetime.now()).strftime("%d.%m.%y"))
                print(datetime.datetime.time(datetime.datetime.now()).strftime("%H:%M:%S"))
                print('chat_id:',event.chat_id)
                print('user_id:',event.object.from_id)
                print('message:',event.object.text)
                chat_id=event.chat_id
                random_id=vk_api.utils.get_random_id()
                #Работа с пользователями
                #Триггер на сообщения пользователей, рандомный выбор ответа (текст/картинка)
                if event.object.from_id==268609423 or event.object.from_id==125672811:
                    choice=random.choice(['message','attachment'])
                    if choice=='attachment':
                        attachment=random.choice(['photo-200293568_457239022','photo-200293568_457239023','photo-200293568_457239025','photo-200293568_457239026',
                                                  'photo-200293568_457239027', 'photo-200293568_457239028','photo-200293568_457239029'])
                        #Триггер на пересланные сообщения/запись на стене (ответ - картинка)
                        if event.object.fwd_messages:
                            vk.messages.send(chat_id=chat_id, attachment=attachment, random_id=random_id)
                        for e in event.object.attachments:
                            if e['type']=='wall':
                                vk.messages.send(chat_id=chat_id, attachment=attachment, random_id=random_id)
                    else:
                         message=random.choice(['мм, хуета','ебать привет','каво','кавоооооо','скипай','скипай нахуй','ну и дерьмо','ливай','го в академ',
                                                ':)','эта важна','ВАЖНО!','не прочитаешь - тебе пизда','шо','шоооооо','че тебе надо','иди своей дорогой, стакер',
                                                'ну и зачем это здесь?','а?','a?!','aaaaaaaaaaaaaaaa','!?','а я говорил, вам это не надо','ы'])
                         #Триггер на пересланные сообщения/запись на стене (ответ - текст)
                         if event.object.fwd_messages:
                            vk.messages.send(chat_id=chat_id, message=message, random_id=random_id)
                         for e in event.object.attachments:
                            if e['type']=='wall':
                                vk.messages.send(chat_id=chat_id, message=message, random_id=random_id)
                #Триггер на пользователя, счетчик его сообщений (по достижению n-счетчиком определенного значения, отправляется сообщение)
                if event.object.from_id==127804475:
                    attachment='photo-200293568_457239024'
                    n+=1
                    print('текущий номер:', n)
                    print('номер срабатывания:', i)
                    if n==i:
                        vk.messages.send(chat_id=chat_id, attachment=attachment, random_id=random_id)
                        i=random.randint(1, 10)
                        n=0
                #Триггер на пределенного пользователя в определенном чате, отсутствует кулдаун (триггер происходит на каждое сообщение)
                if event.chat_id==2:
                    if event.object.from_id==149046462:
                        message=random.choice(['Олег, ты попался','Олег лох', 'Олег :)', 'Ты пытался, Олег', 'Привет, Олег)'])
                        vk.messages.send(chat_id=chat_id, message=message, random_id=random_id+3)
                #Работа с текстом
                #Триггеры на определенные команды/слова в сообщениях
                if event.object.text:
                    response=event.object.text.lower()
                    if response=='да':
                        vk.messages.send(chat_id=chat_id, message='пизда', random_id=random_id+1)
                        vk.messages.send(chat_id=chat_id, message=')', random_id=random_id+2) 
                    if response=='бот, неделя' or response=='/неделя' or response=='/week':
                        whatWeek()
                    if response=='/roll':
                        message=random.randint(0, 100)
                        if message==69:
                            attachment='photo-200293568_457239030'
                            vk.messages.send(chat_id=chat_id, message=message, attachment=attachment, random_id=random_id+1)
                        else:
                            vk.messages.send(chat_id=chat_id, message=message, random_id=random_id+1)
                    if response=='/flip':
                        message=random.choice(['Орёл', 'Решка'])
                        vk.messages.send(chat_id=chat_id, message=message, random_id=random_id+1)
                    if response=='/pic':
                        attachment=random.choice(['photo-200293568_457239022','photo-200293568_457239023','photo-200293568_457239025','photo-200293568_457239026',
                                                  'photo-200293568_457239027', 'photo-200293568_457239028','photo-200293568_457239029'])
                        vk.messages.send(chat_id=chat_id, attachment=attachment, random_id=random_id+1)
                    if 'олег' in response.split(' '):
                        vk.messages.send(chat_id=chat_id, message='Хорошая работа, Олег!', random_id=random_id)
                    if response=='бот, умри' or response=='бот, спать':
                        if event.object.from_id==268609423:
                            vk.messages.send(chat_id=chat_id, message='пока(', random_id=random_id)
                            sys.exit()
                        else:
                            vk.messages.send(chat_id=chat_id, message='наивный :)', random_id=random_id)
                    if 'спасибо' in response.split(' '):
                        message=random.choice(['пожалуйста','не за что','обращайся','за свою улётность денег не беру','но проблем бро',])
                        vk.messages.send(chat_id=chat_id, message=message, random_id=random_id)
