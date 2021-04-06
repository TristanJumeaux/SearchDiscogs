import discogs_client

def identify():
    return discogs_client.Client("TestRequests",user_token="")

def getWantlist(d):
    return d.identity().wantlist

def getRelease(d,release):
    return d.release(release)

def main():

    d = identify()
    wantlist = getWantlist(d)
    results = d.release(44537)
    print(results)
    print(len(wantlist))

main()

