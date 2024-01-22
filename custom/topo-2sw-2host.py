"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        leftHost1 = self.addHost( 'h1',ip='10.1.66.1/24' )
        leftHost2 = self.addHost( 'h2',ip='10.1.66.2/24' )
        leftSwitch1 = self.addSwitch( 's1' )
        leftHost6 = self.addHost( 'h2',ip='10.1.66.6/24' )
        leftSwitch3 = self.addSwitch( 's3' )
        rightHost4 = self.addHost( 'h4',ip='10.1.66.4/24' )
        rightSwitch2 = self.addSwitch( 's2' )
        rightHost5 = self.addHost( 'h4',ip='10.1.66.5/24' )
        rightHost3 = self.addHost( 'h3',ip='10.1.66.3/24' )
        rightSwitch4 = self.addSwitch( 's4' )

        # Add links
        self.addLink( leftHost1, leftSwitch1 )
        self.addLink( leftHost2, leftSwitch1 )
        self.addLink( leftHost6, leftSwitch3 )
        self.addLink( rightHost4, rightSwitch2 )
        self.addLink( rightHost5, rightSwitch4 )
        self.addLink( rightHost3, rightSwitch4 )

       self.addLink(  leftHost1, leftSwitch1, clsTCLink, bw=1, delay='24ms'  )
       self.addLink(  leftHost2, leftSwitch1, clsTCLink, bw=1, delay='24ms'  )
       self.addLink(  leftSwitch1, rightSwitch2, clsTCLink, bw=10, delay='24ms'  )
       self.addLink(  leftSwitch1, leftSwitch3, clsTCLink, bw=10, delay='24ms'  )
       self.addLink(  rightHost4, rightSwitch2, clsTCLink, bw=1, delay='24ms'  )
       self.addLink(  leftHost6, leftSwitch3, clsTCLink, bw=1, delay='24ms'  )
       self.addLink(  leftSwitch3, rightSwitch4, clsTCLink, bw=10, delay='24ms'  )
       self.addLink(  rightHost5, rightSwitch4, clsTCLink, bw=1, delay='24ms'  )
       self.addLink(  rightHost3, rightSwitch4, clsTCLink, bw=1, delay='24ms'  )
       self.addLink(  rightSwitch2, rightSwitch4, clsTCLink, bw=10, delay='24ms'  )



       


topos = { 'mytopo': ( lambda: MyTopo() ) }
