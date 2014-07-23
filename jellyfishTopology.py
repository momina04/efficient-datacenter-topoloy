"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ,n=5,p=5):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

	hosts = []
	switches = []
	ports = []
	isLink = [[0 for x in range(n)] for x in range(n)]
	for i in range(n):
		ports.append(p)
	
        # Add hosts and switches
	for h in range(n):
	        hosts.append(self.addHost( 'h%s'%(h+1))
		switches.append(self.addSwitch('s%s'%(h+1))
		self.addLink(host[h],switch[h])
		ports[h]-=1

        #rightHost = self.addHost( 'h2' )
        #leftSwitch = self.addSwitch( 's3' )
        #rightSwitch = self.addSwitch( 's4' )

        # Add links between switches randomly
	total_ports = p*n
	for ports in range(total_ports):
		s1 = randrange(0,n)
		s2 = randrange(0,n)        
		if (s1 != s2) and (isLink[s1][s2] ==0):
			self.addLink(switches[s1],switches[s2])
			isLink[s1][s2] = 1
			ports[s1]-=1
			ports[s2]-=1
		
	
		
	
	#self.addLink( leftHost, leftSwitch )
        #self.addLink( leftSwitch, rightSwitch )
        #self.addLink( rightSwitch, rightHost )


topos = { 'mytopo': ( lambda: MyTopo() ) }
