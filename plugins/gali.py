# by @krishna_singhal

import asyncio
from random import choice

from userge import Message, userge


async def check_and_send(message: Message, *args, **kwargs):
    replied = message.reply_to_message
    if replied:
        await asyncio.gather(message.delete(), replied.reply(*args, **kwargs))
    else:
        await message.edit(*args, **kwargs)


@userge.on_cmd("gali$", about={"header": "slang to a bitch with power of bot"})
async def gali_func(message):
    gali = choice(gaali)
    stickers = choice(stickers_ids)
    await check_and_send(message, "<code>{}</code>".format(gali), parse_mode="html")
    await message.reply_sticker(sticker="".join(stickers))


gaali = (
    "Abey Ja Na Randi",
    "Abey Ja Na Madarchod",
    "Tu mach gey",
    "You gey gey gey gey gey gey gey gey",
    "Chut mai talwar ghusauga bc chut fat jaegi aur usme se itna khoon niklega ki maza hi ajaega deklena sale sasti jhat",
    "Loda lasun madrchod teri maa ki chut gasti ama ka chutia bacha teri maa ko chod chod k pagal kar dunga maa k lody kisi sastiii randii k bachy teri maa ki choot main teer maarun gandu harami",
    "Maa ke bhosde se bahr aja fir baap se zuban da teri maa ki chut chod chod ke bhosdabnadu madarchod aur uske upar cement lagadu ki tere jesa gandu insaan kabhi bahr na a ske esi gandi chut mai se",
    "Teri college jati baji ka road pey rape karongandu ki olaad haram ki nasal papa hun tera bhen pesh kar ab papa ko teri maa kkale kuss main kisi!",
    "Maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI",
    "Tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike",
    "maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha",
    "Drugs tere gand Me dalunga ki tatti nahi nikle maadarchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi.",
    "Sale tere gand ke balo pe tel laga ke jala du me teko",
    "Tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga",
    "Tere lode pe madhu makkhi Katelode ke ando pe Road roller chale tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode",
    "Tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu",
    "Madarchod Randi ke bacche Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe",
)
stickers_ids = (
    "CAADBQADlgADje9BLb-DhGHGfbx6FgQ",
    "CAADBQADBgAD-xNYN79jb8hXjxhyFgQ",
    "CAADBQADIwAD-xNYN_ZX0TUQ33b5FgQ",
    "CAADBQADtQADje9BLVtdHXr6pvQfFgQ",
    "CAADBQADzwADje9BLT69DmYKUwd_FgQ",
    "CAADBQADAQADh68vOP4aZy5tiSXlFgQ",
    "CAADBQADKAADh68vOAABLBgqCrYYFRYE",
    "CAADBQADLgADh68vODlskrbAM9dEFgQ",
)

@userge.on_cmd("fgali1$", about="Full Gaali")
async def fgali_func(message):
    await message.edit("Madarchod Randi ke bacche Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu tere lode pe madhu makkhi Katelode ke ando pe Road roller chale tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga sale tere gand ke balo pe tel laga ke jala du me teko Anaconda leke gand me dalu tho muh se nikle maa ke lode hamesha chutiyo jaisa bartav kartha he tu maa ke Dai chawal drugs tere gand Me dalunga thi tatti nahi nikle maa darchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI CHUT MAI TALWAR DUNGA BC CHUT FAT JAEGI AUR USME SE ITNA KHOON NIKLEGA MZA AJAEGA DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN DA TERI MAA KI CHUT CHOD CHOD KE BHOSDABNADU MADARCHOD AUR USKE UPAR CENENT LAGADU KI TERE JESA GANDU INSAAN KABHI BAHR NA A SKE ESI GANDI CHUT MAI SE LODA LASUN MADRCHOD TERI MAA KI CHUT GASTI AMA KA CHUTIA BACHA TERI MAA KO CHOD CHOD K PAGAL KAR DUNGA MAA K LODY KISI SASTIII RANDII K BACHY TERI MAA KI CHOOT MAIN TEER MAARUN GANDU HARAMI TERI COLLEGE JATI BAJI KA ROAD PEY RAPE KARONGANDU KI OLAAD HARAM KI NASAL PAPA HUN TERA BHEN PESH KAR AB PAPA KO TERI MAA KKALE KUSS MAIN KISI !")

@userge.on_cmd("fgali2$", about="Full Gaali")
async def fgaali_func(message):
    await message.edit("Behen ke lode madahrchod teri ma randi bhsdk tera pyra khandan randi teri kandan kai ma ka bhods lund katta madarchod tere lund pe road roller chale tere behen ki chut kate tura khandan ke gand me bomb phute teri ma ke bur me 100 log ke lund teri behen ke bur me 100 log ke lund madarchod behenchod mai ka loda behen ka loda randi teri behen ma ki chut behen ki chut teri chut ki chut harami phate hue condom ke nateeje tera baap ko paisa nahi tha to uses condom se teri maa ko chooda benchod lodo hai tu sabka chusta gay lund hai nahi be lund akuad me re hamare desh ki taraf bhi dekha to tatte ukhad ke kutto ko keladenge madharchod Madarchod Randi ke bacche.Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu tere lode pe madhu makkhi Katelode ke ando pe Road roller chale tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga sale tere gand ke balo pe tel laga ke jala du me teko Anaconda leke gand me dalu tho muh se nikle maa ke lode hamesha chutiyo jaisa bartav kartha he tu maa ke Dai chawal drugs tere gand Me dalunga thi tatti nahi nikle maa darchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI CHUT MAI TALWAR DUNGA BC CHUT FAT JAEGI AUR USME SE ITNA KHOON NIKLEGA MZA AJAEGA DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN DA TERI MAA KI CHUT CHOD CHOD KE BHOSDABNADU MADARCHOD AUR USKE UPAR CENENT LAGADU KI TERE JESA GANDU INSAAN KABHI BAHR NA A SKE ESI GANDI CHUT MAI SE LODA LASUN MADRCHOD TERI MAA KI CHUT GASTI AMA KA CHUTIA BACHA TERI MAA KO CHOD CHOD K PAGAL KAR DUNGA MAA K LODY KISI SASTIII RANDII K BACHY TERI MAA KI CHOOT MAIN TEER MAARUN GANDU HARAMI TERI COLLEGE JATI BAJI KA ROAD PEY RAPE KARONGANDU KI OLAAD HARAM KI NASAL PAPA HUN TERA BHEN PESH KAR AB PAPA KO TERI MAA KKALE KUSS MAIN KISI loda leke muh me nachne wale ma ki jaat lund kate tera tiri bb ko chode duniya tiri gand me parmanu dhamaka teri ma ka buur me garam oil ki kadhai teri behen ki bane porn aur upload ho pornhub me teri ma ko 100 logo ne choda tab tu paida hua tra papa gay tu gay tera khandan gay bc mc maki chut belen ki lodi ma ki lodi behen teri randi ma teri randi loda undono ke muh me loda katgaya to muh me lele aur kuch hame bola to tera loda tere muh me deke tere gand se nikalenge madarchod beti teru chodaye beti teri rundi teri beti ki bur me 1000 logo ka lund teri beti ka gangbang tere papa be lund nund na hone ke karan teri ma rundi teri ma randi hone ke karan tu aur tera bhai behen teri behen radi kuki teri ma randi behen radi hone ke karan ro 1000 se choda ke uske 10000 bacche tere lund par hathi dore teri gand me chiti kate kera pura satyanash ho *Main roz teri* *behno ki banjar chut me* *apna lawda daalke andar* *haryali lata tha magar aaj* *unke ke baare me* *sunke mujhe bhut afsos* *huwa..ki unko ab bada loudha chahye..ab mera balatkaaari* *lawda lagataar 4 ghante tk* *apne muh me kon* *rakhega..vo teri* *behne hi thi jo apni kaali* *magar rasilli chut mere* *saamne khol deti aur* *zameen pe naagin ki tarah* *rengne lgti thi jaise ki* *kisine unki chut pe naariyal* *tod diya ho vo b bada wala* *mumbai ka naariyal.")

@userge.on_cmd("fgali3$", about="Full Gaali")
async def fgaali_func(message):
await message.edit("This is for you your a fucking waste of sperm madfaka I   don't know why your parents give birth a worthless shit like you  you faggot ass with a fucking gay bi sextual laurstic slutty minded kid lemaric siliastic  crow  face and ass hahaha your like a pork shit 💩madfaka tell your father to fuck you everynight so that u can have your pussy more effective to everyone  who did fucked you till now  bullshit say to Infront of everyone eyes like I eat bunny's pees at the same time while am sucking his dick bleh 😂 haha 😂😂😂😂 madfaka what u thought maybe u thought like am from India bsdk am not and that's why am fucking isolated from you ya know what your a fucking black ass who is in form of an human you will get fucked again by this bunny wait for it didle doddoy kid with a fucking phony dick 😂😂😂😂😂😂😂😂😂 fuck you🖕i will come again and again  for fucking your black ass shit everytime you  will be in front of my eyes  i will be there for fucking your Lili crow as black face hahaha for you😂😂😂👉👌🖕maderchod who the fuck are u u fucking inferior shitty asshole u know what shit you are the shit who drink my pees instead of drinking water now I will fuck ur mom one-day I went to your house with a condom then literally I went up to your mom shitty asshole and fucked  it like a real hard coocky dicky sumty dick I know like your mom enjoyed it a lot much then your sis caz your mom was a mature shit tho u know what u fucking cow face porky poopypants I also know where do u live and how do u eat let me give a brief description about where do u live you live in a fucking slum where ur mom sell her pussy in a reatil price yo and that the shitty reason how u eat three times hahahaha😂😂😂😂We or I are gonna rape your whole ugly family even tho they are as much as ugly as my shitty poop but so what I will still fuck them and insist them by fucking harder to say it like Bunny Coney  is the best fucker in the  world he  even can defeat the most famous porn star Johnny sins hahaha 😂😂😂Well let me say some stories about your mom actually not your mom's only it's our strory tho Your mother name  is Mrs  Mia khalifa she comes of a fucking pornography hilometic whore family she can suck and lick and you know what she lick she lick my sweet heavy hunktik dick hehe she is so kind I meant  your mom caz she suck my dick too kindly wow  hehe 😍 🙄   your mother Love my coocky dick very much and in back I also  love her sexy sweet pussy  as well mm we love each other  in this way hehe now am gonna tell how I fucked your mom well I used to sleep with her in first place then I slowly used to unfasten your mom bra and 👙 hehe after that I began my part what is too good to go with for me I literally fucked her every night like if I calculate in hours full night huhu I enjoyed those night even tho I still fuck her  lot hmm maybe she also miss those days like I do who knows however   maybe her happiness was know no bounds  and yh in her face I did seen a beams of joy for my hard core fucking hmm  well in profound respect I really wanna fuck her again and again caz I am  indebted to her asshole you know why let me tell you why well I only did fucked her pussy not asshole that's why One-day your sis we're going to her collage and I and some ma friend were waiting for her caz as much as we were concerned about her is she is a fucking bitch who earn money through her pussy postitution  and that's what makes us horny and greedy then that's why we all give her proposal about fucking her  vagina  or u can say pussy in few bucks after that we get Alas!!! And said wait what she is gonna give her fucking Hippocratic pussy in that much money for few bucks then I asked her hey why are u selling your pussy in a retail price then she replied like listen we don't get 3 times food that's why I and my mom's do it at last but not least after that   u know what I said  and what she did  she did fucked me like a fucking horny bitch I swear I enjoyed this part.")
