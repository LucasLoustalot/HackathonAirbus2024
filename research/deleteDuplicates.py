def getDomainName(url: str) -> str:
    domainName = ""
    i = 0
    while url[i] != '/':
        i += 1
    while url[i] != '/':
        domainName += url[i]
        i += 1
    return domainName

def deleteDuplicates(urls: list[str]) -> list[str]:
    domainsNames = []
    newListURLs = []
    skip = False
    for url in urls:
        for domainName in domainsNames:
            if domainName in url:
                skip = True
        if not skip:
            newListURLs.append(url)
            domainsNames.append(getDomainName(url))
        skip = False
    return newListURLs


