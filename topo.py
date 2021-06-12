from mininet.topo import Topo

class s2h2( Topo ):
    # 2 Switches of 2 Hosts

    def build( self ):

        # Add hosts and switches
        h1 = self.addHost( 'h1', ip='11.0.0.1' )
        h2 = self.addHost( 'h2', ip='11.0.0.2' )
        h3 = self.addHost( 'h3', ip='12.0.0.3' )
        h4 = self.addHost( 'h4', ip='12.0.0.4' )
        s1 = self.addSwitch( 's1', ip='11.0.0.' )
        s2 = self.addSwitch( 's2', ip='12.0.0.0' )

        # Add links
        self.addLink( h1, s1,bw=10, delay=150 )
        self.addLink( h2, s1,bw=15, delay=100 )
        self.addLink( s1, s2,bw=10, delay=10 )
        self.addLink( h3, s2,bw=20, delay=75 )
        self.addLink( h4, s2,bw=25, delay=30 )

        


topos = { '2s2h': ( lambda: s2h2() ) }