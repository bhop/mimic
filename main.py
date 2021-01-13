import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=("!"), self_bot=True) # change prefix to what you want

token = "your token"  # your token goes here


@bot.event
async def on_ready():
    print("Ready")

@bot.command()
async def copy(ctx, member: discord.Member, times: int):
   
    print(f"Copying {member} {times} times.")
    await ctx.message.delete()
    
    
    def check(m):
        try:
            return m.author == member and not m.stickers and not m.attachments
        except commands.NotFound:
            return False

    for i in range(times):
        msg = await bot.wait_for('message', check=check)
        await msg.channel.send(msg.content)
        print(f"[{i+1}] Sending {member}'s message in {member.guild.name} ({ctx.channel.name}): " + msg.content)
    
        
    print(f"Finished copying {member}.")


bot.run(token, bot=False)
