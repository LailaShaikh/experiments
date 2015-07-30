from mongoengine import Document, connect, StringField, BooleanField

connect('nava')

class TestMe(Document):
    name = StringField(required=True)
    address = StringField(required=True)
    is_active = BooleanField(default=False)



if __name__ == '__main__':

    # 1. Initial document creation in mongo collections with only two fields(name and address)
    #t = TestMe(name="Navaneethan", address="Bangalore")
    #t.save()

    # running this code upto these lines
    obj = TestMe.objects(name='Navaneethan').first()
    obj.is_active = True
    obj.save()
    print "updated successfully"
