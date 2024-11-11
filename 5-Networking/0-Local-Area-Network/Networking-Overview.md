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

[Back To Top](#networking-overview)

___

<br>



# `Network Connections`
`Network Connectors` are  used to connect devices together in a network, and transmit data between those devices.
| Connector Type | Description| Use Case | Max Range| Max Speed |
|-|-|-|-|-|
| `Ethernet` | Standard copper wire connection using twisted-pair cables (e.g., CAT5, CAT6). | LANs and wired networks| ~100 meters| Up to 10 Gbps |
| `Coaxial`| Cable with a copper core, shielded for signal protection.| Cable internet, TV connections | Up to 500 meters | Up to 1 Gbps|
| `Fiber Optic`| Uses light to transmit data through thin glass or plastic fibers, resistant to interference. | High-speed internet, long-distance WANs| Up to 40 km+ | Up to 100 Gbps|
| `Wi-Fi`| Wireless standard using radio waves to connect devices to a local network. | Wireless LANs, mobile devices| Up to 300 meters | Up to 9.6 Gbps (Wi-Fi 6)|
| `Bluetooth`  | Short-range wireless connection for peripheral devices, using low power and 2.4 GHz radio frequency. | Personal devices (headsets, keyboards)| Up to 100 meters | Up to 3 Mbps (Bluetooth 4.2)  |

<br>

`Special Note on Wi-Fi`
* Wi-Fi is the common name given to the standard of wireless communcation defined by the IEEE 802.11x standards.
* "Wi-Fi" was created by the Wi-Fi Alliance as a marketing phrase to replace the more technical term "IEEE 802.11x".
* "Wi-Fi" is a play on the words "wireless" and "fidelity".
* Most wireless networks use 2.4 GHz and 5 GHz frequencies.

**`What Wi-Fi is NOT: Internet or Wireless Fidelity`**

<br>

The `IEEE (Institute of Electrical and Electronics Engineers)` is a professional association dedicated to advancing technology and innovation across various fields, including electrical engineering, electronics, telecommunications, computer science, and information technology. 
* IEEE sets standards, promotes best practices, and supports research and development that drive technological progress globally.


<br>

[Back To Top](#networking-overview)

___

<br>

# `Bandwidth or Connection Rate`

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

[Back To Top](#networking-overview)

___

<br>

# `Network Interface Card NIC`
`Network Interface Card (NIC)`  also known as a network adapter, local area network (LAN) adapter, or physical network interface, is a hardware component within a device that connects it to a computer network.

`Media Access Control (MAC) address`, also known as a `physical address`, is a unique identifier assigned and burned into a `network interface controller (NIC)`. 

<br>

[Back To Top](#networking-overview)

___

<br>

# `Network Switch`
A `Network Switch` is a hardware device that connects devices within a LAN. It is a multiport bridge that uses `media access control (MAC)` addresses to forward data at the `data link layer (layer 2)` of the `open systems interconnect (OSI) model`.

<br>

`Network Switches`:
* Connect devices within a LAN
* Use MAC addresses to route data
* Package data into `Frames`

<br>

[Back To Top](#networking-overview)

___

<br>

# `Router`
A `Router` is a hardware device that connects two or more networks together. It is a layer 3 device in the open systems interconnect (OSI) model and forwards data packets between networks based on their destination internet protocol (IP) addresses.

`Routers`:
* aka `Default Gateway`
* Connect Networks together
* Use `IP addresses`
* Package data in `Packets`
* Have both a `Public` and `Private` IP address

<br>

An `IP address` (Internet Protocol address) is a unique numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication.


<br>

[Back To Top](#networking-overview)

___

<br>

# `Wireless Access Point WAP`
A `Wireless Access Point (WAP)`, also known as an access point (AP), is a networking hardware device that allows other Wi-Fi devices to connect to a wired network. 
* WAPs are typically used to create a wireless local area network (WLAN) in a home or office.

A `Service Set Identifier (SSID)` is the name given to a wireless network broadcast by a WAP. 

<br>

[Back To Top](#networking-overview)

___

<br>

# `Firewalls`
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

# `Modulator-Demodulator MODEM`
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



# `Optical Network Terminal ONT`
An `Optical Network Terminal (ONT)` is a device that converts optical(light) signals from a fiber optic cable into electrical signals that can be used by a router or other network device. ONTs are typically used in fiber optic networks to provide high-speed internet access.

`ONTs`
* convert light into electricity
* use fiber optic cables to send data across the internet

<br>

[Back To Top](#networking-overview)

___

<br>

# `Satellite Modem`

A `Satellite Modem` is a specialized device that enables the transmission and reception of data over satellite communication networks by modulating digital signals from user devices into `radio frequency (RF)` signals suitable for satellite transmission and demodulating incoming RF signals back into digital data.

`Satellite Modems`
* covert digitial signals to RF signals
* use RF signals to send data across the internet

<br>

[Back To Top](#networking-overview)

___

<br>

# `Basic Network Topology`

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


# `The Internet and the World Wide Web`

The term `Internet` comes from "inter-network," meaning "between networks." It is a global network of interconnected computers and devices that communicate using standardized protocols.

<br> 

An `Internet Service Provider (ISP)` provides access to the infrastructure needed to connect to the Internet.
* This is the company you purchase your Internet service from. 

<br>

The `World Wide Web (www)` is one part of the Internet commonly known simply as `the web`. It is a system of interlinked documents, multimedia content, and applications accessed via the Internet. 
* A `browser` is used to interact with the www to send requests and retrieve information and services from `web servers`. 
* Uses the `Hypertext Transfer Protocol (HTTP)`, or its secure version `HTTPS`.

<br>

[Back To Top](#networking-overview)

___

<br>

*Created and maintained by Mr. Merritt*