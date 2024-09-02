def domain_name(url):
    
    print(url)
    count = url.count('.')
    
    if count == 1:
        if url.find('/') == 5 or url.find('/') == 6:
            domain = url[(url.find('/')+2):url.find('.')]
        else:
            domain = url[:url.find('.')]
        return domain
            
    if count == 2:
        ### 2 cases
        # www.
        # else no www. (e.g. -> .co.jp)
        if url[url.find('.')-1] == 'w':
            domain = url[(url.find('.')+1):]
            domain = domain[:domain.find('.')]
        elif url.find('/') == 5 or url.find('/') == 6:
            domain = url[(url.find('/')+2):url.find('.')]
        else: 
            domain = url[:url.find('.')]

        return domain
        
    if count >= 3:
        domain = url[(url.find('.')+1):]
        domain = domain[:domain.find('.')]
        return domain