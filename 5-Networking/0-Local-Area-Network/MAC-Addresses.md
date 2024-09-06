# `Media Access Control Addresses`

# `Network Interface Cards`

A `Network Interface Card (NIC)` is a hardware component that allows a computer or other device to connect to a network. 
> * The NIC facilitates communication between devices over a network by converting data from the device into a format that can be transmitted over the network and vice versa.

## Types of Network Interface Cards:
Ethernet NIC:
> Wired NIC: This is the most common type of NIC used in desktops and laptops for wired Ethernet connections. It connects to the network using an Ethernet cable (e.g., Cat5, Cat6).  
> Speed Variants: Comes in different speeds such as 10 Mbps, 100 Mbps (Fast Ethernet), 1 Gbps (Gigabit Ethernet), and even 10 Gbps.

<br>

Wireless NIC (Wi-Fi NIC):

> Wi-Fi NIC: These NICs enable wireless communication with a network. They are commonly used in laptops, smartphones, and other mobile devices. Wi-Fi NICs support various wireless standards like 802.11a/b/g/n/ac/ax.  
> Internal or External: Can be built into the device (internal) or added via a USB port or other external means.

<br>

Fiber Optic NIC:

> Fiber NIC: Used for high-speed network connections over fiber optic cables. These NICs are common in data centers and high-performance computing environments where high bandwidth and long-distance communication are required.  
> Speed and Distance: Supports very high speeds, often 10 Gbps, 40 Gbps, or more, and is capable of covering long distances.

<br>

USB NIC:

> USB to Ethernet/Wi-Fi Adapter: This type of NIC connects to a device via a USB port and provides Ethernet or Wi-Fi connectivity. It's useful for devices without built-in network interfaces or for adding additional network interfaces.

<br>

Bluetooth NIC:

> Bluetooth Adapter: Used for wireless communication over short distances, primarily for connecting peripheral devices like keyboards, mice, or speakers. Bluetooth NICs are often built into devices but can also be added externally via USB.

<br>

Virtual NIC:

> Virtual NIC: A software-based NIC used in virtualized environments, such as virtual machines. It provides network connectivity to virtual machines by emulating a physical NIC.

<br>

Combo NICs:

> Combo NICs: These are cards that support multiple types of network interfaces on a single card. For example, a card might offer both Ethernet and Wi-Fi capabilities.

---
# `MAC Addresses`

`Media Access Control (MAC) Addresses` is a unique 12 digit hexadecimal identifier assigned to a network interface card (NIC) for communications on the physical network segment. 
> * MAC addresses are used as a hardware address for devices in a local network.  
> * Each MAC address is unique to the device's network interface card, ensuring no two devices on the same local network share the same MAC address.  
> * MAC addresses operate at the Data Link Layer (Layer 2) of the OSI model. They are used to identify devices on a local network segment and are crucial for frame delivery in Ethernet and other similar networks.  

<br>

*MAC addresses are typically assigned by the manufacturer of the NIC and are burned into the hardware. However, they can sometimes be modified or spoofed via software.*

MAC addresses consist of six groups of two hexadecimal digits, separated by hyphens(-), colons(:), or no separator.
> * The first 6 (3 pairs) hexadecimal digits are the `Organizationally Unique Identifier (OUI) or Manufacturer ID` 
> * The last 6 (3 pairs) hexadecimal digits are the `Device ID`.
> * Range: 00-00-00-00-00-00 to FF-FF-FF-FF-FF-FF

Example:
`FF-FF-FF-00-00-00`
|Organizationally Unique Identifier (OUI)|Device ID|
|:-:|:-:|
|FF-FF-FF|00-00-00|

---
# `Address Resolution Protocol`

`Address Resolution Protocol (ARP)`, is a network protocol used to map an IP address to a MAC (Media Access Control) address within a local network. 
* ARP operates at the Data Link Layer (Layer 2) and is crucial for enabling devices to communicate over Ethernet and other similar network technologies.

## How ARP works at a high level:
1. ARP Request:
> When a device wants to communicate with another device on the same local network but only knows the IP address of the target device, it sends out an ARP request.  
> This ARP request is a broadcast message sent to all devices on the local network, asking "Who has IP address [target IP]? Please send me your MAC address."

<br>

2. ARP Reply:
> The device with the matching IP address responds with an ARP reply.
> This reply contains the MAC address associated with the requested IP address and is sent directly back to the requesting device.

<br>

3. ARP Cache:
> Once the requesting device receives the ARP reply, it stores the IP-to-MAC address mapping in its ARP cache for future reference.
> The ARP cache is a table in the device's memory that keeps track of IP addresses and their corresponding MAC addresses, reducing the need for repeated ARP requests.

<br>

4. Communication:
> With the MAC address now known, the requesting device can frame Ethernet packets addressed to the correct MAC address, enabling successful communication over the local network.


---
# `How do I see my MAC Address?`

Windows CMD 
```
ipconfig /all
```

> Look for the section corresponding to your network adapter. The MAC address is listed as "Physical Address."

<br>

Windows Powershell
```
Get-NetAdapter | Select-Object Name, MacAddress
```

> This command lists all network adapters with their names and MAC addresses.

<br>

Linux/MacOS
```
ip link
```

> Find the network interface you’re interested in (e.g., eth0, wlan0, etc.), and look for the MAC address next to link/ether.
---
