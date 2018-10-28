

class Petition:

    def __init__(self, petition_id, ask, title, city, country_code,
                 lat, lng, created_at, locality, creator, updates, signatures, status, victory, victory_date):
        self.petition_id = petition_id
        self.ask = ask
        self.title = title
        self.city = city
        self.country_code = country_code
        self.lat = lat
        self.lng = lng
        self.created_at = created_at
        self.locality = locality
        self.creator = creator
        self.updates = updates
        self.signatures = signatures
        self.status = status
        self.victory = victory
        self.victory_date = victory_date

    def __repr__(self):
        return '<%s %s %s %s %s %s %s %s>' % (self.petition_id, self.ask, self.title,self.city,self.country_code,
                                              self.creator,self.signatures, self.victory)

