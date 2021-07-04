from youtubesearchpython import * #used to take user input and search youtube and returns url to be used by youtube_dl
def search(term):
    videosSearch = VideosSearch(term, limit = 1, language = 'en', region = 'US') #takes term(user input from discord) and searched youtube and returns a messed up dictonary 
    results= videosSearch.result(mode = ResultMode.dict) #makes the output of the search a dict 
    unfinishedlink = str(results['result']).strip('[]') #remove the messed up parts of the returned dict form the search results
    link = eval(unfinishedlink) #makes the varible unfinisedlink back into a dict (could technicly be unsafe)
    return [link['link']]

def time_search(term):
    videosSearch = VideosSearch(term, limit = 1, language = 'en', region = 'US') #takes term(user input from discord) and searched youtube and returns a messed up dictonary 
    results= videosSearch.result(mode = ResultMode.dict) #makes the output of the search a dict 
    unfinishedlink = str(results['result']).strip('[]') #remove the messed up parts of the returned dict form the search results
    link = eval(unfinishedlink) #makes the varible unfinisedlink back into a dict (could technicly be unsafe)
    minsec = str([link['duration']]).strip("[ '' ]")
    m, s = minsec.split(':')
    duration = int(m) * 60 + int(s)
    return duration
def name_search(term):
    videosSearch = VideosSearch(term, limit = 1, language = 'en', region = 'US') #takes term(user input from discord) and searched youtube and returns a messed up dictonary 
    results= videosSearch.result(mode = ResultMode.dict) #makes the output of the search a dict 
    unfinishedlink = str(results['result']).strip('[]') #remove the messed up parts of the returned dict form the search results
    link = eval(unfinishedlink) #makes the varible unfinisedlink back into a dict (could technicly be unsafe)
    return [link['title']]
