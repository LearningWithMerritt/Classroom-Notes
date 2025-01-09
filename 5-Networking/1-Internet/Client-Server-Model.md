# `The Client-Server Model`

<br>

___

<br>

Covered in this file:
1. [`Internet Communication`](#internet-communication)
1. [`Internet Communication Models`](#internet-communication-models)
1. [`Client Server Model`](#client-server-model)
1. [`Locating the Server`](#locating-the-server)
1. [`How DNS works at a High Level`](#how-dns-works-at-a-high-level)
1. [`Perform Your Own DNS Lookup`](#perform-your-own-dns-lookup)
1. [`Uniform Resource Locators (URLs)`](#uniform-resource-locators-url)
1. [`Sending the Request and Recieving a Response`](#sending-the-request-and-receiving-the-response)

<br>

___

<br>

# `Internet Communication`
`Internet` shortened form of inter network. Inter from latin inter- meaning between. The internet is a vast network of interconnected computer networks that spans the globe. It allows communication and data exchange between devices (computers, smartphones, tablets, etc.) anywhere in the world.  

> Internet access is provided by an `Internet Service Provider (ISP)`.   

> An `ISP` is a company that provides access to the internet for individuals and organizations. They maintain the necessary infrastructure, including cables, towers, and data centers, to connect networks. Think of it like a bridge connecting your device to the vast network of interconnected computers that is the internet.  

<br>

[Back To Top](#the-client-server-model)
___

<br>


# `Internet Communication Models`
> There are several different models used to communicate over the Internet. The most prominent model is the client server model.

<br>
 
## **Client Server Model**
![Client Server Diagram](img/client-server-model.svg "Client Server Diagram")
*Having trouble viewing on Github? Try Right-Clicking on the image and selecting "Open image in a new tab"*

```
Client Side                                      Server Side
             ------------------------Request>>>  
Web Browser  [           Internet             ]  Web Server
             <<<Response----------------------- 
```


> * The Client sends a request to the Server.  
> * The Server sends a response to the Client.  

> A `Client` is any program or device that initiates a communication session with a server to request a service or resource.   
> * In most cases the client is your web browser.   

> A `Server` is a computer program or physical device that provides services or resources to other devices, known as clients. Think of it as a central hub serving information and functionality to multiple users or devices on a network.  
> * In most cases the server is what sends the web page to your browser.   

> The word `query` is often used in computer science, and can be thought of as a request.  


<br>

[Back To Top](#the-client-server-model)
___

<br>

# `Locating the Server`
*Every device in a network, even a massive network like the internet, has an IP address. However IP addresses are not easy to remember so a system for managing these addresses is necessary.*

> A `Domain Name` is the human-readable name for a website, like google.com or wikipedia.org, that acts as a memorable and easy-to-remember address for accessing a website on the internet.  
>   * Domain names are registered through `domain registrars` and mapped to an actual IP address through the `Domain Name System (DNS)`.

Common Domain Registrars:
1. [GoDaddy](https://www.godaddy.com/)
2. [Namecheap](https://www.namecheap.com/)
3. [Bluehost](https://www.bluehost.com/domains)
4. [Google Domains](https://domains.google/)
5. [Hover](https://www.hover.com/)
6. [DreamHost](https://www.dreamhost.com/domains/)
7. [HostGator](https://www.hostgator.com/domains)
8. [Gandi](https://www.gandi.net/en)
9. [1&1 IONOS](https://www.ionos.com/domains)
10. [Name.com](https://www.name.com/)

> `Domain Name System (DNS)` translates human-readable domain names like "google.com" into IP addresses that computers can understand. 
> * DNS is essentially the internet's phone book or contacts app. 

<br>

A `Domain Name System (DNS) server` is a crucial component of the Internet infrastructure that translates human-readable domain names (like www.example.com) into IP addresses (like 192.0.2.1) that computers use to identify each other on the network. This translation process is essential for enabling web browsing, email, and other Internet services.

### Common Open DNS Servers:
`Google Public DNS`
>  - Primary: `8.8.8.8`
>  - Secondary: `8.8.4.4`

`Cloudflare DNS`
>  - Primary: `1.1.1.1`
>  - Secondary: `1.0.0.1` 

`OpenDNS`
>  - Primary: `208.67.222.222`
>  - Secondary: `208.67.220.220`

`Quad9 DNS`
>  - Primary: `9.9.9.9`
>  - Secondary: `149.112.112.112` 

`Comodo Secure DNS`
>  - Primary: `8.26.56.26`
>  - Secondary: `8.20.247.20`

`DNS.Watch`
>  - Primary: `84.200.69.80`
>  - Secondary: `84.200.70.40`

`Verisign Public DNS`
>  - Primary: `64.6.64.6`
>  - Secondary: `64.6.65.6`  

<br>

[Back To Top](#the-client-server-model)
___

<br>

## How DNS works at a High Level:
1. You type a domain name into your web browser.
1. Your browser contacts a DNS server (usually provided by your internet service provider).
1. The DNS server checks its records for the corresponding IP address of the domain name.
1. If found, the IP address is sent back to your browser.
1. Your browser uses the IP address to connect to the web server hosting the website.

<br>

[Back To Top](#the-client-server-model)
___

<br>

## Perform Your Own DNS Lookup

### Windows:
Open up CMD prompt or Poweshell and type the following command.  
Syntax
```
nslookup <domain-name> <dns-server>
```
Example:
```
nslookup www.google.com 8.8.8.8
```

### Linux
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

***Think of it like this:***
> * Domain names are like the names in your contacts app.  
> * IP addresses are like phone numbers.  
> * DNS servers are like the contacts app that looks up the phone numbers for you.  

<br>

[Back To Top](#the-client-server-model)
___

<br>

## Uniform Resource Locators (URL).   
`URLs or web addresses` are used to access resources on servers in a network.   
> These addresses can be broken down into their parts. 
![URL Diagram](./img/url-diagram.svg "URL Diagram")

```
https://www.example.com:443/blog/article?text=a_string

*Having trouble viewing on Github? Try Right-Clicking on the image and selecting "Open image in a new tab"*


> * The `scheme` is the intial part of a URL that specifies the protocol used to access a resource.  
> * A `protocol` is  a set of rules and standards that govern how devices communicate and exchange data over a network.
>   * Examples scheme protocols: http, https, ftp, mailto, file, ssh, etc.  

> * `Subdomains` These are domains within a larger domain, created by adding a prefix to the existing name. For example, mail.google.com is a subdomain of google.com.  

> * `Domain` name of the website.   

> * `Top-Level Domains (TLDs)` These are the highest-level categories in the domain name system, like .com, .org, or .edu.  

> * `Port` is a software defined number assigned to uniquely identify a connection endpoint and to direct data to a specific service.  

> * `File Path` specifies the exact location of a file within the website's directory structure.The path starts from the root (/) and each directory is separated with a “/”.  

> * The `query string separator '?'` is the delimiter that separates the main part of the URL from the query string.  

> * The `query string` is a part of a URL that provides additional information to the web server about the requested resource. 
> 
> example:  
> https://www.google.com/search?q=cats  
>'*q=cats*' is the query string 

<br>

[Back To Top](#the-client-server-model)
___

<br>

# `Sending the Request and Receiving the Response`

## HTTP(HyperText Transfer Protocol)
	
> `HTTP` is a protocol designed for transmitting information, like web pages, between web browsers (client) and web servers. Typically hosted on port 80.

>  `HTTPS (HyperText Transfer Protocol Secure)`is HTTP on top of an encryption layer (Transport Layer Security TLS)that protects the information traveling over the internet. Most browsers and servers use HTTPS. Typically hosted on port 443.

	
> `HTTP Headers` are lines of text that provide additional information about an HTTP request or response. They act like metadata, offering context and instructions for both the client (like a web browser) and the server to ensure smooth communication and efficient data transfer.

## HTTP request methods
> An `HTTP Request Method`  is a command sent from a client to a server that specifies the action to be performed on a resource, such as retrieving data (GET), submitting data (POST), updating data (PUT), or deleting data (DELETE).  
* **GET** - Retrieve information from the server
* **POST** - Send information to the server
* **PUT** - Update data on the server
* **DELETE** - Delete data on the server

More at  https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

## HTTP Response Status Codes
> `HTTP Response Status Codes` are standardized three-digit numbers returned by a server to indicate the outcome of a client's HTTP request, such as success (2xx), redirection (3xx), client errors (4xx), or server errors (5xx).  

`100 - 199 Information Responses:` 

`200 - 299 Successful responses:`  
_ 200  OK

`300 - 399 Redirection Messages:` 

`400 - 499 Client Error responses:`   
_ 400 Bad Request  
_ 401 Unauthorized  
_ 403 Forbidden  
_ 404 Not Found  
_ 405 Method Not Allowed  

`500 - 599 Server Error responses:`   
_ 500 Internal Server Error  
_ 503 Service Unavailable  

> To see the different codes check out: https://httpstat.us/

Check it out on the command line:
```
curl --verbose https://httpstat.us/<code here>
```

>More at https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

> Take a look using Developer Tools 
> * press F12, Ctrl + Shift + I, or by using the browser menu to select More Tools --> Developer Tools.  
> * While using Developer Tools look for the '*Network*' tab.

<br>

[Back To Top](#the-client-server-model)
___

<br>

*Created and maintained by Mr. Merritt*ss
