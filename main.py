import discord
import asyncio
import os
import re
from replit import db
from keep_alive import keep_alive

# 代理:如果希望通过代理连接discord服务器，可以设置括号里的内容
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


# 在“Console”中显示机器人已登录
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    # 展示 `Playing XXX` 状态
    custom_activity = discord.Game('JohnBot | k!help')
    await client.change_presence(status=discord.Status.online,
                                 activity=custom_activity)


# 帮助:需要帮助时发送的消息
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('k!help'):
        await message.channel.send('需要帮助？...这里的代码还没写（')

# 返回at机器人的消息
    elif client.user.mentioned_in(message):
        trim_mentioned_msg = re.sub("<@!?(\d+)>", "", message.content).strip()
        await message.channel.send(
            f"{message.author.mention} Hey!I'm JohnBot!")
    else:
        print("Do nothing with message: %s" % message.content)

    # ping/pong测试，然后删除测试消息
    if message.content == 'k!ping':
        tmp_msg = await message.channel.send('pong')
        await asyncio.sleep(3)
        await tmp_msg.delete()
        await message.delete()

keep_alive()
client.run(os.getenv("bot_token"))
