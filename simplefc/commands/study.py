"""create a new flashcard set"""

from .base import Base
import sqlite3
import os

class Create_set(Base):

    def run(self):
        path = os.path.dirname(os.path.realpath(__file__))
        #print(path + '/../simplefc.db')
        conn = sqlite3.connect(path + '/../simplefc.db')
        cur = conn.cursor()
        name = str(self.options.get('<setname>'))
        cur.execute("create table if not exists " + name +
                    """ (ID integer primary 
                    key autoincrement, term text, definition text, 
                    times_correct integer default 0, times_incorrect 
                    integer default 0, in_play integer default 1);""")
        conn.commit()
        conn.close()
