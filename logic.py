import random as r, string as s, os, discord

def contra(largo):
    elements = s.ascii_letters+s.ascii_lowercase+s.ascii_uppercase+s.digits+s.punctuation
    password = ""

    for i in range(largo):
        password += r.choice(elements)
    return password

def gen_emoji():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return r.choice(emoji)

def moneda():
    flip = r.randint(0, 2)
    if flip == 0:
        return "Cara"
    else:
        return "Cruz"

def meme():
    with open("IMG/Decisiones.jpg", "rb") as IMG:
        pic = discord.File(IMG)
    return pic

def momasos():
    listmeme = r.choice(os.listdir("img"))
    with open(f"IMG/{listmeme}", "rb") as IMG:
        pic = discord.File(IMG)
    return pic