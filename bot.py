import discord
import random
from discord.ext import commands, tasks

# INSIRA AQUI O TOKEN DO SEU BOT
token = ""

intents = discord.Intents.default()
intents.all()

# AQUI A VARIAVEL PARA A MANIPULAÇÃO DO BOT É CRIADO E É DEFINIDO UM PREFIXO
bot = commands.Bot(command_prefix="!", intents=intents)

# AQUI EU INSERI OS XINGAMENTOS FALADOS PELO BOT, É POSSIVEL ALTERAR OU ADICIONAR MAIS
insultos = [
    "quem que te gozou?",
    "mama na sombra.",
    "cu de apertar linguiça.",
    "famoso espanta-xereca.",
    "nunca viu um par de seios.",
    "calvo.",
    "nunca recebeu amor familiar.",
    "ta querendo mamar",
    "ta com cuzin pedindo pica.",
]

# AQUI É DEFINIDO O INCIO DO BOT, SE TUDO DER CERTO, O PRINT APARECE NO CONSOLE, MOSTRANDO QUE O BOT FUNCIONOU


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user.name}")
    insulto_diario.start()


# AQUI FUTURAMENTE VAI ENTRAR UM INSERT COMMAND


# AQUI É DEFINIDO DE QUANTO EM QUANTO TEMPO O BOT VAI FUNCIONAR, PODE ALTERAR O TEMPO DENRO DA VARIAVEL "HOURS"
@tasks.loop(hours=None)
async def insulto_diario():

    # AQUI VOCÊ COLOCA O ID DO SEU SERVIDOR QUE VOCÊ QUE USAR O BOT
    guild = bot.get_guild()

    # AQUI É ONDE A SELEÇÃO DO MEMBRO DO DISCORD ACONTECE
    if guild:
        try:

            membro_aleatorio = random.choice(guild.members)

            insulto = random.choice(insultos)

            # SE QUISER MUDAR O CANAL ONDE O BOT VAI AGIR, É SO COLOCAR O NOME DO CANAL DENTRO DA VARIAVEL "name"
            channel = discord.utils.get(guild.text_channels, name="")

            if channel:
                await channel.send(f"{membro_aleatorio.mention} {insulto}")
        except Exception as e:
            print(f"Erro na tarefa insulto_diario: {type(e).__name__} - {e}")


bot.run(token)
