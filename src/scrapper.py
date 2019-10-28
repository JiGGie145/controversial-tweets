#  Source https://curl.trillworks.com/
import requests

cookies = {
    'personalization_id': 'v1_PY9I+wlE/O5vYKnTxi4dfg==',
    'syndication_guest_id': 'v1%3A155554700190590486',
    'guest_id': 'v1%3A155337971369945963',
    '_ga': 'GA1.2.1206339888.1553379754',
    'ads_prefs': 'HBIRAAA=',
    'kdt': 'OTSmieddOTJUroEvVAtljfZfRlk4spYYqXTz7GyD',
    'remember_checked_on': '1',
    'twid': 'u%3D421837149',
    'auth_token': '3e5100c5c6a7e888257f5f4b14ca6810a6586c43',
    'csrf_same_site_set': '1',
    'rweb_optin': 'side_no_out',
    'csrf_same_site': '1',
    'external_referer': 'padhuUp37zjSBoCQckbj5wrkNqGthya6d1JuD%2BS8Su1PsHfAfnJn%2Fwx5pba48IIanlGvbh3K8YfGXenJ6wYVc8GDk1rkaSZXvneTZ%2BYtuMXmtnWj16XlSQmz%2B8N6F3my%2BOnxf%2FLEXvNBy10K%2Fhkv%2BtGFwhBoxBty|0|GlWr2u5wzZipnVja1ZbglFG7jRzcDRbyg7bgNkbeVpZRXGD6I8pM33Iko7WXBWIGNjiF3%2Bbc%2B4c%3D',
    'tfw_exp': '0',
    'des_opt_in': 'Y',
    'ct0': '05d77dce005c0e3f72355ff440ec6957',
    '_gid': 'GA1.2.18270856.1572040849',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',
    'Accept': '*/*',
    'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
    'x-twitter-active-user': 'yes',
    'x-csrf-token': '05d77dce005c0e3f72355ff440ec6957',
    'Origin': 'https://twitter.com',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = (
    ('include_profile_interstitial_type', '1'),
    ('include_blocking', '1'),
    ('include_blocked_by', '1'),
    ('include_followed_by', '1'),
    ('include_want_retweets', '1'),
    ('include_mute_edge', '1'),
    ('include_can_dm', '1'),
    ('include_can_media_tag', '1'),
    ('skip_status', '1'),
    ('cards_platform', 'Web-12'),
    ('include_cards', '1'),
    ('include_composer_source', 'true'),
    ('include_ext_alt_text', 'true'),
    ('include_reply_count', '1'),
    ('tweet_mode', 'extended'),
    ('include_entities', 'true'),
    ('include_user_entities', 'true'),
    ('include_ext_media_color', 'true'),
    ('include_ext_media_availability', 'true'),
    ('send_error_codes', 'true'),
    ('count', '4000'),
    ('ext', 'mediaStats,highlightedLabel,cameraMoment'),
    ('simple_quoted_tweet', 'true'),
)

response = requests.get('https://api.twitter.com/2/timeline/conversation/1187815574405029893.json', headers=headers, params=params, cookies=cookies)


urls = {
    'cuadernos': ['https://twitter.com/yamilsantoro/status/1187146858633846785'],
    'chequeado': ['https://twitter.com/Chequeado/status/1186118160287698944',
                  'https://twitter.com/Chequeado/status/1186418388412878852',
                  'https://twitter.com/Chequeado/status/1186341468199362562',
                  'https://twitter.com/Chequeado/status/1183912883677212672'
                 ],
    'economia': ['https://twitter.com/Miguel_Boggiano/status/1187815574405029893']
}

def get_tweets(dic_urls, header, params, cookies):
    for key, value in dic_urls.items():
        for url in value:
            id_str = url.split('/')[-1]
            url = 'https://api.twitter.com/2/timeline/conversation/' + id_str + '.json'
            response = requests.get(url, headers=headers, params=params, cookies=cookies)
            with open('../pickle/'+key+ id_str +'.json'+'.pkl', "wb") as fd:
                pickle.dump(response.json()['globalObjects']['tweets'], fd)
