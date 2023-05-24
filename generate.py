from jinja2 import Template

# news = [
#     ("fa-newspaper-o",
#      "Our model AudioGen, which generates audio from textual descriptions got some attention from the media: [<a href='https://www.newscientist.com/article/2341416-metas-text-to-audio-ai-can-create-common-sounds-and-generate-music/' target='blank'>New Scientist</a>]."),
#     ("fa-book", "Our research paper <a href='https://arxiv.org/pdf/2111.07402.pdf' target='blank'><em>Textless Speech Emotion Conversion using Decomposed and Discrete Representations</em></a> was accepted to EMNLP 2022!"),
#     ("fa-microphone",
#      "Our model AudioGen, was covered by Aleksa Gordić: [<a href='https://www.youtube.com/watch?v=RyIn-DxGF-c'>YouTube</a>]."),
#     ("fa-book", "4 papers accapted to INTERSPEECH 2022! More details in publications section."),
#     ("fa-book", "Our paper <a href='https://ieeexplore.ieee.org/document/9747953'><em>Speech Time-Scale Modification With GANs</em></a> was accapted to IEEE Signal Processing Letters 2022!"),
#     ("fa-trophy", "Started as a full-time Research Engineer at Meta AI Research"),
#     ("fa-microphone",
#      "Invited talk at <a href='https://homepages.inf.ed.ac.uk/htang2/sigml/seminar/'>ISCA SIGML Seminar<a>, [<a href='https://www.youtube.com/watch?v=gk6thCWl_eE'>Video</a>]."),
# ]

papers = [
    {
        "title": "<b>Textually Pretrained Speech Language Models</b>",
        "authors": "Michael Hassid, Tal Remez, Tu Anh Nguyen, Itai Gat, Alexis Conneau, Felix Kreuk, Jade Copet, Alexandre Defossez, Gabriel Synnaeve, Emmanuel Dupoux, Roy Schwartz, Yossi Adi",
        "venue": "arXiv, 2023",
        "links": {
            "PDF,": "https://arxiv.org/abs/2305.13009",
            "Samples": "https://pages.cs.huji.ac.il/adiyoss-lab/twist/",
        },
        "year": 2023,
    },
    {
        "title": "AudioToken: Adaptation of Text-Conditioned Diffusion Models for Audio-to-Image Generation",
        "authors": "Guy Yariv, Itai Gat, Lior Wolf, Yossi Adi, Idan Schwartz",
        "venue": "arXiv, 2023",
        "links": {
            "PDF,": "https://arxiv.org/abs/2305.13050",
            "Page,": "https://pages.cs.huji.ac.il/adiyoss-lab/AudioToken/",
            "Code": "https://github.com/guyyariv/AudioToken",
        },
        "year": 2023,
    },
    {
        "title": "Layer Collaboration in the Forward-Forward Algorithm",
        "authors": "Guy Lorberbom*, Itai Gat*, Yossi Adi, Alex Schwing, Tamir Hazan",
        "venue": "arXiv, 2023",
        "links": {
            "PDF": "https://arxiv.org/abs/2305.12393",
        },
        "year": 2023,
    },
    {
        "title": "On the Importance of Gradient Norm in PAC-Bayesian Bounds",
        "authors": "Itai Gat, Yossi Adi, Alex Schwing, Tamir Hazan",
        "venue": "Advances in Neural Information Processing Systems (NeurIPS), 2022",
        "links": {
            "PDF": "https://proceedings.neurips.cc/paper_files/paper/2022/file/6686e3f2e31a0db5bf90ab1cc2272b72-Paper-Conference.pdf",
        },
        "year": 2022,
    },
    {
        "title": "On The Robustness of Self-Supervised Representations for Spoken Language Modeling",
        "authors": "Itai Gat, Felix Kreuk, Ann Lee, Jade Copet, Gabriel Synnaeve, Emmanuel Dupoux, Yossi Adi",
        "venue": "arXiv, 2022",
        "links": {
            "PDF": "https://arxiv.org/abs/2209.15483",
        },
        "year": 2022,
    },
    {
        "title": "A Functional Information Perspective on Model Interpretation",
        "authors": "Itai Gat, Nitay Calderon, Roi Reichart, Tamir Hazan",
        "venue": "Proceedings of the International Conference on Machine Learning (ICML), 2022",
        "links": {
            "PDF": "https://proceedings.mlr.press/v162/gat22a/gat22a.pdf",
        },
        "year": 2022,
    },
    {
        "title": "Speech Emotion Recognition using Self-Supervised Features",
        "authors": "Edmilson Morais, Ron Hoory, Weizhong Zhu, Itai Gat, Matheus Damasceno, Hagai Aronowitz",
        "venue": "IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2022",
        "links": {
            "PDF": "https://arxiv.org/abs/2202.03896",
        },
        "year": 2022,
    },
    {
        "title": "Speaker Normalization for Self-supervised Speech Emotion Recognition",
        "authors": "Itai Gat, Nitay Calderon, Roi Reichart, Tamir Hazan",
        "venue": "IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2022",
        "links": {
            "PDF": "https://arxiv.org/abs/2202.01252",
        },
        "year": 2022,
    },
    {
        "title": "Towards a Common Speech Analysis Engine",
        "authors": "Hagai Aronowitz, Itai Gat, Edmilson Morais, Weizhong Zhu, Ron Hoory",
        "venue": "IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2022",
        "links": {
            "PDF": "https://arxiv.org/abs/2203.00613",
        },
        "year": 2022,
    },
    {
        "title": "Latent Space Explanation by Intervention",
        "authors": "Itai Gat*, Guy Lorberbom*, Idan Schwartz, Tamir Hazan",
        "venue": "Proceedings of the AAAI Conference on Artificial Intelligence, 2021",
        "links": {
            "PDF": "https://ojs.aaai.org/index.php/AAAI/article/view/19948",
        },
        "year": 2021,
    },
    {
        "title": "Perceptual Score: What Data Modalities Does Your Model Perceive?",
        "authors": "Itai Gat, Idan Schwartz, Alexander Schwing",
        "venue": "Advances in Neural Information Processing Systems (NeurIPS), 2021",
        "links": {
            "PDF,": "https://proceedings.neurips.cc/paper/2021/file/b51a15f382ac914391a58850ab343b00-Paper.pdf",
            "Code": "https://github.com/itaigat/perceptual-score"
        },
        "year": 2021,
    },
    {
        "title": "Are VQA Systems RAD? Measuring Robustness to Augmented Data with Focused Interventions",
        "authors": "Daniel Rosenberg, Itai Gat, Amir Feder, Roi Reichart",
        "venue": "Association for Computational Linguistics (ACL), 2021",
        "links": {
            "PDF,": "https://arxiv.org/abs/2106.04484",
            "Website": "https://danrosenberg.github.io/rad-measure/"
        },
        "year": 2021,
    },
    {
        "title": "Removing Bias in Multi-modal Classifiers: Regularization by Maximizing Functional Entropies",
        "authors": "Itai Gat, Idan Schwartz, Alexander Schwing, Tamir Hazan",
        "venue": "Advances in Neural Information Processing Systems (NeurIPS), 2020",
        "links": {
            "PDF,": "https://proceedings.neurips.cc/paper/2020/file/20d749bc05f47d2bd3026ce457dcfd8e-Paper.pdf",
            "Code": "https://github.com/itaigat/removing-bias-in-multi-modal-classifiers"
        },
        "year": 2020,
    },

]

with open("index_template.html", "r") as f:
    site = Template(f.read())

for paper in papers:
    paper["authors"] = paper["authors"].replace("Itai Gat", "<u>Itai Gat</u>")

site = site.render(papers=papers)

with open("index.html", "w") as f:
    f.write(site)
