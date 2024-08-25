

# `Ports`

Ports are defined by the Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP) at the 4th layer of the OSI model. 
A `Port` serves as a communication endpoint for applications and services on a device. It helps in directing data to the correct application or service by providing a unique number associated with that service.

A `Port Number` is a 16-bit integer ranging from 0 to 65535, and is used to uniquely identify a service or application on a device.

`Well-Known Ports`: Range from port 0 to port 1023 and are used by widely recognized services and protocols(ex. port 80 for HTTP, port 443 for HTTPS)

`Registered Ports`: range from port 1024 to port 49151, and are used by software applications that are not universally recognized but still need consistent port assignments.

`Dynamic/Ephemeral Ports`: ranges from port 49152 to port 65535, and are used temporarily by client applications for outgoing connections. These ports are assigned dynamically by the operating system. 


Incoming and Outgoing Connections:
Client applications use ephemeral ports for outgoing connections to servers. These ports are assigned by the operating system and are used for the duration of the connection.
Servers use specific port number assignments to list for incoming connection from clients. For example, a web server listens on port 80 for HTTP requests. 

TCP Ports:
TCP ports are used for connection oriented communication such as loading a webpage. 

UDP Ports:
UDP ports are used for connectionless communications such as streaming video. 