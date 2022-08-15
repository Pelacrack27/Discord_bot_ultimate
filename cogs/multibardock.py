import discord
import random
from discord.ext import commands

animaciones_summons = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_bardock = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/48/Card_1002810_thumb.png/revision/latest/scale-to-width-down/120?cb=20180517100949",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/36/Card_1006510_thumb.png/revision/latest/scale-to-width-down/120?cb=20160623131420",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/8e/Card_1006480_thumb.png/revision/latest/scale-to-width-down/120?cb=20160630102140",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/30/Card_1006500_thumb.png/revision/latest/scale-to-width-down/120?cb=20160630123312",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/ff/Card_1006490_thumb.png/revision/latest/scale-to-width-down/120?cb=20160623131914",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/8d/Card_1002820_thumb.png/revision/latest/scale-to-width-down/120?cb=20160510082102",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/02/Card_1005150_thumb.png/revision/latest/scale-to-width-down/120?cb=20160902152528"
]

cualquier_sr_bardock = [
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
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random"
]

class Multibardock(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("multibardock online")

  #Comandos del bot
  @commands.command()
  async def multibardock(self, ctx):
    await ctx.send("**Empezando multisummon:**")
    await ctx.send("<:SSR_eclair:971672682712141844> Featured - 3 puntos")
    await ctx.send("<:SSR_eclair:971672682712141844> No featured - 2 puntos")
    await ctx.send("<:SR_eclair:971673046496731166>  - 1 punto")
    await ctx.send( random.choice(animaciones_summons))
    puntos = 0
    if random.randint(1, 10000) >= 9500:
        random1 = random.choice(featured_ssr_bardock)
        await ctx.send(random1)
        puntos = puntos + 3
    else:
      await ctx.send(
                "<:SSR_eclair:971672682712141844> Random")
      puntos = puntos + 2
      for i in range(0, 9):
            numero = random.randint(1, 10000)
            if numero >= 9500:
                random2 = random.choice(featured_ssr_bardock)
                await ctx.send(random2)
                puntos = puntos + 3
            elif numero >= 9000:
                await ctx.send(
                    "<:SSR_eclair:971672682712141844> Random")
                puntos = puntos + 2
            elif numero >= 3000:
                await ctx.send(random.choice(cualquier_sr_bardock))
                puntos = puntos + 1
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
	client.add_cog(Multibardock(client))