from jinja2 import Template
from pybtex.database.input import bibtex

with open("index_template.html", "r") as f:
    site = Template(f.read())

parser = bibtex.Parser()
bib_data = parser.parse_file('papers.bib')

# Sort by year
papers = []

"""
{
        "title": "Diverse and Aligned Audio-to-Video Generation via Text-to-Video Model Adaptation",
        "authors": "Guy Yariv, Itai Gat, Sagie Benaim, Lior Wolf, Idan Schwartz, Yossi Adi",
        "venue": "arXiv, 2023",
        "links": {
            "PDF,": "https://arxiv.org/abs/2309.16429",
            "Code and Models,": "https://github.com/guyyariv/TempoTokens",
            "Website,": "https://pages.cs.huji.ac.il/adiyoss-lab/TempoTokens/"
        },
        "year": 2023,
        "bib": "str"
    }
"""
for k, paper in bib_data.entries.items():
    tmp_dict = {}
    
    tmp_dict["title"] = paper.fields["title"]
    
    authors = ""
    
    for idx, author in enumerate(paper.persons["author"]):
        authors += author.first_names[0] + " "
        authors += author.last_names[0]

        if idx != (len(paper.persons["author"]) - 1):
            authors += ", "

    tmp_dict["authors"] = authors
    
    if "journal" in paper.fields:
        tmp_dict["venue"] = paper.fields["journal"]
    elif "booktitle" in paper.fields:
        tmp_dict["venue"] = paper.fields["booktitle"]
    elif "publisher" in paper.fields:
        tmp_dict["publisher"] = paper.fields["publisher"]
    else:
        raise NotImplementedError
    
    tmp_dict["year"] = int(paper.fields["year"])
    tmp_dict["bib"] = paper.to_string('bibtex')
    tmp_dict["links"] = {}

    papers.append(tmp_dict)

for paper in papers:
    paper["authors"] = paper["authors"].replace("Tamir Hazan", "<u>Tamir Hazan</u>")

papers = sorted(papers, key=lambda x: x['year'], reverse=True)

site = site.render(papers=papers)

with open("index.html", "w") as f:
    f.write(site)
