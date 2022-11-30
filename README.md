# notion-portfolio-wallet
Free portfolio template to keep your assets in order

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

    TBD
