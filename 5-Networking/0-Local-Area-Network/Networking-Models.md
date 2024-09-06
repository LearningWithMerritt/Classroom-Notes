# `Networking Models`

`Networking models` are conceptual frameworks that describe how various networking protocols and technologies interact and operate to enable communication between devices on a network. These models help standardize and organize network functionalities, making it easier to design, implement, and troubleshoot network systems. 

Two primary networking models are widely used: the `OSI model` and the `TCP/IP model`.

---
# `Open Systems Interconnect Model`
The `OSI model` is a theoretical framework developed by the International Organization for Standardization (ISO) that divides network communication into seven distinct layers. Each layer has specific functions and interacts with the layers above and below it.

## `Open Systems Interconnect Model`
| Layer | Name | Description|
|:-:|:-:|:-|
| 7|Application|Provides network services directly to `applications`.|
| 6 | Presentation | Translates data between the application layer and the network format. It handles `encryption, compression, and data translation.` |
| 5 | Session| Manages `sessions or connections` between applications. It handles session establishment, maintenance, and termination. |
| 4 | Transport| Manages end-to-end communication, data integrity, and error recovery. |
| 3 | Network| Handles routing of data `packets` between devices across different networks. Uses `IP` addresses for addressing and routing. |
| 2 | Data Link| Provides node-to-node data transfer and error detection. Manages `MAC` addresses and frames data for transmission over the physical layer. |
| 1 | Physical | Deals with the physical connection between devices, including cables, switches, and electrical signals. Defines `hardware elements of a network`. |

---
# `Tranmission Control Protocol/Internet Protocol (TCP/IP)Model`

The `Transmission Control Protocol/Internet Protocol model (TCP/IP) model` is a framework used to describe and implement the protocols and standards that enable communication over the Internet and other similar networks. It was developed by the Department of Defense (DoD) in the 1970s as part of the ARPANET project and has since become the foundation for modern networking.

Current 5 Layer TCP/IP Model
|Layer|Number| Description |
|:-:|:-:|:-|
|5| Application|Provides network services directly to applications. Handles protocols like HTTP, FTP, SMTP.  |
|4| Transport | Manages end-to-end communication, data integrity, and error recovery|
|3| Network | Handles logical addressing, routing, and packet forwarding. Includes the IP protocol. |
|2| Data Link | Corresponds to the OSI model's Data Link layer. Manages data framing, error detection, and MAC addressing. |
|1| Physical| Corresponds to the OSI model's Physical layer. Deals with the physical connection between devices, including cables, switches, and electrical signals. |

<br>

Old 4 Layer TCP/IP Model
| Layer | Description |
|:-:|:-:|
| Application | Provides network services directly to applications. Handles protocols like HTTP, FTP, SMTP.|
| Transport | Manages end-to-end communication, data integrity, and error recovery. |
| Internet| Handles logical addressing, routing, and packet forwarding.  |
| Network Interface | Corresponds to the OSI model's Data Link and Physical layers. Manages data framing, MAC addressing, and physical transmission. |


---
# Mapping OSI and TCP/IP Together

| TCP/IP| OSI| Example Protocols/Services|
|:-:|:-:|:-:|
| Application | Application<br>Presentation<br>Session | HTTP, HTTPS, FTP, SMTP, IMAP, POP3, DNS, Telnet, SNMP|
| Transport | Transport | TCP, UDP |
| Network | Network | IP (IPv4, IPv6), ICMP, IGMP |
| Data Link | Data Link | Ethernet, Wi-Fi (IEEE 802.11), ARP, PPP|
| Physical| Physical| Ethernet cables (Cat5, Cat6), fiber optics, network interface cards (NICs) |
