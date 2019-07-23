from flask import Blueprint
from flask_restful import Api, Resource

from project import cache
from project.api.controllers import daily_live_odds_payload

import datetime

live_blueprint = Blueprint("live", __name__)
api = Api(live_blueprint)


class DailyLiveOdds(Resource):

    @cache.memoize(600)
    def get(self, date):
        """Gets all games for a date"""
        if not date:
            return {}, 400
        return daily_live_odds_payload(datetime.datetime.strptime(date, "%Y%m%d").strftime("%Y-%b-%d"))


api.add_resource(DailyLiveOdds, "/daily/odds/live/<date>")
