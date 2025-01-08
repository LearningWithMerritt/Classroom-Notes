# `Internet Protocol Addresses`
---

Covered in this file:
1. [`Internet Protocol`](#internet-protocol)
1. [`IPv4 32-bit Addresses`](#ipv4-32-bit-addresses)
1. [`IPv4 Address Ranges`](#ipv4-address-ranges)
1. [`IPv6 128-bit Addresses`](#ipv6-128-bit-addresses)
1. [`IPv6 Ranges`](#ipv6-ranges)
1. [`Public vs. Private IP Addresses`](#public-vs-private-ip-addresses)
1. [`Static vs. Dynamic IP Addresses`](#static-vs-dynamic-ip-addresses)
1. [`IP Addresses and Ports`](#ip-addresses-and-ports)
1. [`Subnetting`](#subnetting)
1. [`Assigning IP Addresses: DHCP`](#assigning-ip-addresses-dhcp)
1. [`How Do I See my Public IP? Private IP?`](#how-do-i-see-my-public-ip-private-ip)
1. [`Translating Web Addresses to IP Addresses: DNS`](#translating-web-addresses-to-ip-addresses-dns)


<br>

___

<br>

# `Internet Protocol`

The `Internet Protocol (IP)` is a set of rules and standards that govern how data is sent and received over networks, including the internet. 
> * IP is the primary protocol that enables communication between devices on a network by ensuring that data packets are routed and delivered to the correct destination.  
> * Each device on a network recieves a unique IP address, typically assigned using DHCP,  to identify the source and destination of packets in the network.
> * There are currently 2 versions of the Internet Protocol, `IPv4` and `IPv6`. 

<br>

`Host` refers to any device that communicates over a network and has an IP address assigned to it.   
> * `Hosts` can be computers, servers, printers, smartphones, routers, or any other devices that use network protocols to send and receive data.

<br>

`Client` refers to a computer, device, or program that requests services or resources from another computer or server within a network.   
> * The `client` initiates communication with a `server`, which is a system that provides the requested services or resources.

<br>

`Server` refers to a computer, device, or program that provides services, resources, or data to clients over a network. 
> * The `server` listens/waits for requests from clients and responds by delivering the requested resources or performing specific tasks. 
> * `Servers` can handle multiple client requests simultaneously and can offer various services such as hosting websites, managing emails, storing files, or running applications.

<br>

[Back To Top](#internet-protocol-addresses)
___

<br>

# `IPv4 32-bit addresses` 

`IPv4 addresses` use four 8-bit decimal numbers separated by a period ( . ).  
* Total Range of addresses: 
```
0.0.0.0 <--> 255.255.255.255  
```
* There are 2<sup>32</sup> (4,294,967,296) possible addresses in the IPv4 Protocol.

<br>

Format:
> x = 8 bit (1 byte) number between 0 and 255 called an octet

    x.x.x.x


Dotted Decimal Format Example: 

    192.168.1.1

Binary Format Example:

    11000000.10101000.00000001.00000001

<br>

[Back To Top](#internet-protocol-addresses)
___

<br>

# `IPv4 Address Ranges`

| IP Class | Public IP Range| Private IP Range| Subnet Mask| Total Number of Networks | Total Number of Clients   |
|:-:|:-:|:-:|:-:|:-:|:-:|
| **A**| 1.0.0.0 to 126.0.0.0| 10.0.0.0 to 10.255.255.255 | 255.0.0.0 | 126 (2<sup>7</sup>-2)| 16,777,214 (2<sup>24</sup>-2) |
| **B**| 128.0.0.0 to 191.255.0.0| 172.16.0.0 to 172.31.255.255 | 255.255.0.0 | 16,382 (2<sup>14</sup>-2)| 65,534 (2<sup>16</sup>-2)|
| **C**| 192.0.0.0 to 223.255.255.0| 192.168.0.0 to 192.168.255.255 | 255.255.255.0 | 2,097,150 (2<sup>21</sup>-2) | 254 (2<sup>8</sup>-2)|
| **D**| 224.0.0.0 to 239.255.255.255 | N/A | N/A| N/A| N/A |
| **E**| 240.0.0.0 to 255.255.255.255 | N/A | N/A| N/A| N/A |

*2 is subtracted from the Total Number of Networks and Total Number of Clients because one address is always reserved for the network itself, and one for the broadcast address*

* Class D: used for multicast groups; not used in traditional networks.
* Class E: used for experimental purposes; not used in traditional networking. 

`Loopback Range`

| IP Class | IP Range| Subnet Mask| Total Number of Networks | Total Number of Clients   |
|:-:|:-:|:-:|:-:|:-:|
|**Loopback**| 127.0.0.0 to 127.255.255.255|255.0.0.0|N/A|N/A|

<br>

`Broadcast Addresses`  
A `Broadcast Address` is used to send packets to the entire network.
* Broadcast Addresses are typically the last address in the network and end with .255.

<br>


`Commonly Used IPv4 Addresses`  
* Loopback: `127.0.0.1`  
* Home Router Private IP:   
    * `192.168.0.1` OR `192.168.1.1` OR `192.168.0.254` OR `192.168.1.254` 
* Home Network Broadcast IP: `192.168.0.255` OR `192.168.1.255`



<br>

[Back To Top](#internet-protocol-addresses)
___

<br>

# `IPv6 128-bit addresses`

*IPv6 was designed to accommodate the ever-growing number of internet-connected devices and ensure that we don't run out of IP addresses, which occured with IPv4.*

`IPv6 addresses` use eight 16-bit hexadecimal numbers separated by a colon ( : ). 
* Total Range of IPv6 addresses:
``` 
0000:0000:0000:0000:0000:0000:0000:0000 <--> FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
```
* There are 2<sup>128</sup> (340,282,366,920,938,463,463,374,607,431,768,211,456) possible addresses in the IPv6 Protocol.

<br>

Format:
> x = 16 bit (2 byte) hexadecimal number between 0000 and FFFF

    x:x:x:x:x:x:x:x

Colon Hexadecimal Format Example:

    2001:0db8:85a3:0000:0000:8a2e:0370:7334

Binary Format Example:
> Each group of four hexadecimal digits is converted to a 16-bit binary number.
```
0010000000000001 0000110110111000 1000010110100011 0000000000000000 0000000000000000 1000101000101110 0000001101110000 0111001100110100
```

---
## `Shortening IPv6 Addresses`

`Leading Zeros Omission:`
* Leading zeros in each 16-bit group can be omitted. 

For Example:

    2001:0db8:0045:00ab:0000:00cd:0012:0ef0

> can be shortend to 

    2001:db8:45:ab::cd:12:ef0

<br>

`Zero Compression:`  
* If one or more consecutive 16-bit group contains only zeros, they can be replaced with a double colon ( :: ). 
* This can only be done once in an address to avoid ambiguity. 

<br>

For Example:

    2001:0db8:0000:0000:0000:0000:1428:57ab 

> can be shortened to 

    2001:db8::1428:57ab

# `IPv6 Ranges`
*IPv6 does not have classes like IPv4 addresses do, but there are still specific addresses used for networking*

`Global Unicast Addresses (GUA)`
Globally unique addresses that can be routed on the public internet. 
> * Equivalent to public IPv4 addresses.
> * Range: 2000::/3 (from 2000:: to 3FFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF)

<br>

`Link-Local Addresses`
Link-Local Addresses are used for communication within a single network segment (link) and are not routable beyond that link. 
> * Automatically configured on all IPv6-enabled interfaces.
> * Range: FE80::/10 (from FE80:: to FEBF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF)

<br>

`Unique Local Addresses (ULA)`
These addresses are similar to private IPv4 addresses (e.g., 192.168.0.0/16, 10.0.0.0/8). 
> * Unique Local Addresses are used for local communication within an organization and are not routable on the public internet.
> * Range: FC00::/7 (from FC00:: to FDFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF)

<br>

`Multicast Addresses`
These addresses are used to send a single packet to multiple destinations (a group of interfaces). 
> * Used in applications like streaming video or routing protocols.
> * Range: FF00::/8 (from FF00:: to FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF)

<br>

`Anycast Addresses`
Anycast addresses are assigned to multiple interfaces, usually on different devices. 
> * Packets sent to an anycast address are delivered to the nearest interface, as determined by the routing protocol.
> * No specific range; any unicast address can be used as an anycast address.

<br>

`Reserved Addresses`
These are special-purpose addresses. ::/128 is used when a device does not have an address assigned, and ::1/128 is used for loopback operations, allowing a device to send packets to itself.
> * `Unspecified Address: ::/128` 
> * `Loopback Address: ::1/128`


<br>

[Back To Top](#internet-protocol-addresses)
___

<br>

# `Public vs. Private IP Addresses`

`Public IP Addresses` are assigned to devices that are directly accessible from the internet.
> * Typically a router is assigned a Public IP address by an Internet Service Provider (ISP).
> * Public IPs must be unique across the entire internet. Uniqueness is managed by organizations like the Internet Assigned Numbers Authority (IANA) and regional internet registries. 

<br>

`Private IP Addresses` are used within local networks for communication and are not directly accessible from the internet.
> * Typically a router will assign a Private IP address to each device on its network. 
> * Private IPs are not unique across the internet, and are typically reused by separate local networks.

<br>

`Network Address Translation (NAT)` translates Private IPs to Public IPs when data is sent out and Public IPs to Private IPs when data is recieved. 

<br>

[Back To Top](#internet-protocol-addresses)
___

<br>

# `Static vs. Dynamic IP Addresses`

`Static IP Address`: a fixed addresses assigned to a device that has to be manually set and manually changed.
> * Does not change unless an administrator changes the address manually.
> * A home router can be configure to assign static IPs. 
> * A router can be assigned a static IP from an ISP. 

<br>

`Dynamic IP addresses`: an address assigned by the `Dynamic Host Configuration Protocol (DHCP)` server and can change periodically.
> * Devices are assigned an address from an address pool managed by the DHCP server.
> * A home router typically includes a DHCP server. 
> * ISPs typically assign routers public IPs using DHCP. 

<br>

[Back To Top](#internet-protocol-addresses)
___

<br>

# `IP Addresses and Ports`

*Ports are defined by the Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP) at the Transport layer of the OSI and TCP/IP models.*

A `Port` serves as a communication endpoint for applications and services on a device. It helps in directing data to the correct application or service by providing a unique number associated with that service.

A `Port Number` is a 16-bit integer ranging from 0 to 65535, and is used to uniquely identify a service or application on a device.

Ports are specified in IP addresses by using a `colon (:)` to separate the IP address from the port.

<br>

IPv 4 Example:

    192.168.0.1:80

`:80` is the port

<br>

IPv6 Example:

    2001:db8:85a3::8a2e:370:7334:80

`:80` is the port


<br>

[Back To Top](#internet-protocol-addresses)
___

<br>

# `Subnetting`
`Subnetting` is the process of dividing a larger network into smaller, more manageable sub-networks or subnets. 
> * It helps optimize network performance and improve security by isolating different segments of a network.

<br>

`Subnet Masks` are used in conjunction with IP addresses to define the network and host portions of an address. 
> * They help determine which part of an IP address represents the network and which part represents the host within that network.
> * A `subnet mask` consists of four 8-bit numbers, just like an IP address, and it consists of a series of contiguous 1s followed by a series of contiguous 0s.

<br>

`Classless Inter-Domain Routing(CIDR) Notation`: is a compact representation of a subnet mask and specifies the number of bits used for the network portion of the IP address.
> * For example /24 indicates that the first 24 bits are 1s 
>    * /24 --> 255.255.255.0 --> 11111111.11111111.11111111.00000000

Common Subnets:
|CIDR Notation|Decimal Subnet Mask|Binary Subnet Mask|
|:-:|:-:|:-:|
|/8|255.0.0.0|11111111.00000000.00000000.00000000|
|/16|255.255.0.0|11111111.11111111.00000000.00000000|
|/24|255.255.255.0|11111111.11111111.11111111.00000000|
|/32|255.255.255.255|11111111.11111111.11111111.11111111|

<br>

`Network Portion`: the  1s define the bits used to identify the network portion of the IP address

`Host Portion`: the 0s define the bits used to identify the host portion of the IP address

`Applying a Subnet Mask`  
*A subnet mask is applied to an IP address using a Bitwise AND operation*
Examples
```
    11000000.10101000.00000001.00001010   (IP Address)
AND
    11111111.11111111.11111111.00000000   (Subnet Mask)
-----------------------------------------------------
    11000000.10101000.00000001.00000000   (Network Address)
```
```
    10101100.00010000.00000101.00010100   (IP Address)
AND
    11111111.11111111.11111100.00000000   (Subnet Mask)
-----------------------------------------------------
    10101100.00010000.00000100.00000000   (Network Address)
```
```
    00001010.00000000.00000011.01001101   (IP Address)
AND
    11111111.11111111.11111111.11110000   (Subnet Mask)
-----------------------------------------------------
    00001010.00000000.00000011.01000000   (Network Address)
```
```
    11000000.10101000.01100100.00100011   (IP Address)
AND
    11111111.11111111.11111111.11000000   (Subnet Mask)
-----------------------------------------------------
    11000000.10101000.01100100.00000000   (Network Address)
```

<br>


`Calculating Number of Subnets`:  
*Subnet masks are also called prefixes especially in the use of CIDR notation*  

### 2<sup>(new mask bits - old mask bits)</sup>

Example:
> Original network is 192.168.0.1/8 and the new will be 192.168.0.1/15

2<sup>15-8</sup> =  2<sup>7</sup> subnets

<br>

`Calculating Number of Hosts`:  

### 2<sup>(32 - mask bits)</sup>

Example:
> The network is 192.168.0.1/17

2<sup>32-17</sup> =  2<sup>15</sup> hosts per subnet

<br>

Subnetting Examples:

### 1. You have the IP address block 10.0.0.0/8 and need to create subnets for different departments in an organization. You decide to use a /16 subnet mask to create multiple smaller subnets.


Original Network:
|Network Address| CIDR Notation|Subnet Mask|Total Useable IP addresses|
|:-:| :-:|:-:|:-:|
|10.0.0.0|/8|255.0.0.0| 16,777,214 (2<sup>24</sup>-2)|

New Subnet Mask:
|Network Address|CIDR Notation|Subnet Mask|Total Subnets|Total Host IPs per subnet|
|:-:|:-:|:-:|:-:|:-:|
|10.0.0.0|/16|255.255.0.0| 256 (2<sup>16-8</sup>)| 65534 (2<sup>32-16</sup>-2)|


Subnets:
| Subnet Address | CIDR Notation | Broadcast IP     | Usable Host IP Range          |
|----------------|---------------|------------------|-------------------------------|
| 10.0.0.0       | /16           | 10.0.255.255     | 10.0.0.1 to 10.0.255.254      |
| 10.1.0.0       | /16           | 10.1.255.255     | 10.1.0.1 to 10.1.255.254      |
| 10.2.0.0       | /16           | 10.2.255.255     | 10.2.0.1 to 10.2.255.254      |
| 10.3.0.0       | /16           | 10.3.255.255     | 10.3.0.1 to 10.3.255.254      |
| 10.4.0.0       | /16           | 10.4.255.255     | 10.4.0.1 to 10.4.255.254      |
| 10.5.0.0       | /16           | 10.5.255.255     | 10.5.0.1 to 10.5.255.254      |
| 10.6.0.0       | /16           | 10.6.255.255     | 10.6.0.1 to 10.6.255.254      |
| 10.7.0.0       | /16           | 10.7.255.255     | 10.7.0.1 to 10.7.255.254      |
| 10.8.0.0       | /16           | 10.8.255.255     | 10.8.0.1 to 10.8.255.254      |
| 10.9.0.0       | /16           | 10.9.255.255     | 10.9.0.1 to 10.9.255.254      |
|...||...||...||...|
| 10.255.0.0       | /16           | 10.255.255.255     | 10.255.0.1 to 10.255.255.254      |



<br>

### 2. You have the IP address block 192.168.0.0/16 and need to create subnets for different departments in an organization. You decide to use a /20 subnet mask to create multiple smaller subnets.

Original Network:
|Network Address| CIDR Notation|Subnet Mask|Total Useable IP addresses|
|:-:| :-:|:-:|:-:|
|192.168.0.0|/16|255.255.0.0|65534 (2<sup>16</sup>-2)|

New Subnet Mask:
|Network Address|CIDR Notation|Subnet Mask|Total Subnets|Total Host IPs per subnet|
|:-:|:-:|:-:|:-:|:-:|
|192.168.0.0|/20|255.255.240.0| 16 (2<sup>20-16</sup>)| 4094 (2<sup>32-20</sup>-2)|

Subnets:
|Number| Subnet Address | CIDR Notation | Broadcast IP     | Usable Host IP Range  |
|:-:|:----------------|:---------------:|:------------------:|:-----------------------------:|
|1| 192.168.0.0     | /20           | 192.168.15.255   | 192.168.0.1 to 192.168.15.254 |
|2| 192.168.16.0    | /20           | 192.168.31.255   | 192.168.16.1 to 192.168.31.254|
|3| 192.168.32.0    | /20           | 192.168.47.255   | 192.168.32.1 to 192.168.47.254|
|4| 192.168.48.0    | /20           | 192.168.63.255   | 192.168.48.1 to 192.168.63.254|
|5| 192.168.64.0    | /20           | 192.168.79.255   | 192.168.64.1 to 192.168.79.254|
|6| 192.168.80.0    | /20           | 192.168.95.255   | 192.168.80.1 to 192.168.95.254|
|7| 192.168.96.0    | /20           | 192.168.111.255  | 192.168.96.1 to 192.168.111.254|
|8| 192.168.112.0   | /20           | 192.168.127.255  | 192.168.112.1 to 192.168.127.254|
|9| 192.168.128.0   | /20           | 192.168.143.255  | 192.168.128.1 to 192.168.143.254|
|10| 192.168.144.0  | /20           | 192.168.159.255  | 192.168.144.1 to 192.168.159.254|
|11| 192.168.160.0  | /20           | 192.168.175.255  | 192.168.160.1 to 192.168.175.254|
|12| 192.168.176.0  | /20           | 192.168.191.255  | 192.168.176.1 to 192.168.191.254|
|13| 192.168.192.0  | /20           | 192.168.207.255  | 192.168.192.1 to 192.168.207.254|
|14| 192.168.208.0  | /20           | 192.168.223.255  | 192.168.208.1 to 192.168.223.254|
|15| 192.168.224.0  | /20           | 192.168.239.255  | 192.168.224.1 to 192.168.239.254|
|16| 192.168.240.0  | /20           | 192.168.255.255  | 192.168.240.1 to 192.168.255.254|



<br>

[Back To Top](#internet-protocol-addresses)
___

<br>

# `Assigning IP Addresses: DHCP`

`Dynamic Host Configuration Protocol (DHCP)`, is a network management protocol used to automatically assign IP addresses and other network configuration parameters to devices on a network. 
> * DHCP uses `Media Access Control (MAC)` addresses to identify devices on a network. 
> * Assigned IP addresses are mapped to these MAC addresses. 
> * Typically associated with a router

<br>

How DHCP works at a High Level:

1. `Discovery`: When a device (client) connects to a network, it sends out a DHCP Discover message. This message is a broadcast request for a DHCP server to provide network configuration information.  

2. `Offer`: A DHCP server on the network receives the Discover message and responds with a DHCP Offer message. This message includes an IP address that the server is offering, along with other configuration details like the subnet mask, default gateway, and DNS server addresses.  

3. `Request`: The client receives the Offer and sends back a DHCP Request message to the server, indicating that it has accepted the offered IP address and configuration.  

4. `Acknowledgment`: The DHCP server receives the Request and responds with a DHCP Acknowledgment message. This message confirms that the client can use the offered IP address and includes the full set of configuration details.  

5. `Lease`: The IP address provided by the DHCP server is assigned to the client for a specific period called the lease time. Before the lease expires, the client must renew it if it still needs the IP address.  

6. `Renewal`: The client periodically sends DHCP Request messages to renew its lease. The server responds with an Acknowledgment if it is able to extend the lease.  

<br>

[Back To Top](#internet-protocol-addresses)
___

<br>

# `How Do I see my Public IP? Private IP?`

The simplest what to see your public IP is to go to got to a website like this one [whatismyip.com](https://www.whatismyip.com/)

For Private IPs:

Windows CMD
```
ipconfig
```
> This will display the IP configuration for all network adapters. Look for the section corresponding to your active network adapter, where you will see the private IP address listed under "IPv4 Address."

<br>

Windows Powershell
```
Get-NetIPAddress | Select-Object IPAddress, InterfaceAlias
```

<br>

Linux/MacOS
```
ip addr show
```

> Find the network interface you’re interested in (e.g., eth0, wlan0, etc.). The private IP address will be listed under inet.


<br>

___

[Back To Top](#internet-protocol-addresses)

<br>


# `Translating Web Addresses to IP Addresses: DNS`

`Domain Name System (DNS)` is a hierarchical and decentralized naming system used to translate `human-readable domain names (like www.example.com)` into `machine-readable IP addresses (like 192.0.2.1)` and vice versa. 
*  `DNS` enables users to access resources on the internet without needing to memorize numerical IP addresses.
*  `DNS` Translates Uniform Resource Locators (URLs or Web Addresses) into IP addresses. 

<br>

How DNS Works at a High Level:

1. `Query Initiation (Client Request)`: When a user enters a domain name into a browser or application, the client device generates a DNS Query to resolve the domain name into an IP address. This query is sent to the configured DNS resolver (usually provided by the user's ISP or a public DNS service).

1. `Resolver Request` :The DNS Resolver (Recursive Resolver) receives the query and determines how to fulfill it. If the resolver doesn’t already have the IP address cached, it forwards the request to the appropriate DNS servers in the hierarchy.

1. `Root Server Lookup`: The resolver queries a Root DNS Server, which responds with the address of a Top-Level Domain (TLD) DNS Server based on the domain extension (e.g., .com, .org, .net).

1. `Top Level Domain (TLD) Server Lookup` : The resolver queries the TLD Server, which provides the address of the Authoritative Name Server for the specific domain.

1. `Authoritative Server Response`: The resolver queries the Authoritative Name Server, which holds the DNS records for the requested domain. This server provides the IP address (or other requested information, like MX records for email).

1. `Response to Client`: The DNS Resolver sends the IP address back to the client. The client can then use this IP address to establish a connection with the target server.

1. `Caching`: To optimize performance, the resolver and client device cache the DNS response for a specified duration (TTL—Time to Live). This reduces the need for repeated queries for the same domain.

<br>

Key DNS Record Types:

| Record Type | Description                                    |
|-------------|------------------------------------------------|
| `A`           | Maps a domain name to an IPv4 address.        |
| `AAAA`        | Maps a domain name to an IPv6 address.        |
| `CNAME`       | Points one domain to another (aliasing).      |
| `MX`          | Identifies mail servers for a domain.         |
| `NS`          | Specifies the authoritative name servers for a domain. |
| `TXT`         | Holds text information, often used for verification purposes. |





<br>

[Back To Top](#internet-protocol-addresses)
___

<br>

*Created and maintained by Mr. Merritt*
