16 Formosan Languages Sentences That Need to be Manually Added 

Paiwan
delete: [1.valjulu= 咬人樹 
delete: aicu a pinaka vavauan a dredretan papizuanan tua sinan paravac a zaljum ( vava  
delete:  師教導的。
delete: nu pangtjezan timadju nua kinamalji siveric a nemang pasa kasasavan. 只要 他生氣就會把屋內的東西向 

add:  (some are after (.... ) (... .) and some are because of wacky format like 。.)  
PROBLEM: the (... .) are transcribed with current code but (.... ) is not. And the regular expression is not taking r"\.{4}\s*" for some reason. So the sentences are still being manually added 

add: nu pangtjezan timadju nua kinamalji siveric a nemang pasa kasasavan. 只要 他生氣就會把屋內的東西向 外扔出去。 
add: aicu a pinaka vavauan a dredretan papizuanan tua sinan paravac a zaljum ( vava ). 那稱為聖水之壺的陶壺是用來盛裝聖水(酒)。
add: aicu a vavauan a reretan inikamin a pinuvavan sikapalisilisiuta. 釀聖酒壺是用來裝酒和祭祀用。
add: ayatua iniyanan ka macaqu ti lanpaw a ljemangui ka ljemangui tjimadju se buqbuq. lanpaw 尚未學會游泳一下水就沉下水裡。 
add: na! manu namakuda sun a sika caucau! 唉喲！原來你是這 樣的人。
add: pinaka ti muni ni kina i eleng aku vuvu. 我的孫女被姨媽 eleng( 女子名)命名為muni( 女子名)。
add: aicu a sini vengetj tua qeluz a siravarava petjuq na zua ta lutlutan a siravarava. 用來綁柱子的這一 結繩子是剪自那一捆麻繩。
add: qadjavananga niamadju! 就任憑他們啦！
add: pailjaqa pusaladju! 請你ㄧ起幫忙吧！





Kanakanavu 
PROBLEM: the code and regular expression cannot discren the difference between Chinese half bracket ） and American half bracket ). So the code does not transcribe the pattern of  (\ \）.\s) = space + ） + . + space  (does not transcribe the Chinese half bracket) 

add: 祖父母的總稱或泛指已過世的長輩（百步蛇也稱tamu ）. manmaan ku parʉʉ'ʉna mataa tamu maku, 'ituumuru nguain tamna tavara'a. 我喜歡與爺爺聊天，他懂的很多。
add: 'ituumuru vatu matapari'i nesi, mastaan noo 'umo'ʉcanniin. 這裡有很多 落石，尤其下雨的時候。





Sakizaya 
PROBLEM: (the first one is because the definition ends with 。. and for some reason it is not being transcribed) 
add: tulu ku Banaw hananay ngangan nu niyazu'. 有三個部落名稱是叫Banaw。
(this sentence is being transcribed 2 times so I will also manually add it 2 times! ) 





Saisiyat
PROBLEM: the bracket is not closed, not fully transcribed   
delete: mal'az'aza' [ 在 賽夏族的生 命禮儀當中，從結婚到死亡共有五次的 回娘家儀式，分別是： 1. monSaySa:ip 結婚第三天回娘家
detele: So'o kita' ka hiza tata:a' balaS a hipo'? 你看看那隻雞是公的還是 母的？ [a 用來連接兩個成分，語言學上稱「連語」，出現的情況有以下幾個 1. 人名：子名 a 父名，如 'obay a kalih

PROBLEM: because of this pattern: …）. )  sentence not transcribed 
add: So'o 'amet ka hini tatimae'! 你吃完這些菜！ 
add: 'amet ka hini kasnaw! 喝完這碗 湯！
add: mal'az'aza' [ 在 賽夏族的生 命禮儀當中，從結婚到死亡共有五次的 回娘家儀式，分別是： 1. monSaySa:ip 結婚第三天回娘家 ]
add: So'o kita' ka hiza tata:a' balaS a hipo'? 你看看那隻雞是公的還是 母的？ [a 用來連接兩個成分，語言學上稱「連語」，出現的情況有以下幾個 1. 人名：子名 a 父名，如 'obay a kalih ]





Rukai
PROBLEM: for some reason, the regular expression: (\.{4}\s) is not catching any of the translation that has a definition ending in .... 
add: lri apaw lrimasu apavalavala liniane. 你要分五份給他們。
add: lu kaelaelasu lalakeisu madha capacape padrelreke. 你罵孩子時不要 打在背上。
add: mwakatwasa lalalrange. 走了，小心地走路。
add: luka kalaadravane ki acilay pangwaawsu madu tukange. 水漲的時候要 用網撈來捕魚。
add: kay tawpungu yai kapalrane madu lu mwinwane. 走任何地方狗是我 們真正的同伴。
add: ngwaladha kay tangwadrekanesu si kaseleme kai piapianga. 要為你這 次的跌倒 而不敢再做了。
add: tucaecape kay kamamadha. 木瓜的子較多。
add: this one is because it has a weird pattern: 1. 子多（如 南瓜、木瓜...）.  





yami 
PROBLEM: the ]/)is not fully transcribed, so need add ]/) to sentences 
add ] to: [以前，tao族一天只吃兩餐，早餐吃得早，所以到了下 午約
add ) to: ko ji akan o ya mizazaid a yakan. 我不敢吃有黏稠的菜。(如加了太白粉的 

PROBLEM: add sentences because their definition ends in ..... (5 American periods) / .... (4 American periods)/ ... (3 American periods)  and thus is not transcribed by the code
add: niomlapo no kalikey na, na katoda arakoan am, ya pa ji nimivias. 他從小到大，他 從未掃過地。
add: o amongan am, piyakanan so alibangbang. 飛魚盤是吃飛魚用的盤子。
add: koman ko so ikoa. 我要吃那個 ...。

PROBLEM:  add sentences because they are messed up by 3 american periods in the sentence before
add: ka pa ji absoy ori mo koaimo? 喂，你還沒有吃飽啊? ji ka ngai mo koaimo. 喂，你不要 跟來。 
add: asa doa tilo apat lima.... 一二三四五...。 

delete: 不直呼人名;不指明時間或物時之用語;如漢語的“那個…”之意. koman ko so ikoa. 
delete: asa doa tilo apat lima....





kavalan 
delete: 蓋棉被. 





Saaroa
PROBLEM:  …. (chinese ellipse + american period)
detete: 11 phrases after the ….  --> need to find them and detelet them. This list does NOT include them here. 

PROBLEM: because the definition ends in .... or .... (3 or 4 american periods), the sentence is not transcribed 
add: kuika kapitanʉnai hliangahli naani? 難道長官沒有來這裡？
add: ahlicita'ai ucani pihlingi mavahlaʉvaʉ mʉmʉa. 希望我們全家都平安。
add: kanakanavu nua ihlataia ucanika ahlamata. 卡那卡那 富族與我們亦出同源。 [未來式：ucaniaka]
add: kucikia pahlasʉkʉra paahlumʉlʉngʉsʉ. 咱們沒有辦法唱拉長音唱歌。
add: akuhlamu maini mana muasamu pʉtʉkʉhlʉ'a kʉmʉrangʉ tam saa'au. 以前我們 還是孩子的 時候，會捉kʉhlʉ'a 來燒吃，非常好吃。
add: pasakulaikiia puaruma amihlaina'anan pakiaturuana. 媽媽請老師趕 快進來。 
add: macikia kumita tavavusuia pasakulaikiia micuhlu. 看見眼鏡蛇要趕快走開。 
add: pasakulaikiia maini sikuatitipana. 請動作快 一點。
add: mavacangʉ a mi'a'aisa sala'ana ka, tumahla'ʉ cucu'u miacaacalivi. 他在 路上生意 很好，因為很多人一直經過。
add: kuakuarumuku 'amisana ta'iaraisaka kutuahlʉ musa patʉkʉ hluuhlungu pasaulaula'ʉ. 我不喜歡冬天，因為不能去溪邊玩水。
add: piavacavacangʉ iniciki maruka siaravacangʉ. 說好話才會 有好報。

PROBLEM: (because the definition has …….. / ……...(2 chinese ellipse + 2/3 american periods) --> if this is added to regular expression, it will undermine other patterns. Need to be added manually)  
add: piatʉkʉhlʉ vutukuhluia puatʉkʉhlʉ pangʉ'ʉ. 釣不同魚要用不同的 餌。
add: piavacavacangʉ iniciki maruka siaravacangʉ. 說好話才會 有好報。
add: ta'iaraisa ahlu'u naka tarapangʉ inicita maruka ʉpʉcʉahlu'u aanʉ. 因為蜜蜂 採花蜜，我們才 有蜂蜜可以吃。





Bunun
PROBLEM: add (I don't even know why this is not transcribed) 
add: Kavavaa maun haising! 快點吃飯！. [kavavaa ( 投高花東 )；ma-iskav ( 高)。]

PROBLEM: because the 4 。., the senetnces are not transcribed
add: Muntunuh tu daan hai, pahaisan; nii tu palahaib. 坍方 的路被劃界不可通行。
add: Masa dusang vali hai, pacinlaizu mas sinsusuaz. 從前有兩個太陽，使農作物枯萎。
add: Mais namacingaanin uvaaz hai, asa tu kadavus, na-istan-ali mavala. 當要為小孩命名的時候， 必須釀酒，用以招待姻親。

PROBLEM: the sentence is not fully transcribed because it ends in ？ .
add: Ciang, pasikuunsu sangan binaliv bunbuna? 江，你 剛才買的那些香蕉放在哪裡？
add: Mahansiap kasu maku-uni ahumushutcia ha? 你知道如何使 用那些套頸陷阱 嗎？

PROBLEM: the Chinese translation is not transcribed fully because the definition ends in ？.
add: Mabaliv aupa kata pang? 我們要買點麵包嗎？
add: Mavia sa-ia tu macishahainaz? 她為甚麼一 直跳著？
add: Namahtubin kamu padangian mas inaak tu pingaz-uvaaztan? 憑 什麼把我這個 女兒嫁給你們？
add: Andii sinhaili tu kanadaan hai, nii tu ma-aipi sistuh. 山刀的刀柄不容易?
add: Nalakua kasu kusia Takau? 你什麼時候 要前往高雄？
add: Maaz kazimaun suu maun? 你喜歡吃什麼？
add: Namaaz a isnavasu? 你要教什 麼？
add: Namaaz a tundaansu kusia Takaucia? 你要搭什麼去高雄？
add: Maazamaazang a duma haimangsuttan? 那些其他的東西是些 什麼？
add: Makinpia isuu isaincia kainludunan nasauzan mas utan? 你那邊有多少土堆要 種地瓜？
add: Makua isuu iniliskinan mas laupakadau tu sin-ihumis? 你對於現代生活的想法如何？
add: Namaazbin pakisaivunsu ii? 你到底想要什麼 啊？
add: Sima napasa- uni mas kakaunun? 誰要分配食物？
add: Adu mahtu taublasdanghas pinsial mata? 胡蘿蔔有益眼睛嗎？
add: Mashut aupa isuu sinlibatan? 你所栓的這個螺絲是否拴緊了？
add: Mavia utung tu mazima mavuhvuh lukistan ii? 為什麼猴子喜歡搖樹呢？

PROBLEM: need to delete 14 ? in total
delete: Mahansiap kasu maku-uni ahumushutcia ha? 你知道如何使 用那些套頸陷阱
delete: Ciang, pasikuunsu sangan binaliv bunbuna? 江，你
delete: Mabaliv aupa kata pang?
delete: Mavia sa-ia tu macishahainaz? 她為甚麼一
delete: Namahtubin kamu padangian mas inaak tu pingaz-uvaaztan? 憑 什麼把我這個
delete: Andii sinhaili tu kanadaan hai, nii tu ma-aipi sistuh.
delete: Nalakua kasu kusia Takau? 你什麼時候
delete: Namaaz a tundaansu kusia Takaucia?
delete: Maazamaazang a duma haimangsuttan? 那些其他的東西是些
delete: Makinpia isuu isaincia kainludunan nasauzan mas utan? 你那邊有多少土堆要
delete: Makua isuu iniliskinan mas laupakadau tu sin-ihumis?
delete: Napakisaivunta is-indangaz tu na-isnava
delete: Sima napasa- uni mas kakaunun?
delete: Adu mahtu taublasdanghas pinsial mata? 
delete: Mashut aupa isuu sinlibatan?
delete: Mavia utung tu mazima mavuhvuh lukistan ii?

PROBLEM: because of the 。., the sentences are not fully transcribed, need to delete (they are added fully above)
delete: Muntunuh tu daan hai, pahaisan; nii tu palahaib. 坍方
delete: Masa dusang vali hai, pacinlaizu mas sinsusuaz. 從前有兩個太陽，
delete: Mais namacingaanin uvaaz hai, asa tu kadavus, na-istan-ali mavala. 當要為小孩命名的時候， 必須釀酒，
