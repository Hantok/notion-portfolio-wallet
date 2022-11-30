import requests

secret = ""
base_db_url = "https://api.notion.com/v1/databases/"
base_pg_url = "https://api.notion.com/v1/pages/"
base_crypto_url = "https://api.coinlore.net/api/tickers/"
# need to replace stock API
base_stock_url = "https://www.shikhersrivastava.com/stocktradingapi/stock/quote?symbol="

wallet_db_id = ""
data = {}
header = {"Authorization":secret, "Notion-Version":"2021-05-13", "Content-Type": "application/json"}

response = requests.post(base_db_url + wallet_db_id + "/query", headers=header, data=data)
i = 0

total_asset_amount_in_usd = 0
def update_price(coin):
    price = coin['price_usd']
    price_btc = coin['price_btc']
    pcent_1h = coin['percent_change_1h']
    pcent_24h = coin['percent_change_24h']
    pcent_7days = coin['percent_change_7d']
    coin_url = "https://coinmarketcap.com/currencies/" + coin['nameid']

    data_price = '{"properties":   \
                                        {"Price": { "number":' + str(price) + '},\
                                        "price btc": { "number":' + str(price_btc) + '}, \
                                        "% 1H": { "number":' + str(pcent_1h) + '}, \
                                        "% 24H": { "number":' + str(pcent_24h) + '}, \
                                        "% 7days": { "number":' + str(pcent_7days) + '}, \
                                        "URL": { "url":"' + coin_url + '"}}}'

    requests.patch(base_pg_url + page_id, headers=header, data=data_price)
    print(asset_code + " = " + data_price)

for page in response.json()["results"]:
    page_id = page["id"]
    props = page['properties']

    asset_type = props['Type']['select']['name']
    
    asset_code = props['Code']['rich_text'][0]['plain_text']

    asset_amount_in_usd = props['Total']['formula']['number']

    total_asset_amount_in_usd += asset_amount_in_usd

    # TBD: Add Stock support soon
    # if asset_type == "Stock":
        # response = requests.get(base_stock_url + asset_code).json()
        #
        #
        # stock_price = response[asset_code]['latestPrice']
        # pcent_1h = "{:.2f}".format(100*response[asset_code]['changePercent'])
        # pcent_24h = "{:.2f}".format(response[asset_code]['ytdChange'])
        #
        # data_price = '{"properties": {"Price": { "number":' + str(stock_price) + '},\
        #                                 "% 1H": { "number":' + str(pcent_1h) + '}, \
        #                                 "% 24H": { "number":' + str(pcent_24h) + '}, \
        #                                 "URL": { "url": "https://finance.yahoo.com/quote/' + asset_code + '"}}}'
        #
        # send_price = requests.patch(base_pg_url + page_id, headers=header, data=data_price)
        # print(data_price)

    if asset_type == "Crypto":
        request_by_code = requests.get(base_crypto_url).json()['data']
    
        coin = next((item for item in request_by_code if item["symbol"] == asset_code), None)

        if request_by_code != []:
            while coin is None:
                i += 100
                new_request_by_code = requests.get(base_crypto_url + "?start=" + str(i) + "&limit=100").json()['data']
                new_coin = next((item for item in new_request_by_code if item["symbol"] == asset_code), None)
                if new_coin is None:
                    if i > 10000:
                        i = 0
                        print("Can not update " + asset_code + " coin. Perhaps TICKER is incorrect.")
                        break
                    continue

                update_price(new_coin)
                i = 0
                break

            else:
                update_price(coin)
print(" ")
print("Start updating Deposit percantage of each asset")
print(" ")

response = requests.post(base_db_url + wallet_db_id + "/query", headers=header, data=data)
for page in response.json()["results"]:
    page_id = page["id"]
    props = page['properties']
    asset_amount_in_usd = props['Total']['formula']['number']

    asset_percent = round(asset_amount_in_usd/total_asset_amount_in_usd * 100, 2)

    data_price = '{"properties": {"Deposit %": { "number":' + str(asset_percent) + '}}}'

    requests.patch(base_pg_url + page_id, headers=header, data=data_price)

    asset_code = props['Code']['rich_text'][0]['plain_text']
    print(asset_code + " = " + data_price)