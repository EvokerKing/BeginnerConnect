import discord
from discord.ext import bridge as cmd

intents = discord.Intents.default()
intents.message_content = True
bot = cmd.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("a game"))
    print(f'We have logged in as {bot.user}')

@bot.bridge_command()
async def request(ctx, request):
    embed = discord.Embed(colour=000, title=request)
    post = await ctx.send(embed=embed)
    await post.add_reaction("✅")
    await post.add_reaction("❎")
    await ctx.message.delete()

@bot.bridge_command()
async def ask(ctx, question, description):
    embed = discord.Embed(color=000, title=f"\"{question}\", from {ctx.author.name}", description=description)
    await ctx.send(embed=embed)
    await ctx.message.delete()

bot.run("TOKEN")
