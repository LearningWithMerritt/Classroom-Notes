# `Wireless Communications`


<br>

---

<br>


Covered in this file:
1. [``]()


<br>

[Back To Top](#wireless-communications)

---
<br>


# ``

<br>

[Back To Top](#wireless-communications)

---
<br>



`Wireless Local Area Network WLAN ` is a LAN that uses wireless connections for some or all of its transmissions. 

`Wireless spectrum` commonly called airwaves is a spectrum of electromagnetic waves used for data and voice communication. 
* Defined by the Federal Communication Commission FCC
* bands aka frequency ranges between 9kHz and 300GHz are used for wireless technologies

| Technology          | Frequency Range           | Channels / Notes                                                             | Description                                                                 |
|---------------------|---------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| Infrared (IR)       | 300 GHz – 430 THz         | Not channelized; line-of-sight only                                          | Short-range, line-of-sight communication used in remote controls and data transfer. |
| Bluetooth           | 2.4 GHz                   | 79 channels (1 MHz spacing)                                                  | Short-range wireless communication standard for personal devices.          |
| Wi-Fi (2.4 GHz) <br> 802.11b/g/n | 2.4–2.5 GHz               | 14 channels (only 1, 6, 11 non-overlapping in most countries)               | Common wireless networking band; longer range but more interference.       |
| Wi-Fi (5 GHz) <br> 802.11a/n/ac  | 5.15–5.825 GHz            | 23+ channels (20/40/80/160 MHz widths, varies by region)                     | Higher-speed wireless networking; shorter range, less interference.        |
| Wi-Fi (6 GHz) <br> 802.11ax (Wi-Fi 6E) | 5.925–7.125 GHz           | Up to 59 channels (20 MHz)                                                  | Newer, high-performance band with more bandwidth and lower latency.        |
| Zigbee              | 868 MHz / 915 MHz / 2.4 GHz | 16 channels (2.4 GHz band: channels 11–26)                                   | Low-power protocol for IoT and home automation applications.              |
| Z-Wave              | 868.42 MHz / 908.42 MHz   | Fixed per region (e.g., 868.42 MHz in EU, 908.42 MHz in US)                 | Smart home wireless communication; longer range than Zigbee.              |
| NFC                 | 13.56 MHz                 | Single frequency; no channelization                                          | Near Field Communication for very short-range (a few cm) data exchange.    |
| RFID (Low Freq)     | 125–134 kHz               | No standard channelization                                                   | Used in access cards and animal tracking; low data rate, short range.      |
| RFID (High Freq)    | 13.56 MHz                 | Single frequency; ISM band                                                   | Used in library systems, passports, and ticketing.                         |
| RFID (UHF)          | 860–960 MHz               | Region-specific sub-bands (e.g., 902–928 MHz in US)                          | Longer-range RFID for inventory tracking and logistics.                    |
| LoRa                | 433 MHz / 868 MHz / 915 MHz | Region-specific (e.g., 868 MHz EU, 915 MHz US)                              | Long-range, low-power communication for IoT applications.                 |
| Cellular (3G)       | 850 MHz – 2.1 GHz         | Multiple bands (Band 1–22+, region-dependent)                               | Mobile broadband and voice for smartphones.                                |
| Cellular (4G LTE)   | 600 MHz – 3.8 GHz         | Dozens of LTE bands (Band 1–88, region-dependent)                           | High-speed mobile broadband with global frequency variations.              |
| Cellular (5G)       | 600 MHz – 52.6 GHz        | NR Bands: n1–n79 (FR1), n257–n261 (FR2, mmWave)                             | Next-gen cellular; supports mmWave for ultra-fast speeds and low latency.  |
| Satellite (L-band)  | 1–2 GHz                   | Not channelized in the same way; operator-specific allocations               | Used for GPS, satellite phones, and marine navigation.                     |
| Satellite (Ka-band) | 26.5–40 GHz               | Depends on satellite system; high bandwidth                                 | High-bandwidth satellite communications and broadband internet.            |


<br>

#### `Bands are divided into channels and channels are divided into narrowband channels`

`Frequency Hopping Spread Spectrum FHSS` is a wireless signaling technique in which a signal jumps between several different frequencies within a band in a synchronization pattern known to the channel's receiver and transmitter. 

Frequency Hopping is a process performed by some wireless devices to help reduce interference by quickly hopping between frequencies within a given band of frequencies. 


`Direct Sequence Spread Spectrum DSSS` is a modulation technique that distributes lower-level signals over several frequencies simultaneously. 

Wi-Fi uses DSSS. In the US the FCC has defined:
11 channels for the 2.4GHz band
24 channels for the 5 GHz band
Each channel is 20 MHz wide.

`Access Point AP` is a device used on WLANs that accepts wireless signals from multiple nodes and retransmits them to the rest of the network. 


Bluetooth as defined in the IEEE  802.15.1 standard is a low-power wireless technology that provides close-range communication between devices such as PCs, smartphones, tablets, and accessories. 
* Bluetooth uses FHSS
* 79 channels for the Bluetooth band
* A piconet is a network of Bluetooth devices. 
* devices must be paired

| Class | Max Power Output | Typical Range       | Purpose / Use Case                                  |
|-------|------------------|---------------------|-----------------------------------------------------|
| Class 1   | 100 mW (20 dBm)     | Up to 100 meters      | Industrial, long-range devices, outdoor headsets     |
| Class 1.5 | 10 mW (10 dBm)      | Up to 20 meters       | Some mobile and embedded devices (less common)       |
| Class 2   | 2.5 mW (4 dBm)      | Up to 10 meters       | Most Bluetooth headsets, phones, laptops             |
| Class 3   | 1 mW (0 dBm)        | ~1 meter              | Short-range communication, very low power devices    |

Pairing is the process of two Bluetooth devices communicating with each other. 
| Step | Description                                                                                   |
|------|-----------------------------------------------------------------------------------------------|
| 1. Discovery         | Devices scan for nearby Bluetooth-enabled devices in pairing mode.              |
| 2. Initiation        | One device initiates a connection request to another discovered device.        |
| 3. Authentication    | Devices authenticate each other using a pairing method (e.g., PIN, passkey).   |
| 4. Encryption Setup  | A shared key is generated (e.g., link key or Long Term Key in BLE) to enable encrypted communication. |
| 5. Bonding (optional)| Devices store pairing information (keys) to allow future reconnections without repeating the process. |
| 6. Connection        | A secure communication channel is established, allowing data transfer.         |






Zigbee is based on the IEEE 802.15.4 standard and is a low-powered, battery conserving wireless technology that handles small amounts of data.
* Used in industrial, scientific, and medical sensors
* Used in IoT devices: building automation, HVAC control, Automatic Meter Reading AMR, and fleet management. 
* ZigBee uses DSSS
* 16 channels
* AES-128 bit encryption

Z-Wave is a smart home protocol that provides two basic types of functions: signaling, to manage wireless connections, and control, to transmit data and commands between devices.
* AES-128 bit encryption
* Up to 100m per hop, up to 4 hops through repeaters 


ANT+ is an open source wireless technology that gathers and tracks information from sensors typically embedded in heart rate monitors, GPS devices, and other activity monitoring devices. 
ANT+ uses a fixed frequency and therefore does not use DSSS or FHss



# `Antennas`

Antennas are hardware that are used for both the reception and transmission of wireless signals. 
* Radiation Pattern is the relative strength over a 3D area of all the electromagnetic energy an antenna sends or receives. 
* Unidirectional Antenna aka Directional Antenna is a type of antenna that issues wireless  signals along a single direction, or path. 
* Omnidirectional antenna is a type of antenna that receives wireless signals with equal strength and clarity in all directions.
* An antenna's range is the geographical area in which signals issued from an antenna or wireless system can be consistently and accurately received. 



Propagation is the way in which a wave travels from one point to another. 


Line of Sight LOS is a type of propagation where a wireless signal or path that travels directly in a straight line from its transmitter to its intended receiver. 

Wireless Propagation Phenomena:
| Phenomenon   | Description                                                                                   | Effects on Wireless Signals                                                  |
|--------------|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Fading       | Variation in signal strength over time or space due to multipath propagation or movement.     | Causes signal drops, distortion, or loss; common in mobile environments.     |
| Attenuation  | Gradual loss of signal power over distance or through materials (like walls or air).          | Reduces range and signal strength; more pronounced at higher frequencies.    |
| Interference | Disruption caused by overlapping signals from other devices or systems.                       | Degrades signal quality and causes data errors or connection drops.          |
| Refraction   | Bending of radio waves as they pass through media with different densities (e.g., air layers).| Alters signal path; can cause unexpected coverage areas or dead zones.       |
| Reflection   | Bouncing of waves off surfaces like buildings, walls, or the ground.                          | Can cause multipath propagation leading to fading or phase cancellation.     |
| Scattering   | Signal dispersion due to irregular surfaces or small objects (dust, foliage, rough walls).    | Leads to weaker, unpredictable signals and noise, especially at higher freqs.|
| Diffraction  | Bending of waves around obstacles or edges (e.g., buildings, terrain).                        | Enables signals to reach shadowed areas; lower frequencies diffract better.  |


`Wireless Range Extender` is a device that extends the reach of a wireless signal by repeating the signal from a closer broadcast point. 


`Signal to Noise Ratio SNR` the proportion of noise to the strength of a signal. 



The `Internet of Things IoT` is made up of any device connected to the internet. 


Wireless personal area network WPAN is defined in the IEEE 802.15 specification and is a purely wireless personal area network.
* 802.15.1 Bluetooth
* 802.15.3 High-Rate WPANs
* 802.15.4 Zigbee, Thread and low-rate WPAN protocols
* 802.15.6 Body Area Networks BANs used in medical and wearable devices. 



`Radio Frequency Identification RFID` is a wireless technology that uses electromagnetic fields to store data on a small chip in a tag, which includes an antenna that can both transmit and receive, and possible a battery.


| Term  | Description | Typical Use Case |
|--|--|--|
| `Active Reader Passive Tag` <br> `ARPT` | The reader actively sends out signals, while the passive tag responds using energy from the reader’s signal | Common in supply chain tracking and access control |
| `Passive Reader Active Tag` <br> `PRAT` | The reader listens passively for signals broadcasted by battery-powered active tags | Used in real-time location systems (RTLS) and long-range tracking |
| `Active Reader Active Tag` <br> `ARAT` | Both reader and tag are powered; the tag sends signals actively to the reader | Employed in high-value asset tracking and secure access systems |

<br>

`Near-Field Communication NFC` is a form of radio communication that transfer data wirelessly over very short distances.
* typically 10 cm or less

| Tag Type | Storage                      | Speed (kbps)     | Configuration                          |
|----------|------------------------------|------------------|----------------------------------------|
| Type 1   | 96 bytes – 2 KB              | 106              | Passive, simple protocol, low cost     |
| Type 2   | 48 bytes – 2 KB              | 106              | Passive, widely used, simple read/write|
| Type 3   | Up to 1 MB                   | 212 or 424       | Passive, complex protocol, fast data exchange |
| Type 4   | Up to 32 KB                  | 106, 212, 424    | Passive, supports encryption, configurable access |
| Type 5   | Up to 64 KB                  | 26.48            | Passive, ISO 15693-based, long-range   |


<br>

Based on  Ultra Wide Band radio platform UWB, W-USB products mimic wired USB 2.0 connections with similar speeds, security, ease of use, and compatibility.
* Transmit in the range between 2.1 and 10.6 GHz
* 2.4 and 5 GHz included or the WIGig protocols faster throughput in the 60 GHz band.
* Operates within 10 m

<br>

`Infrared or Infrared Radiation IR` is a wireless technology that uses a bandwidth just below the spectrum that is visible to the human eye, with longer wavelengths than red light. * * standards are defined by the `Infrared Data Association IrDA`

<br>

`Wi-Fi` is the set of IEEE standards and their amendments, extensions, and corrections for wireless networking.
* 802.11 Standards vary at the Physical Layer.

`MAC Sublayer` is the lower portion of the Data Link layer that is specifically involved with managing MAC addresses in message frames.

`Logical Link Control LLC Sublayer` is a sublayer of Layer 2 that is primarily concerned with multiplexing, flow and error control, and reliability.

| Standard | Frequency Band | Max Bandwidth     | Geographic Range         |
|----------|----------------|-------------------|--------------------------|
| 802.11b  | 2.4 GHz         | 11 Mbps           | ~35 meters (indoor) / ~140 meters (outdoor) |
| 802.11a  | 5 GHz           | 54 Mbps           | ~35 meters (indoor) / ~120 meters (outdoor) |
| 802.11g  | 2.4 GHz         | 54 Mbps           | ~38 meters (indoor) / ~140 meters (outdoor) |
| 802.11n  | 2.4 GHz / 5 GHz | 600 Mbps (theoretical) | ~70 meters (indoor) / ~250 meters (outdoor)   |
| 802.11ac | 5 GHz           | 1.3 Gbps (wave 1) – 6.9 Gbps (wave 2) | ~35 meters (indoor) / ~100 meters (outdoor) |


Access Methods
Wireless devices are not designed to transmit and receive simultaneously, and so cannot prevent collisions. 

`Carrier Sense Multiple Access with Collision Avoidance CSMA/CA` is a network access method used on 802.11 wireless networks. It minimizes the potential for collisions. 
1. Using CSMA/CA a node on an 802.11 network checks for existing wireless transmissions before it begins to send data.
    1. If the source node detects no transmission activity it waits a brief random amount of time and then sends its transmission
    1. If the source node does detect activity, it waits a brief period of time before checking again.

2. The destination nodes receives the transmission and, after verifying its accuracy, issues and ACK packet to the source.
    1. If the source receives this ACK, it assumes the transmission was properly completed. 
    1. Interference or other transmissions can impede this exchange. If the ACK is not received then the process starts over. 


`Request to Send/Clear to Send RTS/CTS` an exchange is which a source node requests the exclusive right to communicate with an access point and the access point confirms that it has granted that request.