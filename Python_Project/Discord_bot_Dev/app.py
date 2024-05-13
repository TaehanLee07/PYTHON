import discord
from datetime import datetime

TOKEN = '봇 토큰'
CHANNEL_ID = 채널ID깂
 
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await self.change_presence(status=discord.Status.online, activity=discord.Game("대기중"))
 
    async def on_message(self, message):
        if message.author == self.user:
            return
 
        if message.content == 'ping':
            await message.channel.send('pong {0.author.mention}'.format(message))
        else:
            answer = self.get_answer(message.content)
            await message.channel.send(answer)
 
    def get_day_of_week(self):
        weekday_list = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
 
        weekday = weekday_list[datetime.today().weekday()]
        date = datetime.today().strftime("%Y년 %m월 %d일")
        result = '{}({})'.format(date, weekday)
        return result
 
    def get_time(self):
        return datetime.today().strftime("%H시 %M분 %S초")
 
    def get_answer(self, text):
        trim_text = text.replace(" ", "")
 
        answer_dict = {
            'cat.안녕': '고양이봇 입니다 반가워요~',
            'cat.요일': ':calendar: 오늘은 {}입니다'.format(self.get_day_of_week()),
            'cat.시간': ':clock9: 현재 시간은 {}입니다.'.format(self.get_time()),
        }
 
        if trim_text == '' or None:
            return "알 수 없는 질의입니다. 답변을 드릴 수 없습니다."
        elif trim_text in answer_dict.keys():
            return answer_dict[trim_text]
        else:
            for key in answer_dict.keys():
                if key.find(trim_text) != -1:
                    return "연관 단어 [" + key + "]에 대한 답변입니다.\n" + answer_dict[key]
 
            for key in answer_dict.keys():
                if answer_dict[key].find(text[1:]) != -1:
                    return "질문과 가장 유사한 질문 [" + key + "]에 대한 답변이에요.\n" + answer_dict[key]
 
        return text + "은(는)  없는 질문입니다."
 
 
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)
