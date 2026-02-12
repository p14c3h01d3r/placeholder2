import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='|', intents=intents)
@bot.event
async def on_ready():
    print(f'You have logged in as {bot.user}')
@bot.command()
async def mem1(ctx):
    with open('images/meme1.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)
@bot.command()
async def mem2(ctx):
    with open('images/meme2.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)
@bot.command()
async def mem3(ctx):
    with open('images/meme3.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)
@bot.command()
async def city(ctx):
    with open('images/city.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("Gunakan command |city_info untuk mengetahui lebih jauh!")
@bot.command()
async def city_info(ctx):
    await ctx.send("Kota telah dihancurkan oleh para penjahat, tetapi anda dapat membenarkannya. Gunakan command |save_city untuk menyelamatkan kota!")
@bot.command()
async def save_city(ctx):
    with open('images/citysaved.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
bot.run("insert bot token here")
