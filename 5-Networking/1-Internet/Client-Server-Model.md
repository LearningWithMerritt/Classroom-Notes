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

In the `Client-Server` communication model a client device (e.g., a web browser) sends requests to a server, which processes the request and sends back a response.

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

# `Locating a Server on the Internet`
*Every device in a network, even a massive network like the internet, has an IP address. However IP addresses are not easy to remember so a system for managing these addresses is necessary.*

<br>

To solve this problem, IP addresses can be mapped to a `Domain Name`. 

<br>

A `Domain Name` is the human-readable name for a website, like `google.com` or `wikipedia.org`, that acts as a memorable and easy-to-remember address for accessing a website on the internet.

<br>

Domain names on the internet are registered through `domain registrars` and mapped to an actual IP address through the `Domain Name System (DNS)`.

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

`Domain Name System (DNS)` translates human-readable domain names like `google.com` into IP addresses that computers can understand. 
* DNS is essentially the internet's `phone book` or `contacts app`. 

<br>

A `Domain Name System (DNS) server` is a crucial component of the Internet infrastructure that translates human-readable domain names (like `www.example.com`) into IP addresses (like `192.0.2.1`) that computers use to identify each other on the network. 
* This translation process is essential for enabling web browsing, email, and other Internet services.

<br>

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
