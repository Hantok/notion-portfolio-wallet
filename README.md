# Notion Portfolio Wallet
Free portfolio template to keep your assets in order

* calculate your portfolio items in percent
* loss/gain calculations
* support of all crypto assets available through API

# Requirements

    pip3 install requests
    
API in use

https://www.coinlore.com/cryptocurrency-data-api


Use Cron or any scheduler to run the script in the frequency you want 

    # min | hour | day | month | weekday |  command 0 * * * * /usr/bin/python3 /home/.../portfolio.py

Cron job to run it every hour

    crontab -e
    
Add to the end of file (leave empty line in the end)

    0 * * * * python3 <path_to>/portfolio.py
    
Verify

    crontab -l
    
# Notion Template

* Duplicate the notion template

    https://glory-to-ukraine.notion.site/e137e4fe47934a8eb70e1da5cf4d5dea?v=b536d8e9c3e544618f811092e7ca047c

* Copy your own DB id `long_hash_1`
    
    `https://www.notion.so/<long_hash_1>?v=<long_hash_2>`

* Set variable `wallet_db_id` in `portfolio.py` with your own `long_hash_1`

* Set up new integration and set variable `secret` in `portfolio.py` with your own secret

    https://www.notion.so/help/create-integrations-with-the-notion-api#create-an-internal-integration

* In your own wallet add access to your newly created integration: `Wallet note Settigs` -> `Add connections` -> `<Name_of_your_connection>` 

Script and tamplate based on [this](https://www.notion.so/Portfolio-Template-26e74df51b3147e1a6db4609abd6e0b8).

 # Donate

    BTC: bc1quxyslea2rw7ys40qc5ymnteeu74xn9kmgqqmyv
    ETH/L2: 0x890290037b86c6b21480311686eE24A343C884E3
    TRON/TRC-20: TN2P5TwNFnRGTc9aDQ3ftC8L5nujpEc71Y