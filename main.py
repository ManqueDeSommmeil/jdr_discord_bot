import discord
import os

client = discord.Client()

@client.event
async def onReady():
    print('We have logged in as {0.user}'.format(client))

# Créer un channel privée par partie de jdr par le biais d'une commande !JDR_Party

# Désigner un des participants dans le channel privée comme MJ grâce à la commande !MJ-[@discord_id]

# Ouvrir une discussion privée avec le MJ pour récupérer les fiches d'ennemis, afficher les ressources de la partie (cartes, fiches, logs des lancers de dés, résultats des combats)

# Récupérer les fiches persos et les afficher grâce à la commande Players-list dans le channel de groupe

# Prendre en compte les malus et bonus attribués par le MJ dans la RNG

# Faire les lancers de dés (ouverts ou non au choix du MJ)

# Afficher l'issue des combats dans le channel

# Son spécifique pour réussite ou échec critique

client.run(os.getenv('TOKEN'))
