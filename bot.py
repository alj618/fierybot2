import discord
from discord.ext import commands


client = commands.Bot( command_prefix = '.')
client.remove_command('help')

#Commands

@client.event

async def on_ready():
  print( 'Bot connected')

	await client.change_presence(status = discord.Status.online, activity = discord.Game('.help | by Fiery Science'))

@client.command( pass_context = True)
@commands.has_permissions( administrator = True)

async def clear( ctx, amount = 100 ):
	await ctx.channel.purge( limit = amount )

@client.command( pass_context = True)
@commands.has_permissions(administrator = True)

async def kick( ctx, member: discord.Member, *, reason = None):
	await ctx.channel.purge(limit = 1)

	await member.kick( reason = reason)
	await ctx.send(f"***Kicked { member.mention}***")

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def ban( ctx, member: discord.Member, *, reason = None):
	emb = discord.Embed(title = 'Ban', colour = discord.Color.red())
	await ctx.channel.purge(limit = 1)

	await member.ban( reason = reason)

	emb.set_author(name = member.name, icon_url = member.avatar_url)
	emb.add_field( name = 'Ban', value = 'Baned user : {}'.format( member.mention) )

	await ctx.send(embed = emb)


@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def unban(ctx, *, member):
	await ctx.channel.purge( limit = 1)

	banned_users = await ctx.guild.bans()

	for ban_entry in banned_users:
		user = ban_entry.user

		await ctx.guild.unban(user)
		await ctx.send(f'***Unbaned {user.mention}***')

		return

@client.command(pass_context = True)

async def help( ctx):
	emb = discord.Embed(title = 'Commands')

	emb.add_field(name = '{}clear'.format( "." ), value = 'Clear chat)
	emb.add_field(name = '{}kick'.format( "." ), value = 'Kick member')
	emb.add_field(name = '{}ban'.format( "." ), value = 'Ban member')
	emb.add_field(name = '{}unban'.format( "." ), value = 'Unban membet')
	emb.add_field(name = '{}mute'.format( "." ), value = 'Mute member')

	await ctx.send(embed = emb)

@client.command()

async def user_mute(ctx, member: discord.Member):
	await ctx.channel.purge(limit = 1)

	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'mute')

	await member.add_roles(mute_role)
	await ctx.send(f'User {member.mention} has been muted!')


# Connect

client.run('NjU2Mzg2ODAxNTE4MjQ3OTM2.XrlTEg.qjUNVdyhk_wzDSYrscd2npglulo')