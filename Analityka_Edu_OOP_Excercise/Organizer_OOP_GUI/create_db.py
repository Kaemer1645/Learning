import shelve
import glob

class Data_base:
    def create_db(self, db_list):
        i=0
        with (shelve.open('OrganizerDB')) as db:
            for object in db_list:
                i+=1
                db[object.type+str(i)] = object
    def disp_db(self):
        with (shelve.open('OrganizerDB')) as db:
            for key in sorted(db):
                print(key, '\t=>', db[key])

