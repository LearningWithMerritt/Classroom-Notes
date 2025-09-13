TODO:

Namespace Databases:
DNS follows a distributed database model, storing the DNS namespace data over thousands of servers. 

Namespace databases are stored in DNS zone files which store information in resource records. 
* Each resource begins with a TTL field that identifies how long the record should be saved in a cache or server.

[ICANN Registration Data Lookup Tool](https://lookup.icann.org/en)
Name Servers:
A `root server` is a DNS server maintained by ICANN and IANA that is an authority on how to conduct the top-level domains. ICANN oversees the operation of 13 clusters of root servers around the world.

Root servers connect to TLD servers which connect to Authoratative Servers

An `authoritative server` is the authority on computer names and their IP addresses for computers in their domains.
`DNS zone` is the part of a the DNS namespace for which one organization is assigned authority to manage.

1. Primary DNS server: an authoratitive name server for the organization, which holds the authoritative DNS database for the organizations's zones.
* This server is contacted by clients to resovle DNS queries.

2. Secondary DNS server: The backup authoratative name server for the organization.
* Updating the secondary DNS server's database is called a zone transfer.

3. Caching DNS Server: Teh server that accesses public DNS data and caches teh DNS information it collects 

| DNS Server Type         | Description |
|-------------------------|-------------|
| `Primary DNS Server`  | The authoritative name server for an organization, holding the official DNS records for its zones. Clients contact it directly to resolve DNS queries. |
| `Secondary DNS Server`| A backup authoritative name server that receives updates from the primary server via a `zone transfer`. |
| `Caching DNS Server`  | Queries external DNS servers and stores (caches) the results locally to speed up future DNS lookups. |
| `Forwarding DNS Server` | Forwards DNS queries it can't resolve to another DNS server, typically upstream, rather than performing full recursive resolution. |


Steps in a DNS Lookup:
1. The resolver on a client computer first searches the DNS cache. If a match is not found the resolver sends a DNS Query to the local DNS server.

2. If the caching server doesn't know the IP address, then the local name server queries a root server with the request.

3. The root server responds to the local name server with a list of IP addresses of TLD name servers responsible for whichever TLD was included in the request.

4. The local name server makes the same request to one of the TLD name servers. The TLD name server responds with the IP address of the authoratative server for the domain name.

5. The local name server makes the request to the authoratative name server. The Authoratative name server responds with an IP address of the domain name's host.

6. The local name server responds to the client resolver with the requested IP address. The local name server and the client computer store the information in their DNS caches.

```
                             Request
+--------------+       ------------>    +--------------------+
| DNS RESOLVER |                        |  LOCAL NAME SERVER |
+--------------+                        +--------------------+


                                                                      Request
                                        +-------------------+   ------------>    +--------------+
                                        | LOCAL NAME SERVER |                    |  ROOT SERVER |
                                        +-------------------+   <------------    +--------------+
                                                                Response


                                                                      Request
                                        +-------------------+   ------------>    +--------------+
                                        | LOCAL NAME SERVER |                    |  TLD SERVER  |
                                        +-------------------+   <------------    +--------------+
                                                                Response


                                                                      Request
                                        +-------------------+   ------------>    +-----------------------+
                                        | LOCAL NAME SERVER |                    |  AUTHORITATIVE SERVER |
                                        +-------------------+   <------------    +-----------------------+
                                                                Response




+--------------+                        +--------------------+
| DNS RESOLVER |                        |  LOCAL NAME SERVER |
+--------------+       <------------    +--------------------+
                       Response



    Caching                                    Caching
+--------------+                        +--------------------+
| DNS RESOLVER |                        |  LOCAL NAME SERVER |
+--------------+                        +--------------------+
                       
```


There are 2 types of DNS request:
1. A `Recursive query` is a DNS query that demands a resolution or the response that information cannot be found. 
2. An `Iterative query` is a DNS query that does not demand resolution which means the server provides the information only if it already has that information available.


A `resource record` is the element of DNS database stored on a name server that contains information about TCP/IP host names and their addresses

Resource Records in a DNS Database:
| Record Type | Name                        | Purpose                                                                 |
|-------------|-----------------------------|-------------------------------------------------------------------------|
| `A`           | Address Record              | Maps a domain name to an IPv4 address.                                 |
| `AAAA`        | IPv6 Address Record         | Maps a domain name to an IPv6 address.                                 |
| `CNAME`       | Canonical Name              | Points one domain name to another (aliasing).                          |
| `PTR`         | Pointer Record              | Maps an IP address to a domain name (used in reverse DNS lookups).     |
| `NS`          | Name Server                 | Specifies authoritative DNS servers for the domain.                    |
| `MX`          | Mail Exchange               | Directs email to mail servers for the domain.                          |
| `SRV`         | Service Locator             | Specifies host and port for specific services (e.g., VoIP, IM).        |
| `TXT`         | Text Record                 | Stores human-readable or machine-readable text data.                   |
| `SPF`         | Sender Policy Framework     | A type of `TXT` record used to define which servers can send email.      |
| `DKIM`        | DomainKeys Identified Mail  | A `TXT` record used to store public keys for email signing/authentication. |

<br>

| Zone Type     | Description                                                                                         | Example                              |
|---------------|-----------------------------------------------------------------------------------------------------|--------------------------------------|
| Forward Zone  | Maps domain names to IP addresses using records like `A` (IPv4) and `AAAA` (IPv6).                 | `example.com → 192.0.2.1`            |
| Reverse Zone  | Maps IP addresses to domain names using `PTR` records. Used for reverse DNS lookups.               | `192.0.2.1 → example.com`            |



# `The Client-Server Model`

<br>

___

<br>

Covered in this file:
1. [`Internet Communication`](#internet-communication)
1. [`Internet Communication Models`](#internet-communication-models)
1. [`Client Server Model`](#client-server-model)
1. [`Locating a Server on the Internet`](#locating-a-server-on-the-internet)
1. [`How DNS works at a High Level`](#how-dns-works-at-a-high-level)
1. [`How to Perform Your Own DNS Lookup`](#how-to-perform-your-own-dns-lookup)
1. [`Uniform Resource Locators (URLs)`](#uniform-resource-locators-url)
1. [`Sending a Request and Recieving a Response`](#sending-a-request-and-receiving-a-response)

<br>

___

<br>

# `Internet Communication`
The `Internet` is a global network of interconnected computers and devices (smartphones, tablets, etc.) that communicate using standardized protocols, primarily the Internet Protocol (IP). 
* `Internet` is shortened from `inter network` meaning between networks.
    *   *Inter* from latin *inter-* meaning between.   

<br>

`The Internet Engineering Task Force (IETF)` is an open international standards organization that develops and promotes voluntary internet standards, particularly those related to the TCP/IP protocol suite (the foundation of the internet).

<br>

Internet access is provided by an `Internet Service Provider (ISP)`.   

<br>

An `ISP` is a company that provides access to the internet for individuals and organizations. They maintain the necessary infrastructure, including cables, towers, and data centers, to connect networks. 
* An `ISP` is like a bridge connecting your device to the vast network of interconnected networks that is the internet.  

<br>

[Back To Top](#the-client-server-model)
___

<br>


# `Internet Communication Models`
There are several different models used to communicate over the Internet. The most prominent model is the client server model.

| Communication Model | Description  |
|-------------------------|-----------------------------------------------------------------------------|
| **`Client-Server`** | A centralized model where clients request services, and a server responds. |
| **`Peer-to-Peer (P2P)`**  | A decentralized model where nodes act as both clients and servers.|
| **`Publish-Subscribe`**| A model where publishers send messages to subscribers via a broker.  |
| **`Message Queue`** | Asynchronous communication using a queue to manage messages.  |
| **`Broadcast`**  | A model where messages are sent to all nodes in a network. |
| **`Unicast`** | A model where communication occurs between a single sender and receiver.  |
| **`Multicast`**  | Messages are sent to a group of interested receivers.|
| **`Anycast`** | A message is sent to the nearest or best receiver in a group. |
| **`Point-to-Point`**| Direct communication between two nodes.                                   |


<br>

[Back To Top](#the-client-server-model)
___

<br>
 
# `Client-Server Model`

`Client-Server Applications` are data or services requested by one computer from another.

<br>

In the `Client-Server` communication model a client program (e.g., a web browser) sends requests to a server, which processes the request and sends back a response.

![Client Server Diagram](img/client-server-model.svg "Client Server Diagram")
*Having trouble viewing on Github? Try Right-Clicking on the image and selecting "Open image in a new tab"*

```
Client Side                                      Server Side
             ------------------------Request>>>  
Web Browser  [           Internet             ]  Web Server
             <<<Response----------------------- 
```


1. The `Client` sends a request to the Server.  
1. The `Server` sends a response to the Client.  

<br>

A `Client` is any program or device that initiates a communication session with a server to request a service or resource.   
* In most cases when accessing resources on the internet the `client` is your `web browser`.   

<br>

A `Server` is a computer program or physical device that provides services or resources to other devices, known as clients. 
* Think of it as a central hub serving information and functionality to multiple users or devices on a network.  
* In most cases the server is what sends the web page to your browser.  

<br>

*The word `query` is often used in computer science, and can be thought of as a request.*


<br>

[Back To Top](#the-client-server-model)
___

<br>

# `Domain Names`
A `Domain` is a defined area of a larger network. 
* Domains are given human readable names to identify them. 

<br>

`Fully Qualified Domain Name (FQDN) (Layer 7 Application)` a host name plus a domain name that uniquely identifies a computer or location on a network.

```
hostname.domain.top-level-domain
```

* `Domain Name` the last 2 parts of a FQDN. 

* `Host Name` is the first part of a FQDN which identifies the individual computer on the network. 

* The `Top Level Domain TLD` or `domain suffix` is the last part of the FQDN and is the highest level category used to distinquish domain names

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







# `Locating a Server on the Internet : Domain Name System`
*Every device in a network, even a massive network like the internet, has an IP address. However IP addresses are not easy to remember so a system for managing these addresses is necessary.*

<br>

To solve this problem, IP addresses can be mapped to a `Domain Name`. 
* `Name resolution` is process of discovering the IP address of a host when the FQDN is known.

<br>

A `Domain Name` is the human-readable name for a website, like `google.com` or `wikipedia.org`, that acts as a memorable and easy-to-remember address for accessing a website on the internet.
* `IANA (Internet Assigned Numbers Authority)` manages the IP address allocation and Domain Name System.
* `ICANN (Internet Corporation for Assigned Name and Numbers)` non-profit currently designated by US Gov to maintain and Assign IP addresses. 
* Domain Names must be registerd with ICANN


<br>

Domain names on the internet are registered through `domain registrars` and mapped to an actual IP address through the `Domain Name System (DNS)`.

<br>

A `registry` aka `domain name registry operator` is an organization or country that is responsible for one or more TLDs and maintains a database or registry of TLD information.
* A `domain registrar` is an organization accredited by registries and ICANN to lease domain names to companies or individuals, following the guidelines of TLD registry operators. 

<br>

### `Common Domain Registrars`W
| Domain Registrar    | Website                                   |
|---------------------|-------------------------------------------|
| GoDaddy            | [GoDaddy](https://www.godaddy.com/)       |
| Namecheap          | [Namecheap](https://www.namecheap.com/)   |
| Bluehost           | [Bluehost](https://www.bluehost.com/domains) |
| Google Domains     | [Google Domains](https://domains.google/) |
| Hover              | [Hover](https://www.hover.com/)           |
| DreamHost          | [DreamHost](https://www.dreamhost.com/domains/) |
| HostGator          | [HostGator](https://www.hostgator.com/domains) |
| Gandi              | [Gandi](https://www.gandi.net/en)         |
| 1&1 IONOS          | [1&1 IONOS](https://www.ionos.com/domains) |
| Name.com           | [Name.com](https://www.name.com/)         |

*This is not a complete list, merely some of the commonly used registrars*

<br>

`Domain Name System (DNS)` or `Domain Name Service` translates human-readable domain names like `google.com` into IP addresses that computers can understand. 
* DNS is essentially the internet's `phone book` or `contacts app`. 

<br>

The `namespace` is the entire collection of computer names and their associated IP addresses stored in databases on DNS name servers around the globe.

A `Domain Name System (DNS) server` or `name server` is a crucial component of the Internet infrastructure that translates human-readable domain names (like `www.example.com`) into IP addresses (like `192.0.2.1`) that computers use to identify each other on the network. 
* This translation process is essential for enabling web browsing, email, and other Internet services.

<br>

A `resolver` is the DNS client that requests information from DNS Name Servers.

A computer must know the IP address of a DNS server in order to resolve domain names into IP addresses. 
* Without a DNS server a device cannot find servers on the Internet.


<br>

A `DNS server address` is typically provided from your `Internet Service Provider (ISP)`, which assigns it automatically via `DHCP` when a router connects to their network. 
* Alternatively, you can manually configure your computer or router to use public DNS servers.


### Common Public Open DNS Servers:
| DNS Provider          | Primary          | Secondary        |
|-----------------------|------------------|------------------|
| `Google Public DNS`     | 8.8.8.8          | 8.8.4.4          |
| `Cloudflare DNS`        | 1.1.1.1          | 1.0.0.1          |
| `OpenDNS`               | 208.67.222.222   | 208.67.220.220   |
| `Quad9 DNS`             | 9.9.9.9          | 149.112.112.112  |
| `Comodo Secure DNS`     | 8.26.56.26       | 8.20.247.20      |
| `DNS.Watch`             | 84.200.69.80     | 84.200.70.40     |
| `Verisign Public DNS`   | 64.6.64.6        | 64.6.65.6        |



<br>

[Back To Top](#the-client-server-model)
___

<br>

# `How DNS works at a High Level`
1. You type a domain name into your web browser.
1. Your browser contacts a DNS server (usually provided by your internet service provider).
1. The DNS server checks its records for the corresponding IP address of the domain name.
1. If found, the IP address is sent back to your browser.
1. Your browser uses the IP address to connect to the web server hosting the website.

<br>

[Back To Top](#the-client-server-model)
___

<br>

# `How to Perform Your Own DNS Lookup`

### `Windows`:
Open up CMD prompt or Poweshell and type the following command.  
Syntax
```
nslookup <domain-name> <dns-server>
```
Example:
```
nslookup www.google.com 8.8.8.8
```

<br>

### `Linux`
Open the terminal and type the following command.  
Syntax
```
host <domain-name> <dns-server>
```
Example
```
host www.google.com 8.8.8.8
```


<br>
<br>

***`Think of it like this:`***
> * Domain names are like the names in your contacts app.  
> * IP addresses are like phone numbers.  
> * DNS servers are like the contacts app that looks up the phone numbers for you.  

<br>

[Back To Top](#the-client-server-model)
___

<br>

# `Uniform Resource Locators (URL)`.   
`URLs or web addresses` are used to access resources on servers in a network.   
* These addresses include `domain names`, but have other parts as well.  

![URL Diagram](./img/url-diagram.svg "URL Diagram")
*Having trouble viewing on Github? Try Right-Clicking on the image and selecting "Open image in a new tab"*

<br>

```
https://www.example.com:443/blog/article?text=a_string

  Scheme      Subdomain         TLD            File Path       Query String Parameter
    |            |               |                |                   |
| https | :// | www | example | com | :443 | /blog/article | ? | text=a_string | 
           |            |               |                    |
        Delimeter     Domain           Port         Query String Separator    
```
| Part                   | Value                     | Description |
|------------------------|---------------------------|-------------|
| `Scheme/Protocol`        | https                     |The `scheme` is the intial part of a URL that specifies the protocol used to access a resource. <br><br> A `protocol` is  a set of rules and standards that govern how devices communicate and exchange data over a network. <br> <br>Example scheme protocols: http, https, ftp, mailto, file, ssh, etc.  |
| `Scheme/Protocol Delimiter` | ://                    |This `delimeter` separates the scheme (or protocol, such as https, http, ftp) from the rest of the `Uniform Resource Identifier` (URI). |
| `Subdomain`              | www                       |`Subdomains` These are domains within a larger domain, created by adding a prefix to the existing name. For example, mail.google.com is a subdomain of google.com.|
| `Domain`                 | example                   |`Domain` name of the website. |
| `Top-Level Domain TLD`       | com                       |`Top-Level Domains (TLDs)` These are the highest-level categories in the domain name system, like .com, .org, or .edu.  |
| `Port`                   | 443                       |`Port` is a software defined number assigned to uniquely identify a connection endpoint and to direct data to a specific service.|
| `File Path`              | /blog/article             |`File Path` specifies the exact location of a file within the website's directory structure.The path starts from the root (/) and each directory is separated with a “/”.|
| `Query String Separator` | ?                         |The `query string separator '?'` is the delimiter that separates the main part of the URL from the query string.|
| `Query String Parameters`| text=a_string             |The `query string` is a part of a URL that provides additional information to the web server about the requested resource. |

*The `.` serves as a delimiter (seperator) to distinguish between the domain name structure.*

<br>

Example:
```
https://www.google.com/search?q=cats 

 Scheme        Subdomain       TLD      Query String Separator
    |            |              |              |  
| https | :// | www | google | com | /search | ? | q=cats |
           |            |               |            |
        Delimeter     Domain        File Path      Query String Parameter

```


<br>

[Back To Top](#the-client-server-model)
___

<br>

# `Sending a Request and Receiving a Response`

## `HTTP (HyperText Transfer Protocol)`
`HTTP` is a protocol designed for transmitting information, like web pages, between web browsers (client) and web servers. 
* Typically hosted on `port 80`.

<br>

`HTTPS (HyperText Transfer Protocol Secure)`is the HTTP protocol on top of an encryption layer (`Transport Layer Security TLS`) that protects the information traveling over the internet. 
* Today most browsers and servers use HTTPS. 
* Typically hosted on `port 443`.

<br>

`HTTP Headers` are lines of text that provide additional information about an HTTP request or response. 
* Headers are metadata, offering context and instructions for both the client (like a web browser) and the server to ensure smooth communication and efficient data transfer.

<br>

___

<br>

## `HTTP request methods`
An `HTTP Request Method`  is a command sent from a client to a server that specifies the action to be performed on a resource, such as retrieving data (GET), submitting data (POST), updating data (PUT), or deleting data (DELETE).

| HTTP Method | Description                          |
|:-:|--------------------------------------|
| `GET`     | Retrieve information from the server |
| `POST`    | Send information to the server       |
| `PUT`     | Update data on the server            |
| `DELETE`  | Delete data on the server            |


More at  https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

<br>

___

<br>

## `HTTP Response Status Codes`
`HTTP Response Status Codes` are standardized three-digit numbers returned by a server to indicate the outcome of a client's HTTP request, such as `success (2xx)`, `redirection (3xx)`, `client errors (4xx)`, or `server errors (5xx)`. 

<br>

### `HTTP Status Code Ranges, with common codes`

| Status Code Range       | Common Codes            |
|:-----------------------:|-------------------------|
| **100 - 199 Information Responses**           |   | 
|||
| **200 - 299 Successful Responses**           |  `200 OK`  |
|||
| **300 - 399 Redirection Messages**           |    | 
|||
| **400 - 499 Client Error Responses**           | `400 Bad Request` <br> `401 Unauthorized`  <br> `403 Forbidden`  <br> `404 Not Found`  <br> `405 Method Not Allowed` | 
|                         |  |
| **500 - 599 Server Error Responses**           | `500 Internal Server Error` <br> `503 Service Unavailable` |
|                         |  |



*`To see the different codes check out:` https://httpstat.us/*

Check it out on the command line:
```
curl --verbose https://httpstat.us/<code here>
```
*`More at` https://developer.mozilla.org/en-US/docs/Web/HTTP/Status*

<br>

`Take a look using Developer Tools` 
1. press `F12`, `Ctrl + Shift + I`, or by using the browser menu to select `More Tools --> Developer Tools`.  
1. While using Developer Tools look for the '*Network*' tab.

<br>

[Back To Top](#the-client-server-model)
___

<br>

*Created and maintained by Mr. Merritt*
