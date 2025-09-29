# `Network Cabling`


<br>

---

<br>


Covered in this file:
1. [``]()


<br>

[Back To Top](#network-cabling)

---
<br>


# ``

<br>

[Back To Top](#network-cabling)

---
<br>



Transmission Characteristics

`Bandwidth` is the theoreticaly amount of data that could be transmitted during a given period of time through a given medium.

`Throughput` aka payload rate or effective data rate is the measure of how much actual data is transmitted during a given period of time through a medium.


`Bit rate` is the rate of data transmission expressed in bits transmitted per second.
* `Bits per second` or `bps`
* Standard metric prefixes can be applied. 


| Prefix | Name      | Abbreviation | Power of 10 | Value in bps           |
|--------|-----------|--------------|-------------|-------------------------|
| (none) | Bit       | bps          | 10⁰         | 1 bps                   |
| kilo   | Kilobit   | kbps         | 10³         | 1,000 bps               |
| mega   | Megabit   | Mbps         | 10⁶         | 1,000,000 bps           |
| giga   | Gigabit   | Gbps         | 10⁹         | 1,000,000,000 bps       |
| tera   | Terabit   | Tbps         | 10¹²        | 1,000,000,000,000 bps   |


Important NOTE:
In data storage bytes(B) and binary prefixes are used 2<sup>n</sup>. eg. KB is 2<sup>10</sup> bytes or 1024 bytes.
In data transmission bits (b) and decimal prefixes are used 10<sup>n</sup>. eg. Kbps is 10<sup>3</sup> bits per second or 1000 bits per second.


`Noise` degrades and distorts signals on a network and is measured in decibels dB
Common Sources of noise:
* `Electromagnetic Interference (EMI)`
    * `Radio Frequency Interference RFI` is a type of EMI caused by radio waves. EMI is sometimes referred to as EMI/RFI.
    * Motors, power lines, televisions, copiers, fluorescent lights, microwave ovens, manufacturing machines, thunderstorms, and other source of electrical activity can cause EMI
    * Strong radio broadcast signals from radio or TV antennas can generate RFI.
* `Crosstalk` occurs when a signal from one wire crosses to another wire or cable.
    * `Alien crosstalk` occurs between two cables
    * `NEXT` (near end crosstalk) occurs between wire pairs near the source of a signal
    * `FEXT` (far end crosstalk) occurs between wire pairs at the far end of the cable from the signal source. 

Noise is unavoidable, but can be minimized and overcome.

<br>

`Attenuation` is the loss of a signal's strength as it travels away from its source.
* Signals are often boosted using a `repeater`

A `repeater` is a device used to regenerate a digital signal in its original form.
* A switch on an Ethernet network acts as a multi-port repeater.

Latency:
* The length of a cable affects latency
* Intervening connecting devices such as routers and switches also affect latency.

Round Trip Time is the time it takes for a packet to go from sender to receiver, then back from receiver to sender. 
* Usually measured in milliseconds ms
* Most common way to measure latency

`Jitter` aka `packet delay variation PDV` is a transmission flaw caused by packets experiencing varying amounts of delay and therefore arriving out of order.


# Duplex, Half-Duplex, Simplex, Multiplexing   

`Duplex` aka `Full-Duplex` is a type of transmission in which signals may travel in `both directions` over a medium at the `same time`.

`Half-Duplex` is a type of transmission in which signals may travel in `both directions`, but ONLY `one direction at a time`.

`Simplex` is a type of transmission in which signals can ONLY `travel in one direction`.

<br>

`Speed and Duplex Mismatch` is a problem that occurs when neighboring devices are using different speed or duplex configurations and results in failed transmissions.

`Multiplexing` is a type of transmission that allows for multiple signals to travel at the same time over one medium.
* A multiplexer mux is required on the transmission end to combine signals on a channel.
* A demultiplexer demux is required on the receiving end and separates the combined signals. 

`Time Division Multiplexing TDM` is a method of multiplexing that assigns a time slot in the flow of communications to every node on the network and, in that time slot, carries data from that node. 

`Statistical Time Division Multiplexing STDM` is a type of multiplexing that assigns time slots to nodes but then adjusts these slots according to the priority and need. 

`Frequency Division Multiplexing FDM` is a type of multiplexing that assigns a unique frequency band to each communications subchannel. Signals are modulated with different carrier frequencies, then multiplexed to simultaneously travel over a single channel. 

`Wavelength Division Multiplexing WDM` is a type of multiplexing that assigns each signal on a fiber-optic cable to a different wavelength, which equates to its own subchannel.

* `Dense wavelength division multiplexing  DWDM` is a type of multiplexing that is used over single and multimode fiber optic cable in which each signal is assigned a different wavelength for its carrier wave. 

* `Coarse Wavelength Division Multiplexing CWDM` is a type of multiplexing that is used over single and multimode fiber optic cable in which each signal is assigned a different wavelength for its carrier wave. However, each frequency band is spaced further apart to reduce cost of transceiver equipment.


# Copper Cabling

### Coaxial
`Coaxial Cable` or `coax` is a type of cable that consists of a central metal conducting core, surrounded by an insulator, shielding, and an outer cover. 

Specifications:
| Cable Type | Impedance (Ohms) | Core Material                  | Core Diameter | Shielding Type           | Typical Uses                                      |
|------------|------------------|--------------------------------|----------------|---------------------------|---------------------------------------------------|
| `RG-59`      | 75               | Copper-clad steel or solid copper | ~0.64 mm (22 AWG) | Single or dual braid       | Short-distance analog video, CCTV, baseband video |
| `RG-6`       | 75               | Copper-clad steel or solid copper | ~1.02 mm (18 AWG) | Dual or quad shielding     | Digital TV, satellite, broadband Internet, HDTV   |


<br>

Connector Types:
| Connector Type | Impedance (Ohms) | Typical Cable Types | Locking Mechanism     | Common Uses                                 |
|----------------|------------------|----------------------|------------------------|----------------------------------------------|
| `F-connector`    | 75               | RG-59, RG-6          | Screw-on              | Cable TV, satellite, cable modems            |
| `BNC` <br> Bayonet Neill-Concelman <br> or <br> British Naval Connector            | 50 or 75         | RG-58, RG-59, RG-6   | Bayonet (twist-lock)  | CCTV, test equipment, broadcast video, RF    |


<br>

### Twisted Pair Cable

`Twisted Pair Cable` is a type of cable similar to telephone wiring that consists of color-coded pairs fo insulated copper wires, each with a diameter of 0.4 to 0.8 mm. Every two wires are twisted around each other to form pairs, and all the pairs are encased in a plastic sheet.
* In ethernet networks twisted pair cable contains `4 wire pairs`.
* On `Fast Ethernet networks` (100 Mbps max) one pairs transmits, one pair receives, and the other two are not used for transmission.
* On `Gigabit Ethernet` (1000 Mbps min) and higher, all four pairs are used for transmitting and receiving.
* Maximum segment length on an Ethernet network (supporting 1 Mbps - 10 Gbps) is 100 m (328 ft).

<br>

`Twist Ratio` is the number of twists per meter or foot of cable.
* More twists per unit distance makes the wire pair more resistant to crosstalk and noise.
* More twists also means more cable is required and greater attenuation.
* Balancing these two factors is important for cable manufactures. 

Twisted Pair Cable Standards <br>
`TIA/EIA 568 standard` divides twisted pair cabling into several categories.

| Category | Max Throughput       | Bandwidth / Signal Rate | Description                                                                 |
|----------|----------------------|--------------------------|-----------------------------------------------------------------------------|
| Cat 3    | 10 Mbps              | 16 MHz                   | Used in early Ethernet and telephone lines; obsolete for modern networks.   |
| Cat 5    | 100 Mbps             | 100 MHz                  | Supports 100BASE-T; largely replaced by Cat 5e.                             |
| Cat 5e   | 1 Gbps               | 100 MHz                  | Enhanced Cat 5; reduced crosstalk, supports Gigabit Ethernet.              |
| Cat 6    | 1 Gbps (10 Gbps up to 55m) | 250 MHz         | Tighter specs than Cat 5e; supports 10GBASE-T over short distances.        |
| Cat 6a   | 10 Gbps              | 500 MHz                  | Augmented Cat 6; improved shielding, supports 10GBASE-T up to 100m.        |
| Cat 7    | 10 Gbps              | 600 MHz                  | Individually shielded pairs and overall shield; supports high-speed LANs.  |
| Cat 7a   | 10 Gbps (up to 40-100 Gbps for short range) | 1000 MHz       | Extended version of Cat 7; supports higher frequencies and advanced shielding. |

Modern LANs uses Cat 5e or better wiring in order to support Gigabit networks.

<br>

`Shielded Twisted Pair STP` is a type of copper based cable containing twisted-pair wires that are both individually insulated and surrounded by a shielding made of a metallic substance such as foil. 
* typically more expensive than UTP

Effectiveness of STP depends on:
* amount and type of environmental noise
* shield material thickness
* grounding mechanism
* symmetry and consistency of shielding


<br>

`Unshielded Twisted Pair UTP` is a type of copper based cable containing insulated twisted pair wires contained in a plastic sheath.
* No additional shielding

<br>

Twisted Pair Connecters
| Connector Type | Number of Pins | Typical Cable Types | Common Uses                          | Size Comparison        |
|----------------|----------------|----------------------|--------------------------------------|-------------------------|
| `RJ-45`          | 8 (4 pairs)    | Cat 5, 5e, 6, 6a, 7   | Ethernet networking, LAN, IP cameras | Larger (wider)         |
| `RJ-11`          | 4 or 6 (2 or 3 pairs) | Telephone cable       | Landline telephony, DSL             | Smaller (narrower)      |



Cable Pinouts

Proper cable termination is important for network performance. 

TIA/EIA has two standards for cable termination with Rj-45 plugs.
* TIA/EIA 568A (T568A) typically used for government networks
* TIA/EIA 568B (T568A) typically used for home and business networks

`Pinouts` show the pin numbers and color coded wire assignments used when terminating a cable or installing a jack, as determined by the TIA/EIA standard. 

`TIA/EIA 568A`
```
============================================================================+
Pin 8 --------------- Brown Solid       ]------------+                     
Pin 7 --------------- White Brown       ] Brown Pair |                      
                                                                            
Pin 6 --------------- Orange Solid      ]---------------+-------------+    
                                                        | Orange Pair |    
Pin 5 --------------- White Blue        ] ----------+   |                  
Pin 4 --------------- Blue Solid        ] Blue Pair |   |  
                                                        |   
Pin 3 --------------- White Orange      ]---------------+ 

Pin 2 --------------- Green Solid       ]------------+ 
Pin 1 --------------- White Green       ] Green Pair |
=============================================================================+
```
`TIA/EIA 568B`
```
============================================================================+
Pin 8 --------------- Brown Solid       ]------------+                     
Pin 7 --------------- White Brown       ] Brown Pair |                      
                                                                            
Pin 6 --------------- Green Solid       ]---------------+-------------+    
                                                        | Green Pair  |    
Pin 5 --------------- White Blue        ] ----------+   |                  
Pin 4 --------------- Blue Solid        ] Blue Pair |   |  
                                                        |   
Pin 3 --------------- White Green       ]---------------+ 

Pin 2 --------------- Orange Solid      ]-------------+ 
Pin 1 --------------- White Orange      ] Orange Pair |
=============================================================================+
```
* `Transmission --> TX` 
* `Receive --> RX`

| Pin # | Color (568A)   | Color (568B)   | Fast Ethernet Function | Gigabit Ethernet Function       |
|-------|----------------|----------------|-------------------------|---------------------------------|
| 1     | White/Green    | White/Orange   | TX+                     | Bi-directional (Pair A)         |
| 2     | Green          | Orange         | TX−                     | Bi-directional (Pair A)         |
| 3     | White/Orange   | White/Green    | RX+                     | Bi-directional (Pair B)         |
| 4     | Blue           | Blue           | Unused                  | Bi-directional (Pair C)         |
| 5     | White/Blue     | White/Blue     | Unused                  | Bi-directional (Pair C)         |
| 6     | Orange         | Green          | RX−                     | Bi-directional (Pair B)         |
| 7     | White/Brown    | White/Brown    | Unused                  | Bi-directional (Pair D)         |
| 8     | Brown          | Brown          | Unused                  | Bi-directional (Pair D)         |

<br>

`Straight Through Cable` aka `Patch Cable` is a twisted pair cable in which the wire terminations in both connectors follow the same scheme.
* This is most common type of network cable.
* short section of cable (3 to 25ft) with connectors on both ends.

`Loopback adapters` or `loopback plugs` are troubleshooting tools that plug into a port  and crosses the transmission line with the receive line, allowing outing going signals to be redirected back into the computer for testing. 

<br>

`Crossover cable` is a legacy twisted pair patch cable in which the termination locations of the transmit and receive wires on one end of the cable are reversed as compared with the other end. 


`TX/RX reverse` is a problem caused by mismatched pinout standards, and results in near end crosstalk.

<br>

`Rollover Cable` aka `Console Cables` are used to connect a computer the the console port of a router. 
```
+========================================================+
Pin 8 --- Brown Solid       ...     White Orange --- Pin 8                     
Pin 7 --- White Brown       ...     Orange Solid --- Pin 7 
                                                                            
Pin 6 --- Green Solid       ...     White Green  --- Pin 6

Pin 5 --- White Blue        ...     Blue Solid   --- Pin 5     
Pin 4 --- Blue Solid        ...     White Blue   --- Pin 4

Pin 3 --- White Green       ...     Green Solid  --- Pin 3

Pin 2 --- Orange Solid      ...     White Brown  --- Pin 2 
Pin 1 --- White Orange      ...     Brown Solid  --- Pin 1
+========================================================+
```
| Pin (End A) | Pin (End B) |
|-------------|-------------|
| 1           | 8           |
| 2           | 7           |
| 3           | 6           |
| 4           | 5           |
| 5           | 4           |
| 6           | 3           |
| 7           | 2           |
| 8           | 1           |


<br>

Power over Ethernet PoE

`Power over Ethernet PoE` is the `IEEE 802.3af` standard that specifies a way of supplying electrical power (up to 15.4 watts) over twisted-pair ethernet connections. 
* `PoE+` is the `IEEE 802.3at` standard that allows for up to 25.5 watts
* Requires Cat 5 or better copper cable.


There are 2 types of PoE standard devices:
* `Power Sourcing Equipment PSE` a device that supplies the power
* `Powered Devices PD` devices that receive power from PSE


Ethernet Standards for Twisted-Pair Cabling
| Standard     | Max Transmission Speed | Max Distance per Segment | Physical Media         | Pairs of Wires Used for Transmission |
|--------------|------------------------|---------------------------|------------------------|--------------------------------------|
| 10BASE-T     | 10 Mbps                | 100 meters                | Cat3 or higher UTP     | 2 pairs                             |
| 100BASE-T <br>100BASE-TX   | 100 Mbps               | 100 meters                | Cat5 or higher UTP     | 2 pairs                             |
| 1000BASE-T   | 1 Gbps                 | 100 meters                | Cat5e or higher UTP    | 4 pairs                             |
| 2.5GBASE-T   | 2.5 Gbps               | 100 meters                | Cat5e or higher UTP    | 4 pairs                             |
| 5GBASE-T     | 5 Gbps                 | 100 meters                | Cat5e (short) or Cat6  | 4 pairs                             |
| 10GBASE-T    | 10 Gbps                | 55–100 meters             | Cat6 (short) or Cat6a  | 4 pairs                             |



<br>

---

<br>

# `Fiber-Optic Cable`

`Fiber-optic cable` aka `fiber` contains one or several glass or plastic fibers at its center, or core.
* Extremely high throughput
* Very noise resistance
* Security
* Higher distance before repeating is required 2-40,000 m
* Most expensive transmission medium

The `core` is a cable's central component that is designed to carry a signal, such as glass or plastic fibers in fiber-optic cable or strand of copper in twisted-pair cable. 

Light is sent through a fiber cable using:
* a laser (Light Amplification by Stimulated Emition of Radiation)
* `Light-emitting diode (LED)` is a cool-burning, longlasting technology that creates light by the release of photons as electrons move through a semiconductor material


`Cladding` is the glass or plastic shield around the core of a fiber-optic cable. Cladding reflects light back to the core in patterns that vary depending on the transmission mode. 

`Optical Loss` is the degradation of a light signal on a fiber-optic network as it travels away from its source. 

<br>

`Single Mode Fiber SMF` is a type of fiber-optic cable with a narrow core of 8 to 10 microns in diameter that carries light pulses along a single path from one end of the cable to the other end.
* The internet backbone depends on single mode fiber.
* The cost of single mode fiber is relatively high, and is rarely used for short connections.

<br>

`Multimode Fiber MMF` is a type of fiber-optic cable containing a core that is usually 50 or 62.5 microns in diameter, over which many pulses of light generated by a laser or LED travel at different angles.




`Fiber Distribution Panel FDP` is a device on a rack where fiber cables converge, connect with each other, and connect with fiber-optic terminal equipment from the ISP. 
* Transition between SMF and MMF might occur here

Fiber Connectors:

The `ferrule` is the extended tip of a fiber optic cable connector that encircles the fiber strand to keep it properly aligned and ensure that is makes contact with the receptacle in a jack or other connector. 
* `Ultra Polished Connector UPC` is a type of ferrule in which the tip has been highly polished, thereby increasing the efficiency of the connection.
* `Angle Polished Connector` is a type of ferrule that uses the princples of reflection to its advantage by placing the edge faces of the highly polished ferrules at an angle to each other, thus reducing the effect of back reflection.


`Local Connector LC` is the most common type of 1.25mm ferrule connector, which is used with single-mode, fiber-optic cable.

`Subscriber Connector` or `Standard Connector SC` is a connector with a 2.5mm ferrule that is used with single-mode, fiber-optic cable.

`Straight Tip ST` is a connecter with a 2.5 mm ferrule that is used with single-mode, fiber-optic cable.

`Mechanical Transfer-Registered Jack MTRJ` is the most common type of connector used with multimode fiber-optic cable.


<br>

`Media Converters`

`Media converters` are devices that enable networks or segments running on different media to interconnect and exchange signals. 


`Fiber Transceivers`
Transceivers are a modular interface that can be inserted in a switch to connect its motherboard with an external fiber-optic cable. 

`Hot-Swappable` is a component that can be installed or removed without disrupting operations.


`Gigabit interface converter GBIC` is a standard type of modular interface that may contain RJ-45 or fiber-optic cable ports (such as LC, SC, or ST).  They are inserted into a socket ona connectivity device's backplane.



<br>

[Back To Top](#network-cabling)

___

<br>


*Created and maintained by Mr. Merritt*