# playwright_metascrapers
A meta script to automatically pull cookies and make a data request for json file using playwright.

It requires a bit of trial and error finding the right request to get the data you want and get the right cookie.

Websites make several GET requests and have several cookies, so you have to go through the Json files in the network tab to find the call you want to make.

(Please Note: I made an assumption that the data you seek will most likely be of JSON type, but some websites have different response types such as XML, in the network tab to find the call you want to make.)

First you'll want to find the right Get request call you want, then try to run it with several cookies until you get one that gives your Response 200 (as well as the data you're looking for).
You could make a function to rotate cookie indexes until you get the right one if you wanted to automate that bit.

Instructions for use:

On the playwright_meta.py you need to change the variables *url*, *cookie_location* and *accept_cookies_name*.

>*Url* : will be the url of the website you want the cookie of, any url should be fine so long as you can get cookies from it, if the script doesn't work you may want to try the url at the home page level (ie. https://website.com/home).

>*Cookie_location* : is the index of the cookie you want to use to make the request. The script returns all the cookies as dictionary list, so just try from position 0 to n (n being the number of returned cookies - 1) until it works.

>*Accept_cookies_name* : needs to be equal to the text in the button to accept cookies that opens up once you start the script. In this instance to accept the cookies I need to click on a button that says "That's ok".

I also have attached a template file *playwright_asos* which is where the *main* function is. 
I used this for the Asos website, you can more or less keep the same template and use it for whatever website. 

The variables you can change are:

>*all the email variables at the top* : these are self explanatory, it's to make the gmail notification work.

>*url2* : this is the specific Get request call, it's the one with the data you want, most likely of JSON type, it can be found in the network tab.

>*isInStock* : you need to parse the variable or data you want from the Get response, so this will need to be changed. This will require you to be a bit fluent with nested data indexing, in my current case I'm accessing a nested list and extracting the value of the 'isInStock' key. Most responses will give you nested structures like this, where you have lists and dictionaries inside each other.

The third file is a gmail notification script, you need an app token to make it work (you can simply google it and follow instructions), the variables are all to be changed within *playwright_asos* so you can leave that file as is.

The fourth file 'import requests.py' is one I just use to check full responses from the websites when I have all the cookies etc, it's simply easier to read than on a browser network tab.
