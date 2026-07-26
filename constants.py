# Profile -------------------------------------------------------------------------------------------------------------------------------------
profile = {
            'name':'Jan Michael Aoay', 
            'title': 'Python Developer & Machine Learning Engineer',
            'image_path': 'https://github.com/Nangaaoay246/Portfolio/blob/main/assets/profile1.jpg?raw=true',
            "location": '🌏 Cavite, Philippines',
            "email": '✉️ aoay.janmichael@gmail.com',
            "phone": '📞 0976 339 2122'
        }

# Social Media Links ------------------------------------------------------------------------------------------------------------------------
links = [
    {
        "name": "LinkedIn",
        "url": "https://www.linkedin.com/in/jan-michael-aoay/",
        "icon": "fab fa-linkedin"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/Nangaaoay246",
        "icon": "fab fa-github"
    },
    {
        "name": "Google Scholar",
        "url": "https://scholar.google.com/citations?user=ttu2404AAAAJ&hl=en&authuser=2",
        "icon": "fab fa-google"
    },
    {
        "name": "Portfolio",
        "url": "https://portfolio-nangaaoay.streamlit.app/",
        "icon": "fab fa-at"
    }
]

page_content = {
    'ProjectOverview_1': """
As a newly minted young adult (read: fresh graduate), I’ve been spending most of my time signing up for banks and e-wallets where I can store my future (read: currently non-existent) salary once I finally start working. Lately, :blue[**BDO**] and :orange[**MariBank**] have become my go-tos. Keeping most of my allowance in digital wallets really hammered home just how cashless the Philippines has become.
    """,

    'ProjectOverview_2': """ 
These days, I rarely carry cash whenever I leave the house. Maybe I’ll bring a hundred and fifty pesos in my :green[**smiski**]-keychained wallet; just enough to cover my daily commute to and from Manila. Everything else? I have it on my phone. Whether I’m buying coffee from :red[**Kape Kuripot**], grabbing lunch in :yellow[**McDo**], or stopping by :blue[**Lawson**] to grab myself a bottle of Mogu-mogu, my default question is always, **"Ate, may QR po?"** A quick scan, a few taps, and I'm done. It’s so seamless that I stopped thinking about the mechanics behind it.
    """,

    'ProjectOverview_3': """ 
    ...But, that convenience comes with a catch.

Behind every :blue[**instant**] :red[**transfer**] lies a massive financial pipeline that processes millions upon millions of transactions daily. As more Filipinos go digital, the surface area for fraud grows right alongside us. The very tech that makes paying for coffee effortless also gives scammers a platform to exploit a lot of people.
    """,
    'projectOverview_4': """
That realization was the spark for this project. While we only experience the slick, two-second front end of a digital payment, financial institutions are running a non-stop triage behind the scenes to separate legitimate transfers from scams.

To explore how banks can tackle this, this project compares the effectiveness of `Logistic Regression`, `Decision Trees`, and `Random Forest` models in classifying fraudulent behavior using standard transactional data available to banks.
    """,
    'problemStatement': """
    Every seamless “tap-and-go” transaction conceals months (and probably even years!) of infrastructure built to answer one question: **is this real, or is someone about to loose their hard-earned money?**

In this dataset alone, fraud makes up just **0.13%** of over 6.3 million transactions; that’s roughly about **8,197 cases** buried among a sea of legitimate transfers. What’s worse is that it doesn't show up evenly either; fraud only appears in `TRANSFER` and `CASH_OUT` transactions, the exact kind of movement that mirrors sending money to a friend, paying rent, or, worse, an unverified scammer's account.

This is the needle-in-a-haystack problem banks are up against. Flag too aggressively, and you're interrupting me buying some much-needed Mogu-mogu from the Ate at Lawson; flag too passively, and fraudulent transfers slip through the cracks, dressed up as an ordinary transaction, indistinguishable from the other **99.87%**.
    """,
    'businessObjective': """
The goal of this project is to build and compare three models, `Logistic Regression`, `Decision Tree`, and `Random Forest`, that can reliably separate fraudulent transfers from legitimate ones using only the transactional data banks already have on hand (amount, balances before and after, transaction type).

Accuracy is basically useless here (a model that predicts “:green[legitimate]” every single time would still be right 99.87% of the time), so the real objective isn’t a high accuracy score. It’s a model that:

- Catches as many real fraud cases as possible (recall)

- Without burying analysts in false alarms (precision)

- Holds up under a heavily imbalanced dataset, judged through PR-AUC rather than accuracy alone.

In short, this isn’t just about picking the “best” algorithm on paper. It’s about finding the model a bank could actually deploy, one that protects people’s money without flagging every legitimate :red[Kape Kuripot] run as a crime.
    """,
    'modelEvaluation': """
    With fraud at **~0.13%** of transactions, accuracy is not useful (predicting "not fraud" every time would score ~99.9%). Instead we prioritize:

- **`Recall` (of the fraud class)** - Out of all real fraud cases, how many did we catch?
- **`Precision` (of the fraud class)** - Out of everything we flagged as fraud, how many actually were?
- **`F1-score`** - A single score that balances both Precision and Recall.
- **`PR-AUC` (Average Precision)** - Measures overall model performance amidst heavy class imbalance
    """
}

