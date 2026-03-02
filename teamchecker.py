from pyscript import document

def check_team(event=None):

    # Get form values from HTML
    registration = document.getElementById("regC").checked
    medical = document.getElementById("medC").checked
    grade = document.getElementById("gradeInput").value
    section = document.getElementById("sectionInput").value.lower()

    output = document.getElementById("resultBox")
    image = document.getElementById("teamPic")

    # Hide image by default
    image.style.display = "none"

    # Validate registration
    if not registration:
        output.innerText = "Please complete the online registration first."
        return

    # Validate medical clearance
    if not medical:
        output.innerText = "Please submit your medical clearance first."
        return

    # Team assignment dictionary
    teams = {
        # Yellow Tigers
        ("7", "ruby"): ("Yellow Tigers", "https://cdn.discordapp.com/attachments/1067023708180459521/1477910061182353448/tigers.png?ex=69a67a80&is=69a52900&hm=6cf7b17607d730eaf47ebbe3c374f2ddebe04a6343a5d6eb1452c0084fedb13e&"),
        ("8", "emerald"): ("Yellow Tigers", "https://cdn.discordapp.com/attachments/1067023708180459521/1477910061182353448/tigers.png?ex=69a67a80&is=69a52900&hm=6cf7b17607d730eaf47ebbe3c374f2ddebe04a6343a5d6eb1452c0084fedb13e&"),
        ("9", "sapphire"): ("Yellow Tigers", "https://cdn.discordapp.com/attachments/1067023708180459521/1477910061182353448/tigers.png?ex=69a67a80&is=69a52900&hm=6cf7b17607d730eaf47ebbe3c374f2ddebe04a6343a5d6eb1452c0084fedb13e&"),
        ("10", "sapphire"): ("Yellow Tigers", "https://cdn.discordapp.com/attachments/1067023708180459521/1477910061182353448/tigers.png?ex=69a67a80&is=69a52900&hm=6cf7b17607d730eaf47ebbe3c374f2ddebe04a6343a5d6eb1452c0084fedb13e&"),

        # Red Bulldogs
        ("7", "sapphire"): ("Red Bulldogs", "https://cdn.discordapp.com/attachments/1067023708180459521/1477910060490293488/bulldogs.png?ex=69a67a80&is=69a52900&hm=a05e5f1896988476837041f90256afed6da81fac5ac3294b5e5c7cde6c6394bc&"),
        ("8", "ruby"): ("Red Bulldogs", "https://cdn.discordapp.com/attachments/1067023708180459521/1477910060490293488/bulldogs.png?ex=69a67a80&is=69a52900&hm=a05e5f1896988476837041f90256afed6da81fac5ac3294b5e5c7cde6c6394bc&"),
        ("9", "topaz"): ("Red Bulldogs", "https://cdn.discordapp.com/attachments/1067023708180459521/1477910060490293488/bulldogs.png?ex=69a67a80&is=69a52900&hm=a05e5f1896988476837041f90256afed6da81fac5ac3294b5e5c7cde6c6394bc&"),
        ("10", "emerald"): ("Red Bulldogs", "https://cdn.discordapp.com/attachments/1067023708180459521/1477910060490293488/bulldogs.png?ex=69a67a80&is=69a52900&hm=a05e5f1896988476837041f90256afed6da81fac5ac3294b5e5c7cde6c6394bc&"),

        # Blue Bears
        ("7", "emerald"): ("Blue Bears", "https://media.discordapp.net/attachments/1067023708180459521/1477910060150689823/bears.png?ex=69a67a80&is=69a52900&hm=2467b14e92c6788d90ebe0d74866c28559d718ddf8448d849b11a2960bd2c536&=&format=webp&quality=lossless&width=321&height=266"),
        ("8", "topaz"): ("Blue Bears", "https://media.discordapp.net/attachments/1067023708180459521/1477910060150689823/bears.png?ex=69a67a80&is=69a52900&hm=2467b14e92c6788d90ebe0d74866c28559d718ddf8448d849b11a2960bd2c536&=&format=webp&quality=lossless&width=321&height=266"),
        ("8", "jade"): ("Blue Bears", "https://media.discordapp.net/attachments/1067023708180459521/1477910060150689823/bears.png?ex=69a67a80&is=69a52900&hm=2467b14e92c6788d90ebe0d74866c28559d718ddf8448d849b11a2960bd2c536&=&format=webp&quality=lossless&width=321&height=266"),
        ("9", "ruby"): ("Blue Bears", "https://media.discordapp.net/attachments/1067023708180459521/1477910060150689823/bears.png?ex=69a67a80&is=69a52900&hm=2467b14e92c6788d90ebe0d74866c28559d718ddf8448d849b11a2960bd2c536&=&format=webp&quality=lossless&width=321&height=266"),
        ("10", "topaz"): ("Blue Bears", "https://media.discordapp.net/attachments/1067023708180459521/1477910060150689823/bears.png?ex=69a67a80&is=69a52900&hm=2467b14e92c6788d90ebe0d74866c28559d718ddf8448d849b11a2960bd2c536&=&format=webp&quality=lossless&width=321&height=266"),

        # Green Hornets
        ("7", "jade"): ("Green Hornets", "https://cdn.discordapp.com/attachments/1067023708180459521/1477910060834230373/hornets.png?ex=69a67a80&is=69a52900&hm=b654ac991ee5cfd86b1984ff3fa850dc35679ad6a723d5c530b5ceb4d8e3be4b&"),
        ("9", "emerald"): ("Green Hornets", "https://cdn.discordapp.com/attachments/1067023708180459521/1477910060834230373/hornets.png?ex=69a67a80&is=69a52900&hm=b654ac991ee5cfd86b1984ff3fa850dc35679ad6a723d5c530b5ceb4d8e3be4b&"),
        ("10", "ruby"): ("Green Hornets", "https://cdn.discordapp.com/attachments/1067023708180459521/1477910060834230373/hornets.png?ex=69a67a80&is=69a52900&hm=b654ac991ee5cfd86b1984ff3fa850dc35679ad6a723d5c530b5ceb4d8e3be4b&"),
    }

    # Check if the selected combination exists
    if (grade, section) in teams:

        team, img = teams[(grade, section)]

        # Display team assignment message
        output.innerText = f"You have been successfully assigned to {team}. Welcome to the Intramurals!"

        # Display team image
        image.src = img
        image.style.display = "block"

    else:
        output.innerText = "Invalid grade and section combination. Please try again."