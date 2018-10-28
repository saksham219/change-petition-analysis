
class Target:

    def __init__(self, petition_id, name, description, title, locale, is_primary):
        self.petition_id = petition_id
        self.name = name
        self.description = description
        self.title = title
        self.locale = locale
        self.is_primary = is_primary

    def __repr__(self):
        return '<%s %s %s %s>' % (self.petition_id, self.name, self.title, self.is_primary)


