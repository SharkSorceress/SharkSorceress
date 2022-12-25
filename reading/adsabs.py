import ads, os

f = open("reading/reading.txt", "r")
for lines in f.readlines():
        titles=lines[lines.find("[")+1:lines.find("]")]
        ads.config.token = os.environ['ADSABS_TOKEN']
        papers = list(ads.SearchQuery(q=titles, sort="year"))
        first_paper = papers[0]
        print("[" + lines + "](https://ui.adsabs.harvard.edu/abs/" + first_paper.bibcode +  "/abstract)")


