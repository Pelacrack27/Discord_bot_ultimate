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
    embed.add_field(name="!multimonos (Dragon stones)", value="Multisummon de goku y vegeta ssj4 septimo aniversario", inline=False)
    embed.add_field(name="!multigods (Dragon stones)", value="Multisummon de goku y vegeta ssj god septimo aniversario", inline=False)
    embed.add_field(name="!multizdokkan (Dragon stones)", value="Multisummon de extreme z battle", inline=False)
    embed.add_field(name="!multikaioken (Dragon stones)", value="Multisummon de goku (kaioken) y vegeta", inline=False)
    embed.add_field(name="!tqmonos (tiquets)", value="Summon de tiquets de goku y vegeta ssj4 septimo aniversario", inline=False)
    embed.add_field(name="!tqgods (Dragon stones)", value="Summon de tiquets de goku y vegeta ssj god septimo aniversario", inline=False)
    embed.add_field(name="!tqzdokkan (Dragon stones)", value="Summon de tiquets de extreme z battle", inline=False)
    embed.add_field(name="!tqkaioken(Dragon stones)", value="Summon de tiquets de goku (kaioken) y vegeta", inline=False)
    embed.set_footer(text="Muchas gracias por usar el bot!")
    await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Ayuda(client))