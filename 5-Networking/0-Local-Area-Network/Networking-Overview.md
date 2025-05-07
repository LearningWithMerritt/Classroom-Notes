# `Networking Overview`


TODO:
scalability
client
server (program/device)
Network Operating Systems NOS
    Active Directory
    Active Directory Domain Services
    Windows Domain (a group of users, servers, other resources that share account and security policies)
Network services are resources that the network makes available to users. Includes applications and teh data provided by these applications. 

Client-Server Applications are data or services requested by one computer from another

Backbone is a central conduit of a network that connects network segments and significant shared devices (routers, switches, servers,etc.)



Network Interface is a network connection made by a node or host on a network


Fully Qualified Domain Name (FQDN) (Layer 7 Application) a host name plus a domain name that uniquely identifies a computer or location on a network.
* `hostname.domain.top-level-domain`

`Domain Name` the last 2 parts of a FQDN. 

`Host Name` is the first part of a FQDN which identifies the individual computer on the network. 

The `Top Level Domain TLD` or `domain suffix` is the last part of the FQDN and is the highest level category used to distinquish domain names

Well Known TLDs
| TLD       | Description                          |
|-----------|--------------------------------------|
| `.arpa`   | Originally for ARPANET; now used for technical infrastructure purposes (e.g., reverse DNS lookups) |
| `.com`    | Commercial businesses and general use |
| `.org`    | Nonprofit organizations               |
| `.net`    | Originally for network infrastructure |
| `.edu`    | Educational institutions (mainly U.S.)|
| `.gov`    | U.S. government entities              |
| `.mil`    | U.S. military                         |
| `.int`    | International organizations           |
| `.info`   | Informational websites (Unrestricted Use)|
| `.biz`    | Business or commercial use            |
| `.io`     | Originally for British Indian Ocean Territory, now popular with tech startups |
| `.co`     | Originally for Colombia, widely used as "company" or "corporate" |
| `.us`     | United States                         |
| `.uk`     | United Kingdom                        |
| `.ca`     | Canada                                |
| `.de`     | Germany                               |
| `.jp`     | Japan                                 |
| `.cn`     | China                                 |
| `.au`     | Australia                             |
| `.fr`     | France                                |
| `.in`     | India                                 |


IANA (Internet Assigned Numbers Authority) manages the IP address allocation and Domain Name System.

ICANN (Internet Corporation for Assigned Name and Numbers) non-profit currently designated by US Gov to maintain and Assign IP addresses. 
* Domain Names must be registerd with ICANN

IEEE(Institute of Electrical and Electronics Engineers)



gateway is a computer router or other device that a host uses to access another network. The Default gateway is the gateway device that nodes on a network turn to first for access. 



multicast transmissions in which one host sends messages to multiple hosts
broadcast messages are read by every node on the network.

A broadcast domain is logically grouped network nodes that can communicate directly via broadcast transmissions. By default, switches and repeating devices, such as hubs, extend broadcast domains. Routers and other Layer 3 devices separate broadcast domains.
* Routersd do not forward broadcast messages. 


The area between two firewalls is called a demilitarized zone or DMZ










<br>

___

<br>

Covered in this file:
1. [`Network Defined`](#network-defined)
1. [`Network Data : Layer 1 Physical`](#network-data--layer-1-physical)
1. [`Network Connections : Layer 1 Physcial`](#network-connections-layer-1-physical)
    1. [`Wired Connections`](#wired-connections)
    1. [`Wireless Connections`](#wireless-connections)
        1. [`Wi-Fi : IEEE 802.11x Standard`](#wi-fi--ieee-80211x-standard)
        1. [`Bluetooth`](#bluetooth)
        1. [`Cellular`](#cellular)
1. [`Bandwidth and Latency`](#bandwidth-and-latency)
1. [`Network Interface Card : Layer 2 Data Link`](#network-interface-card-nic--layer-2-data-link)
1. [`Network Switch : Layer 2 Data Link`](#network-switch--layer-2-data-link)
1. [`Router : Layer 3 Network`](#router--layer-3-network)
1. [`Wireless Access Point WAP : Layer 1 Physical`](#wireless-access-point-wap--layer-1-physical)
1. [`Firewalls : Multi Layer`](#firewalls--multi-layer)
1. [`Modulator-Demodulator MODEM : Layer 1 Physical`](#modulator-demodulator-modem--layer-1-physical)
1. [`Optical Network Terminal ONT: Layer 1 Physical`](#optical-network-terminal-ont-layer-1-physical)
1. [`Satellite Modem : Layer 1 Physical`](#satellite-modem--layer-1-physical)
1. [`Basic LAN Topology`](#basic-lan-topology)
1. [`The Internet : Layer 3 Network`](#the-internet-layer-3-network)
1. [`Ports, Protocols, and Services : Layer 4 Transport`](#ports-protocols-and-services--layer-4-transport)
1. [`The World Wide Web`](#the-world-wide-web)



<br>

___

<br>

# `Network Defined`
A `computer network` is a system of interconnected devices that communicate and share resources with each other. 
* Networks allow devices, such as computers, printers, and smartphones, to exchange data, share files, and access shared resources like the Internet, databases, and applications.

<br>

* A Network `Node` is computer or device on a network that has a unique local address, allowing other devices on the same network to find and communicate with it.
* A Network `Host` is an computer on a network that hosts a resource on the network (applications, services, data, etc.)

<br>

Networks are categorized by thier size, and scope. 

| Network Type                   | Description |
|:------------------------------|:------------|
| `Personal Area Network (PAN)` | Covers a very short range, typically a few meters, and connects personal devices such as smartphones, tablets, and `Bluetooth` peripherals. |
| `Local Area Network (LAN)`    | Covers a limited area, such as a home, school, or office building. <br> Each node can communicate directly with other nodes. |
| `Campus Area Network (CAN)`   | Connects multiple LANs within a campus, such as a university or business complex. |
| `Metropolitan Area Network (MAN)` | Connects networks within a city or metropolitan area. |
| `Wide Area Network (WAN)`     | Spans larger geographic areas, often connecting multiple LANs over cities, countries, or continents. |
| `Internet`                    | Global system of interconnected networks that allows devices worldwide to communicate and exchange information. |


<br>

There are two basic network reference models: 
* `OSI (Open Systems Interconnection)` model 
* `TCP/IP (Transmission Control Protocol/Internet Protocol)` model. 

<br>

Both models serve as a framework to understand and design network protocols and communication processes but differs in structure and focus.

<br>

For More on these Networking Reference Models see [Networking-Reference-Models.md](Networking-Reference-Models.md)


<br>

[Back To Top](#networking-overview)

___

<br>

# `Network Data : Layer 1 Physical`
`Network Data` are the bits and bytes of information that are transferred between devices on a network. 
* Data is measured in bits or bytes.

<br>

| Unit  | Symbol | Power of 10 | Value in bits           |
|-------|--------|-------------|--------------------------|
| Kilo  | Kb     | 10³          | 1,000 bits              |
| Mega  | Mb     | 10⁶         | 1,000,000 bits          |
| Giga  | Gb     | 10⁹         | 1,000,000,000 bits      |
| Tera  | Tb     | 10¹²         | 1,000,000,000,000 bits  |

<br>

| Unit  | Symbol | Power of 10 | Value in Bytes           |
|-------|--------|-------------|--------------------------|
| Kilo  | KB     | 10³          | 1,000 bytes              |
| Mega  | MB     | 10⁶         | 1,000,000 bytes          |
| Giga  | GB     | 10⁹         | 1,000,000,000 bytes      |
| Tera  | TB     | 10¹²         | 1,000,000,000,000 bytes  |

<br>

Data traveling throughout networks is `encapsulated` into different `Protocol Data Units (PDUs)` at each layer of the `OSI model`, with each layer adding its own header or footer information to facilitate the data's transmission, routing, and delivery.

<br>


| Layer | PDU (Protocol Data Unit) | Data Representation  | Function  |
|:-:|-|-|-|
| Application Layer | `Data` or `Payload` | Data| User interface and application services|
| Transport Layer | `Segment (TCP)`/ `Datagram (UDP)` | Segments / Datagrams | Manages end-to-end communication and error-checking |
| Network Layer | `Packet` | Packets | Routes data across different networks|
| Data Link Layer | `Frame`| Frames| Manages node-to-node data transfer on a network segment |
| Physical Layer| `Bits` | Bits| Converts data to signals for physical transmission|


<br>

[Back To Top](#networking-overview)

___

<br>


# `Network Connections: Layer 1 Physical`

`Network Connectors` are  used to connect devices together in a network, and transmit data between those devices.

<br>

There are two types of Network Connections:
* `Wired Connections`
* `Wireless Connections`

<br>


`At Layer 1 Physical`
* Data is transmitted in `bits`
* Data is transmitted as `electrical, optical, or radio signals`


<br>

___

<br>

# `Wired Connections`
| Connector Type | Description| Use Case | Max Range| Max Speed |
|-|-|-|-|-|
| `Ethernet` | Standard copper wire connection using twisted-pair cables (e.g., CAT5, CAT6). | LANs and wired networks| ~100 meters| Up to 10 Gbps |
| `Coaxial`| Cable with a copper core, shielded for signal protection.| Cable internet, TV connections | Up to 500 meters | Up to 1 Gbps|
| `Fiber Optic`| Uses light to transmit data through thin glass or plastic fibers, resistant to interference. | High-speed internet, long-distance WANs| Up to 40 km+ | Up to 100 Gbps|


<br>

___

<br>


# `Wireless Connections`

| Connector Type | Description | Use Case | Max Range | Max Speed |
|----------------|-------------|----------|-----------|-----------|
| `Wi-Fi`        | Wireless standard using radio waves to connect devices to a local network. | Wireless LANs, mobile devices | Up to 300 meters | Up to 9.6 Gbps (Wi-Fi 6) |
| `Bluetooth`    | Short-range wireless connection for peripheral devices, using low power and 2.400 to 2.485 GHz radio frequency. | Personal devices (headsets, keyboards) | Up to 100 meters | Up to 3 Mbps (Bluetooth 4.2) |
| `Cellular`     | Mobile wireless network using cellular towers, supporting technologies like 4G and 5G for data and voice communication. | Smartphones, mobile data | Up to several kilometers (depending on tower coverage) | Up to 10 Gbps (5G) |
| `Satellite`    | Wireless communication via satellites orbiting the Earth for internet access in remote or rural areas. | Remote internet access, rural areas | Global coverage | Up to 100 Mbps (Low Earth Orbit satellites like SpaceX Starlink) |


<br>

___

<br>



# `Wi-Fi : IEEE 802.11x Standard`
`Wi-Fi` is the common name given to the IEEE 802.11x standards of wireless communcation.
* "Wi-Fi" was a term created by the Wi-Fi Alliance as a marketing phrase to replace the more technical term "IEEE 802.11x".
* "Wi-Fi" is a play on the words "wireless" and "fidelity".
* Most wireless networks use `2.4 GHz` and `5 GHz` radio frequencies.

**`Wi-Fi is NOT the Internet`**
**`Wi-Fi is NOT Wireless Fidelity`**

<br>

The `IEEE (Institute of Electrical and Electronics Engineers)` is a professional association dedicated to advancing technology and innovation across various fields, including electrical engineering, electronics, telecommunications, computer science, and information technology. 
* IEEE sets standards, promotes best practices, and supports research and development that drive technological progress globally.

<br>

### `2.4 GHz vs. 5 GHz` 

| Feature               | `2.4 GHz Wi-Fi`                       | `5 GHz Wi-Fi `                       |
|-----------------------|---------------------------------------|------------------------------------|
| **Range**             | Longer range, better for large areas | Shorter range, best for smaller spaces |
| **Speed**             | Lower speeds (up to 600 Mbps)        | Higher speeds (up to 9.6 Gbps on Wi-Fi 6) |
| **Interference**      | More prone to interference (e.g., from microwaves, Bluetooth) | Less interference, fewer devices use 5 GHz |
| **Channel Availability** | Fewer non-overlapping channels (3-4) | More non-overlapping channels (23+), less congestion |
| **Penetration**       | Better at penetrating walls and obstacles | More susceptible to signal loss through walls |
| **Ideal Use Case**    | Larger homes or areas with many obstacles | High-speed internet for smaller spaces or devices close to the router |
| **Compatibility**     | Supported by most devices, including older ones | Supported by newer devices and Wi-Fi standards (Wi-Fi 5/6) |



<br>

[Back To Top](#networking-overview)

___

<br>

# `Bluetooth`

`Bluetooth` is a short-range wireless technology standard used to exchange data between devices over short distances using radio waves, typically in the 2.4 GHz range. 

<br>

| Feature            | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Range**          | Typically up to 100 meters, depending on the class of the device. Class 1 devices have the longest range (up to 100 meters), while Class 2 devices have a range of around 10 meters. |
| **Speed**          | Data transfer rates vary by Bluetooth version. Bluetooth 4.2 offers up to 3 Mbps, while Bluetooth 5.0 can achieve up to 2 Mbps with extended range capabilities. |
| **Power Consumption** | Designed to use minimal power, making it ideal for battery-powered devices like headphones, smartwatches, and wireless speakers. |
| **Uses**           | Commonly used to connect peripherals such as headsets, keyboards, mice, speakers, and for data exchange between devices like smartphones, tablets, and laptops. |
| **Security**       | Supports encryption and pairing protocols to secure connections between devices. |


<br>


*The Bluetooth technology we use today is named after King Harald Bluetooth Gormsson, who ruled Denmark and Norway from 958 to 985. He was known for uniting the warring tribes of Denmark and for converting the Danes to Christianity.*

<br>

*The name "Bluetooth" was chosen by Jim Kardach, an engineer at Intel, in 1996. Kardach was familiar with King Harald's nickname, which was derived from his having a dead tooth that was a dark blue/grey color. Kardach felt that the name Bluetooth was appropriate for the technology because it was intended to unite different communication protocols, just as King Harald had united the tribes of Denmark.*

<br>

*The Bluetooth logo is also a reference to King Harald. It is a bind rune that combines the Younger Futhark runes (ᚼ, Hagall) and (ᛒ, Bjarkan), which are the initials of Harald's name in Old Norse.*


<br>

[Back To Top](#networking-overview)

___

<br>

# `Cellular`
`Cellular`refers to a type of wireless communication technology that uses a network of cell towers or base stations to provide coverage over a wide area. 

<br>

| Feature                | `2G`                           | `3G`                           | `4G LTE`                       | `5G`                           |
|------------------------|------------------------------|------------------------------|------------------------------|------------------------------|
| Launch Year         | Early 1990s                  | Early 2000s                  | 2009                         | 2019                         |
| Max Speed           | 50-100 Kbps                  | 384 Kbps to 2 Mbps           | 100 Mbps to 1 Gbps           | 1 Gbps to 10+ Gbps           |
| Technology          | GSM, CDMA                    | UMTS, CDMA2000               | LTE, LTE-Advanced            | NR (New Radio)               |
| Latency             | 100-300 ms                   | 50-200 ms                    | 30-50 ms                     | <10 ms                       |
| Applications        | Voice calls, SMS, limited data | Voice calls, video calling, mobile internet | High-definition video streaming, fast downloads, VoIP | Ultra-fast internet, autonomous vehicles, AR/VR, IoT |
| Network Type        | Circuit-switched (voice), Packet-switched (data) | Packet-switched (data and voice) | Fully packet-switched        | Fully packet-switched        |
| Coverage            | Extensive (Global)           | Global, but less coverage than 2G | High coverage, expanding rapidly | Expanding, with early deployment in select cities |
| Device Compatibility| Basic phones, feature phones  | Smartphones, basic mobile devices | Smartphones, tablets, laptops | Next-gen smartphones, IoT devices, advanced applications |
| Bandwidth Efficiency| Low                          | Moderate                     | High                         | Very high                    |

<br>

`LTE (Long-Term Evolution)` is a standard for wireless broadband communication, commonly used in 4G networks, that provides high-speed data transmission for mobile devices like smartphones, tablets, and laptops.


<br>

[Back To Top](#networking-overview)

___

<br>

# `Bandwidth and Latency`

`Bandwidth` is maximum rate of data transfer across a given path. It is measured in bits per second (bps). The higher the bandwidth, the more data can be transferred over the path in a given amount of time.

| Measurement| Unit| Description |
|-|-|-|
| `Bits per second`  | `bps`| Basic unit of data transfer |
| `Kilobits per second` | `Kbps`  | 1,000 (10<sup>3</sup>) bits per second. |
| `Megabits per second` | `Mbps`  | 1,000,000 (10<sup>6</sup>) bits per second. |
| `Gigabits per second` | `Gbps`  | 1,000,000,000 (10<sup>9</sup>) bits per second. |
| `Terabits per second` | `Tbps`  | 1,000,000,000,000 (10<sup>12</sup>) bits per second.  |
| `Bytes per second`    | `Bps`   | 8 bits per second. |
| `Kilobytes per second` | `KBps` | 1,000 (10<sup>3</sup>) bytes per second. |
| `Megabytes per second` | `MBps` | 1,000,000 (10<sup>6</sup>) bytes per second.|
| `Gigabytes per second` | `GBps` | 1,000,000,000 (10<sup>9</sup>) bytes per second. |

<br>

`Latency` refers to the time delay between the sending of a signal or request and the receipt of the corresponding response or acknowledgment.
* the time it takes for data to travel from its source to its destination and is typically measured in `milliseconds (ms)`.

<br>

[Back To Top](#networking-overview)

___

<br>

# `Network Interface Card NIC : Layer 2 Data Link`

`Network Interface Card (NIC)` also known as a network adapter, local area network (LAN) adapter, or physical network interface, is a hardware component within a device that connects it to a computer network.

<br>

`Media Access Control (MAC) address`, also known as a `physical address`, is a unique identifier assigned and burned into a `network interface controller (NIC)`. 

<br>

 See [MAC-Addresses.md](MAC-Addresses.md) for more on MAC Address.

<br>

### `At Layer 2 Data Link`
* Data is packaged into `Frames`
* `Frames` are routed using `MAC addresses`

`Frames` include:
* Destination MAC address
* Source MAC address
* Frame Type/Length
* Payload Data
* Frame Check Sequence

<br>

Frame Diagram
```
+----------------+-------------------+-------------------+--------------------+
| Destination MAC| Source MAC        | Type/Length       | Payload/Data       |
+----------------+-------------------+-------------------+--------------------+
| FCS (Frame Check Sequence)                                                  |
+-----------------------------------------------------------------------------+
```

<br>

[Back To Top](#networking-overview)

___

<br>

# `Network Switch : Layer 2 Data Link`

A `Network Switch` is a hardware device that connects devices within a LAN. It is a multiport bridge that uses `media access control (MAC)` addresses to route data at the `data link layer (layer 2)` of the `open systems interconnect (OSI) model`.
<br>

Media Access Control (MAC) Addresses
* aka physical address, hardware address, or Data Link Layer Address

TODO:
MAC addresses are short range and only used to find nodes on the local network.

More on MAC addresses : [`MAC-Addresses.md`](./MAC-Addresses.md)

<br>

### `Network Switches`
* Connect devices within a LAN
* Data is packaged into `Frames`
* Use MAC addresses to route `Frames`

<br>

### `At Layer 2 Data Link`
* Data is packaged into `Frames`
* `Frames` are routed using `MAC addresses`

`Frames` include:
* Destination MAC address
* Source MAC address
* Frame Type/Length
* Payload Data
* Frame Check Sequence

<br>

Frame Diagram
```
 0                   1                   2                   3  
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|                    Preamble (7 bytes)                         |  
|           10101010 pattern for synchronization                |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
| Start Frame Delimiter (1 byte): 10101011                      |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|               Destination MAC Address (6 bytes)               |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|                 Source MAC Address (6 bytes)                  |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|     Ethertype (2 bytes)      |                                |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|               Payload / Data (46 to 1500 bytes)               |  
|     (e.g., IP packet with headers and application data)       |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|           Frame Check Sequence (CRC32, 4 bytes)               |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

TODO:
Layer 2
firmware
trailer
Frame includes header payload and trailer


`Address Resolution Protocol ARP` is a Layer 2 : Data Link protocol that works with IPv4 to discover MAC addresses on nodes in a local network and to maintain a database that maps local IP addresses to MAC addresses. 
* ARP works at Layer 2 but uses IP at Layer 3, therefore it is sometimes said to work a Layer 2.5
* ARP only works within its local network bounded by routers. 
* ARP relies on broadcasting to all nodes on the network segment.

<br>

`ARP Table` or `ARP Cache` is a database of records that maps MAC addresses to IP addresses. An ARP table is stored on storage device on a computing device and is used by the ARP utility to supply MAC addresses of network nodes, given their IP addresses. 

<br>

Dynamic ARP table entries are records that are created when a client makes and ARP request that cannot be satisfied by data already in the ARP table. 

Static ARP table entries are records that have been manually entered using an ARP utility. 

On Windows and Linux a command line ARP utility exists called `arp` and can be used to retrieve and manipulate ARP table information.

    arp -a

This command returns the ARP table on the device.

On Linux

    ip neigh

Is a newer command that performs the same task.

<br>

Ethernet II is the current Ethernet standard and is distinguished from other Ethernet frame types in that it contains a 2 byte field to identify the upper-layer protocol contained in the frame. 
* Ethernet adds both a header and a trailer to the payload data.
* Mininmum Frame Size 64 bytes
* Maximum Frame Size 1518 bytes
* VLANs have an extra 4-byte field between source and Type used to manage VLAN traffic

<br>

Maximum Transmission Unit MTU is the largest size in bytes that routers in a message's path will allow at the Network Layer and therefore defines the maximum payload size that a Layer 2 frame can encapsulate. 
* For Ethernet the default MTU is 1500 bytes
* Some special purpose networks use a special version of Ethernet that allows for a `jumbo frame` which can have an MTU as high as 9198 bytes.


<br>

[Back To Top](#networking-overview)

___

<br>

# `Router : Layer 3 Network`

A `Router` is a hardware device that connects two or more networks together. It is a layer 3 device in the open systems interconnect (OSI) model and forwards data packets between networks based on their destination internet protocol (IP) addresses.

<br>

### `Routers`:
* aka `Default Gateway`
* Connect Networks together spanning the `LAN` and `WAN`
* Package data in `Packets`
* Route packets using `IP addresses`
* Have both a `Public` and `Private` IP address

<br>

An `IP address` (Internet Protocol address) is a unique numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication.

<br>

See [IP-Addresses](IP-Addresses.md) for more on IP Addresses.

<br>

### `At Layer 3 Network`
* Data is packaged into `Packets`
* `Packets` are routed using `IP addresses`

`Packets` include:
* Destination IP
* Source IP
* Protocol
* Packet Payload Data
* Header Checksum

<br>

Packet Diagrams

### IPv4 Packet
* The numbers represent bit positions 0-31 (32 bits/ 4 bytes)
```
 0                   1                   2                   3  
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|Version|  IHL  |Type of Service|        Total Length           |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|       Identification          |Flags|     Fragment Offset     |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|  Time to Live |    Protocol   |        Header Checksum        |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|                     Source Address                            |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|                  Destination Address                          |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|                    Options (if any)           |    Padding    |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|                     Payload Data                              |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```


### IPv6 Packet
* The numbers represent bit positions 0-31 (32 bits/ 4 bytes)
```
 0                   1                   2                   3  
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|Version| Traffic Class |           Flow Label                  |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|         Payload Length        |  Next Header  |  Hop Limit    |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|                                                               |  
|                     Source Address (128 bits)                 |  
|                                                               |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|                                                               |  
|                 Destination Address (128 bits)                |  
|                                                               |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|                     Payload Data                              |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

<br>

TODO:
`Internet Protocol (IP)` a core protocol of TCP/IP and the priciple protocol of the Network Layer (Layer 3) that provides information about how and where data should be delivered. 
* `IP addresses` are unique addresses assigned to each node in a TCP/IP network. 
    * Two versions `IPv4` and `IPv6`



<br>

A `Packet` is the entire Network Layer message.<br>
Including:
1. Network Layer Header 
2. Segement (TCP) or Datagram (UDP) from Layer 4

<br>



Maximum Transmission Unit
Fragmentation is a Network Layer service that subdivides packets into smaller packets when those packets exceed the maximum size for the network.


Layer 3 Protocols
`Internet Control Message Protocol ICMP` is a Layer 3 Network protocol that reports on the success or failure of data delivery. 

```
 0                   1                   2                   3  
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|     Type      |     Code      |          Checksum             |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|           Identifier          |        Sequence Number        |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
|                          Payload Data                         |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

IPv6 uses ICMPv6 to perform the functions of ICMPv4 and ARP in IPv4 netowrks. 

`Time to Live TTL` is the maximum duration that an IPv4 packet can remain on thet network before it is discarded. It represents the number of router hops remaining before the packet is dropped. 

----------------------------------













<br>

[Back To Top](#networking-overview)

___

<br>

# `Wireless Access Point WAP : Layer 1 Physical`
A `Wireless Access Point (WAP)`, also known as an access point (AP), is a networking hardware device that allows other Wi-Fi devices to connect to a wired network. 
* WAPs are typically used to create a wireless local area network (WLAN) in a home or office.

<br>

A `Service Set Identifier (SSID)` is the name given to a wireless network broadcast by a WAP. 

<br>

[Back To Top](#networking-overview)

___

<br>

# `Firewalls : Multi Layer`
A `Firewall` is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. It is designed to block unauthorized access to a protected network. Firewalls can be implemented as hardware, software, or a combination of both.

<br>

### `Firewalls`
* act as a filter for network traffic
* can be hardware or software
* Device Level Firewalls exist on each device
* Network Level Firewalls exist on the Router

<br>

| Feature | `Device Level Firewalls`| `Network Level Firewalls`|
|-|-|-|
| `Definition`              | Firewalls installed on individual devices (e.g., PCs, servers) to protect them from unauthorized access and threats. | Firewalls that are implemented on the network as a whole, protecting all devices and resources within that network. |
| `Location`                | Operates at the endpoint level (individual devices).    | Operates at the network boundary or gateway.            |
| `Deployment`              | Installed and configured on each `device` separately.    | Installed on `routers` or dedicated firewall appliances.   |
| `Protection Scope`        | Protects only the device it is installed on.           | Protects the entire network and all connected devices.   |
| `Examples`                | Windows Firewall, macOS Firewall, antivirus software with built-in firewall features. | Cisco ASA, Fortinet FortiGate, Palo Alto Networks, and pfSense. |




<br>

[Back To Top](#networking-overview)

___

<br>

# `Modulator-Demodulator MODEM : Layer 1 Physical`
A `Modulator-Demodulator (Modem)` is a hardware device that converts digital data into analog signals and vice versa. It is used to connect a computer or router to a broadband network (the internet), such as cable or digital subscriber line(DSL).

<br>

### `Modems`
* convert `digitial` data to `analog`
* use `coaxial cables` to send data across the internet

<br>


`Digital` refers to the representation of information using discrete values, typically in binary form (0s and 1s). 
* In digital systems, data is encoded in a way that allows for precise replication, storage, and transmission. 
* Digital signals consist of distinct levels or states, which makes them less susceptible to noise and interference compared to analog signals.

<br>

`Analog` refers to the representation of information using continuous signals or waves. 
* In analog systems, data varies smoothly and can take on any value within a given range. 
* Analog signals represent physical quantities (like sound, light, or temperature) and are often subject to distortion and noise, which can affect the quality of the transmitted information.


<br>

[Back To Top](#networking-overview)

___

<br>



# `Optical Network Terminal ONT: Layer 1 Physical`
An `Optical Network Terminal (ONT)` is a device that converts `optical (light) signals` from a fiber optic cable into `electrical signals` that can be used by a router or other network device. 
* ONTs are typically used in fiber optic networks to provide high-speed internet access.

<br>

### `ONTs`
* convert `light` into `electricity`
* use `fiber optic cables` to send data across the internet

<br>

[Back To Top](#networking-overview)

___

<br>

# `Satellite Modem : Layer 1 Physical`

A `Satellite Modem` is a specialized device that enables the transmission and reception of data over satellite communication networks by modulating digital signals from user devices into `radio frequency (RF)` signals suitable for satellite transmission and demodulating incoming RF signals back into digital data.

<br>

### `Satellite Modems`
* covert `digital` signals to `RF` signals
* use RF signals to send data across the internet

<br>

[Back To Top](#networking-overview)

___

<br>

# `Basic LAN Topology`

Many modern networking setups use a single device that combines the functions of a modem, router, and switch, streamlining internet connectivity and local network management. These all-in-one devices provide convenience and efficiency for both home and small business users.

<br>


```                                                         
                                                              Digital                Radio Frequency --> 
                                                             -------[Satellite Modem]------------------
                                                            /            |             RF Signal
                                                           /             OR
                                                          /   Digital    |             Light  --> 
[Devices]---------->[Switches]---------->[Router]-----------------------[ONT]--------------------------
         Ethernet              Ethernet      /   Ethernet \              |         Fiber Optic Cable
          Cable                 Cable       /     Cable    \             OR 
                                           /                \  Digital   |             Analog --> 
                                     [WAP]-                  -----------[Modem]------------------------  
                                                                                     Coaxial Cable

``` 


`TODO:`
Topology
Physical Topology vs. Logical Topology
Physical Topology is the physical layout of the media, nodes, and devices on a network.
Logical topology is the way in which data is transmitted between nodes, including network and resource access controls. 
star topology
mesh topology
star-bus toplogy
bus topology
hybrid topology
ring topology



<br>

[Back To Top](#networking-overview)

___

<br>


# `The Internet: Layer 3 Network`

The term `Internet` comes from "inter-network," meaning "between networks." It is a global network of interconnected computers and devices that communicate using standardized protocols.

<br> 

An `Internet Service Provider (ISP)` provides access to the infrastructure needed to connect to the Internet.
* This is the company you purchase your Internet service from. 

<br>



<br>

[Back To Top](#networking-overview)

___

<br>

# `Ports, Protocols, and Services : Layer 4 Transport`

A `protocol` is a set of rules and conventions that define how data is transmitted and processed over a network or communication system. 
* `Protocols` establish the procedures for data exchange, ensuring that devices and systems can communicate effectively and understand each other. 

<br><br>

A `Port` serves as a logical communication endpoint for applications and services on a device. 
* It helps in directing data to the correct application or service by providing a unique number associated with that service.

<br><br>

`Networking services` refer to a range of functionalities and operations provided over a network that facilitate communication, resource sharing, and data management between devices and systems. 
* `These services opperate at Layers 5-7`. 

<br><br>

### `At Layer 4 Transport`  
There are 2 protocols:  
* `Transmission Control Protocol (TCP)(Connection-Oriented)  `
* `User Datagram Protocol (UDP)(Connectionless)`  

<br>

User Datagram Protocol UDP is a connectionless protocol.
* Does not guarantee delivery of data.
* Data is packaged as `Datagrams`  
* Datagrams are routed to `UDP Ports`
* Faster and more efficient than TCP  

```
+---------------------------------------------------------+
|                      UDP Datagram                      |
+---------------------------------------------------------+
| Destination Port (2 bytes)                             |
+---------------------------------------------------------+
| Source Port (2 bytes)                                  |
+---------------------------------------------------------+
| Length (2 bytes)                                       |
+---------------------------------------------------------+
| Checksum (2 bytes)                                     |
+---------------------------------------------------------+
| Data (variable length)                                 |
+---------------------------------------------------------+
```

<br>

Transmission Control Protocol TCP is a connection oriented protocol.
* Uses a `three-way handshake` to establish a TCP connection. 
* Data is packaged as `Segments`  
* Segments are routed to `TCP Ports`  
* A `checksum` is used to verify data integrity and reciept.

```
+---------------------------------------------------------------+
|                      TCP Segment                              |
+---------------------------------------------------------------+
| Destination Port (2 bytes)                                    |
+---------------------------------------------------------------+
| Source Port (2 bytes)                                         |
+---------------------------------------------------------------+
| Sequence Number (4 bytes)                                     |
+---------------------------------------------------------------+
| Acknowledgment Number (4 bytes)                               |
+---------------------------------------------------------------+
| TCP Header Length (4 bits) | Reserved (6 bits) |Flags (6 bits)|
+---------------------------------------------------------------+
| Window Size (2 bytes)                                         |
+---------------------------------------------------------------+
| Checksum (2 bytes)                                            |
+---------------------------------------------------------------+
| Urgent Pointer (2 bytes)                                      |
+---------------------------------------------------------------+
| Options (0-4 bytes)                                           |
+---------------------------------------------------------------+
| Paddin (variable length)                                      |
+---------------------------------------------------------------+
| Data (variable length)                                        |
+---------------------------------------------------------------+
```

<br>

Steps in a Three Way Handshake
1. Synchronize Request (SYN): 
* the requesting computer selects a random number to synchronize communication. 
* the SYN bit is set to 1 meaning the SYN flag is activated indicating the request to communicate and synchronize sequence numbers. 
* the ACK bit is usually set to 0 since the responding computer has not yet sent a response.

2. Synchronize/Acknowledge (SYN/ACK) computer 2 recieves the SYN request and responds with a segment.
* The ACK and SYN bits are both set to 1.
* The Acknowledgement number field contains a number that equals the sequence number computer 1 orginally sent, plus 1. 
* The sequence number field computer 2 sends its own random number.

3. Acknowledge (ACK) computer 1 recieves the SYN/ACK and responds with a segment.
* Containing the expected sequence number from computer 2
* The Acknowledgement number field equals the sequence number that computer 2 sent plus 1.
* The ACK bit is set to 1.

4. The connection has now been established. 

<br>

For more on Ports, Protocols, and Services: [Ports-Protocols-Services.md](Ports-Protocols-Services.md)

<br>

[Back To Top](#networking-overview)

___

<br>


`TODO:`

Session
Presentation
Application

`Payload Data` is data passed between applications or utility programs and the operating system, and includes control information.

`Header` data added to the beginning of a payload where protocols add control information.


`Encapsulation` the processs of adding a header to data inherited from the layer above. 

<br>

[Back To Top](#networking-overview)

___

<br>


# `The World Wide Web`

The `World Wide Web (www)` is one part of the Internet commonly known simply as `the web`. It is a system of interlinked documents, multimedia content, and applications accessed via the Internet. 

* A `browser` is used to interact with the www to send requests and retrieve information and services from `web servers`. 
* Uses the `Hypertext Transfer Protocol (HTTP)`, or its secure version `HTTPS`.

<br>

[Back To Top](#networking-overview)

___

<br>

*Created and maintained by Mr. Merritt*