from django.shortcuts import render

data = [
    {
        "id": 1,
        "title": "Python for Beginners Workshop",
        "description": "A hands-on introductory workshop covering Python syntax, data types, and basic programming logic for newcomers.",
        "category": "education",
        "location": "City Library, Room 204",
        "status": "upcoming",
    },
    {
        "id": 2,
        "title": "AI & Machine Learning Summit",
        "description": "Industry experts share the latest trends in artificial intelligence, machine learning, and their real-world applications.",
        "category": "technology",
        "location": "Grand Convention Center, Hall A",
        "status": "upcoming",
    },
    {
        "id": 3,
        "title": "City Marathon 2026",
        "description": "An annual marathon event open to all skill levels, featuring 5K, 10K, and full marathon routes through downtown.",
        "category": "sport",
        "location": "Downtown Riverfront Park",
        "status": "ongoing",
    },
    {
        "id": 4,
        "title": "Jazz Night Live",
        "description": "An evening of live jazz performances featuring local and touring musicians in an intimate lounge setting.",
        "category": "entertainment",
        "location": "Blue Note Lounge",
        "status": "upcoming",
    },
    {
        "id": 5,
        "title": "Startup Pitch Competition",
        "description": "Early-stage founders pitch their startups to a panel of investors for a chance to win seed funding.",
        "category": "technology",
        "location": "Innovation Hub, Main Auditorium",
        "status": "completed",
    },
    {
        "id": 6,
        "title": "Community Charity Bazaar",
        "description": "A local fundraising event featuring food stalls, handmade crafts, and games to support community projects.",
        "category": "other",
        "location": "Central Square",
        "status": "completed",
    },
    {
        "id": 7,
        "title": "Youth Basketball Tournament",
        "description": "A regional tournament showcasing youth basketball teams competing for the annual championship trophy.",
        "category": "sport",
        "location": "Riverside Sports Complex",
        "status": "cancelled",
    },
    {
        "id": 8,
        "title": "Web Development Bootcamp",
        "description": "An intensive weekend bootcamp teaching HTML, CSS, JavaScript, and modern frameworks to aspiring developers.",
        "category": "education",
        "location": "Tech Campus, Building C",
        "status": "upcoming",
    },
    {
        "id": 9,
        "title": "Outdoor Movie Night",
        "description": "A free outdoor screening of a classic film, complete with popcorn stands and blankets under the stars.",
        "category": "entertainment",
        "location": "Sunset Park Amphitheater",
        "status": "ongoing",
    },
    {
        "id": 10,
        "title": "Cybersecurity Awareness Conference",
        "description": "A conference dedicated to educating businesses and individuals on best practices for staying safe online.",
        "category": "technology",
        "location": "Grand Convention Center, Hall B",
        "status": "upcoming",
    },
]


def index(request):
    context = {
        "events": data,
    }
    return render(request, "main/home.html", context)