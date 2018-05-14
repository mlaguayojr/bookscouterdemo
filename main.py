"""
    Demo for https://www.reddit.com/r/Python/comments/8j5sjv/can_you_build_a_python_web_bot_that_doesnt_open_a/
    
    Python 3
"""

# imported modules
from sys import argv, exit
from json import loads
from urllib.request import urlopen

def main(options):
    
    # The site has three options: sell, buy, rent
    # After looking at how the page functions:
    url = "https://api.bookscouter.com/v3/search?term=%s" % (options[0])

    req = urlopen(url)
    
    # If the request failed, print error and why it failed, then close
    if req.code != 200:
        print("HTTP ERROR:", req.status_code)
        print("REASON:", req.reason)
        exit()
    
    # Continue if the request went through
    data = loads( req.read() )

    # The response is a dictionary with an index as an array
    data = data['data'][0]
    print(data)

if __name__=="__main__":

    # Test
    main([9780764573712])