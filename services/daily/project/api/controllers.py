from sports_data_io_sdk.odds import SportsDataOddsClient

client = SportsDataOddsClient("nba")


def daily_live_odds_payload(date):
    return client.live_odds_by_date(date).json()


def daily_pregame_odds_payload(date):
    print('req')
    return client.pregame_odds_by_date(date).json()

