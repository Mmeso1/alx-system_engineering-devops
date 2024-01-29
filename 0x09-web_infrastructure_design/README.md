# My Take On The Web Infrastructure Design

# I wil be using the second task to give a general overview on how everything works from my understanding

On a whiteboard, design a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.

## Requirements:

- You must add:
-- 3 firewalls
-- 1 SSL certificate to serve www.foobar.com over HTTPS
-- 3 monitoring clients (data collector for Sumologic or other monitoring services)
-- You must be able to explain some specifics about this infrastructure:
  
## For every additional element, why you are adding it
-- What are firewalls for
-- Why is the traffic served over HTTPS
-- What monitoring is used for
-- How the monitoring tool is collecting data
-- Explain what to do if you want to monitor your web server QPS

## You must be able to explain what the issues are with this infrastructure:
-- Why terminating SSL at the load balancer level is an issue
-- Why having only one MySQL server capable of accepting writes is an issue
-- Why having servers with all the same components (database, web server and application server) might be a problem
Please, remember that everything must be written in English to further your technical ability in a variety of settings.


## Let's Begin
* When a user on their client server (PC) type in the website pages they want to view, in this case www.foobar.com.
* 
* The browser sends a request to DNS to resolve the IP address associated with the website. Since the website is hosted on a company's domain, which is www, the DNS lookup returns a CNAME record pointing to the actual hostname (A record) of the hosting server.
* 
* The browser sends an HTTP request to the IP address obtained from the DNS resolution. The web server, which in this case is Nginx, receives this request.

* The Nginx web server first checks its cache to see if the website content is stored locally. If the content is found in the cache, indicating a static website, Nginx renders the content directly. However, in this case the site is dynamic since it uses a database.

* Subsequently, as the website content is dynamic and not cached, the web server forwards the request to the load balancer of the hosting company, which in this case is www.

* The load balancer, in this instance HAProxy, is responsible for distributing incoming traffic among multiple application servers to prevent server overload. Employing a Round-Robin technique, the load balancer evenly divides requests across the available application servers hosting the requested page.

* The load balancer presents the SSL certificate for the site to the Nginx web server. If the SSL certificate is valid, a secure connection is established through a digital handshake between the site and the browser. The load balancer then decrypts the request using SSL and forwards it to the backend application server.

* The application servers operate in an Active-passive configuration, ensuring continuous availability. If one server experiences downtime, the next server in line automatically takes over to maintain uninterrupted service.

* Following this, the load balancer distributes incoming traffic to the designated default application server. The application server generates the necessary application files.

* With a database in place, the default application server queries the database to populate HTML content. It primarily interacts with the primary database responsible for CRUD operations. Other application servers have their own replicas of the primary database, ensuring redundancy and minimizing the risk of a Single Point Of Failure (SPOF). This setup ensures system resilience in case of primary database failure, preventing system-wide disruptions.

* The application server sends the completed web pages back to the web server, which then delivers the content to the user's browser for viewing.

* Firewalls are placed between the user's connection and the load balancer, as well as between each server and the load balancer, to regulate traffic flow and enhance network security.
* Monitoring services are deployed on both the load balancer and the application servers to track user requests and detect any potential security threats or attacks.
