import discord
from discord.ext import commands

class Ayuda(commands.Cog):
  
  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("ayuda online")

  #Comandos del bot
  @commands.command()
  async def ayuda(self, ctx):
    embed=discord.Embed(title="Ayuda",  description="A continuación se muestran los multisummons diponibles", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name,  icon_url=ctx.author.avatar_url)
    embed.add_field(name="!multicarnival (Dragon stones)", value="Multisummon de carnival dokkan", inline=False)
    embed.add_field(name="!multicooler (Dragon stones)", value="Multisummon de cooler LR", inline=False)
    embed.add_field(name="!multidokkan1 (Dragon stones)", value="Multisummon de campaña mundial 1", inline=False)
    embed.add_field(name="!multidokkan2 (Dragon stones)", value="Multisummon de campaña mundial 2", inline=False)
    embed.add_field(name="!tqmovies (Tiquets)", value="Summon de tiquets de dragon ball super: super hero", inline=False)
    embed.add_field(name="!tqdokkan1 (Tiquets)", value="Summon de tiquets de campaña mundial 1", inline=False)
    embed.add_field(name="!tqdokkan2 (Tiquets)", value="Summon de tiquets de campaña mundial 2", inline=False)

    embed.set_footer(text="Muchas gracias por usar el bot!")
    await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Ayuda(client))