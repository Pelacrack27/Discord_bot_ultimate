import discord
import random
from discord.ext import commands

animaciones_summons = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_stepup4 = [
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/73/Card_1024280_thumb.png/revision/latest/scale-to-width-down/120?cb=20220426040336",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/11/Card_1024370_thumb.png/revision/latest/scale-to-width-down/120?cb=20220426051407",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/e/ea/Card_1024050_thumb.png/revision/latest/scale-to-width-down/120?cb=20220808053004",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/8c/Card_1023970_thumb.png/revision/latest/scale-to-width-down/120?cb=20220317024841",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/a/ac/Card_1023760_thumb.png/revision/latest/scale-to-width-down/120?cb=20220530065542",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/8e/Card_1023450_thumb.png/revision/latest/scale-to-width-down/120?cb=20220331140325",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/60/Card_1023480_thumb.png/revision/latest/scale-to-width-down/120?cb=20220331143311",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/c/c4/Card_1023350_thumb.png/revision/latest/scale-to-width-down/120?cb=20220127083447",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/55/Card_1023100_thumb.png/revision/latest/scale-to-width-down/120?cb=20220225075649",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/28/Card_1022820_thumb.png/revision/latest/scale-to-width-down/120?cb=20211202073154",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/31/Card_1022640_thumb.png/revision/latest/scale-to-width-down/120?cb=20211230080241"
]

cualquier_ssr_stepup4 = [
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random"
]

cualquier_sr_stepup4 = [
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

class Stepup4(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("stepup4 online")

  #Comandos del bot
  @commands.command()
  async def stepup4(self, ctx):
    await ctx.send("**Empezando multisummon:**")
    await ctx.send("<:SSR_eclair:971672682712141844> Featured - 3 puntos")
    await ctx.send("<:SSR_eclair:971672682712141844> No featured - 2 puntos")
    await ctx.send("<:SR_eclair:971673046496731166>  - 1 punto")
    await ctx.send(random.choice(animaciones_summons))
    puntos = 0
    for i in range(0, 9):
            numero = random.randint(1, 10000)
            if numero >= 9500:
                random2 = random.choice(featured_ssr_stepup4)
                await ctx.send(random2)                             
                puntos = puntos + 3
            elif numero >= 9000:
                await ctx.send(random.choice(cualquier_ssr_stepup4))
                puntos = puntos + 2
            elif numero >= 3000:
                await ctx.send(random.choice(cualquier_sr_stepup4))
                puntos = puntos + 1
            else:
                await ctx.send("<:R_eclair:971673105024045056> Personaje kk")  
    await ctx.send(random.choice(featured_ssr_stepup4))
    puntos = puntos + 3
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
	client.add_cog(Stepup4(client))