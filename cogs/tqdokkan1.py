import discord
import random
from discord.ext import commands

animaciones_summons = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_dokkan1 = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/f4/Card_1021910_thumb.png/revision/latest/scale-to-width-down/120?cb=20210427041153",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/31/Card_1022640_thumb.png/revision/latest/scale-to-width-down/120?cb=20211230080241",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/f2/Card_1021660_thumb.png/revision/latest/scale-to-width-down/120?cb=20210317024428",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/bf/Card_1021320_thumb.png/revision/latest/scale-to-width-down/120?cb=20210331131538",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/a/ad/Card_1021040_thumb.png/revision/latest/scale-to-width-down/120?cb=20210228003027",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/0c/Card_1020490_thumb.png/revision/latest/scale-to-width-down/120?cb=20201231110139",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/35/Card_1020080_thumb.png/revision/latest/scale-to-width-down/120?cb=20201004105257",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/24/Card_1019620_thumb.png/revision/latest/scale-to-width-down/120?cb=20201106101145",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/1a/Card_1019130_thumb.png/revision/latest/scale-to-width-down/120?cb=20200317024013",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/4e/Card_1018750_thumb.png/revision/latest/scale-to-width-down/120?cb=20200507075815",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/8a/Card_1018260_thumb.png/revision/latest/scale-to-width-down/120?cb=20200402002017",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/e/ed/Card_1018180_thumb.png/revision/latest/scale-to-width-down/120?cb=20200301220427",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/60/Card_1017170_thumb.png/revision/latest/scale-to-width-down/120?cb=20191002074259",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/78/Card_1017110_thumb.png/revision/latest/scale-to-width-down/120?cb=20191111070043",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/5e/Card_1016500_thumb.png/revision/latest/scale-to-width-down/120?cb=20190321193440",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/e/ea/Card_1016560_thumb.png/revision/latest/scale-to-width-down/120?cb=20190606065913",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/e/e3/Card_1015990_thumb.png/revision/latest/scale-to-width-down/120?cb=20190213021335",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/7a/Card_1015360_thumb.png/revision/latest/scale-to-width-down/120?cb=20190403014549",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/10/Card_1015040_thumb.png/revision/latest/scale-to-width-down/120?cb=20190115230927",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/6d/Card_1014810_thumb.png/revision/latest/scale-to-width-down/120?cb=20180831034838",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/04/Card_1014120_thumb.png/revision/latest/scale-to-width-down/120?cb=20181121011820",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/96/Card_1013850_thumb.png/revision/latest/scale-to-width-down/120?cb=20181212001716",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/dc/Card_1013560_thumb.png/revision/latest/scale-to-width-down/120?cb=20180813001431",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/de/Card_1012750_thumb.png/revision/latest/scale-to-width-down/120?cb=20180420044345",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/a/ae/Card_1012580_thumb.png/revision/latest/scale-to-width-down/120?cb=20180212003836",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/dc/Card_1011810_thumb.png/revision/latest/scale-to-width-down/120?cb=20171228080425",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/dc/Card_1011810_thumb.png/revision/latest/scale-to-width-down/120?cb=20171228080425",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/c/c2/Card_1011160_thumb.png/revision/latest/scale-to-width-down/120?cb=20180131023143",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/15/Card_1010840_thumb.png/revision/latest/scale-to-width-down/120?cb=20171123185348",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/91/Card_1009650_thumb.png/revision/latest/scale-to-width-down/120?cb=20170925121520",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/53/Card_1010240_thumb.png/revision/latest/scale-to-width-down/120?cb=20171012103612",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/98/Card_1009820_thumb.png/revision/latest/scale-to-width-down/120?cb=20170707192214",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/a/a1/Card_1009750_thumb.png/revision/latest/scale-to-width-down/120?cb=20170111100818",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/a/a9/Card_1009570_thumb.png/revision/latest/scale-to-width-down/120?cb=20170105092223",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/51/Card_1009320_thumb.png/revision/latest/scale-to-width-down/120?cb=20161117102039",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/04/Card_1006410_thumb.png/revision/latest/scale-to-width-down/120?cb=20160930094841",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/81/Card_1008730_thumb.png/revision/latest/scale-to-width-down/120?cb=20181126171456",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/92/Card_1007920_thumb.png/revision/latest/scale-to-width-down/120?cb=20161226095657",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/b0/Card_1007930_thumb.png/revision/latest/scale-to-width-down/120?cb=20160923082818",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/4d/Card_1005630_thumb.png/revision/latest/scale-to-width-down/120?cb=20160602080950",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/3f/Card_1003320_thumb.png/revision/latest/scale-to-width-down/120?cb=20160301225440",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/f9/Card_1002800_thumb.png/revision/latest/scale-to-width-down/120?cb=20160203224822",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/b3/Card_1003300_thumb.png/revision/latest/scale-to-width-down/120?cb=20151030192532",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/2a/Card_2000640_thumb.png/revision/latest/scale-to-width-down/120?cb=20151007224406"

    
]

cualquier_ssr_dokkan1 = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/a/a2/Card_1018470_thumb.png/revision/latest/scale-to-width-down/120?cb=20200419104819",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/81/Card_1016820_thumb.png/revision/latest/scale-to-width-down/120?cb=20191218040222",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/6a/Card_1011620_thumb.png/revision/latest/scale-to-width-down/120?cb=20180222012651",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/1b/Card_1019380_thumb.png/revision/latest/scale-to-width-down/120?cb=20200622044640",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/e/e5/Card_1016380_thumb.png/revision/latest/scale-to-width-down/120?cb=20190722232029",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/e/e4/Card_1010150_thumb.png/revision/latest/scale-to-width-down/120?cb=20170612132201",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/00/Card_1014950_thumb.png/revision/latest/scale-to-width-down/120?cb=20180912061410",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/15/Card_1007830_thumb.png/revision/latest/scale-to-width-down/120?cb=20180525003303",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/38/Card_1016850_thumb.png/revision/latest/scale-to-width-down/120?cb=20190520094451",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/90/Card_1011120_thumb.png/revision/latest/scale-to-width-down/120?cb=20171031001751",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/c/c6/Card_1018230_thumb.png/revision/latest/scale-to-width-down/120?cb=20200216181642",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/33/Card_1016350_thumb.png/revision/latest/scale-to-width-down/120?cb=20190722231718",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/b1/Card_1010050_thumb.png/revision/latest/scale-to-width-down/120?cb=20170707192320",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/df/Card_1018860_thumb.png/revision/latest/scale-to-width-down/120?cb=20200726045128",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/9c/Card_1012140_thumb.png/revision/latest/scale-to-width-down/120?cb=20180410100206",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/6a/Card_1019800_thumb.png/revision/latest/scale-to-width-down/120?cb=20200521235814",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/63/Card_1015600_thumb.png/revision/latest/scale-to-width-down/120?cb=20190201002233",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/42/Card_1013750_thumb.png/revision/latest/scale-to-width-down/120?cb=20180816223826",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/97/Card_1005010_thumb.png/revision/latest/scale-to-width-down/120?cb=20191017070304",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/31/Card_1010420_thumb.png/revision/latest/scale-to-width-down/120?cb=20170502115948",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/09/Card_1014000_thumb.png/revision/latest/scale-to-width-down/120?cb=20181111033231",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/3e/Card_1011700_thumb.png/revision/latest/scale-to-width-down/120?cb=20180122093608",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/5f/Card_1018980_thumb.png/revision/latest/scale-to-width-down/120?cb=20200726045058",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/e/e2/Card_1018010_thumb.png/revision/latest/scale-to-width-down/120?cb=20190917051921",
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
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
    "<:SSR_eclair:971672682712141844> Random",
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

cualquier_sr_dokkan1 = [
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

class Tqdokkan1(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("tqdokkan1 online")

  #Comandos del bot
  @commands.command()
  async def tqdokkan1(self, ctx):
    await ctx.send("**Empezando multisummon:**")
    await ctx.send("<:SSR_eclair:971672682712141844> Featured - 3 puntos")
    await ctx.send("<:SSR_eclair:971672682712141844> No featured - 2 puntos")
    await ctx.send("<:SR_eclair:971673046496731166>  - 1 punto")
    await ctx.send( random.choice(animaciones_summons))
    puntos = 0
    for i in range(0, 7):
            numero = random.randint(1, 10000)
            if numero >= 9500:
                random2 = random.choice(featured_ssr_dokkan1)
                await ctx.send(random2)
                puntos = puntos + 3
            elif numero >= 9000:
                await ctx.send(random.choice(cualquier_ssr_dokkan1))
                puntos = puntos + 2
            elif numero >= 3000:
                await ctx.send(random.choice(cualquier_sr_dokkan1))
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
	client.add_cog(Tqdokkan1(client))