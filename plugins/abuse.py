# Plugin inspired by the Gaali Machine
# Do not touch
# Teri Gaand Faad Dunga Bhosdike

import random

from userge import userge

RENDISTR = [
    "`I Know Uh ez Rendi Bhay Dont show Your Randi Pesa Here`",
    "`Jag Suna suna laage Sab #maderchod bhay`",
    "`you talking behind meh wew uh iz my fan now bhay`",
    "`Wanna pass in Life Goto BRAZZER.CAM BHAY`",
    "`Uh iz Pro i iz noob your boob is landi uh are Randi`",
    "`Sellers Nasa calling Uh bhay😆`",
    "`Badwoo ki yojna behan bna ke ch*da uh iz badwa its your yozja?`",
    "`CHAND PE CHADA HAI CHANDYAAN KA GHODA TERA NAAM HAI MANSUR TU HAI BEHAN KA LOD*😂`",
    "`Jab se dil lga baithe tanhai me maa chu*da baithe wo kho gyi kisi aur ke pyar hum apne hi jaato me aag lga baithe`",
    "`Chadii ke ander se lal pani kha se ata hai ky teri masuka ka bhosda bhi paan khata hai😂`",
    "`Sun bhosdi ke By anonyCrew MOHABBAT KE SIWA AUR BHI GAM HAI JAMANE ME BSDK GAND PAHAT JATI HAI PAISA KAMANE ME`",
    "`Thaan liya tha Sayri nhi krege Unka pichwada dekha Alfaaz nikal gye`",
    "`Ravivaar ko dekha Chand Ka Tukra Itna Baar Dekha par Jaath na Ukra`",
    "`Katal kro Tir se Talwar me Ky Rkkha hai Maal Chodo Sari Me Salwar me Ky Rkkha hai`",
]

ABUSE_STRINGS = [
    "`Chutiya he rah jaye ga`",
    "`Ja be Gaandu`",
    "`Muh Me Lega Bhosdike ?`",
    "`Kro Gandu giri kam nhi toh Gand Maar lenge tumhari hum😂`",
    "`Suno Lodu Jyda muh na chalo be muh me lawda pel Diyaa jayega`",
    "`Sharam aagyi toh aakhe juka lijia land me dam nhi hai apke toh Shilajit kha lijia`",
    "`Kahe Rahiman Kaviraaj C**t Ki Mahima Aisi,L**d Murjha Jaaye Par Ch**t Waisi Ki Waisi`",
    "`Chudakkad Raand Ki Ch**T Mein Pele L*Nd Kabeer, Par Aisa Bhi Kya Choda Ki Ban Gaye Fakeer`",
]

CHU_STRINGS = [
    "`Taare hai Asmaan me very very bright jaat na jla bskd dekh le apni hight.`",
    "`jindagi ki na toote lari iski lulli hoti nhi khadi`",
    "`Kbhi kbhi meri dil me khyaal ata hai ayse chutiyo ko kon paida kr jata hai😂.`",
    "`Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.`",
    "`Dil ke armaa ansuon me beh jaye tum bskd ke chutiye hi reh gye.`",
    "`Ishq Se Tabiyat Ne Zeest Ka Mazaa aya maine is lodu ko randi khane me paya.`",
    "`Mirza galib ki yeh khani hai tu bhosdika hai yeh sab ki jubani hai.`",
]

FUK_STRINGS = [
    "`It's better to let someone think you are an Idiot than to open your mouth and prove it.`",
    "`Talking to a liberal is like trying to explain social media to a 70 years old`",
    "`CHAND PE HAI APUN LAWDE.`",
    "`Pehle main tereko chakna dega, fir daru pilayega, fir jab aap dimag se nahi L*nd se sochoge, tab bolega..`",
    "`Pardhan mantri se number liya, parliament apne :__;baap ka hai...`",
    "`Cachaa Ooo bhosdi wale Chacha`",
    "`Aaisi Londiya Chodiye, L*nd Ka Aapa Khoye, Auro Se Chudi Na Ho, Biwi Wo Hi Hoye`",
    "`Nachoo Bhosdike Nachoo`",
    "`Jinda toh jaat ke baal bhi hai`",
    "`Sab ko pta tu randi ka baccha hai (its just a joke)`",
]

THANOS_STRINGS = [
    "`Mashoor Rand, Ne Arz Kiya Hai. Aane Wale Aate Hai, Jaane Wale Jaate Hai. Yaade Bas Unki Reh Jaati Hai, Jo G**Nd Sujaa Ke Jaate Hai`",
    "`Pani kam hai matkey me ga*d mardunga teri ek jatke me`",
    "`Aand kitne bhi bade ho, lund ke niche hi rehte hai`",
    "`Tum Ameer hum gareeb hum jhopdiwale Tum bhosiwale`",
    "`Sisi Bhari Gulab ki padi palang ke pass chodne wale chod gye ab q baitha udaas`",
    "`Phuloo Ka Raja Gulaab Kaato me Rehta hai Jeewan ka Nirmata jaato me rehta hai😂`",
    "`Chude hue maal ko yaad mt krna Jo Chut na de usse kabhi friyad mt karna jise chudna hai wo chud ke rhegi bekar me muth maar ke apni jindagi barbaad mt krna`",
    "`Gand mare gandu Chut mare Chutiya Sabse accha mutti 2 mint me chutti😛`",
    "`Marzi Ka Sex Pap Nahi Hota.. Piche Se Dalne Wala Kabhi Baap Nahi Hota.. Condom Zarur Lagana Mere Dost Qki.. Sex K Waqt Popat Ke Pass Dimag Nahi Hota.`",
    "`Uss Ne Hothon Se Chhu Kar Lowd* Pe Nasha Kar Diya; Lu*D Ki Baat To Aur Thi, Uss Ne To Jhato* Ko Bhi Khada Kar Diya!`",
]

ABUSEHARD_STRING = [
    "`Madarchod Randi ke bacche.Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu tere lode pe madhu makkhi Katelode ke ando pe Road roller chale tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga sale tere gand ke balo pe tel laga ke jala du me teko Anaconda leke gand me dalu tho muh se nikle maa ke lode hamesha chutiyo jaisa bartav kartha he tu maa ke Dai chawal drugs tere gand Me dalunga thi tatti nahi nikle maa darchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI CHUT MAI TALWAR DUNGA BC CHUT FAT JAEGI AUR USME SE ITNA KHOON NIKLEGA MZA AJAEGA DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN DA TERI MAA KI CHUT CHOD CHOD KE BHOSDABNADU MADARCHOD AUR USKE UPAR CENENT LAGADU KI TERE JESA GANDU INSAAN KABHI BAHR NA A SKE ESI GANDI CHUT MAI SE LODA LASUN MADRCHOD TERI MAA KI CHUT GASTI AMA KA CHUTIA BACHA TERI MAA KO CHOD CHOD K PAGAL KAR DUNGA MAA K LODY KISI SASTIII RANDII K BACHY TERI MAA KI CHOOT MAIN TEER MAARUN GANDU HARAMI TERI COLLEGE JATI BAJI KA ROAD PEY RAPE KARONGANDU KI OLAAD HARAM KI NASAL PAPA HUN TERA BHEN PESH KAR AB PAPA KO TERI MAA KKALE KUSS MAIN KIS`",
    "`Main roz teri behno ki banjar chut me apna lawda daalke andar haryali lata tha magar aaj unke ke baare me sunke mujhe bhut afsos huwa..ki unko ab bada loudha chahye..ab mera balatkaaari lawda lagataar 4 ghante tk apne muh me kon rakhega..vo teri behne hi thi jo apni kaali magar rasilli chut mere saamne khol deti aur zameen pe naagin ki tarah rengne lgti thi jaise ki kisine unki chut pe naariyal tod diya ho vo b bada wala mumbai ka naariyal..apni chennal maa ko b nhi bhej rahe mere paas to main kaixe tum logo se vaada karu ki main teri maa chodd dungaw..ab agar tun sach me chahta hai ki main tum dono k mc ki chut me dhammal karu to mera lawda apne muh me rakho aur kaho Sameer hamare sage papa hain... Aur agar tb b the apni maa ki kaali chut mere saamne nahi rakhi to tumhare ghar me ghuske tumhari maa ka balatkaar kar dungaw jaixe delhi me huwa tha...ab teri chudi hui kuttiyo ki tarah apni gaand hilaate hue mere aage kalapna mt ni to tumhari fatti bhoxdi me 100 ched karunga`",
    "`Taare hai Asmaan me very very bright jaat na jla bskd dekh le apni hight.`",
    "`Zindagi ki na toote lari iski lulli hoti nhi khadi`",
    "`Kbhi kbhi meri dil me khyaal ata hai ayse chutiyo ko kon paida kr jata hai😂.`",
    "`Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.`",
    "`Dil ke armaa ansuon me beh jaye tum bskd ke chutiye hi reh gye.`",
    "`Ishq Se Tabiyat Ne Zeest Ka Mazaa aya maine is lodu ko randi khane me paya.`",
    "`Mirza galib ki yeh khani hai tu bhosdika hai yeh sab ki jubani hai.`",
    "`Mashoor Rand, Ne Arz Kiya Hai. Aane Wale Aate Hai, Jaane Wale Jaate Hai. Yaade Bas Unki Reh Jaati Hai, Jo G**Nd Sujaa Ke Jaate Hai`",
    "`Pani kam hai matke me gand marlunga jhatke me.`",
    "`Aand kitne bhi bade ho, lund ke niche hi rehte hai`",
    "`Tum Ameer hum gareeb hum jhopdiwale Tum bhosiwale`",
    "`Sisi Bhari Gulab ki padi palang ke pass chodne wale chod gye ab q baitha udaas`",
    "`Phuloo Ka Raja Gulaab Kaato me Rehta hai Jeewan ka Nirmata jaato me rehta hai😂`",
    "`Chude hue maal ko yaad mt krna Jo Chut na de usse kabhi friyad mt karna jise chudna hai wo chud ke rhegi bekar me muth maar ke apni jindagi barbaad mt krna`",
    "`Gand mare gandu Chut mare Chutiya Sabse accha mutti 2 mint me chutti😛`",
    "`Marzi Ka Sex Pap Nahi Hota.. Piche Se Dalne Wala Kabhi Baap Nahi Hota.. Condom Zarur Lagana Mere Dost Qki.. Sex K Waqt Popat Ke Pass Dimag Nahi Hota.`",
    "`Uss Ne Hothon Se Chhu Kar Lowd* Pe Nasha Kar Diya; Lu*D Ki Baat To Aur Thi, Uss Ne To Jhato* Ko Bhi Khada Kar Diya!`",
]


@userge.on_cmd("abuse$", about="Abuse means gali XD")
async def abuse_func(message):
    strAbu = random.randint(0, len(ABUSE_STRINGS) - 1)
    # input_str = event.pattern_match.group(1)
    reply_text = ABUSE_STRINGS[strAbu]
    await message.edit(reply_text)


@userge.on_cmd("rendi$", about="Randiiiiiiiiiii")
async def rendi_func(message):
    strRen = random.randint(0, len(RENDISTR) - 1)
    # input_str = event.pattern_match.group(1)
    reply_text = RENDISTR[strRen]
    await message.edit(reply_text)


@userge.on_cmd("chutiya$", about="Chutiyaaaa Saalaaaaaa")
async def chutiya_func(message):
    strChu = random.randint(0, len(CHU_STRINGS) - 1)
    # input_str = event.pattern_match.group(1)
    reply_text = CHU_STRINGS[strChu]
    await message.edit(reply_text)


@userge.on_cmd("fucc$", about="Fuuuuuuuucccccc*kkkkkkkkkkkkk")
async def fucc_func(message):
    strFuk = random.randint(0, len(FUK_STRINGS) - 1)
    # input_str = event.pattern_match.group(1)
    reply_text = FUK_STRINGS[strFuk]
    await message.edit(reply_text)


@userge.on_cmd("gshayri$", about="Galio se bhari shayri (Sort of)")
async def gshayri_func(message):
    strSha = random.randint(0, len(THANOS_STRINGS) - 1)
    # input_str = event.pattern_match.group(1)
    reply_text = THANOS_STRINGS[strSha]
    await message.edit(reply_text)


@userge.on_cmd("abusehard$", about="Hard Abusives")
async def abusehard_func(message):
    strHar = random.randint(0, len(ABUSEHARD_STRING) - 1)
    # input_str = event.pattern_match.group(1)
    reply_text = ABUSEHARD_STRING[strHar]
    await message.edit(reply_text)
