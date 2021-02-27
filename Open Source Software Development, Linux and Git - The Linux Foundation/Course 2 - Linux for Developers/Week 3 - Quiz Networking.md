## Week 3 - Networking

**1.** Which networking configuration interface is newer and has extended capabilities?

**ip**


**2.** Using Predictable Network Interface Device Names (PNIDN) has come into use because:

**On modern systems, the order in which network hardware is found is less predictable**

**Many computers are no longer in one location; for example, laptops are on the move, and available interfaces are subject to change**

**Hardware such as USB devices can be added and removed at runtime**


**3.** Which command(s) will bring the network interface eth0 up and assign an address to it?

**sudo ifconfig eth0 up 192.168.1.100**

**sudo ip addr add 192.168.1.100 dev eth0**


**4.** You can see statistics for the eth0 interface by (select all answers that apply):

**doing sudo ip -s link show eth0**

**doing sudo ifconfig eth0**

**looking at /sys/class/net/eth0/statistics**


**5.** What does MTU stand for?

**Maximum Transfer Unit (usually 1500 bytes by default) for Ethernet packets**
