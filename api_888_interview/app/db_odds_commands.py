# -*- coding: utf-8 -*-

from api_888_interview.app.db_event_commands import EventCommandsDB


class OddsCommandDB(EventCommandsDB):
    def update_odds(self, event_index_id, modified_event_odds):
        return self.db.db_collection.update_one(
            {'id': event_index_id},
            {'$set': modified_event_odds}
        )
