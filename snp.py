import discord
from discord.ext import commands, tasks
from asyncio import sleep as sp
from discord.utils import get

class snp(commands.Cog):

    def __init__(self, bot):
        self.bot= bot
        self.channelId= 854889475124887582
        self.messageId= 854925311669436436
        self.listn= False
        self.doneListning= True
        self.msg= None
        self.msgRecieved= None
        self.emAlli= "<:alliance:854960909571325974>"
        self.emHor= "<:horde:854960909712359425>"
        self.perSonals= {}
        self.signUpLog= {}
        self.aChannels={845489981392945162: None, 845493589763948544: None, 845500864164134922: None, 845493633230962728: None, 845500938503585792: None, 
                        852395226551025714: None, 852395501264830474: None, 633467952305405986: None, 688922122013245598: None, 
                        845490068419510342: None, 845494682712014928: None, 845500975456190485: None, 845494708855898112: None, 845501005981679636: None, 
                        852395640906317864: None, 852395841523679232: None, 845525125352652800: None, 688922450037309448: None}
        self.tankList={845489981392945162: {}, 845493589763948544: {}, 845500864164134922: {}, 845493633230962728: {}, 845500938503585792: {}, 
                        852395226551025714: {}, 852395501264830474: {}, 633467952305405986: {}, 688922122013245598: {}, 
                        845490068419510342: {}, 845494682712014928: {}, 845500975456190485: {}, 845494708855898112: {}, 845501005981679636: {}, 
                        852395640906317864: {}, 852395841523679232: {}, 845525125352652800: {}, 688922450037309448: {}}
        self.healerList={845489981392945162: {}, 845493589763948544: {}, 845500864164134922: {}, 845493633230962728: {}, 845500938503585792: {}, 
                        852395226551025714: {}, 852395501264830474: {}, 633467952305405986: {}, 688922122013245598: {}, 
                        845490068419510342: {}, 845494682712014928: {}, 845500975456190485: {}, 845494708855898112: {}, 845501005981679636: {}, 
                        852395640906317864: {}, 852395841523679232: {}, 845525125352652800: {}, 688922450037309448: {}}
        self.dpsList={845489981392945162: {}, 845493589763948544: {}, 845500864164134922: {}, 845493633230962728: {}, 845500938503585792: {}, 
                        852395226551025714: {}, 852395501264830474: {}, 633467952305405986: {}, 688922122013245598: {}, 
                        845490068419510342: {}, 845494682712014928: {}, 845500975456190485: {}, 845494708855898112: {}, 845501005981679636: {}, 
                        852395640906317864: {}, 852395841523679232: {}, 845525125352652800: {}, 688922450037309448: {}}
        self.advertList= {845489981392945162: None, 845493589763948544: None, 845500864164134922: None, 845493633230962728: None, 845500938503585792: None, 
                        852395226551025714: None, 852395501264830474: None, 633467952305405986: None, 688922122013245598: None, 
                        845490068419510342: None, 845494682712014928: None, 845500975456190485: None, 845494708855898112: None, 845501005981679636: None, 
                        852395640906317864: None, 852395841523679232: None, 845525125352652800: None, 688922450037309448: None}
        self.tRole= '<<@&675054347251482656>>'
        self.emTank= '<:tank:849144095825985556>'
        self.hRole= '<@&675054271619924024>'
        self.emHealer= '<:healer:628592563871285278>'
        self.dRole= '<@&675054493238427648>'
        self.emDps= '<:dps:628592130360868877>'
        self.lRole= '<@&848415470747123782>'
        self.pRole= '<@&848415466624253952>'
        self.cRole= '<@&848415473187815445>'
        self.mRole= '<@&848415467772837889>'
        self.warRole= '<@&789787911222460436>'
        self.palRole= '<@&789787670150119444>'
        self.hunRole= '<@&789787211666817064>'
        self.rogRole= '<@&789786522110787615>'
        self.prRole= '<@&789785311068684308>'
        self.shaRole= '<@&789786818413068308>'
        self.magRole= '<@&789784551744339998>'
        self.locRole='<@&789768292481892362>'
        self.monRole= '<@&789786266510032906>'
        self.druRole= '<@&789785941661319178>'
        self.dmhRole= '<@&789785646767276032>'
        self.dkRole= '<@&789787450352468018>'
        
        self.emCheck='<:pinkcheckmark:838204522811490304>'
        self.emKS= '<:keystone:855250845448929320>'
        self.emCross= '<:slbcoin8bitred:757090701673496576>'
        self.sgEmotes= [self.emTank, self.emHealer, self.emDps, self.emCheck, self.emCross]


    # @commands.command()
    # async def init(self, ctx):
    #     self.channel= self.bot.get_channel(self.channelId)
    #     self.msg= await self.channel.send("Base Message Created")
    #     await sp(2)
    #     embed= self.baseMessage()
    #     await self.msg.edit(embed= embed)
    #     await self.msg.add_reaction(self.emAlli)
    #     await self.msg.add_reaction(self.emHor)

    @commands.command()
    async def signup(self, ctx, keyNo, buyerMod, cuts, *, Notes= None): #key no with modifier.
        if self.aChannels[ctx.channel.id] != None:
            await ctx.channel.send(content='Signup in progress, try again later', delete_after= 15)
            return

        self.tankList[ctx.channel.id].clear()
        self.dpsList[ctx.channel.id].clear()
        self.healerList[ctx.channel.id].clear()

        keyMods= keyNo.split('-')
        embed= discord.Embed(title= 'Starlight Boosting M+ Sign Up', description='{} // Armor Stack {} // {}-{} Runs // {} // Buyer {} // Cuts Total {}'.format(
            self.checkClass(keyMods), 
            self.checkStack(keyMods), 
            keyMods[0], self.checkTorUT(keyMods), 
            self.findKey(keyMods), 
            'Will Participate' if 'p' == buyerMod else 'AFK', 
            cuts
             ))
        # if Notes != None:
        embed.add_field(name='Additional Notes', value='> {}'.format(Notes), inline= False)
        embed.add_field(name='Tank {}'.format(self.emTank), value='> Filling', inline= True)
        embed.add_field(name='Healer {}'.format(self.emHealer), value='> Filling', inline= True)
        embed.add_field(name='DPS {}'.format(self.emDps), value='> Filling', inline= True)

        embed.set_author(name= "{}".format(ctx.author))

        self.aChannels[ctx.channel.id]= await ctx.channel.send(content=self.checkClass(keyMods), embed= embed)
        self.advertList[ctx.channel.id]= ctx.author.id
        for emotes in self.sgEmotes:
            await self.aChannels[ctx.channel.id].add_reaction(emotes)

        await sp(420)
        self.aChannels[ctx.channel.id]= None

    def checkClass(self, mods):
        if 'ls' in mods:
            return '{} {} {} {}'.format(self.rogRole, self.monRole, self.druRole, self.dmhRole)
        elif 'ps' in mods:
            return '{} {} {}'.format(self.warRole, self.palRole, self.dkRole)
        elif 'cs' in mods:
            return '{} {} {}'.format(self.prRole, self.magRole, self.locRole)
        elif 'ms' in mods:
            return '{} {}'.format(self.hunRole, self.shaRole)
        else:
            return '{} {} {}'.format(self.tRole, self.hRole, self.dRole)

    def checkStack(self, mods):
        if 'ls' in mods:
            return self.lRole
        elif 'ps' in mods:
            return self.pRole
        else:
            return 'N/A'
    
    def checkTorUT(self, mods):
        if 'UT' in mods:
            return '**UNTIMED**'
        else:
            return '**TIMED**'

    def findKey(self, mods):
        if 'SK' in mods:
            return 'Need Key {}'.format(mods[-1])
        elif 'NK' in mods:
            return 'Need Any Key'
        else:
            return 'Buyers Key'


    @commands.command()
    async def cTeam(self, ctx, tank: discord.Member, healer: discord.Member, dps1: discord.Member, dps2: discord.Member, wisp= None, val= '4'):
        embed= discord.Embed(title= 'Starlight Boosting Team Formation', description= 'Login and get ready to Yeet the Key')
        if val== '1':
            embed.add_field(name= '**TANK**', value='> *{}* {}'.format(tank.mention, self.emKS), inline= False)
        else:
            embed.add_field(name= '**TANK**', value='> *{}*'.format(tank.mention), inline= False)
        if val== '2':
            embed.add_field(name= '**HEALER**', value='> *{}* {}'.format(healer.mention, self.emKS), inline= False)
        else:
            embed.add_field(name= '**HEALER**', value='> *{}*'.format(healer.mention), inline= False)
        if val== '3':
            embed.add_field(name= '**DPS1**', value='> *{}* {}'.format(dps1.mention, self.emKS), inline= False)
        else:
            embed.add_field(name= '**DPS1**', value='> *{}*'.format(dps1.mention), inline= False)
        if val== '4':
            embed.add_field(name= '**DPS2**', value='> *{}* {}'.format(dps2.mention, self.emKS), inline= False)
        else:
            embed.add_field(name= '**DPS2**', value='> *{}*'.format(dps2.mention), inline= False)
        
        embed.add_field(name= 'Wisper invite', value='> /w *{}* inv'.format(wisp), inline= False)
        await ctx.channel.send(embed= embed)
        await tank.send(embed= embed)
        await healer.send(embed= embed)
        await dps1.send(embed= embed)
        await dps2.send(embed= embed)
        await ctx.channel.send('%vc')
        self.aChannels[ctx.channel.id]= None
        



    # def baseMessage(self):
    #     embed= discord.Embed(title= "Starlight Boosting", description= "State your Allegiance")
    #     embed.add_field(name= "Horde", value= "{}".format(self.emHor), inline= True)
    #     embed.add_field(name= "Alliance", value= "{}".format(self.emAlli), inline= True)
    #     embed.set_image(url= 'https://i.pinimg.com/originals/a0/09/84/a009841fe4b23bd268d760cd3d969dd1.jpg')
    #     return embed

    # async def getMessage(self):
    #     self.channel= self.bot.get_channel(self.channelId)       
    #     self.msg= await self.channel.fetch_message(self.messageId)
    #     await self.channel.send("Check Message ID in script", delete_after= 10)
    #     pass

    @commands.Cog.listener()
    async def  on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        # print(payload)
        if payload.message_id == self.aChannels[payload.channel_id].id:
            if str(payload.emoji) == self.emTank:
                self.tankList[payload.channel_id][payload.member.id]= payload.member.mention
                self.aChannels[payload.channel_id].embeds[0].set_field_at(
                    index= 1, name='Tank {}'.format(self.emTank), value=''.join(['\n> %s' % i for i in self.tankList[payload.channel_id].values()]), inline= True)
                await self.aChannels[payload.channel_id].edit(embed= self.aChannels[payload.channel_id].embeds[0])

            if str(payload.emoji) == self.emHealer:
                self.healerList[payload.channel_id][payload.member.id]= payload.member.mention
                self.aChannels[payload.channel_id].embeds[0].set_field_at(
                    index= 2, name='Healer {}'.format(self.emHealer), value=''.join(['\n> %s' % i for i in self.healerList[payload.channel_id].values()]), inline= True)
                await self.aChannels[payload.channel_id].edit(embed= self.aChannels[payload.channel_id].embeds[0])

            if str(payload.emoji) == self.emDps:
                self.dpsList[payload.channel_id][payload.member.id]= payload.member.mention
                self.aChannels[payload.channel_id].embeds[0].set_field_at(
                    index= 3, name='DPS {}'.format(self.emDps), value=''.join(['\n> %s' % i for i in self.dpsList[payload.channel_id].values()]), inline= True)
                await self.aChannels[payload.channel_id].edit(embed= self.aChannels[payload.channel_id].embeds[0])


            ## Need to implement cross selection only by real author, to update the signup sheet no longer running (addfield) and clear the channel list
            if str(payload.emoji) == self.emCross:
                if payload.member.id == self.advertList[payload.channel_id]:
                    self.aChannels[payload.channel_id].embeds[0].add_field(
                                                name='**RUN CANCLED**', value='**Buyer Backout Sorry!!!', inline= False)
                    await self.aChannels[payload.channel_id].edit(embed= self.aChannels[payload.channel_id].embeds[0])
                    self.aChannels[payload.channel_id]= None

            if str(payload.emoji) == self.emCheck:
                if payload.member.id == self.advertList[payload.channel_id]:
                    self.aChannels[payload.channel_id].embeds[0].add_field(
                                                name='**Run Completed // Team Formation Done**', value='**New Advertiser can post', inline= False)
                    await self.aChannels[payload.channel_id].edit(embed= self.aChannels[payload.channel_id].embeds[0])
                    self.aChannels[payload.channel_id]= None

        else:
            return

    @commands.Cog.listener()
    async def  on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        if payload.message_id == self.aChannels[payload.channel_id].id:
            if str(payload.emoji) == self.emTank:
                self.tankList[payload.channel_id].pop(payload.user_id, None)
                self.aChannels[payload.channel_id].embeds[0].set_field_at(
                    index= 1, name='Tank {}'.format(self.emTank), value=''.join(['\n> %s' % i for i in self.tankList[payload.channel_id].values()]), inline= True)
                await self.aChannels[payload.channel_id].edit(embed= self.aChannels[payload.channel_id].embeds[0])

            if str(payload.emoji) == self.emHealer:
                self.healerList[payload.channel_id].pop(payload.user_id, None)
                self.aChannels[payload.channel_id].embeds[0].set_field_at(
                    index= 2, name='Healer {}'.format(self.emHealer), value=''.join(['\n> %s' % i for i in self.healerList[payload.channel_id].values()]), inline= True)
                await self.aChannels[payload.channel_id].edit(embed= self.aChannels[payload.channel_id].embeds[0])

            if str(payload.emoji) == self.emDps:
                self.dpsList[payload.channel_id].pop(payload.user_id, None)
                self.aChannels[payload.channel_id].embeds[0].set_field_at(
                    index= 3, name='DPS {}'.format(self.emDps), value=''.join(['\n> %s' % i for i in self.dpsList[payload.channel_id].values()]), inline= True)
                await self.aChannels[payload.channel_id].edit(embed= self.aChannels[payload.channel_id].embeds[0])


            ## Need to implement cross selection only by real author, to update the signup sheet no longer running (addfield) and clear the channel list
            if str(payload.emoji) == self.emCross:
                if str(payload.member) == str(self.aChannels[payload.channel_id].embeds[0].author):
                    print('author done')
        else:
            return



def setup(client):
    client.add_cog(snp(client))

