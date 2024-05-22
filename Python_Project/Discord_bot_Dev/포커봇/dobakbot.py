import discord
import random
import asyncio
import json
import os

TOKEN = ''  # 실제 봇 토큰으로 대체하십시오.
CHANNEL_ID = 1215531550591033354
DATA_FILE = 'user_data.json'


class GambleBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_balances = {}  # 사용자 잔액을 저장하는 딕셔너리
        self.loan_amounts = {}  # 사용자가 빌린 사채 금액을 저장하는 딕셔너리
        self.load_data()

    async def setup_hook(self):
        # 비동기 초기화 작업 수행
        self.loop.create_task(self.apply_penalties())

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
                self.user_balances = data.get('balances', {})
                self.loan_amounts = data.get('loans', {})

    def save_data(self):
        with open(DATA_FILE, 'w') as f:
            json.dump({
                'balances': self.user_balances,
                'loans': self.loan_amounts
            }, f)

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

        elif message.content.startswith('포커 배율'):
            await self.show_poker_odds(message.channel)

        elif message.content.startswith('포커'):
            await self.play_poker(message)

    async def show_game_list(self, channel):
        game_list = """
        게임 목록:
        1. 포커
        """
        game_list = "\n".join(line.strip() for line in game_list.strip().split('\n'))
        await channel.send(game_list)

    async def check_balance(self, message):
        user_id = str(message.author.id)
        balance = self.user_balances.get(user_id, 1000000)  # 기본 잔액 100만 루블
        await message.channel.send(f'{message.author.name}님의 잔액은 {int(balance):,.0f} 루블입니다.')

    async def add_balance(self, message):
        try:
            parts = message.content.split()
            if len(parts) < 2:
                await message.channel.send('충전할 금액을 올바르게 입력해주세요.')
                return

            amount = int(parts[1].replace(',', ''))
            user_id = str(message.author.id)

            self.user_balances[user_id] = self.user_balances.get(user_id, 1000000) + amount
            self.save_data()
            await message.channel.send(f'{amount:,.0f} 루블이 충전되었습니다. 현재 잔액은 {self.user_balances[user_id]:,} 루블입니다.')

        except ValueError:
            await message.channel.send('충전할 금액을 올바르게 입력해주세요.')

    async def give_allowance(self, message):
        user_id = str(message.author.id)
        self.user_balances[user_id] = self.user_balances.get(user_id, 1000000) + 100000
        self.save_data()
        await message.channel.send(f'10만원이 지급되었습니다. 현재 잔액은 {self.user_balances[user_id]:,} 루블입니다.')

    async def give_sanwa_money(self, message):
        user_id = str(message.author.id)
        loan_amount = 100000000
        self.user_balances[user_id] = self.user_balances.get(user_id, 1000000) + loan_amount
        self.loan_amounts[user_id] = self.loan_amounts.get(user_id, 0) + loan_amount
        self.save_data()
        await message.channel.send(f'1억이 지급되었습니다. 현재 잔액은 {int(self.user_balances[user_id]):,.0f} 루블입니다. 그러나 조심하십시오')

        # 1분 후 첫 패널티 적용
        await asyncio.sleep(60)
        await self.apply_penalty_to_user(user_id)

    async def apply_penalty_to_user(self, user_id):
        if user_id not in self.user_balances or user_id not in self.loan_amounts:
            return

        balance = self.user_balances[user_id]
        loan_amount = self.loan_amounts[user_id]
        if loan_amount > 0:
            penalty_rate = random.uniform(0.02, 0.10)  # 2%에서 10% 사이의 랜덤한 비율
            penalty_amount = balance * penalty_rate
            self.user_balances[user_id] -= penalty_amount
            self.user_balances[user_id] = max(self.user_balances[user_id], 0)

            user = self.get_user(int(user_id))
            if user:
                await user.send(
                    f'빚으로 인해 {penalty_amount:,.0f} 루블이 차감되었습니다. 현재 잔액은 {self.user_balances[user_id]:,.0f} 루블입니다. 조심하세요!')
            else:
                print(f"사용자 {user_id}에 대한 정보를 찾을 수 없습니다.")

            if self.user_balances[user_id] >= loan_amount * 2:
                self.user_balances[user_id] -= loan_amount * 2
                self.loan_amounts[user_id] = 0
                if user:
                    await user.send(f'빚을 모두 갚으셨습니다. 남은 잔액은 {self.user_balances[user_id]:,.0f} 루블입니다.')
                else:
                    print(f"사용자 {user_id}에 대한 정보를 찾을 수 없습니다.")

            self.save_data()

    async def apply_penalties(self):
        while True:
            for user_id in list(self.user_balances.keys()):
                await self.apply_penalty_to_user(user_id)
            await asyncio.sleep(60)  # 패널티를 매 1분마다 적용

    async def play_poker(self, message):
        try:
            bet = int(message.content.split()[1].replace(',', ''))
            user_id = str(message.author.id)
            balance = self.user_balances.get(user_id, 1000000)

            if bet > balance:
                await message.channel.send('잔액이 부족합니다.')
                return

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

            self.user_balances[user_id] = balance + winnings - bet
            self.save_data()
            await message.channel.send(f'{message.author.name}님의 핸드: {result}! {winnings:,.0f} 루블을 획득했습니다!')

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
