# playwright_metascrapers
A meta script to automatically pull cookies and make a data request for json file using playwright,
Requires a bit of trial and error finding the right request to get the data you want and get the right cookie.

On the playwright_meta.py you need to change url, cookie_location and accept_cookies_name.

>*Url* will be the base url of the website you want the cookie of.

>*Cookie_location* is the index of the cookie you want to use to make the request.

>*Accept_cookies_name* needs to be equal to the text in the button to accept cookies that opens up once you start the script.

Websites have several cookies, it's a bit of trial and error to find the right one, likewise they make several GET requests and receive several responses so you have to go through the Json files in the network tab or js/html to find the call you want to make.

First you find the right Get request call you want, then try to make it with several cookies until you get one that gives your Response 200 (ie. the data you're looking for).
You could make a function to rotate cookie indexes until you get the right one if you wanted to automate that bit.

I also have attached a template file *playwright_asos* which is where *main* is. 
I used for the Asos website, you can more or less keep the same template and use it for whatever website. The variables you can change are:

>*all email variables at the top* self explanatory, it's to make the gmail notification work

>*url2* this is the specific Get request call.

>*isInStock* you need to parse the variable you want from the Get response, so this will need to be changed.

The third file is a gmail notification script, you need an app token to make it work (just google it), the variables are all to be changed in *playwright_asos* so you can leave that file as is.

Fourth file I just use to check full responses from the websites when I have all the cookies etc, it's simply easier to read than on a browser network tab.
