import requests
import json

url = 'https://www.asos.com/api/customer/recommendation/v4/customer/me/alike'
params = {
    'productids': '205495961',
    'type': 'ymal',
    'expand': 'products',
    'limit': '18',
    'store': 'COM',
    'country': 'GB',
    'currency': 'GBP',
    'lang': 'en-GB',
    'keyStoreDataversion': 'h7g0xmn-38'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjB6Y3RJdzd2WHdZSGRTT1J1NW5JWnRjajNrQSIsImtpZCI6IkQzMzcyRDIzMEVFRjVGMDYwNzc1MjM5MUJCOTlDODY2RDcyM0RFNDAifQ.eyJpc3MiOiJodHRwczovL215LmFzb3MuY29tL3RydXN0IiwiYXVkIjoiaHR0cHM6Ly9hcGkuYXNvcy5jb20iLCJleHAiOjE3MzMxMDIwOTgsIm5iZiI6MTcwMTU2NjA5OCwiY2xpZW50X2lkIjoiRDkxRjJEQUEtODk4Qy00RTEwLTkxMDItRDZDOTc0QUZCRDU5Iiwic2NvcGUiOiJzZW5zaXRpdmUiLCJzdWIiOiI0OTY1MTIwNjkyMjg0Y2ZlOGIxNDMzMDQ2YTI2YjIxOCIsImF1dGhfdGltZSI6MTcwMTU2NjA5OCwiaWRwIjoic2l0ZSIsInNlc3MiOiIyM2FjN2QwNzczMjg0OWNmOWVlYTYxZjFkMGE2ZmYwZCIsImFtciI6WyJhbm9uIl19.fncq35Z_8W6qx2IEEsAfNKv-558Oha9dkzWWhblIy5Q82xFud8CdLkl5HqzwX4TucvRBiZE_W5BLjB9UdOY0f_OSomyn35IKIALkM4SmJyD-GHXzbzL4Ev3AeIAYgMCPKGjlWBDXbhKHXsA3oGb43QzPuVMBNdpgpvmikOfKVKvNrFJH4BRB9pwEguRr5-iEhuIt1hexXjkJ46G7jjGSJq4gft03iBP3HIcIZbLNP3OAiVqIHESaPyBuYtpJkiYW4rWL7SS6EQe_5Cg_b7yfcS6OV0MlIsY-9THIVCoQt394zp5Fai5ltniBOPZNFoyjCZY8GkKbITmV9iDP8YyHNK8vQE_TIpIedZl06U72F8OIrHKm-Lq0I_iDX6D5jvOSrGGb8ZjOqiTDWmcyeOYGA8bgfpoFQd0DgsAyFC6VqGo1YjnQu1Ei6RiNruHarAbbjPjwuM2KXfUuV4IRc-LsehTGNtuQBtWIirOqz7xFLGxklG64yZqFUGYzkzyS2Zgxk5wyuBfyhY3YvDNILlU6u0leY8LBzWn0XBdZ0kWHB_gE06L4GFXIcN8MwY5iX4aEFHFb-jCXwMzYnqO5lUUV6s4h4f4Lvl8saCI-L331JpnKIs4lZwoKMpnwGesfiJPugsC4POMbA9QPW2WIbmzBujoZ__LrUC3XNvyjMuEKz44',
    'asos-c-recs-scope': 'pdp_ymal',
    'asos-cid': 'feaed8d8-ab75-459d-af5f-28f9eb731727',
    'asos-c-plat': 'web',
    'asos-c-name': 'asos-web-productpage',
    'asos-c-ver': '1.0.0-70dfa4472a6d-16520',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.asos.com/asos-design/asos-design-herringbone-tailored-trousers-in-grey/prd/205495961',
    'Cookie': 'featuresId=fbb3f6b3-2609-4b80-8c13-05d5670c2166; _abck=23F3CD5E1DC92F2508D0BF7EB665B2DF~-1~YAAQ9XEyuO5ND9yLAQAA2XxgMAq5u2HYin6BGKRnd107nOC7fJWAnDbx7gEJsP5tkHNHZCeSjla7Xnis5z33rjTlO+qNQTJel9hTeQMnOkXVIKNzqmE4V17BpHSHzDX2fDcN7EgApemM+EcIyPXuhE0dkhTlihMNmFOtiaP9tVjG2D2qlVi6gCQ6eujAvQMlKuDW/n2010P5r9IBTm2IlOJm2Bl0zyXGS3oUCTsjFsKsvgZqIgEM6+9CQ7qPhxTDhBYQaKy9MMOzDeVLe4jRbVM6DDcsSwDtOil0qnn56v2q'
}
    
response = requests.get(url, params=params, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request successful!")
    print("Response:")
    formatted_json = json.dumps(response.json(), indent=2)
    print(formatted_json)
else:
    print(f"Request failed with status code {response.status_code}")
    print("Response:")
    print(response.text)