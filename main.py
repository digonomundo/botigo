import discord
from discord import app_commands

import random
from discord.ext import commands,tasks

id_do_servidor = 741157422621786194





class SubButton(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        self.timeout=600

        botaourl = discord.ui.Button(label="Inscreva-se no Canal!",url="https://www.youtube.com/@digonomundo?sub_confirmation=1")
        self.add_item(botaourl)

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False 

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #Checar se os comandos slash foram sincronizados 
          
            await tree.sync(guild = discord.Object(id=id_do_servidor)) 
            self.synced = True
        print(f"Entramos como {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'teste', description='Testando')
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Estou funcionando!", ephemeral = True)

aclient.run('MTE1NzE2NTY0MDg2NDUxMDAyNA.Gauqx6.0E-_4Y2yxy2jgxV7Y_Ib9NwIM5no77r02-FzVc')