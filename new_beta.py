import discord
from discord.ext import commands
from discord import Option
bot = commands.Bot()
import asyncio
staff = 943986930314530847
token = ""

"""@bot.event
async def on_ready():
	user =
    channel = bot.get_channel('1000146340841521162')
    role = discord.utils.get(user.server.roles, name="Whitelisted")
    message = await bot.send_message(channel, "React to me to get your whitelist!")
    while True:
        reaction = await bot.wait_for_reaction(emoji="🟢", message=message)
        await bot.add_roles(reaction.message.author, role)"""


@bot.event
async def on_ready():
	print("ready")












def add_warn(username):
	j = str(username)
	with open("warns.txt","r") as warns:
		data = warns.readlines()
	x = 0
	print("going in")
	for warn in data:
		print("gor in")
		if j in warn:
			print("1")
			warn = warn.rstrip()
			print("2")
			go = warn.split(":")
			print("3")
			go[1] = str(int(go[1])+1)
			print("4")
			ga = ''.join(go[0] + ":" +go[1])
			print("5")
			ga.replace(" ","")
			print("6")
			ga = ga + "\n"
			print("7")
			data[x] = ga + "\n"
			print("8")
			with open("warns.txt","w") as file:
				print("9")
				file.writelines(data)
				print("done")
				return
		else:
			x =+ 1
	h = str(username)
	print("not in")
	with open("warns.txt","a") as warns:
		print("10")
		warns.writelines( h + ":1" + "\n")
def check_warn(username):
  with open("warns.txt","r") as warns:
  	print("1")
  	data = warns.readlines()
  print("goin ins")
  for warn in data:
  	print("2")
  	if str(username) in warn:
  		print("3")
  		warn = warn.rstrip()
  		print("4")
  		go = warn.split(":")
  		print("5")
  		print(go[1])
  		print("6")
  		return(str(go[1]))
  	else:
  		print("pass")
  		pass
  print("no")
  return "no"
def rm_warn(username):
	h = str(username)
	print("1")
	with open("warns.txt","r") as warns:
		print("2")
		data = warns.readlines()
	x = 0
	print("GOIN IN")
	for warn in data:
		print("3")
		if h in warn:
			print("4")
			warn = warn.rstrip()
			print("5")
			go = warn.split(":")
			print("6")
			if int(go[1]) <= 1:
				print("7")
				ga = ""
				print("8")
				data[x] = ga
				print("9")
				with open("warns.txt","w") as file:
					print("10")
					file.writelines(data)
					print("11")
					return
			else:
				print("ELSE")
				j = go[0] + ":"+str(int(go[1]) - 1)
				print("12")
				data[x] = j
				print("13")
				with open("warns.txt","w") as file:
					print("14")
					file.writelines(data)
					print("done")
					return

		else:
			print("nop")
	print("noop")
	return "nop"




"""@commands.has_permissions(administrator = True)"""
@bot.slash_command(description="debug")
async def debug(ctx):
	await ctx.respond("hello")


"""@commands.has_permissions(administrator=True)"""
@commands.has_role(staff)
@bot.slash_command(description="whitelist someone")
async def whitelist(ctx,user: Option(discord.Member,"the person to whitelist",required=True,default=None)):
	mention = ctx.author.mention
	member = user
	role = discord.utils.get(ctx.guild.roles, name="WHITELISTED")
	await member.add_roles(role)

	embed=discord.Embed(title="Success", description=f"**you have succesfully whitelisted **{user.mention}", color=0xc0b423)
	await ctx.respond(embed=embed, delete_after=5)


	embed= discord.Embed(
			title="WHITELIST:",
			color=0xc0b423
		)
	embed.add_field(name='WHITELISTER:',value=f"{mention}",inline=True)
	embed.add_field(name='WHITELISTED:',value=f"{user.mention}",inline=True)
	embed.add_field(name=' ‏‏‎',value="**Welcome to TUNISIAN ELITE ROLE PLAY**",inline=False)
	embed.set_author(name=user.name,icon_url=user.avatar.url)
	embed.set_thumbnail(url=user.display_avatar.url)
	embed.set_image(url="https://cdn.discordapp.com/attachments/983054815594700920/1000022850117304432/X.png")


	"""embeds=discord.Embed(title="WHITELISTED",description=f"{user.mention} **got whitelisted by ‏‏‎{mention}\nwe hope you will enjoy your whitelist**", color=0x00b6ff)"""
	channel = bot.get_channel(1000546285855703060)
	await channel.send(embed=embed)
    
	 
@whitelist.error
async def whitelist_error(ctx,error):
	mention = ctx.author.mention
	if isinstance(error, commands.MissingRole):
		embed=discord.Embed(title="ERROR", description=f"**{mention} you do not have the role to whitelist**", color=0xc0b423)
		await ctx.respond(embed=embed, delete_after=5)

@commands.has_permissions(kick_members = True)
@bot.slash_command(description="ban someone")
async def ban(ctx,user: Option(discord.Member,"the person to ban",required=True,default=None),duration: Option(int,"the duration of the ban (hours)",required=True,default="No reason"),reason: Option(str,"the reason of the ban",required=False,default="No reason")):
	print("1")
	durations = str(int(duration) * 3600)
	role = discord.utils.get(ctx.guild.roles, name="📛┊Banned")
	whitelist_role = discord.utils.get(ctx.guild.roles, name="WHITELISTED")
	mention = ctx.author.mention
	auth = ctx.author
	print("2")

	embeds= discord.Embed(
			title="PUNICHEMENT:",
			color=0xc0b423
		)
	embeds.add_field(name='PUNICHER:',value=f"{mention}",inline=True)
	embeds.add_field(name='TARGET:',value=f"{user.mention}",inline=True)
	embeds.add_field(name='PUNICHEMENT TYPE:',value="`  BLACKLISTED  `",inline=False)
	embeds.add_field(name='REASON:',value=f"{reason}",inline=False)
	embeds.add_field(name='DURATION:',value=f"{str(duration)} hour(s)",inline=False)
	embeds.set_author(name=auth.name,icon_url=auth.avatar.url)
	embeds.set_thumbnail(url=user.display_avatar.url)
	embeds.set_image(url="https://cdn.discordapp.com/attachments/983054815594700920/1000022850117304432/X.png")
	print("embed")
	try:
		print("1")
		await user.remove_roles(whitelist_role)
		print("removed role")
		await user.add_roles(role)
		print("blacklisted role")
	except:
		print("2")
		await user.add_roles(role)
		print("new blacklisted role")

	embed=discord.Embed(title="Success", description=f"**you have succesfully banned {user.mention} for reason:\n**{reason}", color=0xc0b423)
	#embeds=discord.Embed(title="PUNICHEMENT",description=f" ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ \n**PUNICHER**:  {mention}\n\n**PUNICHEMENT TYPE**: `  BAN  `\n\n**TARGET**:  {user.mention}\n\n**REASON**:  {reason}", color=0x000000)
	await ctx.respond(embed=embed, delete_after=5)
	channel = bot.get_channel(943987113324576778)
	await channel.send(embed=embeds)

	await asyncio.sleep(durations)
	await user.remove_roles(role)
	await user.add_roles(whitelist_role)


	


		

@ban.error
async def ban_error(ctx,error):
	mention = ctx.author.mention
	if isinstance(error, commands.MissingPermissions):
		embed=discord.Embed(title="ERROR", description=f"**you do not have the pemission to ban**", color=0xc0b423)
		await ctx.respond(embed=embed, delete_after=5)

@commands.has_permissions(kick_members = True)
@bot.slash_command(description="unban someone")
async def unban(ctx,user: Option(discord.Member,"the person to unban",required=True,default=None),reason: Option(str,"the reason of the unban",required=False,default="No reason")):
	role = discord.utils.get(ctx.guild.roles, name="📛┊Banned")
	mention = ctx.author.mention
	await user.remove_roles(role)

	embed=discord.Embed(title="Success", description=f"**you have succesfully revoked the ban from {user.mention} for reason:\n**{reason}", color=0xc0b423)
	await ctx.respond(embed=embed, delete_after=5)


	embeds= discord.Embed(
			title="REVOKE:",
			color=0xc0b423
		)
	embeds.add_field(name='REVOKER:',value=f"{mention}",inline=True)
	embeds.add_field(name='USER:',value=f"{user.mention}",inline=True)
	embeds.add_field(name='REVOKED From:',value=f"BAN",inline=False)
	embeds.add_field(name='REASON:',value=f"**{reason}**",inline=False)
	embeds.set_author(name=user.name,icon_url=user.avatar.url)
	embeds.set_thumbnail(url=user.display_avatar.url)
	embeds.set_image(url="https://cdn.discordapp.com/attachments/983054815594700920/1000022850117304432/X.png")


	#embeds=discord.Embed(title="REVOKE",description=f" ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ \n**REVOKER**:  {mention}\n\n**REVOKED FROM**: `  BAN  `\n\n**TARGET**:  {user.mention}\n\n**REASON**:  {reason}", color=0x00b6ff)
	channel = bot.get_channel(1000547091250159616)
	await channel.send(embed=embeds)
	
@unban.error
async def unban_error(ctx,error):
	mention = ctx.author.mention
	if isinstance(error, commands.MissingPermissions):
		embed=discord.Embed(title="ERROR", description=f"**you do not have the permission to unban**", color=0xc0b423)
		await ctx.respond(embed=embed, delete_after=5)

@commands.has_permissions(kick_members = True)
@bot.slash_command(description="warn someone")
async def warn(ctx,user: Option(discord.Member,"the person to warn",required=True,default=None),reason: Option(str,"the reason of the warn",required=False,default="No reason")):
	member = user
	channel = bot.get_channel(943987111722360944)
	role = discord.utils.get(ctx.guild.roles, name="📛┊Banned")
	whitelist_role = discord.utils.get(ctx.guild.roles, name="WHITELISTED")
	mention = ctx.author.mention
	add_warn(user)
	if check_warn(user) == "3":
		print("3!!!!")
		await member.add_roles(role)
		await member.remove_roles(whitelist_role)
		embed=discord.Embed(title="Success", description=f"**{user.mention} is now blacklisted for reason:\n**{reason}", color=0xc0b423)
		await ctx.respond(embed=embed, delete_after=5)

		embeds= discord.Embed(
			title="PUNICHEMENT:",
			color=0xc0b423
		)
		embeds.add_field(name='PUNICHER:',value=f"{mention}",inline=True)
		embeds.add_field(name='PUNICHED:',value=f"{user.mention}",inline=True)
		embeds.add_field(name='PUNICHEMENT TYPE:',value=f"BLACKLIST",inline=False)
		embeds.add_field(name='ENDING IN:',value=f"3 days",inline=False)
		embeds.add_field(name='REASON:',value=f"**{reason}**",inline=False)
		embeds.set_author(name=user.name,icon_url=user.avatar.url)
		embeds.set_thumbnail(url=user.display_avatar.url)
		embeds.set_image(url="https://cdn.discordapp.com/attachments/983054815594700920/1000022850117304432/X.png")


		#embeds=discord.Embed(title="BLACKLIST",description=f" ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ \n**PUNICHER**:  {mention}\n\n**PUNICHEMENT TYPE**: `  BLACKLIST  `\n\n**TARGET**:  {user.mention}\n\n**REASON**:  {reason}", color=0xff0000)
		await channel.send(embed=embeds)
		print("waiting")
		await asyncio.sleep(259200)
		print("removing role")
		await member.remove_roles(role)
		await member.add_roles(whitelist_role)
		rm_warn(user)
		print("role removed")
	else:
		embed=discord.Embed(title="Success", description=f"**you have succesfully warned {user.mention} for reason:\n**{reason}", color=0xc0b423)
		await ctx.respond(embed=embed, delete_after=5)
		embeds= discord.Embed(
			title="PUNICHEMENT:",
			color=0xc0b423
		)
		embeds.add_field(name='PUNICHER:',value=f"{mention}",inline=True)
		embeds.add_field(name='PUNICHED:',value=f"{user.mention}",inline=True)
		embeds.add_field(name='PUNICHEMENT TYPE:',value=f"WARN",inline=False)
		embeds.add_field(name='REASON:',value=f"**{reason}**",inline=False)
		embeds.set_author(name=user.name,icon_url=user.avatar.url)
		embeds.set_thumbnail(url=user.display_avatar.url)
		embeds.set_image(url="https://cdn.discordapp.com/attachments/983054815594700920/1000022850117304432/X.png")

		#embeds=discord.Embed(title="WARN",description=f" ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ \n**PUNICHER**:  {mention}\n\n**PUNICHEMENT TYPE**: `  WARN  `\n\n**TARGET**:  {user.mention}\n\n**REASON**:  {reason}", color=0xff0000)
		await channel.send(embed=embeds)

@warn.error
async def warn_error(ctx,error):
	mention = ctx.author.mention
	if isinstance(error, commands.MissingPermissions):
		embed=discord.Embed(title="ERROR", description=f"**you do not have the permission to warn**", color=0xc0b423)
		await ctx.respond(embed=embed, delete_after=5)






@commands.has_permissions(kick_members = True)
@bot.slash_command(description="unwarn someone")
async def unwarn(ctx,user: Option(discord.Member,"the person to unwarn",required=True,default=None),reason: Option(str,"the reason of the unwarn",required=False,default="No reason")):
	member = user
	
	role = discord.utils.get(ctx.guild.roles, name="Blacklisted")
	
	mention = ctx.author.mention

	if check_warn(user) == "3":
		rm_warn(user)
		await member.remove_roles(role)
		embed=discord.Embed(title="Success", description=f"**{user.mention} is now out of blacklist for reason:\n**{reason}", color=0xc0b423)
		await ctx.respond(embed=embed, delete_after=5)
		channel = bot.get_channel(1000547091250159616)

		embeds= discord.Embed(
									title="REVOKE:",
									color=0xc0b423
								)
		embeds.add_field(name='REVOKER:',value=f"{mention}",inline=True)
		embeds.add_field(name='USER:',value=f"{user.mention}",inline=True)
		embeds.add_field(name='REVOKED From:',value=f"WARN",inline=False)
		embeds.add_field(name='REASON:',value=f"**{reason}**",inline=False)
		embeds.set_author(name=user.name,icon_url=user.avatar.url)
		embeds.set_thumbnail(url=user.display_avatar.url)
		embeds.set_image(url="https://cdn.discordapp.com/attachments/983054815594700920/1000022850117304432/X.png")

		#embeds=discord.Embed(title="REVOKE",description=f" ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ \n**REVOKER**:  {mention}\n\n**REVOKED FROM **: `  WARN  `\n\n**USER**:  {user.mention}\n\n**REASON**:  {reason}", color=0xff0000)
		await channel.send(embed=embeds)
		return
	else:
		rm_warn(user)
		embed=discord.Embed(title="Success", description=f"**you have succesfully unwarned {user.mention} for reason:\n**{reason}", color=0xc0b423)
		await ctx.respond(embed=embed, delete_after=5)
		embeds= discord.Embed(
									title="REVOKE:",
									color=0xc0b423
								)
		embeds.add_field(name='REVOKER:',value=f"{mention}",inline=True)
		embeds.add_field(name='USER:',value=f"{user.mention}",inline=True)
		embeds.add_field(name='REVOKED From:',value=f"WARN",inline=False)
		embeds.add_field(name='REASON:',value=f"**{reason}**",inline=False)
		embeds.set_author(name=user.name,icon_url=user.avatar.url)
		embeds.set_thumbnail(url=user.display_avatar.url)
		embeds.set_image(url="https://cdn.discordapp.com/attachments/983054815594700920/1000022850117304432/X.png")



		#embeds=discord.Embed(title="REVOKE",description=f" ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ \n**REVOKER**:  {mention}\n\n**REMOVED**: `  1 WARN  `\n\n**USER**:  {user.mention}\n\n**REASON**:  {reason}", color=0x00b6ff)
		channel = bot.get_channel(1000547091250159616)
		await channel.send(embed=embeds)
	


	
@unwarn.error
async def unwarn_error(ctx,error):
	mention = ctx.author.mention
	if isinstance(error, commands.MissingPermissions):
		embed=discord.Embed(title="ERROR", description=f"**you do not have the permission to unwarn**", color=0xc0b423)
		await ctx.respond(embed=embed, delete_after=5)



@bot.slash_command(description="check how many warns the user have")
async def warn_check(ctx,user: Option(discord.Member,"the person that you want to check warns",required=True,default=None)):

	a = check_warn(user)

	embed=discord.Embed(title=f"{user.name}", description=f"**{user.mention}has actually {a} warn(s)**", color=0xc0b423)
	await ctx.respond(embed=embed, delete_after=20)

    
    



bot.run(token)