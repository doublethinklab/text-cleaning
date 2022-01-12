import unittest
from typing import Dict

from text_cleaning.pipelines.twitter import \
    TwitterEnglishTextCleaningPipeline, \
    TwitterEnglishTokensCleaningPipeline


class TestTwitterCleaningPipelines(unittest.TestCase):

    def setUp(self):
        self.rules = {
            'usa': ['U.S.A.', 'USA', 'U.S.', 'US'],
            'covid19': ['COVID-19', 'COVID19', 'COVID',
                        'Covid-19', 'Covid',
                        'covid-19', 'covid',
                        '#COVID-19', '#COVID19', '#COVID',
                        '#covid-19', '#covid', '#Covid-19', 'Covid'],
            'worldhealthorganization': ['WHO', 'W.H.O.',
                                        'World Health Organization'],
        }
        self.clean_text = TwitterEnglishTextCleaningPipeline(
            standardization_rules=self.rules, debug=False)
        self.clean_tokens = TwitterEnglishTokensCleaningPipeline(debug=False)

    def _test(self, sample: Dict):
        text = self.clean_text(sample['tweet'])
        tokens = text.split(' ')
        tokens = self.clean_tokens(tokens)
        if tokens != sample['expected']:
            print('-' * 8)
            print(sample['tweet'])
            print(text)
            print(tokens)
        self.assertEqual(sample['expected'], tokens)

    def test_urls_not_destroyed_by_remove_garbage(self):
        text = 'Azar says https://t.co/CwnG8H94mh https://t.co/E1ROgNAqlw'
        text = self.clean_text(text)
        self.assertIn('https://t.co/cwng8h94mh', text)
        self.assertIn('https://t.co/e1rognaqlw', text)

    def test_samples(self):
        for sample in data:
            self._test(sample)


data = [
    {
        'tweet': '#COVID19 vaccine could be available to "all Americans" by '
                 'early April, U.S. Health and Human Services Secretary Alex '
                 'Azar says https://t.co/CwnG8H94mh https://t.co/E1ROgNAqlw',
        'expected': ['covid19', 'vaccine', 'could', 'be', 'available', 'to',
                     'all', 'americans', 'by', 'early', 'april', 'usa',
                     'health', 'and', 'human', 'services', 'secretary',
                     'alex', 'azar', 'says']
    },
    {
        'tweet': '24 provincial-level regions across China report zero new '
                 'cases of #COVID-19 infection on Monday. '
                 'https://t.co/SALtWuqFJP',
        'expected': ['numtoken', 'provincial', 'level', 'regions', 'across',
                     'china', 'report', 'zero', 'new', 'cases', 'of', 'covid19',
                     'infection', 'on', 'monday']
    },
    {
        'tweet': '＃环球时报Editorial: After destroying Afghanistan and making '
                 'hasty withdrawal, the US has made people believe that '
                 'today’s world is facing a fundamental misfortune: The '
                 'strongest country is good at destruction, but not '
                 'interested in reconstruction.\u3000'
                 'https://t.co/iFHlg6qfYe https://t.co/4kyQkHWMqd',
        'expected': ['editorial', 'after', 'destroying', 'afghanistan', 'and',
                     'making', 'hasty', 'withdrawal', 'the', 'usa', 'has',
                     'made', 'people', 'believe', 'that', 'today', 'world',
                     'is', 'facing', 'a', 'fundamental', 'misfortune',
                     'the', 'strongest', 'country', 'is', 'good', 'at',
                     'destruction', 'but', 'not', 'interested', 'in',
                     'reconstruction']
    },
    {
        'tweet': "To prevent and contain #COVID19, indoor dinning will be "
                 "suspended in some areas of Guangzhou's Panyu district, "
                 "S China's Guangdong Province. The takeout, delivery and "
                 "dining in private rooms with a capacity of less than "
                 "10 people still remain. https://t.co/gUFug3uqqI",
        'expected': ['to', 'prevent', 'and', 'contain', 'covid19', 'indoor',
                     'dinning', 'will', 'be', 'suspended', 'in', 'some',
                     'areas', 'of', 'guangzhou', 'panyu', 'district', 'china',
                     'guangdong', 'province', 'the', 'takeout', 'delivery',
                     'and', 'dining', 'in', 'private', 'rooms', 'with', 'a',
                     'capacity', 'of', 'less', 'than', 'numtoken', 'people',
                     'still', 'remain']
    },
    {
        'tweet': 'U.S. consumer prices jumped in July, but weak demand and '
                 'the lapse in enhanced unemployment benefits will keep '
                 'inflation under control, economists said. '
                 'https://t.co/Ul2TZb3lnB https://t.co/Z1FQUsgJes',
        'expected': ['usa', 'consumer', 'prices', 'jumped', 'in', 'july',
                     'but', 'weak', 'demand', 'and', 'the', 'lapse', 'in',
                     'enhanced', 'unemployment', 'benefits', 'will', 'keep',
                     'inflation', 'under', 'control', 'economists', 'said']
    },
    {
        'tweet': 'Zambia on Tuesday reported the highest COVID-19 deaths in '
                 'a single day as the second wave of the pandemic takes a '
                 'toll on the southern African nation',
        'expected': ['zambia', 'on', 'tuesday', 'reported', 'the', 'highest',
                     'covid19', 'deaths', 'in', 'a', 'single', 'day', 'as',
                     'the', 'second', 'wave', 'of', 'the', 'pandemic', 'takes',
                     'a', 'toll', 'on', 'the', 'southern', 'african', 'nation']
    },
    {
        'tweet': 'https://t.co/dpyqd7ePix',
        'expected': []
    },
    {
        'tweet': "Former president of Colombia, Álvaro Uribe has tested "
                 "positive for COVID-19. The former South American leader "
                 "was put on house arrest yesterday in relation to a case "
                 "investigating alleged witness tampering. He's not "
                 "reporting any symptoms. https://t.co/dz9qGwhbST",
        'expected': ['former', 'president', 'of', 'colombia', 'álvaro',
                     'uribe', 'has', 'tested', 'positive', 'for', 'covid19',
                     'the', 'former', 'south', 'american', 'leader', 'was',
                     'put', 'on', 'house', 'arrest', 'yesterday', 'in',
                     'relation', 'to', 'a', 'case', 'investigating', 'alleged',
                     'witness', 'tampering', 'he', 'not', 'reporting', 'any',
                     'symptoms']
    },
    {
        'tweet': 'African states seek UN report on racism after Floyd killing',
        'expected': ['african', 'states', 'seek', 'un', 'report', 'on',
                     'racism', 'after', 'floyd', 'killing']
    },
    {
        'tweet': 'https://t.co/Db2WonzpUm',
        'expected': []
    },
    {
        'tweet': 'Xi expressed his hope that the US side can adopt concrete '
                 'measures to protect the safety and health of Chinese '
                 'citizens, including students, in the US. #coronavirus '
                 'https://t.co/jKtUDL1PDC',
        'expected': ['xi', 'expressed', 'his', 'hope', 'that', 'the', 'usa',
                     'side', 'can', 'adopt', 'concrete', 'measures', 'to',
                     'protect', 'the', 'safety', 'and', 'health', 'of',
                     'chinese', 'citizens', 'including', 'students', 'in',
                     'the', 'usa', 'coronavirus']
    },
    {
        'tweet': 'This week on the Agenda Podcast with @cole_stephen we '
                 'look at election systems around the world. We speak to '
                 'the founder of @SwapmyVote and Prof. Albert Weale about '
                 'understanding elections and how they keep our democracies '
                 'moving along.',
        'expected': ['this', 'week', 'on', 'the', 'agenda', 'podcast',
                     'with', 'mentiontoken', 'we', 'look', 'at', 'election',
                     'systems', 'around', 'the', 'world', 'we', 'speak', 'to',
                     'the', 'founder', 'of', 'mentiontoken', 'and', 'prof',
                     'albert', 'weale', 'about', 'understanding', 'elections',
                     'and', 'how', 'they', 'keep', 'our', 'democracies',
                     'moving', 'along']
    },
    {
        'tweet': 'HAVE A LISTEN',
        'expected': ['have', 'a', 'listen']
    },
    {
        'tweet': 'https://t.co/kf8Cihd62l https://t.co/Kb1Usyc6fG',
        'expected': []
    },
    {
        'tweet': 'China walks fine line to contain inflation while '
                 'maintaining growth '
                 'https://t.co/xO6nn1gPYv https://t.co/FtuCmTYNPC',
        'expected': ['china', 'walks', 'fine', 'line', 'to', 'contain',
                     'inflation', 'while', 'maintaining', 'growth']
    },
    {
        'tweet': 'Patriots governing HK VS Rioters destroying HK '
                 'https://t.co/Z4nFwSnLUQ',
        'expected': ['patriots', 'governing', 'hk', 'vs', 'rioters',
                     'destroying', 'hk']
    },
    {
        'tweet': 'Girls playing chess in insurgency-plagued and conservative '
                 'Afghanistan is new phenomenon that has been growing slowly '
                 'but steadily. More than 50 girls are currently learning '
                 'chess and the number is on the rise '
                 'https://t.co/9HBamMTQzc https://t.co/ColxMOnEVY',
        'expected': ['girls', 'playing', 'chess', 'in', 'insurgency',
                     'plagued', 'and', 'conservative', 'afghanistan', 'is',
                     'new', 'phenomenon', 'that', 'has', 'been', 'growing',
                     'slowly', 'but', 'steadily', 'more', 'than', 'numtoken',
                     'girls', 'are', 'currently', 'learning', 'chess', 'and',
                     'the', 'number', 'is', 'on', 'the', 'rise']
    },
    {
        'tweet': '#ChinaDefense The Chinese military could adopt #blockchain '
                 'technology to manage personnel data, give incentives, '
                 'boost training and maintain confidentiality. #PLA '
                 'https://t.co/QQLHYmp4sY https://t.co/Fs0qmnQ8nx',
        'expected': ['chinadefense', 'the', 'chinese', 'military', 'could',
                     'adopt', 'blockchain', 'technology', 'to', 'manage',
                     'personnel', 'data', 'give', 'incentives', 'boost',
                     'training', 'and', 'maintain', 'confidentiality', 'pla']
    },
    {
        'tweet': '#Opinion: A totally amicable restart of US-Russian '
                 'relations is impossible, but US and Russia still need '
                 'to maintain a minimum level of cooperation. Biden may '
                 'dislike Russia, but he still needs Russia. '
                 'https://t.co/FXumJL06Qy https://t.co/D5O4wPFyX4',
        'expected': ['opinion', 'a', 'totally', 'amicable', 'restart', 'of',
                     'usa', 'russian', 'relations', 'is', 'impossible', 'but',
                     'usa', 'and', 'russia', 'still', 'need', 'to', 'maintain',
                     'a', 'minimum', 'level', 'of', 'cooperation', 'biden',
                     'may', 'dislike', 'russia', 'but', 'he', 'still', 'needs',
                     'russia']
    },
    {
        'tweet': "President Xi told HK Chief Exec. #CarrieLam that the "
                 "central govt fully supports the #HKSAR's work plan "
                 "that Lam presented during her duty visit in Beijing "
                 "early this week and hoped that HKSAR govt departments "
                 "could work closely to create synergy and do a good job. "
                 "https://t.co/mQTWH1FMij",
        'expected': ['president', 'xi', 'told', 'hk', 'chief', 'exec',
                     'carrielam', 'that', 'the', 'central', 'govt', 'fully',
                     'supports', 'the', 'hksar', 'work', 'plan', 'that', 'lam',
                     'presented', 'during', 'her', 'duty', 'visit', 'in',
                     'beijing', 'early', 'this', 'week', 'and', 'hoped', 'that',
                     'hksar', 'govt', 'departments', 'could', 'work', 'closely',
                     'to', 'create', 'synergy', 'and', 'do', 'a', 'good',
                     'job']
    },
    {
        'tweet': 'HSBC chair supports #HongKong resolution under "One '
                 'Country, Two Systems" https://t.co/qvzY2Ndp5l '
                 'https://t.co/K6m9EfUUil',
        'expected': ['hsbc', 'chair', 'supports', 'hongkong', 'resolution',
                     'under', 'one', 'country', 'two', 'systems']
    },
    {
        'tweet': 'WATCH LIVE: View of Beirut port after massive blast '
                 'https://t.co/9G2kPmqi3c',
        'expected': ['watch', 'live', 'view', 'of', 'beirut', 'port', 'after',
                     'massive', 'blast']
    },
    {
        'tweet': 'Why has the West misunderstood and showed bias toward '
                 'China’s political system and economic development? '
                 'Check GT’s interview with scholar Zheng Yongnian '
                 'deconstructing those misinterpretations about China. '
                 'https://t.co/h3dBy3kXY6',
        'expected': ['why', 'has', 'the', 'west', 'misunderstood', 'and',
                     'showed', 'bias', 'toward', 'china', 'political',
                     'system', 'and', 'economic', 'development', 'check', 'gt',
                     'interview', 'with', 'scholar', 'zheng', 'yongnian',
                     'deconstructing', 'those', 'misinterpretations', 'about',
                     'china']
    },
    {
        'tweet': '#HK #LegCo lawmakers will be disqualified if they:',
        'expected': ['hk', 'legco', 'lawmakers', 'will', 'be', 'disqualified',
                     'if', 'they']
    },
    {
        'tweet': '- advocate or support "Hong Kong independence"',
        'expected': ['advocate', 'or', 'support', 'hong', 'kong',
                     'independence']
    },
    {
        'tweet': "- refuse to admit #China's sovereignty over #HKSAR",
        'expected': ['refuse', 'to', 'admit', 'china', 'sovereignty', 'over',
                     'hksar']
    },
    {
        'tweet': '- seek foreign interference in #HK affairs, endangering '
                 'national security',
        'expected': ['seek', 'foreign', 'interference', 'in', 'hk', 'affairs',
                     'endangering', 'national', 'security']
    },
    {
        'tweet': '- fail to uphold Basic Law, local regulations '
                 'https://t.co/Zz1ise4b9o',
        'expected': ['fail', 'to', 'uphold', 'basic', 'law', 'local',
                     'regulations']
    },
    {
        'tweet': 'Hunter Biden bombshell emails complete Burisma saga '
                 'puzzle with more to come, journo says',
        'expected': ['hunter', 'biden', 'bombshell', 'emails', 'complete',
                     'burisma', 'saga', 'puzzle', 'with', 'more', 'to', 'come',
                     'journo', 'says']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': '@JoeBiden https://t.co/7rDscKgUO5',
        'expected': ['mentiontoken']
    },
    {
        'tweet': '#Stoltenberg and #Austin deliver remarks before meeting',
        'expected': ['stoltenberg', 'and', 'austin', 'deliver', 'remarks',
                     'before', 'meeting']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': 'LIVE: https://t.co/VgkU6Osg0u https://t.co/QDuGfEf3SA',
        'expected': ['live']
    },
    {
        'tweet': 'Smuggled softshell tortoise abandoned on road in southern '
                 'India - photos',
        'expected': ['smuggled', 'softshell', 'tortoise', 'abandoned', 'on',
                     'road', 'in', 'southern', 'india', 'photos']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': 'https://t.co/OqcgldsMo2',
        'expected': []
    },
    {
        'tweet': 'UPDATE: Australians can get free coronavirus vaccine early '
                 'next year - prime minister',
        'expected': ['update', 'australians', 'can', 'get', 'free',
                     'coronavirus', 'vaccine', 'early', 'next', 'year',
                     'prime', 'minister']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': '#SputnikUpdates https://t.co/9R6xlYR4B0',
        'expected': ['sputnikupdates']
    },
    {
        'tweet': "Decades in the making, Russia's ‘50 years of victory’ "
                 "icebreaker is able to smash through ice that’s over two "
                 "metres thick – and it can reach parts of the North Pole "
                 "that no other ship can",
        'expected': ['decades', 'in', 'the', 'making', 'russia', 'numtoken',
                     'years', 'of', 'victory', 'icebreaker', 'is', 'able',
                     'to', 'smash', 'through', 'ice', 'that', 'over', 'two',
                     'metres', 'thick', 'and', 'it', 'can', 'reach', 'parts',
                     'of', 'the', 'north', 'pole', 'that', 'no', 'other',
                     'ship', 'can']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': 'FULL STORY: https://t.co/yNr4Q1HI4x https://t.co/LtcoSa44NG',
        'expected': ['full', 'story']
    },
    {
        'tweet': 'Coronavirus has exposed stark divides in US society as the '
                 'wealthy hole up in their homes and the poor are reduced to '
                 'delivering their supplies in often-unsafe conditions. '
                 'With mass layoffs underway, is class war imminent? - '
                 '@velocirapture23',
        'expected': ['coronavirus', 'has', 'exposed', 'stark', 'divides',
                     'in', 'usa', 'society', 'as', 'the', 'wealthy', 'hole',
                     'up', 'in', 'their', 'homes', 'and', 'the', 'poor', 'are',
                     'reduced', 'to', 'delivering', 'their', 'supplies', 'in',
                     'often', 'unsafe', 'conditions', 'with', 'mass',
                     'layoffs', 'underway', 'is', 'class', 'war', 'imminent',
                     'mentiontoken']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': 'https://t.co/Kt5sn6elk0',
        'expected': []
    },
    {
        'tweet': "Germany's Lufthansa to reduce quarter of flights during "
                 "next weeks over coronavirus spread",
        'expected': ['germany', 'lufthansa', 'to', 'reduce', 'quarter', 'of',
                     'flights', 'during', 'next', 'weeks', 'over',
                     'coronavirus', 'spread']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': '@lufthansa https://t.co/cYc1nRojTu',
        'expected': ['mentiontoken']
    },
    {
        'tweet': 'Two #Russian fighter jets, the #Su27 and #Su30SM, '
                 'intercepted the #USAirForce’s strategic bombers over '
                 'the neutral waters of the Black and #Baltic Seas on '
                 'Friday, according to a statement released by Russia’s '
                 'Ministry of Defence. https://t.co/DRRLotkTcH',
        'expected': ['two', 'russian', 'fighter', 'jets', 'the', 'su27', 'and',
                     'su30sm', 'intercepted', 'the', 'usairforce', 'strategic',
                     'bombers', 'over', 'the', 'neutral', 'waters', 'of',
                     'the', 'black', 'and', 'baltic', 'seas', 'on', 'friday',
                     'according', 'to', 'a', 'statement', 'released', 'by',
                     'russia', 'ministry', 'of', 'defence']
    },
    {
        'tweet': "Video: At least one person shot in #Florida's #BocaRaton "
                 "mall, suspect at large https://t.co/ThVDmTrH6I",
        'expected': ['video', 'at', 'least', 'one', 'person', 'shot', 'in',
                     'florida', 'bocaraton', 'mall', 'suspect', 'at', 'large']
    },
    {
        'tweet': 'Hey US, stop this muscle-flexing already, will you?',
        'expected': ['hey', 'usa', 'stop', 'this', 'muscle', 'flexing',
                     'already', 'will', 'you']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': 'https://t.co/2kT0hJQLuE',
        'expected': []
    },
    {
        'tweet': 'Oh boy! A review of 29 FBI applications to spy on '
                 'US citizens or residents found mistakes in every '
                 'single one.',
        'expected': ['oh', 'boy', 'a', 'review', 'of', 'numtoken', 'fbi',
                     'applications', 'to', 'spy', 'on', 'usa', 'citizens',
                     'or', 'residents', 'found', 'mistakes', 'in', 'every',
                     'single', 'one']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': 'https://t.co/gyu05VIzXy https://t.co/l7lxv9o4Ey',
        'expected': []
    },
    {
        'tweet': 'UPDATE | Israel plans to start vaccinating teenagers '
                 'aged 12-16',
        'expected': ['update', 'israel', 'plans', 'to', 'start', 'vaccinating',
                     'teenagers', 'aged', 'numtoken', 'numtoken']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': '#SputnikUpdates https://t.co/U7zUC6DVdi',
        'expected': ['sputnikupdates']
    },
    {
        'tweet': 'Protest over death of Black man in police custody '
                 'rocks #Brussels',
        'expected': ['protest', 'over', 'death', 'of', 'black', 'man', 'in',
                     'police', 'custody', 'rocks', 'brussels']
    },
    {
        'tweet': '#Belgium https://t.co/b47zAsuZ64',
        'expected': ['belgium']
    },
    {
        'tweet': 'WHO Wuhan mission expert advises against steep reliance on '
                 'US intelligence on COVID-19',
        'expected': ['worldhealthorganization', 'wuhan', 'mission', 'expert',
                     'advises', 'against', 'steep', 'reliance', 'on', 'usa',
                     'intelligence', 'on', 'covid19']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': 'https://t.co/nLLT0xqRJE',
        'expected': []
    },
    {
        'tweet': 'US Air Force needs to reverse-engineer parts for aging '
                 'stealth bomber',
        'expected': ['usa', 'air', 'force', 'needs', 'to', 'reverse',
                     'engineer', 'parts', 'for', 'aging', 'stealth', 'bomber']
    },
    {
        'tweet': 'https://t.co/sMvlFDA1Lq',
        'expected': []
    },
    {
        'tweet': 'UPDATE: Greece quarantines migrant shelter for '
                 'unaccompanied minors over COVID-19 outbreak',
        'expected': ['update', 'greece', 'quarantines', 'migrant', 'shelter',
                     'for', 'unaccompanied', 'minors', 'over', 'covid19',
                     'outbreak']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': '#SputnikUpdates https://t.co/J4285W0XUc',
        'expected': ['sputnikupdates']
    },
    {
        'tweet': 'UPDATE: Tally of COVID-19 cases in #Japan surpasses 63,500 '
                 'as 745 new infections confirmed, reports say',
        'expected': ['update', 'tally', 'of', 'covid19', 'cases', 'in',
                     'japan', 'surpasses', 'numtoken', 'as', 'numtoken', 'new',
                     'infections', 'confirmed', 'reports', 'say']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': '#SputnikUpdates https://t.co/vuHObVJA0y',
        'expected': ['sputnikupdates']
    },
    {
        'tweet': 'Shoppers return to #Rome street market as growth of '
                 '#COVID19 cases slows',
        'expected': ['shoppers', 'return', 'to', 'rome', 'street', 'market',
                     'as', 'growth', 'of', 'covid19', 'cases', 'slows']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': 'https://t.co/YH8jF0rRIU https://t.co/7gcxD1fAMp',
        'expected': []
    },
    {
        'tweet': "BREAKING: Yemen's Houthis down US-made drone near "
                 "Saudi border - reports https://t.co/kMBMpVWEfJ "
                 "https://t.co/4jo6vJpCUa",
        'expected': ['breaking', 'yemen', 'houthis', 'down', 'usa', 'made',
                     'drone', 'near', 'saudi', 'border', 'reports']
    },
    {
        'tweet': "Australia’s Prime Minister says that Canberra will "
                 "stand by its values and continue to act with its own "
                 "interests at heart after China accused it of "
                 "'poisoning bilateral relations'",
        'expected': ['australia', 'prime', 'minister', 'says', 'that',
                     'canberra', 'will', 'stand', 'by', 'its', 'values', 'and',
                     'continue', 'to', 'act', 'with', 'its', 'own',
                     'interests', 'at', 'heart', 'after', 'china', 'accused',
                     'it', 'of', 'poisoning', 'bilateral', 'relations']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': 'https://t.co/LZO2aMA8D6',
        'expected': []
    },
    {
        'tweet': "Prince Philip spends night in hospital for 'observation "
                 "and treatment' https://t.co/ZnYmEqJqzu",
        'expected': ['prince', 'philip', 'spends', 'night', 'in', 'hospital',
                     'for', 'observation', 'and', 'treatment']
    },
    {
        'tweet': 'Covid-19 has changed the way people keep fit 🏋🏽\u200d♀️',
        'expected': ['covid19', 'has', 'changed', 'the', 'way',
                     'people', 'keep', 'fit']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': 'With gyms closed, virtual exercises and home workouts are '
                 'order of the day - so has exercise changed forever?',
        'expected': ['with', 'gyms', 'closed', 'virtual', 'exercises', 'and',
                     'home', 'workouts', 'are', 'order', 'of', 'the', 'day',
                     'so', 'has', 'exercise', 'changed', 'forever']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': '#WorklifeIndia https://t.co/VHkOXdBTWq',
        'expected': ['worklifeindia']
    },
    {
        'tweet':
            'Hong Kong protests: NBA fans join anti-China display '
            'https://t.co/BlzLRwDmEn',
        'expected': ['hong', 'kong', 'protests', 'nba', 'fans', 'join', 'anti',
                     'china', 'display']
    },
    {
        'tweet': 'Corey Lewandowski: Ex-Trump aide stonewalls impeachment '
                 'hearing https://t.co/xBnQw6XWUa',
        'expected': ['corey', 'lewandowski', 'ex', 'trump', 'aide',
                     'stonewalls', 'impeachment', 'hearing']
    },
    {
        'tweet': 'Fukushima: Radioactive water may be dumped in Pacific '
                 'https://t.co/nv3jUtFMfH',
        'expected': ['fukushima', 'radioactive', 'water', 'may', 'be',
                     'dumped', 'in', 'pacific']
    },
    {
        'tweet': "Lawro's predictions: Man City v Chelsea - Champions "
                 "League final special with Noel Gallagher and Dot Major "
                 "https://t.co/CvN7zOlyNF",
        'expected': ['lawro', 'predictions', 'man', 'city', 'chelsea',
                     'champions', 'league', 'final', 'special', 'with', 'noel',
                     'gallagher', 'and', 'dot', 'major']
    },
    {
        'tweet': 'New Zealand: Man brings clown to redundancy meeting '
                 'https://t.co/STHO6MtC7J',
        'expected': ['new', 'zealand', 'man', 'brings', 'clown', 'to',
                     'redundancy', 'meeting']
    },
    {
        'tweet': "Italy v Scotland: Six Nations must-win for Gregor "
                 "Townsend's side https://t.co/8oR6qxpcKb",
        'expected': ['italy', 'scotland', 'six', 'nations', 'must', 'win',
                     'for', 'gregor', 'townsend', 'side']
    },
    {
        'tweet': 'The fungus and bacteria tackling plastic waste '
                 'https://t.co/UCzCkpvjsF',
        'expected': ['the', 'fungus', 'and', 'bacteria', 'tackling', 'plastic',
                     'waste']
    },
    {
        'tweet': "London Ambulance Service: 'We take thousands of calls "
                 "every day - it's tough' https://t.co/anRkG9NIuy",
        'expected': ['london', 'ambulance', 'service', 'we', 'take',
                     'thousands', 'of', 'calls', 'every', 'day', 'it', 'tough']
    },
    {
        'tweet': '#Euro2020: Teesside restaurant to honour 2,000 free '
                 'parmo pledge if England wins https://t.co/t2XJ9QQxBk',
        'expected': ['euro2020', 'teesside', 'restaurant', 'to', 'honour',
                     'numtoken', 'free', 'parmo', 'pledge', 'if', 'england',
                     'wins']
    },
    {
        'tweet': 'The UK government has extended a ban on commercial '
                 'evictions, brought in to protect firms struggling in the '
                 'pandemic.',
        'expected': ['the', 'uk', 'government', 'has', 'extended', 'a', 'ban',
                     'on', 'commercial', 'evictions', 'brought', 'in', 'to',
                     'protect', 'firms', 'struggling', 'in', 'the', 'pandemic']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': 'Yet many firms are still being taken to court over rent '
                 'they have not paid https://t.co/1Tzarbekzq',
        'expected': ['yet', 'many', 'firms', 'are', 'still', 'being', 'taken',
                     'to', 'court', 'over', 'rent', 'they', 'have', 'not',
                     'paid']
    },
    {
        'tweet': 'US West Coast fires in maps, graphics and images '
                 'https://t.co/i2uQ0vHi0T',
        'expected': ['usa', 'west', 'coast', 'fires', 'in', 'maps', 'graphics',
                     'and', 'images']
    },
    {
        'tweet': 'Scottish ministers seek clarity over Covid-19 '
                 'vaccine supply https://t.co/vcN4Q5UsPN',
        'expected': ['scottish', 'ministers', 'seek', 'clarity', 'over',
                     'covid19', 'vaccine', 'supply']
    },
    {
        'tweet': '(5/9) “We put our faith in almighty God” and “The battle '
                 'for the soul of the nation”',
        'expected': ['numtoken', 'we', 'put', 'our', 'faith', 'in', 'almighty',
                     'god', 'and', 'the', 'battle', 'for', 'the', 'soul', 'of',
                     'the', 'nation']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': 'Here’s why the Christian vote is so significant in US '
                 'elections',
        'expected': ['here', 'why', 'the', 'christian', 'vote', 'is', 'so',
                     'significant', 'in', 'usa', 'elections']

    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': '#Election2020 #ElectionDay',
        'expected': ['election2020', 'electionday']
    },
    {
        'tweet': '',
        'expected': []
    },
    {
        'tweet': 'https://t.co/BgzFyI0XaU',
        'expected': []
    },
    {
        'tweet': "Top US Nike executive resigns from company after "
                 "details of son's sneaker resale business become "
                 "public https://t.co/g6lDFWmBxm",
        'expected': ['top', 'usa', 'nike', 'executive', 'resigns', 'from',
                     'company', 'after', 'details', 'of', 'son', 'sneaker',
                     'resale', 'business', 'become', 'public']
    },
    {
        'tweet': 'Herman Cain, Republican ex-presidential candidate, '
                 'dies after Covid fight https://t.co/HjCVvmLTyO',
        'expected': ['herman', 'cain', 'republican', 'ex', 'presidential',
                     'candidate', 'dies', 'after', 'covid19', 'fight']
    },
    {
        'tweet': 'i weekend: "Virus shock to global economy" #BBCPapers '
                 '#TomorrowsPapersToday (via @hendopolis) '
                 'https://t.co/i1I3Jje9hI',
        'expected': ['i', 'weekend', 'virus', 'shock', 'to', 'global',
                     'economy', 'bbcpapers', 'tomorrowspaperstoday', 'via',
                     'mentiontoken']
    },
    {
        'tweet': 'Australians to be offered half-price flights to boost '
                 'local tourism https://t.co/CWTq0rKTwS',
        'expected': ['australians', 'to', 'be', 'offered', 'half', 'price',
                     'flights', 'to', 'boost', 'local', 'tourism']
    },
    {
        'tweet': "Coronavirus deaths rise over 1,000 in Italy, with "
                 "cases in Europe's worst hit country passing 15,000 "
                 "https://t.co/Wqtez0Y7FH",
        'expected': ['coronavirus', 'deaths', 'rise', 'over', 'numtoken',
                     'in', 'italy', 'with', 'cases', 'in', 'europe', 'worst',
                     'hit', 'country', 'passing', 'numtoken']
    }
]
