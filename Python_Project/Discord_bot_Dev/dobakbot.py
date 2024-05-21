import discord
import random
import asyncio

TOKEN = 'MTI0MDQ3NzI4MjIzNDAxMTY2MA.GOfH2d.UVDOUMsnewNWHDDAxS9rL6R0Gc92KwEPjj43hg'  # Replace with your actual bot token
CHANNEL_ID = 1215531550591033354


class GambleBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_balances = {}  # 사용자 잔액을 저장하는 딕셔너리

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('게임'):
            await self.show_game_list(message.channel)

        elif message.content.startswith('잔액 확인'):
            await self.check_balance(message)

        elif message.content.startswith('잔액 충전'):
            await self.add_balance(message)

        elif message.content.startswith('용돈줘'):
            await self.give_allowance(message)

        elif message.content.startswith('사채'):
            await self.give_sanwa_money(message)

        elif message.content.startswith('홀짝 맞추기'):
            await self.play_even_odd(message)

        elif message.content.startswith('행운의 주사위'):
            await self.play_lucky_dice(message)

        elif message.content.startswith('포커 배율'):
            await self.show_poker_odds(message.channel)

        elif message.content.startswith('포커'):
            await self.play_poker(message)

    async def show_game_list(self, channel):
        game_list = """
        게임 목록:
        1. 홀짝 맞추기
        2. 행운의 주사위
        3. 포커
        """
        game_list = "\n".join(line.strip() for line in game_list.strip().split('\n'))
        await channel.send(game_list)

    async def check_balance(self, message):
        user_id = message.author.id
        balance = self.user_balances.get(user_id, 1000000)  # 기본 잔액 100만 루블
        await message.channel.send(f'{message.author.name}님의 잔액은 {balance:,.0f} 루블입니다.')

    async def add_balance(self, message):
        try:
            parts = message.content.split()
            if len(parts) < 2:
                await message.channel.send('충전할 금액을 올바르게 입력해주세요.')
                return

            amount = int(parts[1].replace(',', ''))
            user_id = message.author.id

            self.user_balances[user_id] = self.user_balances.get(user_id, 1000000) + amount
            await message.channel.send(f'{amount:,.0f} 루블이 충전되었습니다. 현재 잔액은 {self.user_balances[user_id]:,} 루블입니다.')

        except ValueError:
            await message.channel.send('충전할 금액을 올바르게 입력해주세요.')

    async def give_allowance(self, message):
        user_id = message.author.id
        self.user_balances[user_id] = self.user_balances.get(user_id, 1000000) + 100000
        await message.channel.send(f'10만원이 지급되었습니다. 현재 잔액은 {self.user_balances[user_id]:,} 루블입니다.')

    async def give_sanwa_money(self, message):
        user_id = message.author.id
        self.user_balances[user_id] = self.user_balances.get(user_id, 1000000) + 100000000
        await message.channel.send(f'1억이 지급되었습니다. 현재 잔액은 {self.user_balances[user_id]:,} 루블입니다. 그러나 조심하십시요')

    async def play_even_odd(self, message):
        try:
            bet, choice = message.content.split()[1:3]
            bet = int(bet.replace(',', ''))
            if choice not in {'홀', '짝'}:
                await message.channel.send('홀 또는 짝을 선택해주세요.')
                return

            user_id = message.author.id
            balance = self.user_balances.get(user_id, 1000000)

            if bet > balance:
                await message.channel.send('잔액이 부족합니다.')
                return

            result = random.choice(['홀', '짝'])
            if result == choice:
                self.user_balances[user_id] = balance + bet
                await message.channel.send(f'결과: {result}! 축하합니다! {bet * 2:,.0f} 루블을 획득했습니다.')
            else:
                self.user_balances[user_id] = balance - bet
                await message.channel.send(f'결과: {result}! 아쉽네요... {bet:,.0f} 루블을 잃었습니다.')

        except (IndexError, ValueError):
            await message.channel.send('올바른 형식으로 입력해주세요. 예: "홀짝 맞추기 1000 홀"')

    async def play_lucky_dice(self, message):
        try:
            bet, choice, num = message.content.split()[1:4]
            bet = int(bet.replace(',', ''))
            num = int(num)
            if choice not in {'위', '아래'} or not (1 <= num <= 12):
                await message.channel.send('위 또는 아래를 선택하고 1에서 12 사이의 숫자를 입력해주세요.')
                return

            user_id = message.author.id
            balance = self.user_balances.get(user_id, 1000000)

            if bet > balance:
                await message.channel.send('잔액이 부족합니다.')
                return

            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            total = dice1 + dice2
            multiplier = random.randint(2, 5)

            if (choice == '위' and total > num) or (choice == '아래' and total < num):
                winnings = bet * multiplier
                self.user_balances[user_id] = balance + winnings
                await message.channel.send(f'주사위 결과: {dice1} + {dice2} = {total}! 축하합니다! {winnings:,.0f} 루블을 획득했습니다.')
            else:
                self.user_balances[user_id] = balance - bet
                await message.channel.send(f'주사위 결과: {dice1} + {dice2} = {total}! 아쉽네요... {bet:,.0f} 루블을 잃었습니다.')

        except (IndexError, ValueError):
            await message.channel.send('올바른 형식으로 입력해주세요. 예: "행운의 주사위 [위, 아래] [숫자]"')

    async def play_poker(self, message):
        try:
            bet = int(message.content.split()[1].replace(',', ''))
            user_id = message.author.id
            balance = self.user_balances.get(user_id, 1000000)

            if bet > balance:
                await message.channel.send('잔액이 부족합니다.')
                return

            # 간단한 포커 핸드 결정 (랜덤)
            hand_outcomes = [
                ("노페어", 0),
                ("원페어", 1.5),
                ("투페어", 3),
                ("플러쉬", 9),
                ("트리플", 9),
                ("풀하우스", 16),
                ("스트레이트 플러쉬", 25),
                ("백스트레이트 플러쉬", 30),
                ("포카드", 36),
                ("로얄 스트레이트 플러쉬", 999)
            ]

            result, multiplier = random.choices(hand_outcomes, weights=[40, 20, 12, 10, 10, 8, 5, 4, 2, 0.01])[0]
            winnings = bet * multiplier

            self.user_balances[user_id] = balance + winnings - bet  # 배팅 금액 차감하고 배당금 추가

            await message.channel.send(f'당신의 핸드: {result}! {winnings:,.0f} 루블을 획득했습니다!')

        except (IndexError, ValueError):
            await message.channel.send('올바른 형식으로 입력해주세요. 예: "포커 [베팅 금액]"')

    async def show_poker_odds(self, channel):
        hand_outcomes = [
            ("노페어", 0),
            ("원페어", 1.5),
            ("투페어", 3),
            ("플러쉬", 9),
            ("트리플", 9),
            ("풀하우스", 16),
            ("스트레이트 플러쉬", 25),
            ("백스트레이트 플러쉬", 25),
            ("포카드", 36),
            ("로얄 스트레이트 플러쉬", 999)
        ]

        odds_message = "포커 배율:\n"
        for hand, multiplier in hand_outcomes:
            odds_message += f"{hand}: {multiplier}배\n"

        await channel.send(odds_message)


intents = discord.Intents.default()
intents.message_content = True
client = GambleBot(intents=intents)
client.run(TOKEN)
