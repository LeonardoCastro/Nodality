#from analysis_text import keywords_lf_generator, regex_lf_generator
import re
from snorkel.labeling import labeling_function

# Constants
UKRAINE = 1
LOCAL_ELECTIONS = 2
COVID = 3
PARTYGATE = 4
CRISIS = 5
BREXIT = 6

ABSTAIN = -1

lfs_dict = dict()
collection_dicts = dict()

#### Labeling functions generators
def keywords_lf_generator(keywords: list, 
                          constant: int, 
                          name: str = 'keywordsLabelingFunction',
                          ABSTAIN: int = -1):
    @labeling_function()
    def func(x):
        return constant if any(word in x.text.lower() for word in keywords) else ABSTAIN
    func.name = name
    return func
        
def regex_lf_generator(regex, 
                       constant: int, 
                       name: str = 'regexLabelingFunction',
                       ABSTAIN: int = -1):
    @labeling_function()
    def func(x):
        return constant if re.search(regex, x.text.lower(), flags=re.I) else ABSTAIN
    func.name = name
    return func


######## Ukraine lfs
ukraine_keywords = [
                'ukraine', 'russia', 'ukrainian', 'russian', 'putin', "zelensky", 'zelensk', "mariupol", 
                "luhansk", "donetsk", "#ukraine", 'donbas', 'invasion', 'finland', 'oligarch',
                #'visa', 'nato', " war ",
                ]

ukraine_lfs = {
    'ukraine_keywords': keywords_lf_generator(ukraine_keywords, UKRAINE, 'ukraine_keywords'),
    'ukraine_regex': regex_lf_generator(r"ukrain.", UKRAINE, 'ukraine_regex'),
    'russia_regex': regex_lf_generator(r"russia", UKRAINE, 'russia_regex'),
    'putin_regex': regex_lf_generator(r"putin", UKRAINE, 'putin_regex'),
    'oligarch_regex': regex_lf_generator(r"oligarch", UKRAINE, 'oligarch_regex'),
    }

collection_dicts['ukraine_lfs'] = ukraine_lfs

######## Local elections lfs
elections_keywords = [
                'elections', 'results', 'vote', 'voting', 'council', 'councils', 'poll', 'candidate',
                ]

elections_lfs = {
    'elections_keywords': keywords_lf_generator(elections_keywords, LOCAL_ELECTIONS, 'elections_keywords'),
    'elections_regex': regex_lf_generator(r"election", LOCAL_ELECTIONS, 'elections_regex'),
    'polls_regex': regex_lf_generator(r"poll", LOCAL_ELECTIONS, 'polls_regex'),
    'candidate_regex': regex_lf_generator(r"candidate", LOCAL_ELECTIONS, 'candidate_regex'),
    'voting_regex': regex_lf_generator(r" vot", LOCAL_ELECTIONS, 'voting_regex'), 
    'le2_regex': regex_lf_generator(r"le2", LOCAL_ELECTIONS, 'le2_regex'),
    'labourdoorstep_regex': regex_lf_generator(r"labourdoorstep", LOCAL_ELECTIONS, 'labourdoorstep_regex'),
    'may5_regex': regex_lf_generator(r"(may|5th|5)\W+(?:\w+\W+){0,6}?(5|may)", LOCAL_ELECTIONS, 'may5_regex')
    }

collection_dicts['elections_lfs'] = elections_lfs

######## COVID lfs
covid_keywords = [
                'covid', 'covid-19', 'sars-cov-2', 'coronavirus', 'pandemic', 'lockdown', 'vaccine', 'vaccines', 
                'rollout', 'vaccination', 
                #'cases'
                ]

covid_lfs = {
    'covid_keywords': keywords_lf_generator(covid_keywords, COVID, 'covid_keywords'),
    'vaccines_regex': regex_lf_generator(r"vaccin", COVID, 'vaccines_regex'),
    'rollout_regex': regex_lf_generator(r"vaccin\W+ rollout", COVID, 'rollout_regex'),
    'covid_regex': regex_lf_generator(r"covid", COVID, 'covid_regex'),
    'lockdown_regex': regex_lf_generator(r"lockdown", COVID, 'lockdown_regex'),
    'pandemic_regex': regex_lf_generator(r"vaccin", COVID, 'pandemic_regex'),   
    'corona_regex': regex_lf_generator(r"corona", COVID, 'corona_regex'),
}

collection_dicts['covid_lfs'] = covid_lfs

######## Partygate lfs
partygate_keywords = [
                '#partygate', 'partygate', 'illegal', 'sue gray', 'suegray', 
                'report', 'investigation', 'misled', 'sue', 'gray', 
                #'bojo', 'boris', 'johnson'
                ]

partygate_lfs = {
    'partygate_kewyords': keywords_lf_generator(partygate_keywords, PARTYGATE, 'partygate_keywords'),
    'parliament_regex': regex_lf_generator(r"(misled|parliament)\W+(?:\w+\W+){1,6}?(misled|parliament)", 
                                           PARTYGATE, 'parliament_regex'),
    'rules_regex': regex_lf_generator(r"break\W+(?:\w+\W+){0,6}?rule", PARTYGATE, 'rules_regex'),
    'suegray_regex': regex_lf_generator(r"sue gray", PARTYGATE, 'suegray_regex'),
    'suegray2_regex': regex_lf_generator(r"suegray", PARTYGATE, 'suegray2_regex'),
    'partygate_regex': regex_lf_generator(r"partygate", PARTYGATE, 'partygate_regex'),
    'illegal_regex': regex_lf_generator(r"illegal\W+(?:\w+\W+){0,6}?part", PARTYGATE, 'illegal_regex'),
}

collection_dicts['partygate_lfs'] = partygate_lfs

######## Cost of living crisis lfs
crisis_keywords = [
                "fuel", "bills", "petrol", "energy", "inflation", 'costs', 'electricity', 'oil',
                'poverty', 'austerity', 'windfall', 'poverty', 'cost-of-living', 'council tax'
                ]

crisis_lfs = {
    'crisis_keywords': keywords_lf_generator(crisis_keywords, CRISIS, 'crisis_keywords'),
    'living_regex': regex_lf_generator(r"cost\W+of\W+living", CRISIS, 'living_regex'),
    'living2_regex': regex_lf_generator(r"costofliving", CRISIS, 'living2_regex'),
    'prices_regex': regex_lf_generator(r"(increasing|rising|energy) (price|bill)", CRISIS, 'prices_regex'),
    'tax_regex': regex_lf_generator(r"tax", CRISIS, 'tax_regex'),
    'natins_regex': regex_lf_generator(r"national insurance", CRISIS, 'natins_regex'),
    'council_regex': regex_lf_generator(r"council tax", CRISIS, 'council_regex'),
    'inflation_regex': regex_lf_generator(r"(rising|increasing|historic|high) inflation", CRISIS, 'inflation_regex')
    }

collection_dicts['crisis_lfs'] = crisis_lfs

######## Brexit lfs
brexit_keywords = [
                'brexit', 'protocol', 'article 50', 'european union', 'northern ireland protocol', 
                #' eu '
                ]

brexit_lfs = {
    'brexit_keywords': keywords_lf_generator(brexit_keywords, BREXIT, 'brexit_keywords'),
    'brexit_regex': regex_lf_generator(r"brexit", BREXIT, 'brexit_regex'),
    'protocol_regex': regex_lf_generator(r"northern ireland protocol", BREXIT, 'protocol_regex'),
    'ni_regex': regex_lf_generator(r"northern ireland", BREXIT, 'ni_regex'),
    'goodfriday_regex': regex_lf_generator(r"good friday", BREXIT, 'goodfriday_regex'),
    'article50_regex': regex_lf_generator(r"article 50", BREXIT, 'article50_regex'),   
    'eu_regex': regex_lf_generator(r"european union", BREXIT, 'eu_regex'),
}

collection_dicts['brexit_lfs'] = brexit_lfs

######### Export dictionary

for (_, dict_) in collection_dicts.items():
    for (key, lf) in dict_.items():
        lfs_dict[key] = lf

