#!/usr/bin/python

"""
This example shows how to work with both wireless and wired medium
"""

from mininet.optical import LINCNet, LINCSwitch, LINCLink

from mininet.net import Mininet
from mininet.node import  Controller, OVSKernelSwitch, RemoteController, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

def topology():
    "Create a network."
    onos = lambda n: RemoteController(n, ip="10.0.2.15", port=6633, inNamespace=False)


    #net = Mininet( controller=Controller, link=TCLink, switch=OVSKernelSwitch )
    #net = LINCNet(controller=Controller, autoStaticArp=True, listenPort=6634)
    net = LINCNet(controller=onos, autoStaticArp=True, listenPort=6634)
    c1 = net.addController('c1')

    print "*** Creating nodes"
    ap1 = net.addAccessPoint( 'ap1', ssid="ssid_ap1", mode="g", channel="5" )
    ap2 = net.addAccessPoint('ap2', ssid="ssid_ap2", mode="g", channel="5")
    sta1 = net.addStation( 'sta1', ip='192.168.0.1/24' )
    sta2 = net.addStation( 'sta2', ip='192.168.0.2/24' )
    h3 = net.addHost( 'h3', ip='192.168.0.3/24' )
    h4 = net.addHost( 'h4', ip='192.168.0.4/24' )
    #c0 = net.addController('c0', controller=Controller, ip='127.0.0.1' )

    # Add optical switches
    r1 = net.addSwitch('r1', dpid='00:00:00:00:00:00:00:11', cls=LINCSwitch)
    r2 = net.addSwitch('r2', dpid='00:00:00:00:00:00:00:12', cls=LINCSwitch)
    r3 = net.addSwitch('r3', dpid='00:00:00:00:00:00:00:13', cls=LINCSwitch)
    r4 = net.addSwitch('r4', dpid='00:00:00:00:00:00:00:14', cls=LINCSwitch)
    r5 = net.addSwitch('r5', dpid='00:00:00:00:00:00:00:15', cls=LINCSwitch)
    r6 = net.addSwitch('r6', dpid='00:00:00:00:00:00:00:16', cls=LINCSwitch)
    r7 = net.addSwitch('r7', dpid='00:00:00:00:00:00:00:17', cls=LINCSwitch)
    r8 = net.addSwitch('r8', dpid='00:00:00:00:00:00:00:18', cls=LINCSwitch)

    print "*** Configuring wifi nodes"
    net.configureWifiNodes()

    print "*** Adding Link"
    net.addLink(sta1, ap1, bw=10, loss=20)
    net.addLink(sta2, ap2)
    net.addLink(h3, ap1)
    net.addLink(h4, ap2)

    # Connect access points to optical switches
    print "*** Connecting AP to ROADM"
    net.addLink(ap1, r1, 2, 1, cls=LINCLink)
    net.addLink(ap1, r1, 3, 2, cls=LINCLink)
    net.addLink(ap2, r2, 2, 1, cls=LINCLink)
    net.addLink(ap2, r2, 3, 2, cls=LINCLink)


    # Connect optical switches to each other
    print "*** Connecting ROADMs"
    net.addLink(r1, r3, 3, 1, cls=LINCLink)
    net.addLink(r1, r5, 4, 1, cls=LINCLink)
    net.addLink(r1, r6, 5, 1, cls=LINCLink)
    net.addLink(r1, r7, 6, 1, cls=LINCLink)
    net.addLink(r2, r4, 3, 2, cls=LINCLink)
    net.addLink(r2, r5, 4, 2, cls=LINCLink)
    net.addLink(r2, r6, 5, 2, cls=LINCLink)
    net.addLink(r2, r8, 6, 2, cls=LINCLink)
    net.addLink(r3, r4, 2, 1, cls=LINCLink)
    net.addLink(r7, r8, 2, 1, cls=LINCLink)

    print "*** Starting network"
    net.build()
    net.start()
    #c0.start()
    #ap1.start( [c0] )

    print "*** Running CLI"
    CLI( net )

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
