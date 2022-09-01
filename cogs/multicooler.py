import discord
import random
from discord.ext import commands

animaciones_summons = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_cooler = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/84/Card_1024810_thumb.png/revision/latest/scale-to-width-down/120?cb=20220828140016",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/e/e2/Card_1024940_thumb.png/revision/latest/scale-to-width-down/120?cb=20220825062251",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/de/Card_1022610_thumb.png/revision/latest/scale-to-width-down/120?cb=20210828060442",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/c/cc/Card_1020320_thumb.png/revision/latest/scale-to-width-down/120?cb=20210708070827",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/9c/Card_1020350_thumb.png/revision/latest/scale-to-width-down/120?cb=20200829043721",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/73/Card_1024280_thumb.png/revision/latest/scale-to-width-down/120?cb=20220426040336",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/8e/Card_1023450_thumb.png/revision/latest/scale-to-width-down/120?cb=20220331140325",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/60/Card_1017170_thumb.png/revision/latest/scale-to-width-down/120?cb=20191002074259",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/b8/Card_1022210_thumb.png/revision/latest/scale-to-width-down/120?cb=20211005121123",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/e/ed/Card_1018180_thumb.png/revision/latest/scale-to-width-down/120?cb=20200301220427"   
]

cualquier_sr_cooler = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/7c/Card_1002470_thumb.png/revision/latest/scale-to-width-down/120?cb=20151010221811",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/9b/Card_1003510_thumb.png/revision/latest/scale-to-width-down/120?cb=20151026173336",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/f2/Card_1000900_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925121208",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/0d/Card_1000120_thumb.png/revision/latest/scale-to-width-down/120?cb=20150922212751",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/65/Card_1003750_thumb.png/revision/latest/scale-to-width-down/120?cb=20151026231128",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/c/c2/Card_1003570_thumb.png/revision/latest/scale-to-width-down/120?cb=20160403132855",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/38/Card_1002130_thumb.png/revision/latest/scale-to-width-down/120?cb=20151023121313",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/be/Card_1000850_thumb.png/revision/latest/scale-to-width-down/120?cb=20150910082207",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/c/c5/Card_1000030_thumb.png/revision/latest/scale-to-width-down/120?cb=20150828224647",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/40/Card_1001620_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925131924",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/31/Card_1000870_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925115947",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/14/Card_1000090_thumb.png/revision/latest/scale-to-width-down/120?cb=20150922211825",
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

class Multicooler(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("multicooler online")

  #Comandos del bot
  @commands.command()
  async def multicooler(self, ctx):
    await ctx.send("**Empezando multisummon:**")
    await ctx.send("<:SSR_eclair:971672682712141844> Featured - 3 puntos")
    await ctx.send("<:SSR_eclair:971672682712141844> No featured - 2 puntos")
    await ctx.send("<:SR_eclair:971673046496731166>  - 1 punto")
    await ctx.send( random.choice(animaciones_summons))
    puntos = 0
    for i in range(0, 9):
            numero = random.randint(1, 10000)
            if numero >= 9500:
                random2 = random.choice(featured_ssr_cooler)
                await ctx.send(random2)
                puntos = puntos + 3
            elif numero >= 9000:
                await ctx.send("<:SSR_eclair:971672682712141844> Random")
                puntos = puntos + 2
            elif numero >= 3000:
                await ctx.send(random.choice(cualquier_sr_cooler))
                puntos = puntos + 1
            else:
                await ctx.send(
                    "<:R_eclair:971673105024045056> Personaje kk")
    if random.randint(1, 10000) >= 9500:
        random1 = random.choice(featured_ssr_cooler)
        await ctx.send(random1)
        puntos = puntos + 3
    else:
      await ctx.send("<:SSR_eclair:971672682712141844> Random")
      puntos = puntos + 2
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
	client.add_cog(Multicooler(client))