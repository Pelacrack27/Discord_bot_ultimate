import discord
import random
from discord.ext import commands

animaciones_summons = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_raditz = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/e/ea/Card_1024050_thumb.png/revision/latest/scale-to-width-down/120?cb=20220808053004",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/4d/Card_1024070_thumb.png/revision/latest/scale-to-width-down/120?cb=20220808053128",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/55/Card_1023100_thumb.png/revision/latest/scale-to-width-down/120?cb=20220225075649",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/b8/Card_1022210_thumb.png/revision/latest/scale-to-width-down/120?cb=20211005121123",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/a/a1/Card_1020980_thumb.png/revision/latest/scale-to-width-down/120?cb=20210131044905",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/07/Card_1017480_thumb.png/revision/latest/scale-to-width-down/120?cb=20200105175645",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/e/ea/Card_1016560_thumb.png/revision/latest/scale-to-width-down/120?cb=20190606065913"
]

cualquier_sr_raditz = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/2f/Card_1001430_thumb.png/revision/latest/scale-to-width-down/120?cb=20150908174827",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/6a/Card_1000160_thumb.png/revision/latest/scale-to-width-down/120?cb=20180902213956",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/fe/Card_1001420_thumb.png/revision/latest/scale-to-width-down/120?cb=20150908142904",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/f4/Card_1000170_thumb.png/revision/latest/scale-to-width-down/120?cb=20150924222834",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/0b/Card_1001860_thumb.png/revision/latest/scale-to-width-down/120?cb=20151009084104",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/fa/Card_1000880_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925120349",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/95/Card_1000100_thumb.png/revision/latest/scale-to-width-down/120?cb=20150922212120",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/40/Card_1001620_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925131924",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/31/Card_1000870_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925115947",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/14/Card_1000090_thumb.png/revision/latest/scale-to-width-down/120?cb=20150922211825",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/14/Card_1000090_thumb.png/revision/latest/scale-to-width-down/120?cb=20150922211825",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/9b/Card_1003510_thumb.png/revision/latest/scale-to-width-down/120?cb=20151026173336",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/9b/Card_1003510_thumb.png/revision/latest/scale-to-width-down/120?cb=20151026173336",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/0d/Card_1000120_thumb.png/revision/latest/scale-to-width-down/120?cb=20150922212751",
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

class Multiraditz(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("multiraditz online")

  #Comandos del bot
  @commands.command()
  async def multiraditz(self, ctx):
    await ctx.send("**Empezando multisummon:**")
    await ctx.send("<:SSR_eclair:971672682712141844> Featured - 3 puntos")
    await ctx.send("<:SSR_eclair:971672682712141844> No featured - 2 puntos")
    await ctx.send("<:SR_eclair:971673046496731166>  - 1 punto")
    await ctx.send( random.choice(animaciones_summons))
    puntos = 0
    if random.randint(1, 10000) >= 9500:
        random1 = random.choice(featured_ssr_raditz)
        await ctx.send(random1)
        puntos = puntos + 3
    else:
      await ctx.send(
                "<:SSR_eclair:971672682712141844> Random")
      puntos = puntos + 2
      for i in range(0, 9):
            numero = random.randint(1, 10000)
            if numero >= 9500:
                random2 = random.choice(featured_ssr_raditz)
                await ctx.send(random2)
                puntos = puntos + 3
            elif numero >= 9000:
                await ctx.send(
                    "<:SSR_eclair:971672682712141844> Random")
                puntos = puntos + 2
            elif numero >= 3000:
                await ctx.send(random.choice(cualquier_sr_raditz
            ))
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
	client.add_cog(Multiraditz(client))