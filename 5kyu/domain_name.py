def domain_name(url):
    seperators=[":", "/", "."]
    
    for sep in seperators:
        url = url.replace(sep, " ")
    
    url_words=url.split(" ")
    print(url_words)
    
    possible_prefixes=["http", "https", "www" , ""]
    
    for word in url_words:
        if word not in possible_prefixes:
            return word
