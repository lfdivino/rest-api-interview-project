# -*- coding: utf-8 -*-

from .db_event import DBEvent


class DBOdds(DBEvent):
    """Class responsible to control all the actions about the Odds of the
    ```Events```"""
    def update_odds(self, event_index_id, modified_event_odds):
        """Return True or False after trying to update the Odds of a
        specified event by it 'id' """
        return self.db_collection.update_one(
            {'id': event_index_id},
            {'$set': modified_event_odds}
        )
