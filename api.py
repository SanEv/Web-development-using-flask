import paralleldots
paralleldots.set_api_key('LSOHkGeW6WSP4kHGnMqgphZoTCxqS07m1LCvh86iQQ8')

def ner(text):
    ner = paralleldots.ner(text)
    return ner

def sa(text):
    sa = paralleldots.sentiment(text)
    return sa

def abuse_detec(text):
    ad = paralleldots.abuse(text)
    return ad

