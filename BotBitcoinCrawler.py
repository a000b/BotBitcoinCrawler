import socket, sqlite3
from sqlite3 import Error


class Peer:
    def __init__(self, source, ip_addr, port):
        self.source = source
        self.ip_addr = ip_addr
        self.port = port
        
class BotBitcoinCrawler:
    def __init__(self):
        self.baza = []
    
    def add_peer(self, source, ip_addr, port):
        p = Peer(source, ip_addr, port)
        self.baza.append(p)
    
    def print_peer(self, index):
        peer = self.baza[index]
        print("{:5} | {:32} | {:16} | {:4}".format(index, peer.source, peer.ip_addr, peer.port))
                                                  
    def print_all(self):
        for index in range(len(self.baza)):
            self.print_peer(index)
    

    def get_node_addresses(self):
        # lista nodów z https://github.com/bitcoin/bitcoin/blob/master/src/chainparams.cpp
        # seed.bitcoin.jonasschnelli.ch nie działa
        dns_seeds = [
            ("seed.bitcoin.sipa.be", 8333),
            ("dnsseed.bluematt.me", 8333),
            ("dnsseed.bitcoin.dashjr.org", 8333),
            ("seed.bitcoinstats.com", 8333),
            ("seed.btc.petertodd.org", 8333),
            ("seed.bitcoin.sprovoost.nl", 8333),
            ("dnsseed.emzy.de", 8333),
            ("seed.bitcoin.jonasschnelli.ch", 8333)
        ]
        
        try:
            for (ip_address, port) in dns_seeds:

                for info in socket.getaddrinfo(ip_address, port,
                                               socket.AF_INET, socket.SOCK_STREAM,
                                               socket.IPPROTO_TCP):
                    self.add_peer(ip_address, info[4][0], info[4][1])
        except:
                print(ip_address, "Ops, jakiś error")

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_entry(conn, sql, v1, v2):
    
    dane = (None, v1, v2, 8333)

    try:
        c = conn.cursor()
        c.execute(sql, dane)
        conn.commit()
    except Error as e:
        print("Err :", e)

def select_entry(conn):

    c = conn.cursor()
    print("SELECT * FROM NODES ORDER BY ID DESC LIMIT 5")
    c.execute("SELECT * FROM NODES ORDER BY ID DESC LIMIT 5")
 
    rows = c.fetchall()
 
    for row in rows:
        print(row)
        
def create_baza():
    database = "nodes_ips.db"

    sql_create_nodes_table = """ CREATE TABLE IF NOT EXISTS nodes (
                                        id INTEGER PRIMARY KEY,
                                        seed VARCHAR(50) NOT NULL,
                                        nodeip VARCHAR(50),
                                        nodeport INTEGER,
                                        ts TIMESTAMP DATETIME DEFAULT CURRENT_TIMESTAMP
                                    ) """
    sql_insert_nodes_table = """ INSERT INTO nodes(id, seed, nodeip, nodeport)
              VALUES(?, ?, ?, ?)""" 

    
    conn = create_connection(database)
    
    if conn is not None:
        create_table(conn, sql_create_nodes_table)
        
        for index in range(len(bot.baza)):
            wiersz_l = bot.baza[index]
            create_entry(conn, sql_insert_nodes_table, wiersz_l.source, wiersz_l.ip_addr)
            
        select_entry(conn)
    else:
        print("Error! cannot create the database connection.")


bot = BotBitcoinCrawler()
bot.get_node_addresses()
create_baza()



##bot.print_all()
