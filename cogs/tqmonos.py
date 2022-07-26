import discord
import random
from discord.ext import commands

animaciones_summons = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_monos = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/26/Card_1022400_thumb.png/revision/latest/scale-to-width-down/120?cb=20220708062141",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/e/e7/Card_1023580_thumb.png/revision/latest/scale-to-width-down/120?cb=20220708062309",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/de/Card_1022610_thumb.png/revision/latest/scale-to-width-down/120?cb=20210828060442",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/d5/Card_1020290_thumb.png/revision/latest/scale-to-width-down/120?cb=20210708070713",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/43/Card_1020440_thumb.png/revision/latest/scale-to-width-down/120?cb=20200829043246",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/0c/Card_1015740_thumb.png/revision/latest/scale-to-width-down/120?cb=20190705085758",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/2f/Card_1015760_thumb.png/revision/latest/scale-to-width-down/120?cb=20190705090214",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/58/Card_1012880_thumb.png/revision/latest/scale-to-width-down/120?cb=20180708215123",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/f4/Card_1021910_thumb.png/revision/latest/scale-to-width-down/120?cb=20210427041153",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/06/Card_1021930_thumb.png/revision/latest/scale-to-width-down/120?cb=20210427041155"
]

cualquier_sr_monos = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/56/Card_1011490_thumb.png/revision/latest/scale-to-width-down/120?cb=20171123185619",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/65/Card_1003750_thumb.png/revision/latest/scale-to-width-down/120?cb=20151026231128",
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

class Multimonos(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("multimonos online")

  #Comandos del bot
  @commands.command()
  async def multimonos(self, ctx):
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
                random2 = random.choice(featured_ssr_monos)
                await ctx.send(random2)
                if random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/26/Card_1022400_thumb.png/revision/latest/scale-to-width-down/120?cb=20220708062141":
                    puntos = puntos + 5
                elif random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/de/Card_1022610_thumb.png/revision/latest/scale-to-width-down/120?cb=20210828060442":
                    puntos = puntos + 5
                elif random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/d5/Card_1020290_thumb.png/revision/latest/scale-to-width-down/120?cb=20210708070713":
                    puntos = puntos + 5
                elif random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/43/Card_1020440_thumb.png/revision/latest/scale-to-width-down/120?cb=20200829043246":
                    puntos = puntos + 5
                elif random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/0c/Card_1015740_thumb.png/revision/latest/scale-to-width-down/120?cb=20190705085758":
                    puntos = puntos + 5
                elif random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/2f/Card_1015760_thumb.png/revision/latest/scale-to-width-down/120?cb=20190705090214":
                    puntos = puntos + 5
                elif random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/58/Card_1012880_thumb.png/revision/latest/scale-to-width-down/120?cb=20180708215123":
                    puntos = puntos + 5
                else:
                    puntos = puntos + 3
                puntos = puntos + 3
            elif numero >= 9000:
                await ctx.send(
                    "<:SSR_eclair:971672682712141844> Random")
                puntos = puntos + 2
            elif numero >= 3000:
                await ctx.send(random.choice(cualquier_sr_monos))
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
	client.add_cog(Multimonos(client))