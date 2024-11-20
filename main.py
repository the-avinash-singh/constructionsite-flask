from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    data=[{},{},{}]
    matterData=[
        {
        "heading":"Quiet Spaces",
        "title":"Low-noise neighborhood for calm living."
    },
        {
        "heading":"Clean Air Localities",
        "title":"Escape the city smog and enjoy suburban living."
    },
        {
        "heading":"Rental Income Properties",
        "title":"Own it, we'll handel the rent. You just sit back and enjoy."
    },
        {
        "heading":"Gourmet Neighborhoods",
        "title":"Food lovers, your home is here."
    },
        {
        "heading":"Metro-Connected Homers",
        "title":"Convenient living, just steps away from the metro."
    },
        {
        "heading":"EV-Friendly Areas",
        "title":"Neighborhoods with electric vehicle charging stations."
    },
    ]
    letFindData=[
        "Bangalore",
        "Pune",
        "Delhi",
        "Mumbai",
        "Hyderabad",
        "Chennai (Coming-soon!)"
    ]
    browseBtnData=[
        "Fresh off the market",
        "Ready-to-move- in homes",
        "Luxury Living",
        "Pocket friendly properties",
        "Bachlor pads",
        "Gently used properties"
    ]
    redefineData=[
        "Dubai",
        "Londan",
        "Middle East"
    ]
    bestData=[
        {
            "heading":"ProPr:",
            "title":"Your dream home, handpicked by All!",
            "body":"Take our home-matching quiz and let the ProPr read your mind and match you future address."
        },
        {
            "heading":"Worry-Free:",
            "title":"Property Management: your Home, our headache.",
            "body":"we'll manage your property while you manage your time."
        },
        {
            "heading":"Refer & Relax:",
            "title":"Spread the buzz, cash in on the fun!",
            "body":"Earn Amazon vouchers, vacations, or even a home makeover-just by referring a friend!"
        }
    ]
    return render_template("index.html" ,
                           apiData=data, 
                           matterData=matterData, 
                           letFindData=letFindData, 
                           browseBtnData=browseBtnData,
                           redefineData=redefineData,
                           bestData=bestData,
                           )