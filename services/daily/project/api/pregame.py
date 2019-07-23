from flask import Blueprint
from flask_restful import Api, Resource

from project import cache
from project.api.controllers import daily_pregame_odds_payload

import datetime

pregame_blueprint = Blueprint("pregame", __name__)
api = Api(pregame_blueprint)


class DailyPregameOdds(Resource):

    @cache.memoize(600)
    def get(self, date):
        """Gets all games for a date"""
        if not date:
            return {}, 400
        return daily_pregame_odds_payload(datetime.datetime.strptime(date, "%Y%m%d").strftime("%Y-%b-%d"))


api.add_resource(DailyPregameOdds, "/daily/odds/pregame/<date>")
