from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():

    "Create an empty network and add nodes to it."

    net = Mininet(controller=RemoteController )

    info( '*** Adding controller\n' )
    net.addController( 'c0', controller=RemoteController,ip="192.168.57.3",port=6633 )

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='11.0.0.1' )
    h2 = net.addHost( 'h2', ip='11.0.0.2' )
    h3 = net.addHost( 'h3', ip='12.0.0.3' )
    h4 = net.addHost( 'h3', ip='12.0.0.4' )


    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1', ip='11.0.0.0' )
    s2 = net.addSwitch( 's2', ip='12.0.0.0' )

    info( '*** Creating links\n' )
    net.addLink( h1, s1 )
    net.addLink( h2, s1 )
    net.addLink( s1, s2 )
    net.addLink( h3, s2 )
    net.addLink( h4, s2 )

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()