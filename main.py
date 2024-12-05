from flask import Flask,render_template, jsonify

app=Flask(__name__)

data=[{},{},{}]
matterData=[
        {
        "heading":"Quiet Spaces",
        "title":"Low-noise neighborhood for calm living.",
        "filter":"quite-space"
    },
        {
        "heading":"Clean Air Localities",
        "title":"Escape the city smog and enjoy suburban living.",
        "filter":"clean-air"
    },
        {
        "heading":"Rental Income Properties",
        "title":"Own it, we'll handel the rent. You just sit back and enjoy.",
        "filter":"rental-income"
    },
        {
        "heading":"Gourmet Neighborhoods",
        "title":"Food lovers, your home is here.",
        "filter":"gourmet"
    },
        {
        "heading":"Metro-Connected Homers",
        "title":"Convenient living, just steps away from the metro.",
        "filter":"metro"
    },
        {
        "heading":"EV-Friendly Areas",
        "title":"Neighborhoods with electric vehicle charging stations.",
        "filter":"ev-friedly"
    },
    ]
letFindData=[
        {
            "text":"Bangalore",
            "filter":"Bangalore"
        },
        {"text":"Pune",
         "filter":"Pune"
        },
        {"text":"Delhi",
         "filter":"Delhi"
         },
        {"text":"Mumbai",
         "filter":"Mumbai"
         },
        {"text":"Hyderabad",
         "filter":"Hyderabad"
         },
        {"text":"Chennai (Coming-soon!)",
         "filter":"Chennai"
         }
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
cardData=[
    {
        "buildingName": "Express Astra",
        "builderName": "Express Builders",
        "builderAdd": "Greater Noida West, Noida",
        "buildArea": "1150",
        "minPrice": "1",
        "maxPrice": "5",
        "filter": ["quite-space", "ev-friedly", "clean-air", "metro", "Bangalore"]
    },
    {
        "buildingName": "Elite Enclave",
        "builderName": "Prestige Group",
        "builderAdd": "Sector 62, Gurgaon",
        "buildArea": "1450",
        "minPrice": "2",
        "maxPrice": "4",
        "filter": ["clean-air", "metro", "rental-income", "Delhi"]
    },
    {
        "buildingName": "Orchid Greens",
        "builderName": "DLF Builders",
        "builderAdd": "Sector 76, Noida",
        "buildArea": "1650",
        "minPrice": "3",
        "maxPrice": "6",
        "filter": ["gourmet", "quite-space", "clean-air", "Mumbai"]
    },
    {
        "buildingName": "Maple Residency",
        "builderName": "Godrej Properties",
        "builderAdd": "Whitefield, Bangalore",
        "buildArea": "1200",
        "minPrice": "1.5",
        "maxPrice": "3",
        "filter": ["rental-income", "ev-friedly", "gourmet", "Hyderabad"]
    },
    {
        "buildingName": "Rosewood Villas",
        "builderName": "Tata Housing",
        "builderAdd": "Panvel, Mumbai",
        "buildArea": "1900",
        "minPrice": "4",
        "maxPrice": "8",
        "filter": ["gourmet", "clean-air", "quite-space", "metro", "Chennai"]
    },
    {
        "buildingName": "Cedar Heights",
        "builderName": "Sobha Developers",
        "builderAdd": "Bannerghatta, Bangalore",
        "buildArea": "1400",
        "minPrice": "2.5",
        "maxPrice": "5",
        "filter": ["quite-space", "metro", "rental-income", "ev-friedly", "Pune"]
    },
    {
        "buildingName": "Emerald Court",
        "builderName": "Jaypee Group",
        "builderAdd": "Sector 128, Noida",
        "buildArea": "1750",
        "minPrice": "3",
        "maxPrice": "6",
        "filter": ["rental-income", "clean-air", "gourmet", "Delhi"]
    },
    {
        "buildingName": "Silver Mist",
        "builderName": "Brigade Group",
        "builderAdd": "Electronic City, Bangalore",
        "buildArea": "1500",
        "minPrice": "2",
        "maxPrice": "4",
        "filter": ["ev-friedly", "metro", "quite-space", "Chennai"]
    },
    {
        "buildingName": "Amber Residences",
        "builderName": "Lodha Group",
        "builderAdd": "Thane, Mumbai",
        "buildArea": "1300",
        "minPrice": "2.5",
        "maxPrice": "5.5",
        "filter": ["clean-air", "quite-space", "metro", "Bangalore"]
    },
    {
        "buildingName": "Golden Horizon",
        "builderName": "Mahindra Lifespaces",
        "builderAdd": "Gachibowli, Hyderabad",
        "buildArea": "1250",
        "minPrice": "1.2",
        "maxPrice": "3.5",
        "filter": ["gourmet", "metro", "clean-air", "ev-friedly", "Mumbai"]
    },
    {
        "buildingName": "Pearl Residency",
        "builderName": "Shapoorji Pallonji",
        "builderAdd": "Kolkata South, Kolkata",
        "buildArea": "1600",
        "minPrice": "2",
        "maxPrice": "4",
        "filter": ["rental-income", "ev-friedly", "quite-space", "Pune"]
    },
    {
        "buildingName": "Crystal Homes",
        "builderName": "Piramal Realty",
        "builderAdd": "Andheri, Mumbai",
        "buildArea": "1800",
        "minPrice": "3.5",
        "maxPrice": "7",
        "filter": ["gourmet", "quite-space", "clean-air", "Hyderabad"]
    },
    {
        "buildingName": "Platinum Towers",
        "builderName": "Raheja Developers",
        "builderAdd": "MG Road, Gurgaon",
        "buildArea": "1350",
        "minPrice": "1.8",
        "maxPrice": "3.6",
        "filter": ["metro", "clean-air", "ev-friedly", "Delhi"]
    },
    {
        "buildingName": "Azure Villas",
        "builderName": "Hiranandani Group",
        "builderAdd": "Powai, Mumbai",
        "buildArea": "2100",
        "minPrice": "5",
        "maxPrice": "10",
        "filter": ["ev-friedly", "quite-space", "clean-air", "Chennai"]
    },
    {
        "buildingName": "Opal Heights",
        "builderName": "Oberoi Realty",
        "builderAdd": "Goregaon, Mumbai",
        "buildArea": "2000",
        "minPrice": "4.5",
        "maxPrice": "9",
        "filter": ["clean-air", "rental-income", "gourmet", "quite-space", "Pune"]
    },
    {
        "buildingName": "Ivory Towers",
        "builderName": "Century Builders",
        "builderAdd": "Sector 49, Gurgaon",
        "buildArea": "1550",
        "minPrice": "2.3",
        "maxPrice": "4.8",
        "filter": ["metro", "rental-income", "clean-air", "ev-friedly", "Bangalore"]
    }
]

filterData=[
        {
            "name":"No. of Bedrooms",
            "icon":"fa-solid fa-bed",
            "body":[
                {
                 "type":"1 BHK",
                },
                {
                "type":"2 BHK",
                },
                {
                "type":"3 BHK",
                },
                {
                "type":"4 BHK",
                },
                {
                "type":"5 BHK",
                }
                ],
            "type":"btn"
        },
        {
            "name":"Property Type",
            "icon":"fa-solid fa-building",
            'type':"btn",
            "body":[
                {
        "type":"Quiet Spaces",
        "filter":"quite-space"
    },
        {
        "type":"Clean Air Localities",
        "filter":"clean-air"
    },
        {
        "type":"Rental Income Properties",
        "filter":"rental-income"
    },
        {
        "type":"Gourmet Neighborhoods",
        "filter":"gourmet"
    },
        {
        "type":"Metro-Connected Homers",
        "filter":"metro"
    },
        {
        "type":"EV-Friendly Areas",
        "filter":"ev-friedly"
    },
    ]
        },
        {
            "name":"Budget",
            "icon":"fa-solid fa-sack-dollar",
            "type":"range"
        },
        {
            "name":"Possission",
            "icon":"fa-solid fa-shop",
            "type":"btn",
            "body":[
                  {
                        "type":"Actual Possession",
                  },
                  {
                        "type":"Lease",
                  },
                  {
                        "type":"Joint Possession",
                  },
                  {
                        "type":"Sole Ownership",
                  },
                  {
                        "type":"Immediate Possession",
                  },
                  {
                        "type":"Vested Ownership",
                  },
            ],
        },
        {
            "name":"More Filter",
            "icon":"fa-solid fa-sliders",
        },
    ]
events = [
    {"title": "Morning Connect", "start": "2024-12-25T02:00:00", "end": "2024-12-25T02:30:00","color":" #CCCCFF"},
    {"title": "Evening Connect", "start": "2024-12-25T02:30:00", "end": "2024-12-25T03:00:00", "color":"red"},
    {"title": "Morning Connect", "start": "2024-12-05T02:00:00", "end": "2024-12-05T02:30:00","color":" #CCCCFF"},
    {"title": "Here is a link", "start": "2024-12-06T02:30:00", "end": "2024-12-06T03:00:00", "color":"green",'url':"www.google.com",},
    {"title": "Morning Connect", "start": "2024-12-07T02:00:00", "end": "2024-12-07T02:30:00","color":"yellow"},
    {"title": "Evening Connect", "start": "2024-12-08T02:30:00", "end": "2024-12-08T03:00:00", "color":"#98A869"},
    ]

@app.route('/')
def home():
        return render_template("index.html" ,
                           apiData=data, 
                           matterData=matterData, 
                           letFindData=letFindData, 
                           browseBtnData=browseBtnData,
                           redefineData=redefineData,
                           bestData=bestData,
                           cssFileName="page.css",
                           title="Construction Site",
                           events=events,
                           )

@app.route('/filter/<string:filter>')
def filter(filter):
    if(filter=='all'):
           return render_template(
                'cityListPage.html',
                cardData=cardData,
                filterData=filterData,
                cssFileName="city.css",
                title="Construction site: location"
           )
    filteredCardData = [property for property in cardData if filter in property['filter']]
    return render_template(
             'cityListPage.html',
             cardData=filteredCardData,
             filterData=filterData,
             cssFileName="city.css",
             title="Construction site: location"
            )

@app.route("/login")
def login():
      return render_template(
           "login.html",
            cssFileName="login.css",
            title="Construction Site"
        )