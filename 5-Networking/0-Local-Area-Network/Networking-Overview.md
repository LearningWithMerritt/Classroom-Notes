# `Networking Overview`

<br>

___

<br>

Covered in this file:
1. [`Network Defined`](#network-defined)
1. [`Network Connections`](#network-connections)
1. [`Bandwidth or Connection Rate`](#bandwidth-or-connection-rate)
1. [`Network Interface Card NIC`](#network-interface-card-nic)
1. [`Network Switch`](#network-switch)
1. [`Router`](#router)
1. [`Wireless Access Point WAP`](#wireless-access-point-wap)
1. [`Firewalls`](#firewalls)
1. [`Modulator-Demodulator Modem`](#modulator-demodulator-modem)
1. [`Optical Network Terminal ONT`](#optical-network-terminal-ont)
1. [`Satellite Modem`](#satellite-modem)
1. [`Basic Network Topology`](#basic-network-topology)


<br>

___

<br>

# `Network Defined`
A `computer network` is a system of interconnected devices that communicate and share resources with each other. 
* Networks allow devices, such as computers, printers, and smartphones, to exchange data, share files, and access shared resources like the Internet, databases, and applications.

<br>

Networks are categorized by thier size, and scope. 

| Network Type| Description|
|:-|:-|
| `Local Area Network (LAN)`| Covers a limited area, such as a home, school, or office building.|
| `Wide Area Network (WAN)` | Spans larger geographic areas, often connecting multiple LANs over cities, countries, or continents.|
| `Metropolitan Area Network (MAN)` | Connects networks within a city or metropolitan area.|
| `Internet` | Global system of interconnected networks that allows devices worldwide to communicate and exchange information. |

<br>

There are two basic network models: 
* `OSI (Open Systems Interconnection)` model 
* `TCP/IP (Transmission Control Protocol/Internet Protocol)` model. 

<br>

Both models serve as a framework to understand and design network protocols and communication processes but differs in structure and focus.

For More on these Networking Models see [Networking-Models.md](Networking-Models.md)

To focus our understanding of Networking we will follow the layers of these models. 


<br>

[Back To Top](#networking-overview)

___

<br>

# `Network Data (Layer 1:Physical)`
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
| Application Layer | `Data` | Data| User interface and application services|
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
* Data is transmitted as electrical, optical, or radio signals


<br>

# `Wired Connections:`
| Connector Type | Description| Use Case | Max Range| Max Speed |
|-|-|-|-|-|
| `Ethernet` | Standard copper wire connection using twisted-pair cables (e.g., CAT5, CAT6). | LANs and wired networks| ~100 meters| Up to 10 Gbps |
| `Coaxial`| Cable with a copper core, shielded for signal protection.| Cable internet, TV connections | Up to 500 meters | Up to 1 Gbps|
| `Fiber Optic`| Uses light to transmit data through thin glass or plastic fibers, resistant to interference. | High-speed internet, long-distance WANs| Up to 40 km+ | Up to 100 Gbps|


<br>


# `Wireless Connections`

| Connector Type | Description | Use Case | Max Range | Max Speed |
|----------------|-------------|----------|-----------|-----------|
| `Wi-Fi`        | Wireless standard using radio waves to connect devices to a local network. | Wireless LANs, mobile devices | Up to 300 meters | Up to 9.6 Gbps (Wi-Fi 6) |
| `Bluetooth`    | Short-range wireless connection for peripheral devices, using low power and 2.400 to 2.485 GHz radio frequency. | Personal devices (headsets, keyboards) | Up to 100 meters | Up to 3 Mbps (Bluetooth 4.2) |
| `Cellular`     | Mobile wireless network using cellular towers, supporting technologies like 4G and 5G for data and voice communication. | Smartphones, mobile data | Up to several kilometers (depending on tower coverage) | Up to 10 Gbps (5G) |
| `Satellite`    | Wireless communication via satellites orbiting the Earth for internet access in remote or rural areas. | Remote internet access, rural areas | Global coverage | Up to 100 Mbps (Low Earth Orbit satellites like SpaceX Starlink) |


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

`Network Interface Card (NIC)`  also known as a network adapter, local area network (LAN) adapter, or physical network interface, is a hardware component within a device that connects it to a computer network.

`Media Access Control (MAC) address`, also known as a `physical address`, is a unique identifier assigned and burned into a `network interface controller (NIC)`. 

For more on MAC Address: [MAC-Addresses.md](MAC-Addresses.md)

<br>

`At Layer 2 Data Link`
* Data is packaged into `Frames`
* Frames are routed using `MAC addresses`

Frames include:
* Destination MAC address
* Source MAC address
* Frame Type/Length
* Payload Data
* Frame Check Sequence

<br>

```
+----------------+-------------------+-------------------+--------------------+
| Destination MAC| Source MAC        | Type/Length       | Payload/Data       |
+----------------+-------------------+-------------------+--------------------+
| FCS (Frame Check Sequence)                                           |
+---------------------------------------------------------------------+
```

<br>

[Back To Top](#networking-overview)

___

<br>

# `Network Switch : Layer 2 Data Link`

A `Network Switch` is a hardware device that connects devices within a LAN. It is a multiport bridge that uses `media access control (MAC)` addresses to forward data at the `data link layer (layer 2)` of the `open systems interconnect (OSI) model`.

<br>

`Network Switches`:
* Connect devices within a LAN
* Data is packaged into Frames
* Use MAC addresses to route Frames

<br>

`At Layer 2 Data Link`
* Data is packaged into `Frames`
* Frames routed using `MAC addresses`

Frames include:
* Destination MAC address
* Source MAC address
* Frame Type/Length
* Payload Data
* Frame Check Sequence

<br>

```
+----------------+-------------------+-------------------+--------------------+
| Destination MAC| Source MAC        | Type/Length       | Payload/Data       |
+----------------+-------------------+-------------------+--------------------+
| FCS (Frame Check Sequence)                                           |
+---------------------------------------------------------------------+

```

<br>

[Back To Top](#networking-overview)

___

<br>

# `Router : Layer 3 Network`

A `Router` is a hardware device that connects two or more networks together. It is a layer 3 device in the open systems interconnect (OSI) model and forwards data packets between networks based on their destination internet protocol (IP) addresses.

`Routers`:
* aka `Default Gateway`
* Connect Networks together
* Package data in `Packets`
* Route packets using `IP addresses`
* Have both a `Public` and `Private` IP address

<br>

An `IP address` (Internet Protocol address) is a unique numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication.

For more on IP addresses: [IP-Addresses](IP-Addresses.md)

<br>

`At Layer 3 Network`
* Data is packaged into `Packets`
* Packets are routed using `IP addresses`

Packets include:
* Destination IP
* Source IP
* Protocol
* Packet Payload Data
* Header Checksum

<br>

```
+--------------------+--------------------+---------------------+-----------------------+-----------------+
| Destination IP     | Source IP          | Protocol            | Packet Data (Payload) | Header Checksum |
+--------------------+--------------------+---------------------+-----------------------+-----------------+
```
<br>

[Back To Top](#networking-overview)

___

<br>

# `Wireless Access Point WAP : Layer 1 Physical`
A `Wireless Access Point (WAP)`, also known as an access point (AP), is a networking hardware device that allows other Wi-Fi devices to connect to a wired network. 
* WAPs are typically used to create a wireless local area network (WLAN) in a home or office.

A `Service Set Identifier (SSID)` is the name given to a wireless network broadcast by a WAP. 

<br>

[Back To Top](#networking-overview)

___

<br>

# `Firewalls : Multi Layer`
A `Firewall` is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. It is designed to block unauthorized access to a protected network. Firewalls can be implemented as hardware, software, or a combination of both.

`Firewalls`:
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

`Modems`:
* convert digitial data to analog
* use coaxial cables to send data across the internet

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
An `Optical Network Terminal (ONT)` is a device that converts optical(light) signals from a fiber optic cable into electrical signals that can be used by a router or other network device. ONTs are typically used in fiber optic networks to provide high-speed internet access.

`ONTs`
* convert light into electricity
* use fiber optic cables to send data across the internet

<br>

[Back To Top](#networking-overview)

___

<br>

# `Satellite Modem : Layer 1 Physical`

A `Satellite Modem` is a specialized device that enables the transmission and reception of data over satellite communication networks by modulating digital signals from user devices into `radio frequency (RF)` signals suitable for satellite transmission and demodulating incoming RF signals back into digital data.

`Satellite Modems`
* covert digitial signals to RF signals
* use RF signals to send data across the internet

<br>

[Back To Top](#networking-overview)

___

<br>

# `Basic LAN Network Topology`

Many modern networking setups use a single device that combines the functions of a modem, router, and switch, streamlining internet connectivity and local network management. These all-in-one devices provide convenience and efficiency for both home and small business users.

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

[Back To Top](#networking-overview)

___

<br>

# `Ports, Protocols, and Services : Layer 4 Transport`

A `protocol` is a set of rules and conventions that define how data is transmitted and processed over a network or communication system. 
* `Protocols` establish the procedures for data exchange, ensuring that devices and systems can communicate effectively and understand each other. 

<br>

A `Port` serves as a logical communication endpoint for applications and services on a device. 
* It helps in directing data to the correct application or service by providing a unique number associated with that service.

<br>

`Networking services` refer to a range of functionalities and operations provided over a network that facilitate communication, resource sharing, and data management between devices and systems. 
* `These services opperate at Layers 5-7`. 

<br>

`At Layer 4 Transport`  
There are 2 protocols:  
* Transmission Control Protocol (TCP)(Connection-Oriented)  
      * User Datagram Protocol (UDP)(Connectionless)  

UDP  
* Data is packaged as `Datagrams`  
* Datagrams are routed to `UDP Ports`  

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

TCP  
* Data is packaged as `Segments`  
* Segments are routed to `TCP Ports`  

```
+---------------------------------------------------------+
|                      TCP Segment                        |
+---------------------------------------------------------+
| Destination Port (2 bytes)                              |
+---------------------------------------------------------+
| Source Port (2 bytes)                                   |
+---------------------------------------------------------+
| Sequence Number (4 bytes)                               |
+---------------------------------------------------------+
| Acknowledgment Number (4 bytes)                         |
+---------------------------------------------------------+
| Data Offset (4 bits) | Reserved (3 bits) |Flags (9 bits)|
+---------------------------------------------------------+
| Window Size (2 bytes)                                   |
+---------------------------------------------------------+
| Checksum (2 bytes)                                      |
+---------------------------------------------------------+
| Urgent Pointer (2 bytes)                                |
+---------------------------------------------------------+
| Options (variable length)                               |
+---------------------------------------------------------+
| Data (variable length)                                  |
+---------------------------------------------------------+
```

<br>

For more on Ports, Protocols, and Services: [Ports-Protocols-Services.md](Ports-Protocols-Services.md)

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