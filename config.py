from datetime import datetime
from pytz import timezone

eastern_tz = timezone('EST')

CONF = {
    # 'launch_time': datetime(2020, 11, 25, 21, 0, 0, tzinfo=eastern_tz),
    'launch_time': datetime(2020, 11, 24, 14, 7, 0, tzinfo=eastern_tz),
    'chrome_profile_dir': '/Users/satyanedunuri/Library/Application\ Support/Google/Chrome/Default',
    'cvv': '',
    'item_urls': [
        # 'https://www.walmart.com/ip/PlayStation-5-Console/363472942',
        'https://www.walmart.com/ip/Marvel-s-Spider-Man-Miles-Morales-Ultimate-Launch-Edition-Sony-PlayStation-5/795159051',
    ]
}
