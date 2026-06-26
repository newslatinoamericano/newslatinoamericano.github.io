import feedparser
import json

bbc = feedparser.parse(
'https://feeds.bbci.co.uk/mundo/rss.xml'
)

items=[]

for noticia in bbc.entries[:5]:

    items.append(

        {

            "region":"BBC Mundo",

            "texto":noticia.title

        }

    )


with open(

'panorama.json',

'w',

encoding='utf8'

) as f:


    json.dump(

        items,

        f,

        ensure_ascii=False,

        indent=2

    )
