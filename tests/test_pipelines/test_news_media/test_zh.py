import unittest

from text_cleaning.pipelines.news_media.zh import *



class TestCleanMandarinNewsMediaText(unittest.TestCase):

    def setUp(self):
        self.clean = CleanMandarinNewsMediaText()

    def test_english_names_preserved(self):
        text = '俄羅斯入侵烏克蘭4天後，西方國家終於拿出像樣的經濟制裁手段，2月27日，' \
               '美國白宮宣布，法、德、義、英、加等國已經同意將俄羅斯部分銀行踢出全球金融' \
               '支付系統「環球銀行金融電信協會」（SWIFT），此舉將切斷俄國的匯款、' \
               '支付確認、貿易與換匯資訊，重擊俄國經濟。果然，消息傳出後，' \
               '俄羅斯盧布對美元一度貶至119.5，貶幅達30%，' \
               '俄國各地也出現提領美元現鈔的人潮；俄羅斯央行隨後宣布，' \
               '停止外國人出售俄國證券，此外，因盧布匯率在受到國際制裁後創下歷史新低，' \
               '故而將關鍵利率從9.5%提高到20%。' \
               '此番經濟制裁將對俄羅斯經濟造成多大的傷害？2014年俄羅斯併吞克里米亞時，' \
               '西方國家曾威脅要將俄羅斯逐出SWIFT，時任俄羅斯財政部長庫德林（' \
               'Alexei Kudrin）估算，一年內，俄羅斯GDP將減少5%。' \
               '曾任永豐銀資深副總經理的東華大學新經濟政策研究中心主任陳松興認為，' \
               '俄國被踢出SWIFT，再加上凍結俄國央行的美元資產，將造成盧布大幅貶值、' \
               '外資不敢投資、貿易受阻，最終瓦解俄國金融體系。陳松興指出，' \
               '把俄國踢出SWIFT只是西方國家對俄羅斯全面作戰的一部分，' \
               '先瓦解支持普丁的財閥，最後逼普丁下台。陳松興指出，其實普丁的決策圈很小，' \
               '從前幾天，他在俄國國安會議上宣布重提核威懾的畫面中可以發現，' \
               '普丁與其他國安官員的距離「超乎尋常的遠」，這可以解釋是「防疫需要」，' \
               '同時也可以解釋為「防範暗殺」。而能影響普丁決策的財閥，陳松興認為，' \
               '美方都已經掌握並列入制裁名單，這群人支持普丁入侵烏克蘭，' \
               '就是要藉機奪取烏克蘭的石油、天然氣、珍貴金屬、糧食等天然資源，' \
               '同時為俄國天然氣尋找出海口。2014年普丁併吞克里米亞時，' \
               '這些支持他的財閥都將資產轉移給家族其他成員，' \
               '但這次經濟制裁來的這麼廣泛又猛烈，陳松興認為，基本上，' \
               '支持普丁的財閥都跑不掉。' \
               '支持普丁的財閥也可以利用虛擬貨幣交易來進行資產轉移，陳松興指出，' \
               '美國聯準會已公開表示，有能力破解所有的虛擬貨幣交易過程，' \
               '加上被制裁的俄國財閥已經公布，這意謂他們在全球的資產都將被凍結。' \
               '至於中國是否為幫俄羅斯應付脫鉤SWIFT，例如俄羅斯媒體SPUTNIK報導稱，' \
               '歐美使出的「和SWIFT脱鈎」的這一手段可能會推動俄羅斯加入' \
               '中國的人民幣跨境支付系統CIPS；陳松興認為，' \
               '中國對歐美的貿易依存度遠高於中國對俄國的貿易依存，' \
               '在這種情況下，若中國不理會SWIFT的禁令，恐將增加歐美對中國的提防，' \
               '中國最後也會受到牽連而受傷。事實上，在俄羅斯被踢出SWIFT後，' \
               '大陸的中國銀行新加坡分行已停止為涉及俄羅斯石油和俄羅斯公司的交易融資；' \
               '拜登政府高級官員也向媒體證實，到目前為止，' \
               '中國似乎沒有幫助俄羅斯逃避西方對其入侵烏克蘭而實施的金融制裁，跡象表明，' \
               '「中國沒有提供金融援助」。陳松興強調，中國國家主席習近平不同於普丁，' \
               '普丁是狂人，而習卻是一個深思熟慮的人，' \
               '現在他已經看到西方國家經濟制裁重創俄國經濟，' \
               '再加上今年年底即將舉行中共二十大，至少今年，' \
               '習在俄烏衝突上將持續觀望態度，不會輕易出手。'
        result = self.clean(text)
        self.assertIn('Alexei Kudrin', result)

    def test_whitespace_normalized(self):
           text = '人民网北京3月1日电 （记者王连香）近日，交通运输部、国家铁路局、' \
                  '中国民用航空局、国家邮政局联合印发《新时代推动中部地区交通运输高质量' \
                  '发展的实施意见》（以下简称《意见》），旨在充分发挥中部地区承东启西、' \
                  '连南接北的区位优势，着力建设现代化交通基础设施体系，' \
                  '为中部地区加快崛起提供有力保障。\n\n\t《意见》从创新、协调、绿色、' \
                  '开放、共享等方面提出了目标要求。到2025年，中部地区国内国际循环中的' \
                  '大通道大枢纽功能显著增强，国家综合立体交通网主骨架进一步完善，' \
                  '交通全球连接度显著提高，交通运输创新能力建设取得明显成效，' \
                  '货运物流新模式新业态有序发展，城乡区域交通运输发展协调性进一步增强，' \
                  '交通运输单位周转量能源消耗降幅达到全国平均水平，碳排放强度持续下降，' \
                  '交通运输民生服务更加多元化、精细化。到2035年，' \
                  '中部地区大通道大枢纽基本建成，开放型运输网络连通全球，' \
                  '现代化交通基础设施体系基本形成，城乡区域交通协调发展达到较高水平，' \
                  '绿色低碳生产生活方式基本形成，交通运输民生服务品质大幅跃升，' \
                  '支撑服务共同富裕取得明显的实质性进展。\n\n\n(责编：王连香、高雷)' \
                  '\n分享让更多人看到'
           result = self.clean(text)
           self.assertNotIn('\n\n\t', result)
           self.assertNotIn('\n\n\n', result)

    def test_garbage_removed(self):
           text = '茫茫大海作考场——海军某勤务船大队海上训练考核掠影■解放军报特约记者 ' \
                  '\u3000薛成清 \u3000特约通讯员\u3000 武欢庆 摄影报道茫茫大海，' \
                  '逐浪砺兵，战舰犁出道道航迹……近日，南部战区海军某勤务船大队携手' \
                  '兄弟单位组成舰艇编队，赴某海域开展海上训练考核。图①：' \
                  '小艇前出模拟可疑目标。图②：海上补给训练考核。编队航行途中，' \
                  '考核组下达“敌”情通报：“发现快速移动目标来袭！”闻令而动，' \
                  '参训官兵迅速识别目标并做好防御准备。“机舱破损进水”“补给站起火”……' \
                  '战斗打响后，各种险情接踵而至。堵漏、灭火、抢修、排除故障，' \
                  '官兵们沉着应对，及时化解了一个个险情。抵达补给海域后，' \
                  '医疗船快速占领补给阵位。官兵们在补给舰和医疗船之间架起承载索，' \
                  '顺利完成输油软管对接。海面波浪翻卷，舰船上下起伏，' \
                  '官兵克服困难精准操纵，成功完成补给。图③：损管队员开展灭火训练考核。' \
                  '图④：舰炮对海上目标实施打击。不久，战斗警报再次拉响，' \
                  '火炮对海实弹射击随即展开。雷达判明目标性质后，' \
                  '某舰艇迅速锁定目标并对其实施打击。此外，编队还围绕定点抛锚、' \
                  '离靠漂泊舰等课目组织考核。考场即战场，考核如打仗。' \
                  '此次考核结合海上态势随机嵌入特情，多课目连贯实施加大难度，' \
                  '锤炼了官兵应急处突和协同作战能力。'
           result = self.clean(text)
           garbage = ['\u3000', '①', '②', '③', '④']
           for x in garbage:
              self.assertNotIn(x, result)