from pyscript import document
# Function that displays the players of a selected team
# team_name = name of the team (string)
# players = list of players belonging to that team
def display_players(team_name, players):

    output = document.getElementById("playerList")

    output.innerHTML = f"<h5 class='mt-3'>{team_name}</h5>"

    if len(players) == 0:
        output.innerHTML += "<p>No players added yet.</p>"
        return

    output.innerHTML += "<ul>"

    for player in players:
        output.innerHTML += f"<li>{player}</li>"

    output.innerHTML += "</ul>"


# PLAYERS FROM GRADE 10 BATCH

yellow_tigers = [
    "Balagat, Michael",
    "Bernardo, Miko",
    "Caguiron, Carriena",
    "Calida, Lorenzo",
    "Chan, Jazmar",
    "Cruz, Rohann",
    "David, Antonio",
    "De Guzman, Uno",
    "De Guzman, Nia",
    "Francisco, Annika",
    "Kaur, Navjot",
    "Laconsay, Heleina",
    "Lepasana, Khen",
    "Lopez, Liam",
    "Lucman, Mohammad",
    "Malapitan, Caleb",
    "Manahan, Samantha",
    "Manuel, Elyze",
    "Mendoza, Matthew",
    "Palafox, Coby",
    "Ramirez, Alfiona",
    "Reynoso, Izeck",
    "Santos, Cas",
    "Santos, Rafaela",
    "Tolentino, Kelsey",
    "Toribio, Sasha",
    "Valdez, David"
]   

red_bulldogs = [
    "Agudo, Jairo",
    "Alaiza, Mikko",
    "Al Hazmi, Naser",
    "Banaag, Matthew",
    "Barcelona, Emille",
    "Brion, Cyrene",
    "Buo, Miguel",
    "Castro, Lian",
    "Cruz, Shia",
    "Del Prado, KC",
    "Entrada, Gianna",
    "Francisco, Gavin",
    "Gavina, Adrian",
    "Goyenechea, Xylee",
    "Guevarra, Sofia",
    "Haberia, Ioana",
    "Janayan, Alexander",
    "Libutan, Jabez",
    "Lubo, Arabella",
    "Manuel, Luisa",
    "Mariposque, Janine",
    "Pagtalunan, Rycob",
    "Reyes, Lucas",
    "Singh, Fateh",
    "Subaan, Tyronne",
    "Tan, Audrey",
    "Vargas, Alexandra",
    "Zaldivar, James"
]

blue_bears = [
    "Andes, Jake",
    "Ayala, Fil",
    "Cabrillos, Martina",
    "Daed, Mary",
    "Damondamon, Gabrielle",
    "De Jesus, Mike",
    "Deray, Joseph",
    "Dumaguing, Audrey",
    "Ecraela, Pauline",
    "Escarda, Giovanni",
    "Fabul, Zion",
    "Ferrer, Margaux",
    "Gorom, Vic",
    "Grande, Nathan",
    "Ligas, John",
    "Manese, Marley",
    "Mendez, Cyrenne",
    "Noble, Danielle",
    "Salapunen, Riso",
    "Santos, Ashley",
    "Tacan, Alexander",
    "Taruc, John",
    "Tenorio, Kurt",
    "Tiongson, Nathan",
    "Ubana, Aurora",
    "Villanueva, Aelxi",
    "Zales, Jarix"
]

green_hornets = [
    "Al Hazmi, Ebtisam",
    "Alvarez, Aeiou",
    "Belsa, Ethan",
    "Bernas, Giana",
    "Calaycay, Julianna",
    "Castelo, Jamila",
    "Cruz, Francesca",
    "Defensor, Ely",
    "Dimasuhid, Danielle",
    "Francisco, Althea",
    "Hsu, Cristina",
    "Juatchon, Denise",
    "Judge, Judah",
    "Lilagan, Francis",
    "Luna, Sam",
    "Macaranas, Enzo",
    "Mateo, Pain",
    "Mondragon, Ashley",
    "Naldoza, Lance",
    "Natividad, Gabriel",
    "Ng, Sofia",
    "Ong, Hendrich",
    "Paz, Trisha",
    "Ramos, Miguel",
    "Ramos, Queeny",
    "Ramos, Samantha",
    "Reodica, Ashlei",
    "Repolona, Vaughn"
]



# Button Functions

def show_yellow(event=None):
    display_players("Yellow Tigers", yellow_tigers)

def show_red(event=None):
    display_players("Red Bulldogs", red_bulldogs)

def show_blue(event=None):
    display_players("Blue Bears", blue_bears)

def show_green(event=None):
    display_players("Green Hornets", green_hornets)