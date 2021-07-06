"""APP ID :856885365524529214
Public Key :a27e021639c8c8ec1fd8735566e7472e35a5c97c619234d4538b09f368d7d16c
Token : ODU2ODg1MzY1NTI0NTI5MjE0.YNHirw.Wjncn5ikWndMCTdRBi6iH-atADc
"""

import discord
import random
import asyncio
from discord import Message
from discord.ext import commands,tasks
import random

st=0
sp=0
tdi={}
td={}
aut=""
pagei=[]
L=[]
gifsst=["https://tenor.com/view/book-worm-read-a-book-read-reading-gif-4432504","https://tenor.com/view/reading-if-i-read-fast-enough-i-can-read-more-books-kid-baby-gif-16744748","https://tenor.com/view/cat-cat-reading-allow-me-to-read-this-reading-gif-17847133","https://tenor.com/view/keep-reading-book-read-more-read-just-read-gif-15997731","https://tenor.com/view/read-read-the-book-melissa-mc-carthy-gif-9502336","https://tenor.com/view/the-more-you-read-the-smarter-you-will-get-carina-fragozo-english-in-brazil-keep-on-reading-read-up-gif-20316162"]
gifsen=["https://tenor.com/view/awesome-reaction-you-who-whos-awesome-gif-4860921","https://tenor.com/view/parks-and-rec-parks-and-recreation-ron-swanson-gif-5603552","https://tenor.com/view/pitch-perfect-comedy-rebel-wilson-crushed-it-well-done-gif-3459487"]
client=commands.Bot(command_prefix="!",case_insensitive=True)



@client.event
async def on_ready():
	print("Bot is ready")

"""@client.event
async def on_message(message) :
	global aut
	autj=""
	jd={}
	autc=""
	cd={}
	global td
	global st
	global pagei
	l=f"{message.content}".split(" ")
	print(l)
	if (("!join" in f"{message.content}") and len(l)==2) :
		pagei=l[2]
		autj=str(f"{message.author}")
		await message.channel.send(autj+" successfully joined the sprint with a starting count of "+str(pagei)+"!")
	elif (("!count" in f"{message.content}")and len(l)==2) :
		pagef=l[2]
		autc=str(f"{message.author}")
		cd[autc]=int(pagef)
		if autc in jd :
			td[autc]=cd[autc]-jd[autc]
			await message.channel.send(autc+" has read "+str(td[autc])+" in "+str(st)+" minutes!.")
			await message.channel.send("The user "+autc+" doesn't exist in the list. Please join the next sprint. Thank you!")
	else :	
		ctx = await client.get_context(message)
		await client.invoke(ctx)
	jd[autj]=int(str(pagei))
"""

"""@client.event
async def on_message(message):
	if "Please confirm" in f"{message.content}":
		await message.add_reaction('<img aria-label=":white_check_mark:" src="/assets/212e30e47232be03033a87dc58edaa95.svg" alt=":white_check_mark:" draggable="false" class="emoji jumboable">')
		await message.add_reaction('<img aria-label=":x:" src="/assets/8becd37ab9d13cdfe37c08c496a9def3.svg" alt=":x:" draggable="false" class="emoji jumboable">')
"""
	

@client.command()
async def hello(ctx):
	await ctx.channel.send(ctx.author.mention)
	print(ctx.author)

@client.command()
async def quest(ctx):
	n=random.randint(1,3)
	await ctx.send(file=discord.File(str(n)+'.png'))


@client.command(aliases=['start'])
async def _start(ctx,t1:int,t2:int):
	global st
	global sp
	st=t1*60
	sp=t2*60
	await ctx.send("A Sprint of "+str(t1)+" minutes will start in "+str(t2)+" minutes.")
	await asyncio.sleep(sp)
	await ctx.send("\n:books::books::books: **SPRINT STARTED: Duration:"+str(t1)+" minutes** :books::books::books:\nTo join the sprint, type `!join [starting word/page count]`\nTo leave the sprint, type `!leave`\n"+random.choice(gifsst))
	msg=await ctx.send("```Clock :\nTime Left - "+str(st)+"```")
	for i in range(1,st+1):
		await asyncio.sleep(1)	
		await msg.edit(content="```Clock :\nTime Left - "+str(st-i)+"```")
	
	await ctx.channel.send(ctx.author.mention)
	await ctx.send(":books::books::books: SPRINT ENDED :books::books::books:\n"+random.choice(gifsen))

@client.command(aliases=['join'])
async def _join(ctx,pg:int):
	global tdi
	global aut
	aut=str(ctx.author)
	tdi[aut]=pg
	await ctx.channel.send(ctx.author.mention)
	await ctx.send("successfully joined the sprint with a starting count of "+str(pg)+"!")
	aut=""

@client.command(aliases=['count'])
async def _count(ctx,pg:int):
	global td
	global tdi
	global st
	t=0
	if str(ctx.author) in tdi :
		td[str(ctx.author)]=pg-tdi[str(ctx.author)]
		try :
			t=td[str(ctx.author)]*60/st
		except :
			await ctx.send("Please start a sprint first!")
		td[str(ctx.author)]=t
	else :
		await ctx.send(str(ctx.author)+" has not joined the sprint. Please join the next one.")
	await ctx.send("`"+str(ctx.author)+"` has read `"+str(td[str(ctx.author)])+"` pages with the speed of `"+str(t)+"` per minute.")



	
"""@tasks.loop(seconds=10)
async def your_loop():
    
    ch = client.get_channel(856879561589391370)
    def check(msg):
        return msg.channel.id == ch.id and msg.author != client.user

    try:
        msg = await client.wait_for('message', check=check, timeout=10)
    except TimeoutError:
        await ctx.send('reminder')

your_loop.start()

@client.command(aliases=['join'])
async def _join(ctx,pgno:int):
	global pagei
	global aut
	pagei=list(str(pgno))
	await ctx.send(aut+"successfully joined the sprint with a starting count of !")
"""
"""
This is for looping timers
@tasks.loop(minutes=st)
async def called_once_a_day():
	target_channel_id = 856879561589391370
	message_channel = client.get_channel(target_channel_id)
	await message_channel.send("\n:books::books::books: **SPRINT STARTED: Duration:"+str(st)+" minutes** :books::books::books:\nTo join the sprint, type `!sprint join [starting word/page count]`\nTo leave the sprint, type `!sprint leave`\n"+random.choice(gifsst))

@called_once_a_day.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")

called_once_a_day.start()"""

client.run("ODU2ODg1MzY1NTI0NTI5MjE0.YNHirw.Wjncn5ikWndMCTdRBi6iH-atADc")
