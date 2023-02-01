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
    embed.add_field(name="!probs", value="Probabilidades de summons (por si alguien no se las sabe)", inline=False)
    embed.add_field(name="!multigohan", value="Multisummon de Gohan no-beast", inline=False)
    embed.add_field(name="!multipiccolo", value="Multisummon de piccolo gigachad", inline=False)
    embed.add_field(name="!stepup1", value="Multisummon de step-up (Primera rotacion)", inline=False)
    embed.add_field(name="!stepup2", value="Multisummon de step-up (Segunda rotacion)", inline=False)
    embed.add_field(name="!stepup3", value="Multisummon de step-up (Tercera rotacion)", inline=False)
    embed.add_field(name="!stepup4", value="Multisummon de step-up (Cuarta rotacion)", inline=False)
    embed.add_field(name="!stepup5", value="Multisummon de step-up (Quinta rotacion)", inline=False)
    embed.add_field(name="!multigolden", value="Multisummon de golden Freezer LR", inline=False)


    embed.set_footer(text="Muchas gracias por usar el bot!")
    await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Ayuda(client))