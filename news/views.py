from django.shortcuts import render

from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key ='4dbc17e007ab436fb66416009dfb59a8')

#BBC
top = newsapi.get_top_headlines(sources ='bbc-news')
l = top['articles']
news =[]
url =[]
for i in range(len(l)):
    f = l[i]
    news.append(f['title'])
    url.append(f['url'])   
mylist = zip(news, url)

#CNN
cnn = newsapi.get_top_headlines(sources ='cnn')
cnn_l = cnn['articles']
cnn_news = []
cnn_url = []
for x in range(len(cnn_l)):
    c_f = cnn_l[x]
    cnn_news.append(c_f['title'])
    cnn_url.append(c_f['url'])
cnn_list = zip(cnn_news, cnn_url)

#Reuters
rt = newsapi.get_top_headlines(sources ='reuters')
rl = rt['articles']
rnews =[]
rurl =[]
for ri in range(len(rl)):
    rf = rl[ri]
    rnews.append(rf['title'])
    rurl.append(rf['url'])   
rmylist = zip(rnews, rurl)

#ABC NEWS
at = newsapi.get_top_headlines(sources ='abc-news')
al = at['articles']
anews =[]
aurl =[]
for ai in range(len(al)):
    af = al[ai]
    anews.append(af['title'])
    aurl.append(af['url'])   
amylist = zip(anews, aurl)

#Google News
gt = newsapi.get_top_headlines(sources ='google-news')
gl = gt['articles']
gnews =[]
gurl =[]
for gi in range(len(gl)):
    gf = gl[gi]
    gnews.append(gf['title'])
    gurl.append(gf['url'])   
gmylist = zip(gnews, gurl)

#Tech Crunch
tt = newsapi.get_top_headlines(sources ='techcrunch')
tl = tt['articles']
tnews =[]
turl =[]
for ti in range(len(tl)):
    tf = tl[ti]
    tnews.append(tf['title'])
    turl.append(tf['url'])   
tmylist = zip(tnews, turl)

def index(request):
    
    

    context = {

        "mylist":mylist,
        "cnn_list":cnn_list,
        "rmylist":rmylist,
        "amylist":amylist,
        "gmylist":gmylist,
        "tmylist":tmylist,
    }

    return render(request, 'index.html', context)
