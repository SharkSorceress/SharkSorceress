import ads, os

f = open("reading/reading.txt", "r")
book = ":blue_book:"
for lines in f.readlines():
        if lines == "---\n":
                book = ":notebook_with_decorative_cover:"
        else:
                titles=lines[lines.find("[")+1:lines.find("]")]
                ads.config.token = os.environ['ADSABS_TOKEN']
                papers = list(ads.SearchQuery(q=titles, sort="year"))
                first_paper = papers[0]
                print(book + "[" + lines + "](https://ui.adsabs.harvard.edu/abs/" + first_paper.bibcode +  "/abstract)\n")
