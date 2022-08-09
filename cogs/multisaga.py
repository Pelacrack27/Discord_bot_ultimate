import discord
import random
from discord.ext import commands

animaciones_summons = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_saga = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/f9/Card_1019290_thumb.png/revision/latest/scale-to-width-down/120?cb=20200317024243",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/81/Card_1005140_thumb.png/revision/latest/scale-to-width-down/120?cb=20160510030150",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/76/Card_1013200_thumb.png/revision/latest/scale-to-width-down/120?cb=20180708214934",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/76/Card_1013200_thumb.png/revision/latest/scale-to-width-down/120?cb=20180708214934",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/5a/Card_1013190_thumb.png/revision/latest/scale-to-width-down/120?cb=20180708214951"
]

cualquier_sr_saga = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/2f/Card_1001430_thumb.png/revision/latest/scale-to-width-down/120?cb=20150908174827",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/37/Card_1003220_thumb.png/revision/latest/scale-to-width-down/120?cb=20151024231112",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/75/Card_1002140_thumb.png/revision/latest/scale-to-width-down/120?cb=20151009204458",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/f7/Card_1000860_thumb.png/revision/latest/scale-to-width-down/120?cb=20180902213728",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/be/Card_1000040_thumb.png/revision/latest/scale-to-width-down/120?cb=20150922210156",
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

class Multisaga(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("multisaga online")

  #Comandos del bot
  @commands.command()
  async def multisaga(self, ctx):
    await ctx.send("**Empezando multisummon:**")
    await ctx.send("<:SSR_eclair:971672682712141844> Featured - 3 puntos")
    await ctx.send("<:SSR_eclair:971672682712141844> No featured - 2 puntos")
    await ctx.send("<:SR_eclair:971673046496731166>  - 1 punto")
    await ctx.send( random.choice(animaciones_summons))
    puntos = 0
    if random.randint(1, 10000) >= 9500:
        random1 = random.choice(featured_ssr_saga)
        await ctx.send(random1)
        puntos = puntos + 3
    else:
      await ctx.send(
                "<:SSR_eclair:971672682712141844> Random")
      puntos = puntos + 2
      for i in range(0, 9):
            numero = random.randint(1, 10000)
            if numero >= 9500:
                random2 = random.choice(featured_ssr_saga)
                await ctx.send(random2)
                puntos = puntos + 3
            elif numero >= 9000:
                await ctx.send(
                    "<:SSR_eclair:971672682712141844> Random")
                puntos = puntos + 2
            elif numero >= 3000:
                await ctx.send(random.choice(cualquier_sr_saga))
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
	client.add_cog(Multisaga(client))