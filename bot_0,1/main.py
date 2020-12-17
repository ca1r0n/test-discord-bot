import discord
import asyncio
from discord.ext import commands
from config import settings
from handler import sql_test

bot = commands.Bot(settings['prefix'])
bot.remove_command("help")



@bot.command()
async def start(ctx):
    id_user=ctx.author.id
    if sql_test.chek_user_questions(id_user)=="Юзера нет":
        sql_test.app_new(id_user)
        await ctx.author.send(f"Вот твой вопрос: {settings['question1']}")
    elif sql_test.chek_user_questions(id_user)=="Юзер не ответил на все вопросы":
        await ctx.author.send("Закончи опрос!")
    else:
        await ctx.author.send("Ты уже ответил")

@bot.command()
async def result(ctx):
    id_user=ctx.author.id
    if sql_test.chek_user_questions(id_user)=="Юзера нет":
        await ctx.author.send(f"Чтобы начать опрос, напиши !start")
    else:
        anwers=sql_test.chek_answer(id_user)
        await ctx.author.send(f'''ответ на 1 вопрос: {anwers[0]}
ответ на 2 вопрос: {anwers[1]}
ответ на 3 вопрос: {anwers[2]}
ответ на 4 вопрос: {anwers[3]}
ответ на 5 вопрос: {anwers[4]}''')

#ответ
@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)
    if ctx.author.id!=settings['id'] and ctx.content[0]!='!':
        id_user=ctx.author.id
        if sql_test.chek_user_questions(id_user)=="Юзера нет":
            await ctx.author.send(f"Чтобы начать опрос, напиши !start")
        elif sql_test.chek_user_questions(id_user)=="Юзер уже ответил":
            await ctx.author.send("Ты уже ответил")
        elif sql_test.chek_user_questions(id_user)=="Юзер не ответил на все вопросы" and ctx.content!='!start' :
            number_question=sql_test.chek_number_question(id_user)
            if int(number_question)==0:
                await ctx.author.send(f"Вот твой вопрос: {settings['question2']}")
            elif int(number_question)==1:
                await ctx.author.send(f"Вот твой вопрос: {settings['question3']}")
            elif int(number_question)==2:
                await ctx.author.send(f"Вот твой вопрос: {settings['question4']}")
            elif int(number_question)==3:
                await ctx.author.send(f"Вот твой вопрос: {settings['question5']}")
            elif int(number_question)==4:
                await ctx.author.send(f"Спасибо за прохождение опроса!")
            sql_test.update_answer(id_user,ctx.content,int(number_question))
bot.run(settings['token'])

#url=https://discordapp.com/oauth2/authorize?&client_id={}&scope=bot&permissions=8.format(setting[id])

#TIME
#import datetime
#now_date=datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

#emb creat
#emb=discord.Embed(title='Описание системы тикетов')
#emb.add_field(name='', value="",inline=False)
#await ctx.send(embed=emb)

#Author in emb massage
#emb.set_author(name=bot.user.name,icon_url=bot.user.avatar_url)
#emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)

#Status bot(not can have custon predix)
#await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Говно из жопы"))   