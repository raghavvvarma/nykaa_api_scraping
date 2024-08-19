import http.client
import gzip
import brotli
import zlib
import json
import csv
import datetime
from datetime import date, timedelta
import os




conn = http.client.HTTPSConnection("www.nykaa.com")

payload = ""
products = []
count = 0  # Initialize count to 0 before starting the loop

# Define CSV file headers
csv_headers = ["product_name", "Tag", "Price", "Final Price", "Discount", "Rating", "Rating Count", "Product URL"]






# now = datetime.now()
# now = now + timedelta(minutes = 330)
# current_date = now.strftime("%d_%m_%Y")
# current_date_time = now.strftime("%d_%m_%Y_%H")

# print(current_date_time)

today = date.today().strftime("%Y_%m_%d")  # Format: YYYYMMDD
                    #    C:\Users\redseer\Desktop\brandverse\shampoo_data\Amazon
data_directory_name = "C://Users//redseer//Desktop//brandverse//shampoo_data//Nykaa//data_nykaa_l1_" + str(today)



# Check if the directory exists
if not os.path.exists(data_directory_name):
    # Create the directory
    os.mkdir(data_directory_name)
else:
    print("Data Directory already exists!")






# Create the file name with the date
file_name = f"{data_directory_name}//nykaa_l1_data_{today}.csv"


with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)

    for i in range(1, 100):
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
            'Accept': "application/json, text/plain, */*",
            'Accept-Language': "en-US,en;q=0.5",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Referer': "https://www.nykaa.com/hair-care/hair/shampoo/c/316?page_no=2&sort=popularity&search_redirection=True&eq=desktop",
            'X-NewRelic-ID': "undefined",
            'newrelic': "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjEyMjUxNTkiLCJhcCI6IjEwMDE0NzQ3MTciLCJpZCI6ImE1MjBlMWNiNjk1YzcyNjciLCJ0ciI6ImZkMDZhODMxOGI3MTVmNTA5MGZhY2QwODFmZTc5ZjAwIiwidGkiOjE3MTgzNjA3MTcxODd9fQ==",
            'traceparent': "00-fd06a8318b715f5090facd081fe79f00-a520e1cb695c7267-01",
            'tracestate': "1225159@nr=0-1-1225159-1001474717-a520e1cb695c7267----1718360717187",
            'x-csrf-token': "BBgj7wEjusBsdPhf",
            'Sec-Fetch-Dest': "empty",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Site': "same-origin",
            'Connection': "keep-alive",
            'Cookie': "bcookie=cb2f2684-919f-47a2-aa46-cce5f113c0e3; EXP_NEW_SIGN_UP=DEFAULT; EXP_CART_LOGIN_SEGMENT=A; EXP_ADP_RV_REORDER=A; EXP_ADP_RV_SEGMENT=A; EXP_AB_AUTOFILL=B; EXP_ADP_RV_VIEW_SIMILAR_HLP=A; EXP_ADP_RV_VIEW_SIMILAR=D; EXP_ADP_RV_PLP_CONFIGURABLE_NO_RESULTS=A; EXP_ADP_RV_PRODUCT_V3=CONTROL; EXP_AB_HLP_CARD_REVAMP=B; EXP_AB_WISHLIST=A; EXP_AB_PRICE_REVEAL_NEW=A; EXP_PLP_INLINE_FILTER=A; EXP_EDD_DELIVERY_WIDGET=A; EXP_ADP_RV_MULTI_COUPONS=A; EXP_ADP_RV_SEARCH_BAR_NEW=A; EXP_AB_AUTH_PAGE=A; EXP_AB_AUTH_DWEB=CONTROL; EXP_INCORRECT_SLUG_REDIRECT=A; EXP_PLP_PINKBOX_CTA=CONTROL; EXP_SLP_RELATED_SEARCHES=A; EXP_QUERY_PARAM_EXP=CONTROL; EXP_AB_HLP_CTA=A; EXP_AB_PDP_IMAGE=CONTROL; EXP_AB_CALLOUT_NUDGE=A; EXP_AB_PRICE_REVAMP=A; EXP_AB_TRUECALLER=DEFAULT; EXP_AB_GOOGLE_ONE_TAP=DEFAULT; EXP_ORGANIC_GUIDES=A; EXP_AB_NEW_PLP=A; EXP_PDP_RATING_REVAMP=A; EXP_AB_BREADCRUMB_POSITION=A; EXP_PRODUCT_CARD_CTA=A; EXP_AB_MULTI_MRP=A; EXP_AB_SIZE_MINI_PRODUCT=A; EXP_AB_BRAND_SEP_PDP=A; EXP_AB_TOP_NAV_CONFIG=CONTROL; EXP_QUERY_PARAM_EXP_DWEB=CONTROL; EXP_AB_BEAUTY_PORTFOLIO=A; EXP_AB_HAMBURGUR_BANNER=A; EXP_AB_HP_SEARCH_ANIMATION=CONTROL; EXP_AB_PDP_HAMBURGER=CONTROL; EXP_AB_HLP_OFFERS=A; EXP_AB_RECO_PRODUCT_V4=CONTROL; EXP_AB_WEB_AUTOREAD_OTP=A; EXP_AD_BRV=variant1; EXP_PDP_RELEVANT_CATEGORY=CONTROL; EXP_AB_PRODUCT_VARIENTS_ORDER=DEFAULT; EXP_AB_AUTO_FILL_OTP=A; EXP_AB_REMOVE_LOGIN_BOTTOMSHEET=CONTROL; EXP_AB_PRODUCT_HIGHLIGHTS_CAROUSEL=A; EXP_AB_HORIZONTAL_WIDGET_TYPE=A; EXP_UPDATED_AT=1718251802638; EXP_SSR_CACHE=a67d042e4c89a70759a99b89ea55d3c4; SITE_VISIT_COUNT=25; run=9; EXP_REVIEW_COLLECTION=1; D_LST=1; D_PDP=1; PHPSESSID=Xhe0sBuqWgFwRSS1718260268607; _gcl_au=1.1.1255162781.1718260271; _ga_LKNEBVRZRG=GS1.1.1718358768.3.1.1718360712.2.0.0; _ga=GA1.2.1488179109.1718260271; WZRK_G=4a0d2ae4a898409594d84b397dd6c35e; _ga_JQ1CQHSXRX=GS1.2.1718358769.2.1.1718360711.2.0.0; __cf_bm=nZRp85Okz.hikKlbIxriMCx42jRtzcQWjUeOI2bHSVU-1718360654-1.0.1.1-K7B0f.NdV2FFxYgnOfrMuHJv_sQFiFUIOg5vTPFVQoK_YTHxJBC_zCzrV.Xb.8WwJyz5yYqixjTRqOJpbTQFMw; head_data_react={'id':'','nykaa_pro':false,'group_id':''}; pro=false; ck_q=sampoo; ck_root=search; ck_searchType=Manual; ck_sourcepage=home; WZRK_S_656-WZ5-7K5Z={'p':33,'s':1718358770,'t':1718360711}; _gid=GA1.2.1698388464.1718358769; ck_search_redirection=True; cf_clearance=syyo3biVJOczrcVNSkzlNteg8PB7aJWDvjHRxOhoG44-1718359148-1.0.1.1-iw4JxdtU6NzptE.dVoi5UPSP02YUNAJFhvcVUhcvWf7nAcFbfFLzT0NpUd7kisIXWvqXf9xql2hHMW4VJMHhgA; _cfuvid=zpwPL5312fNfDSIIPvi.5kk_1RboSG.aygBjOLNdIpU-1718360387372-0.0.1.1-604800000; ck_page_no=1; ck_sort=popularity; ck_eq=desktop",
            'Priority': "u=1",
            'TE': "trailers"
        }

        conn.request("GET", f"/app-api/index.php/products/list?category_id=316&client=react&filter_format=v2&page_no={i}&platform=website&sort=popularity", payload, headers)

        res = conn.getresponse()
        compressed_data = res.read()

        # Check the response encoding
        encoding = res.getheader('Content-Encoding')

        if encoding == 'gzip':
            decompressed_data = gzip.decompress(compressed_data)
        elif encoding == 'br':
            decompressed_data = brotli.decompress(compressed_data)
        elif encoding == 'deflate':
            decompressed_data = zlib.decompress(compressed_data)
        else:
            decompressed_data = compressed_data

        # Try to decode with utf-8, if it fails use latin1
        try:
            decoded_data = decompressed_data.decode('utf-8')
        except UnicodeDecodeError:
            decoded_data = decompressed_data.decode('latin1')

        # Parse JSON data
        data = json.loads(decoded_data)

        # Extract names of all products from the current page
        try:
            page_products = data["response"]["products"]
            for product in page_products:
                tags = ", ".join(product["curation_tags"]) if product["curation_tags"] else ""
                product_details = {
                    "product_name": product["name"],
                    "Tag" : tags,
                    "Price": product["price"],
                    "Final Price": product["final_price"],
                    "Discount": product["discount"],
                    "Rating": product["rating"],
                    "Rating Count": product["rating_count"],
                    "Product URL": product["product_url"]
                    
                }

                products.append(product_details)
                count += 1
                print(f"{count}: {product_details['Name']}")

                # Write to CSV file
                writer.writerow([
                    product_details["product_name"],
                    product_details["Tag"],
                    product_details["Price"],
                    product_details["Final Price"],
                    product_details["Discount"],
                    product_details["Rating"],
                    product_details["Rating Count"],
                    product_details["Product URL"]
                ])

        except KeyError:
            print(f"No products found on page {i}")

print(f"Total products: {count}")
