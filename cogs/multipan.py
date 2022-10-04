import discord
import random
from discord.ext import commands

animaciones_summons = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_pan = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/d0/Card_1024980_thumb.png/revision/latest/scale-to-width-down/120?cb=20221003083008",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/39/Card_1024770_thumb.png/revision/latest/scale-to-width-down/120?cb=20221003083304",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/a/ac/Card_1023760_thumb.png/revision/latest/scale-to-width-down/120?cb=20220530065542",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/55/Card_1023100_thumb.png/revision/latest/scale-to-width-down/120?cb=20220225075649",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/a/a1/Card_1020980_thumb.png/revision/latest/scale-to-width-down/120?cb=20210131044905",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/f4/Card_1021910_thumb.png/revision/latest/scale-to-width-down/120?cb=20210427041153",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/06/Card_1021930_thumb.png/revision/latest/scale-to-width-down/120?cb=20210427041155"

    
]

cualquier_ssr_pan = [
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
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random"
]

cualquier_sr_pan = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/d9/Card_1005870_thumb.png/revision/latest/scale-to-width-down/120?cb=20160329223116",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/d2/Card_1002980_thumb.png/revision/latest/scale-to-width-down/120?cb=20151023213208",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/c/cd/Card_1000950_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925122226",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/12/Card_1000190_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925053429",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/0b/Card_1001860_thumb.png/revision/latest/scale-to-width-down/120?cb=20151009084104",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/fa/Card_1000880_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925120349",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/95/Card_1000100_thumb.png/revision/latest/scale-to-width-down/120?cb=20150922212120",
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

class Multipan(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("multipan online")

  #Comandos del bot
  @commands.command()
  async def multipan(self, ctx):
    await ctx.send("**Empezando multisummon:**")
    await ctx.send("<:SSR_eclair:971672682712141844> Featured - 3 puntos")
    await ctx.send("<:SSR_eclair:971672682712141844> No featured - 2 puntos")
    await ctx.send("<:SR_eclair:971673046496731166>  - 1 punto")
    await ctx.send(random.choice(animaciones_summons))
    puntos = 0
    for i in range(0, 9):
            numero = random.randint(1, 10000)
            if numero >= 9500:
                random2 = random.choice(featured_ssr_pan)
                await ctx.send(random2)
                puntos = puntos + 3
            elif numero >= 9000:
                await ctx.send(random.choice(cualquier_ssr_pan))
                puntos = puntos + 2
            elif numero >= 3000:
                await ctx.send(random.choice(cualquier_sr_pan))
                puntos = puntos + 1
            else:
                await ctx.send("<:R_eclair:971673105024045056> Personaje kk")  
    if random.randint(1, 10000) >= 9500:
        await ctx.send(random.choice(featured_ssr_pan))
        puntos = puntos + 3
    else:
        await ctx.send(random.choice(cualquier_ssr_pan))
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
	client.add_cog(Multipan(client))