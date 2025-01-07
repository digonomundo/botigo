import discord
from discord import app_commands
import os

id_do_servidor = 741157422621786194

class SubButton(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        self.timeout = 600

        botaourl = discord.ui.Button(
            label="Inscreva-se no Canal!",
            url="https://www.youtube.com/@digonomundo?sub_confirmation=1"
        )
        self.add_item(botaourl)

class Client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)
        self.synced = False

    async def setup_hook(self):
        if not self.synced:
            await self.tree.sync(guild=discord.Object(id=id_do_servidor))
            self.synced = True

    async def on_ready(self):
        print(f"Entramos como {self.user}.")

aclient = Client()

# Definindo um comando slash
@aclient.tree.command(
    guild=discord.Object(id=id_do_servidor),
    name="teste",
    description="Testando"
)
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message("Estou funcionando!", ephemeral=True)

# Executando o bot
if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    if not TOKEN:
        print("Token não encontrado. Configure a variável de ambiente DISCORD_BOT_TOKEN.")
    else:
        try:
            aclient.run(TOKEN)
        except Exception as e:
            print(f"Erro ao executar o bot: {e}")
