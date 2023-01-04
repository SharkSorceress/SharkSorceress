import ads, os
import requests
import json
# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


board_url = "https://trello.com/b/lHYXexvL/development-tasks.json"
board_reponse = requests.get(board_url)

board_json = json.loads(board_reponse.content)

for i in range(0, len(list(board_json['lists']))):
        if board_json["cards"][i]["name"] == "github-reading-list":
                card_id = board_json["cards"][i]["id"]

url = "https://trello.com/card/" + card_id + ".json"

response = requests.get(url)

reading_list = json.loads(response.content)["desc"].splitlines()

text = ""
book = ":blue_book:"
for lines in list(filter(None, reading_list)):
        if lines == "---":
                book = ":notebook_with_decorative_cover:"
        else:
                titles=lines[lines.find("[")+1:lines.find("]")]
                ads.config.token = os.environ['ADSABS_TOKEN']
                papers = list(ads.SearchQuery(q=titles, sort="year"))
                first_paper = papers[0]
                print(book + "[" + lines + "](https://ui.adsabs.harvard.edu/abs/" + first_paper.bibcode +  "/abstract)\n")
                text += str(first_paper._get_field("abstract"))

# text = ' '.join( [w for w in text.split() if "SUP" not in w] )
                
# wordcloud = WordCloud(include_numbers=False, min_word_length=3, colormap='plasma').generate(text)
# wordcloud.to_file("wordcloud.png")
# wordcloud_svg = wordcloud.to_svg("wordcloud.png")
# f = open("wordcloud.svg","w+")
# f.write(wordcloud_svg)
# f.close()
