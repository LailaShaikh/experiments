class MyRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'blog':
            return 'read_db'
        return None

    def db_for_write(self, model, **hints):
        print model._meta.app_label
        if model._meta.app_label == 'blog':
            return 'write_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'blog' or \
           obj2._meta.app_label == 'blog':
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == 'write_db':
            return model._meta.app_label == 'blog'
        elif model._meta.app_label == 'blog':
            return False
        return None
