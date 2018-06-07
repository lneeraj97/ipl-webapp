class iplRouter(object):
    def db_for_read(self, model, **hints):
        "Point all operations on ipl models to 'ipl'"
        if model._meta.app_label == 'ipl':
            return 'ipl'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on ipl models to 'ipl'"
        if model._meta.app_label == 'ipl':
            return 'ipl'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in ipl app"
        if obj1._meta.app_label == 'ipl' and obj2._meta.app_label == 'ipl':
            return True
        # Allow if neither is ipl app
        elif 'ipl' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_syncdb(self, db, model):
        if db == 'ipl' or model._meta.app_label == "ipl":
            return False  # we're not using syncdb on our legacy database
        else:  # but all other models/databases are fine
            return True
