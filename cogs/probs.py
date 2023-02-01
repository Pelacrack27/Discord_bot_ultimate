import discord
from discord.ext import commands

class Probs(commands.Cog):
  
  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("probs online")

  #Comandos del bot
  @commands.command()
  async def probs(self, ctx):
    embed=discord.Embed(title="Probabilidades",  description="A continuación se muestran las probabilidades de los diferentes rangos de personajes", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name,  icon_url=ctx.author.avatar_url)
    embed.add_field(name="SSR asegurado:", value="5% <:SSR_eclair:971672682712141844> Featured | 95% <:SSR_eclair:971672682712141844> No featured", inline=False)
    embed.add_field(name="SSR no asegurado:", value="5% <:SSR_eclair:971672682712141844> Featured | 5% <:SSR_eclair:971672682712141844> No featured | 60% <:SR_eclair:971673046496731166> Aleatorio | 30% <:R_eclair:971673105024045056> Aleatorio", inline=False)


    embed.set_footer(text="Muchas gracias por usar el bot!")
    await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Probs(client))