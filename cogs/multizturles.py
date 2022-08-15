import discord
import random
from discord.ext import commands

animaciones_summons = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_zturles = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/dc/Card_1013560_thumb.png/revision/latest/scale-to-width-down/120?cb=20180813001431",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/f1/Card_1015150_thumb.png/revision/latest/scale-to-width-down/120?cb=20180831034133",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/6d/Card_1014810_thumb.png/revision/latest/scale-to-width-down/120?cb=20180831034838"
]

cualquier_sr_zturles = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/e/eb/Card_1000060_thumb.png/revision/latest/scale-to-width-down/120?cb=20150922211230",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/4a/Card_1000050_thumb.png/revision/latest/scale-to-width-down/120?cb=20150922210531",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/38/Card_1002130_thumb.png/revision/latest/scale-to-width-down/120?cb=20151023121313",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/be/Card_1000850_thumb.png/revision/latest/scale-to-width-down/120?cb=20150910082207",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/c/c5/Card_1000030_thumb.png/revision/latest/scale-to-width-down/120?cb=20150828224647",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random"
]

class Multizturles(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("multizturles online")

  #Comandos del bot
  @commands.command()
  async def multizturles(self, ctx):
    await ctx.send("**Empezando multisummon:**")
    await ctx.send("<:SSR_eclair:971672682712141844> Featured - 3 puntos")
    await ctx.send("<:SSR_eclair:971672682712141844> No featured - 2 puntos")
    await ctx.send("<:SR_eclair:971673046496731166>  - 1 punto")
    await ctx.send( random.choice(animaciones_summons))
    puntos = 0
    if random.randint(1, 10000) >= 9500:
        random1 = random.choice(featured_ssr_zturles)
        await ctx.send(random1)
        puntos = puntos + 3
    else:
      await ctx.send(
                "<:SSR_eclair:971672682712141844> Random")
      puntos = puntos + 2
      for i in range(0, 9):
            numero = random.randint(1, 10000)
            if numero >= 9500:
                random2 = random.choice(featured_ssr_zturles)
                await ctx.send(random2)
                puntos = puntos + 3
            elif numero >= 9000:
                await ctx.send(
                    "<:SSR_eclair:971672682712141844> Random")
                puntos = puntos + 2
            elif numero >= 3000:
                await ctx.send(random.choice(cualquier_sr_zturles))
                puntos = puntos + 1
            else:
                await ctx.send(
                    "<:R_eclair:971673105024045056> Personaje kk")
      await ctx.send(f"Total de puntos: {puntos}")
      if puntos >= 15:
          await ctx.send("https://i.pinimg.com/564x/4c/4d/88/4c4d8867c58389c11d6d05221aa16632.jpg")
      elif puntos >= 10:
          await ctx.send("https://i.pinimg.com/550x/09/19/b6/0919b6dcf57e6a6b4bf31ac5fd1e7928.jpg")
      elif puntos >= 7:
          await ctx.send("https://i.ytimg.com/vi/ffHN6_8HDuI/mqdefault.jpg")
      elif puntos >= 5:
          await ctx.send("https://i.pinimg.com/736x/35/b7/3e/35b73e01e63b253e041e874aa590681e.jpg")
      else: 
          await ctx.send("https://pbs.twimg.com/media/EaLXbstWAAETAaT.jpg")
      await ctx.send("**Multisummon finalizado**")


def setup(client):
	client.add_cog(Multizturles(client))