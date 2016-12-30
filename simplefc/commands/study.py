"""Present entries individually, either by term (-t), 
definition (-d), or both (-b). Include all (-a), many (exclude 
easy ones; -m), or few (only the hard ones; -f)."""

from .base import Base
import sqlite3
import os
import sys

class _Getch:
    """Gets a single character from standard input. Does not 
echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

class Study(Base):

    def flash(self):
        print("\nPress 'a' to see correct answer.\n")
        ch1 = _Getch()
        ch = ch1()
        if ch == 'a':
            answer = self.cur.execute("select " +self.tdb[1]+
            " from " +self.name+ " where ID is " +str(self.i)+ ";")
            [print(j[0]) for j in answer]
            print("\n'c' if you got it, 'i' if not, 'e' to exit\n")
            ch2 = _Getch()
            ch = ch2()
            if ch == 'c':
                self.cur.execute("update " +self.name+ " set correct"
                "=correct+1 where ID is " +str(self.i)+ ";")
            elif ch == 'i':
                self.cur.execute("update " +self.name+ " set "
                "incorrect=incorrect+1 where ID is " +str(self.i)+ 
                ";")
            elif ch == 'e':
                self.conn.commit()
                self.conn.close()
                sys.exit('Progress saved.')
            else:
                print('invalid')
                self.flash()
        else:
            print('invalid')
            self.flash()

    def mode_parser(self):
        if self.options.get('-s') or self.default == True:
            if self.options.get('-b'):
                
            else:
                for i in self.pool:
                    term = self.cur.execute("select " +self.tdb[0]+
                    " from " +self.name+ " where ID is " +str(i)+
                    " and archived='N';")
                    [print(j[0]) for j in term]
                    self.i = i
                    self.flash()

    def allfc(self):
        self.pool = self.cur.execute("select ID from " +self.name+
                    " where archived='N';")
        self.termdef()

    def manyfc(self):
        self.pool = self.cur.execute("select ID from " +self.name+
                    " where archived='N' and correct/incorrect"
                    "<=2;")
        self.termdef()

    def fewfc(self):
        self.pool = self.cur.execute("select ID from " +self.name+
                    " where archived='N' and correct/incorrect"
                    "<=0.75;")
        self.termdef()

    def termdef(self):
        self.pool = [i[0] for i in self.pool]
        if self.options.get('-t'):
            self.tdb = ['term','definition']
        elif self.options.get('-d'):
            self.tdb = ['definition','term']
        else:
            pass

        self.mode_parser()
        
    def run(self):
        path = os.path.dirname(os.path.realpath(__file__))
        self.conn = sqlite3.connect(path + '/../simplefc.db')
        self.cur = self.conn.cursor()
        self.name = str(self.options.get('<setname>'))
        
        flags = ['-t','-d','-b','-a','-m','-f','-s','-r']
        TF = [self.options.get(i) for i in flags]
        used = [i[0] for i in list(zip(flags, TF)) if i[1]]
        key = ''.join(sorted(''.join(used).replace('-','')))
        
        if key in ['ast','art','abs','abr','ads','adr']:
            self.allfc()
        elif key in ['mst','mrt','bms','bmr','dms','dmr']:
            self.manyfc()
        elif key in ['fst','ftr','bfs','bfr','dfs','dfr']:
            self.fewfc()
        elif key == '':
            self.tdb = ['term','definition']
            self.default = True
            self.allfc()
        else:
            sys.exit("Need one flag each from -tdb -amf and -sr,\n"
                     "or no flags for the default (-tas).\n"
                     "Enter 'simplefc -h' for details.")

        #flagdict = {'ast':self.allfc(), 'art':self.allfc(),
        #            'abs':self.allfc(), 'abr':sel,'ads','adr','mst','mrt','bms','bmr','dms','dmr','fst','frt','bfs','bfr','dfs','dfr'}
        #self.ast()
        
            

        #ts = [self.options.get(i) for i in ['-t','-s']]
        #if all(ts):
        #    pool = 
        #    cur.execute("

        self.conn.commit()
        self.conn.close()
