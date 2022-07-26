import discord
import random
from discord.ext import commands

animaciones_summons = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_gods = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/8b/Card_1022360_thumb.png/revision/latest/scale-to-width-down/120?cb=20220708062009",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/08/Card_1023560_thumb.png/revision/latest/scale-to-width-down/120?cb=20220708062239",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/08/Card_1022730_thumb.png/revision/latest/scale-to-width-down/120?cb=20210828064526",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/d5/Card_1020290_thumb.png/revision/latest/scale-to-width-down/120?cb=20210708070713",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/9c/Card_1020350_thumb.png/revision/latest/scale-to-width-down/120?cb=20200829043721",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/72/Card_1018600_thumb.png/revision/latest/scale-to-width-down/120?cb=20200708043244",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/64/Card_1018630_thumb.png/revision/latest/scale-to-width-down/120?cb=20200708043139",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/0f/Card_1012910_thumb.png/revision/latest/scale-to-width-down/120?cb=20180708215348",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/4e/Card_1018750_thumb.png/revision/latest/scale-to-width-down/120?cb=20200507075815",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/d1/Card_1018770_thumb.png/revision/latest/scale-to-width-down/120?cb=20200507075655"
]

cualquier_sr_gods = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/c/c2/Card_1003570_thumb.png/revision/latest/scale-to-width-down/120?cb=20160403132855",
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
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random"
]

class Tqgods(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("tqgods online")

  #Comandos del bot
  @commands.command()
  async def tqgods(self, ctx):
    await ctx.send("**Empezando multisummon:**")
    await ctx.send("<:LR_logo_apng:978185948787531816> featured - 5 puntos")
    await ctx.send("<:SSR_eclair:971672682712141844> Featured - 3 puntos")
    await ctx.send("<:SSR_eclair:971672682712141844> No featured - 2 puntos")
    await ctx.send("<:SR_eclair:971673046496731166>  - 1 punto")
    await ctx.send( random.choice(animaciones_summons))
    puntos = 0
    for i in range(0, 7):
            numero = random.randint(1, 10000)
            if numero >= 9500:
                random2 = random.choice(featured_ssr_gods)
                await ctx.send(random2)
                if random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/8b/Card_1022360_thumb.png/revision/latest/scale-to-width-down/120?cb=20220708062009":
                    puntos = puntos + 5
                elif random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/08/Card_1022730_thumb.png/revision/latest/scale-to-width-down/120?cb=20210828064526":
                    puntos = puntos + 5
                elif random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/d5/Card_1020290_thumb.png/revision/latest/scale-to-width-down/120?cb=20210708070713":
                    puntos = puntos + 5
                elif random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/9c/Card_1020350_thumb.png/revision/latest/scale-to-width-down/120?cb=20200829043721":
                    puntos = puntos + 5
                elif random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/72/Card_1018600_thumb.png/revision/latest/scale-to-width-down/120?cb=20200708043244":
                    puntos = puntos + 5
                elif random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/64/Card_1018630_thumb.png/revision/latest/scale-to-width-down/120?cb=20200708043139":
                    puntos = puntos + 5
                elif random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/0f/Card_1012910_thumb.png/revision/latest/scale-to-width-down/120?cb=20180708215348":
                    puntos = puntos + 5
                else:
                    puntos = puntos + 3
                puntos = puntos + 3
            elif numero >= 9000:
                await ctx.send(
                    "<:SSR_eclair:971672682712141844> Random")
                puntos = puntos + 2
            elif numero >= 3000:
                await ctx.send(random.choice(cualquier_sr_gods))
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
	client.add_cog(Tqgods(client))