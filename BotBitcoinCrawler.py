import socket
import time

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
        # lista nodów z https://en.bitcoin.it/wiki/Satoshi_Client_Node_Discovery#DNS_Addresses
        # seed.bitcoin.jonasschnelli.ch nie działa
        dns_seeds = [
            ("seed.bitcoin.sipa.be", 8333),
            ("dnsseed.bluematt.me", 8333),
            ("dnsseed.bitcoin.dashjr.org", 8333),
            ("seed.bitcoinstats.com", 8333),
            ("seed.btc.petertodd.org", 8333),
            ("bitcoinseed.jonasschnelli.ch", 8333),
        ]
        err = []
        
        try:
            for (ip_address, port) in dns_seeds:

                for info in socket.getaddrinfo(ip_address, port,
                                               socket.AF_INET, socket.SOCK_STREAM,
                                               socket.IPPROTO_TCP):
                    self.add_peer(ip_address, info[4][0], info[4][1])
        except:
                print(ip_address, "Ops, jakiś error")



bot = BotBitcoinCrawler()
bot.get_node_addresses()
bot.print_all()
