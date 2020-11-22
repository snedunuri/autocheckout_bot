from datetime import datetime
from pytz import timezone

eastern_tz = timezone('EST')

CONF = {
    # 'launch_time': datetime(2020, 11, 25, 21, 0, 0, tzinfo=eastern_tz),
    'launch_time': datetime(2020, 11, 22, 12, 0, 0, tzinfo=eastern_tz),
    'item_urls': [
        # 'https://www.walmart.com/ip/PlayStation-5-Console/363472942',
        # 'https://www.walmart.com/ip/XB1-Xbox-Series-X/443574645'
        'https://www.walmart.com/ip/Marvel-s-Spider-Man-Miles-Morales-Ultimate-Launch-Edition-Sony-PlayStation-5/795159051',
        # 'https://www.walmart.com/ip/X-Rocker-Solo-Led-Floor-Rocker/368830955?athcpid=368830955&athpgid=cart&athcgid=TrendingItems&athznid=ItemCarouselType_Trending-on-walmart-com&athieid=v0&athstid=CS020&athguid=cca784f7-007-175f07a5a9e005&athancid=null&athena=true'
    ]
}
