import discord
import asyncio
from discord.ext import commands
from config import settings
from handler import sql_test
import handler
bot = commands.Bot(command_prefix=settings['prefix'],intents=discord.Intents.all())
bot.remove_command("help")  
@bot.event
async def on_ready():
    print('bot ready')
@bot.command()
async def top(ctx):
    top_user=sql_test.top_user(settings['limit_top'])
    if top_user==[]:
       await ctx.send(settings['no_user_in_top'])
    else:
        emb=discord.Embed(title=settings['name_table'],color=discord.Color.blue())
        n=1
        for id_user in top_user:
            user_name=bot.get_user(int(id_user[0]))
            emb.add_field(name=f"{settings['start_msg_top']} {n}",value=f'{user_name}  --  {id_user[1]}',inline=False)
            n+=1
        await ctx.send(embed=emb)
@bot.command()
async def help(ctx):
    emb=discord.Embed(title=settings['title_help'],color=discord.Color.blue())
    emb.add_field(name="!start",value=settings['value_start'],inline=False)
    emb.add_field(name="!result",value=settings['value_result'],inline=False)
    await ctx.author.send(embed=emb)
@bot.command()
async def start(ctx):
    id_user=ctx.author.id
    if sql_test.chek_user_questions(id_user)=="Юзера нет":
        sql_test.app_new(id_user,str(ctx.author.name))
        await ctx.author.send(f"{settings['start_msg_question']} \n{settings['question1']}")
    elif sql_test.chek_user_questions(id_user)=="Юзер не ответил на все вопросы":
        await ctx.author.send(settings['start_no_end_test'])
    else:
        await ctx.author.send(settings['user_already_answered'])
@bot.command()
async def start_test(ctx):
    emb=discord.Embed(title=settings['emb_msg_title'] , color=discord.Color.blue())
    emb.add_field(name=settings['emb_field_name'] , value=settings['emb_field_value'],inline=False)
    ctx = await ctx.send(embed=emb)
    emoji = bot.get_emoji(settings['emoji_id'])
    await ctx.add_reaction(emoji=emoji)
    settings['id_message_with_info']=int(ctx.id)
@bot.command()
async def result(ctx):
    id_user=ctx.author.id
    if sql_test.chek_user_questions(id_user)=="Юзера нет":
        await ctx.author.send(settings['result_no_user'])
    elif sql_test.chek_user_questions(id_user)=="Юзер не ответил на все вопросы":
        await ctx.author.send(settings['result_no_end_test'])
    else:
        await ctx.author.send(settings['result_right_answer_start']+str(sql_test.right_answer(id_user))+settings['result_right_answer_end'])
@bot.event
async def on_raw_reaction_add(payload):
    if payload.user_id != settings['id'] and payload.message_id==settings['id_message_with_info']:
        author=bot.get_user(payload.user_id)
        await author.send(settings['send_text'])
@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)
    if ctx.author.id!=settings['id'] and ctx.content[0]!='!':
        id_user=ctx.author.id
        if sql_test.chek_user_questions(id_user)=="Юзера нет":
            await ctx.author.send(settings['on_msg_no_user'])
        elif sql_test.chek_user_questions(id_user)=="Юзер уже ответил":
            await ctx.author.send(settings['om_msg_user_already_answered'])
        elif sql_test.chek_user_questions(id_user)=="Юзер не ответил на все вопросы" and ctx.content!='!start' :
            number_question=sql_test.chek_number_question(id_user)
            try:
                await ctx.author.send(f"{settings['start_msg_question']} \n{settings[f'question{int(number_question)+2}']}")
            except:
                await ctx.author.send(settings['end_test'])
            sql_test.update_answer(id_user,ctx.content,int(number_question))
bot.run(settings['token'])
