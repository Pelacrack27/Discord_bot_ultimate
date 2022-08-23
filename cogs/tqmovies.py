import discord
import random
from discord.ext import commands

animaciones_summons = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_movies = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/26/Card_1021340_thumb.png/revision/latest/scale-to-width-down/120?cb=20210708070805",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/12/Card_1007010_thumb.png/revision/latest/scale-to-width-down/120?cb=20160725092940",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/7f/Card_1016020_thumb.png/revision/latest/scale-to-width-down/120?cb=20190213021138",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/00/Card_1016040_thumb.png/revision/latest/scale-to-width-down/120?cb=20190213020952",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/d7/Card_1012640_thumb.png/revision/latest/scale-to-width-down/120?cb=20180118124528",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/d9/Card_1020020_thumb.png/revision/latest/scale-to-width-down/120?cb=20201203071252",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/95/Card_1012040_thumb.png/revision/latest/scale-to-width-down/120?cb=20180515232826"
]

cualquier_ssr_movies = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/1a/Card_1023400_thumb.png/revision/latest/scale-to-width-down/120?cb=20220214090326",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/f4/Card_1022920_thumb.png/revision/latest/scale-to-width-down/120?cb=20210915081038",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/a/a2/Card_1018470_thumb.png/revision/latest/scale-to-width-down/120?cb=20200419104819",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/81/Card_1016820_thumb.png/revision/latest/scale-to-width-down/120?cb=20191218040222",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/6a/Card_1011620_thumb.png/revision/latest/scale-to-width-down/120?cb=20180222012651",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/1b/Card_1019380_thumb.png/revision/latest/scale-to-width-down/120?cb=20200622044640",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/e/e5/Card_1016380_thumb.png/revision/latest/scale-to-width-down/120?cb=20190722232029",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/e/e4/Card_1010150_thumb.png/revision/latest/scale-to-width-down/120?cb=20170612132201",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/64/Card_1021120_thumb.png/revision/latest/scale-to-width-down/120?cb=20201214024421",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/5f/Card_1014700_thumb.png/revision/latest/scale-to-width-down/120?cb=20210117021434",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/00/Card_1014950_thumb.png/revision/latest/scale-to-width-down/120?cb=20180912061410",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/15/Card_1007830_thumb.png/revision/latest/scale-to-width-down/120?cb=20180525003303",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/0b/Card_1022070_thumb.png/revision/latest/scale-to-width-down/120?cb=20210519024043",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/38/Card_1016850_thumb.png/revision/latest/scale-to-width-down/120?cb=20190520094451",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/90/Card_1011120_thumb.png/revision/latest/scale-to-width-down/120?cb=20171031001751",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/d6/Card_1022100_thumb.png/revision/latest/scale-to-width-down/120?cb=20211020070205",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/8b/Card_1021460_thumb.png/revision/latest/scale-to-width-down/120?cb=20210723072819",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/c/c6/Card_1018230_thumb.png/revision/latest/scale-to-width-down/120?cb=20200216181642",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/33/Card_1016350_thumb.png/revision/latest/scale-to-width-down/120?cb=20190722231718",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/b1/Card_1010050_thumb.png/revision/latest/scale-to-width-down/120?cb=20170707192320",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/9b/Card_1023020_thumb.png/revision/latest/scale-to-width-down/120?cb=20210915063628",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/df/Card_1018860_thumb.png/revision/latest/scale-to-width-down/120?cb=20200726045128",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/9c/Card_1012140_thumb.png/revision/latest/scale-to-width-down/120?cb=20180410100206",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/11/Card_1021950_thumb.png/revision/latest/scale-to-width-down/120?cb=20210619201823",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/6a/Card_1019800_thumb.png/revision/latest/scale-to-width-down/120?cb=20200521235814",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/63/Card_1015600_thumb.png/revision/latest/scale-to-width-down/120?cb=20190201002233",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/42/Card_1013750_thumb.png/revision/latest/scale-to-width-down/120?cb=20180816223826",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/b5/Card_1023070_thumb.png/revision/latest/scale-to-width-down/120?cb=20211214155638",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/e/ee/Card_1020730_thumb.png/revision/latest/scale-to-width-down/120?cb=20210215215547",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/97/Card_1005010_thumb.png/revision/latest/scale-to-width-down/120?cb=20191017070304",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/31/Card_1010420_thumb.png/revision/latest/scale-to-width-down/120?cb=20170502115948",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/8d/Card_1020200_thumb.png/revision/latest/scale-to-width-down/120?cb=20200916043802",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/09/Card_1014000_thumb.png/revision/latest/scale-to-width-down/120?cb=20181111033231",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/3e/Card_1011700_thumb.png/revision/latest/scale-to-width-down/120?cb=20180122093608",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/b4/Card_1022570_thumb.png/revision/latest/scale-to-width-down/120?cb=20220117023331",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/a/aa/Card_1021410_thumb.png/revision/latest/scale-to-width-down/120?cb=20210723072843",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/5f/Card_1018980_thumb.png/revision/latest/scale-to-width-down/120?cb=20200726045058",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/9c/Card_1014920_thumb.png/revision/latest/scale-to-width-down/120?cb=20181017101240",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
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

cualquier_sr_movies = [
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

class Tqmovies(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("tqmovies online")

  #Comandos del bot
  @commands.command()
  async def tqmovies(self, ctx):
    await ctx.send("**Empezando multisummon:**")
    await ctx.send("<:SSR_eclair:971672682712141844> Featured - 3 puntos")
    await ctx.send("<:SSR_eclair:971672682712141844> No featured - 2 puntos")
    await ctx.send("<:SR_eclair:971673046496731166>  - 1 punto")
    await ctx.send( random.choice(animaciones_summons))
    puntos = 0
    for i in range(0, 7):
            numero = random.randint(1, 10000)
            if numero >= 9500:
                random2 = random.choice(featured_ssr_movies)
                await ctx.send(random2)
                puntos = puntos + 3
            elif numero >= 9000:
                await ctx.send(random.choice(cualquier_ssr_movies))
                puntos = puntos + 2
            else:
                await ctx.send(random.choice(cualquier_sr_movies))
                puntos = puntos + 1
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
	client.add_cog(Tqmovies(client))