# Chapter 09 - Answers

## Question 9.1: Stock data app to push end of the day results to clients
Server fetches data from persistence (since its presumed you already
have the data) and pushing the information to connected clients via websockets
for example or normal REST in case of rehydration upon visit
to x consumers running the app.


## Question 9.2: Social Network

## Question 9.3: Design of web crawler to avoid infinite loops
Store visited URLs enriched with datetime. <br>
For storage see answer to question 9.4, replace HashSet with Hashtable or stay with database storage

## Question 9.4: How to find duplicate URLs among 10 billion?
###############<br>
Space needed? ##<br>
###############<br>

* 10^9 URLs
* Single URL max. 2048 bytes

 => 2.05^12 bytes => 2.05TB
 
##########<br>
Storage? ##<br>
##########<br>
Either database (key, value store) with index in the URL entry<br>
or <br>
bigger machine with >2.5TB RAM => HashSet von O(1) lookup time<br>
hashtable could be dumped to drive for persistence

## Question 9.5: Design cache system for a search engine
Obviously the data needs to fit into a data structure<br>
Hints: Combine Hashtable and LinkedList to fit into one machine<br>
Assumption about machine: RAM size should be what?<br>
Lets take a google cloud machine m1-ultramem-40 with ~1TB RAM for 3.2K/month<br>
data structure of more than 2TB data needs to fit into ~1TB<br>
=> study Hashtable & LinkedList again

How is the cache update designed?<br>
############################<br>
To reduce unnecessary steps, only update when crawler visited URL<br>
Post-URL visit and indexing trigger event => Push update job with new information
into a stream like Redis or Kafka being consumed by x machines => Each machine updates
its data structure.

## Question 9.6. Design eCommerce system to track and report most selling products as well as most selling per category
* Track product purchase in SQL DB, upon purchase:
  * Persist datetime of purchase
  * Persist category of purchase
* Custom views can be defined for reports on
  * Year / Month / Day basis as well as category combination

## Question 9.7: Design personal financial manager like mint.com

## Question 9.8: Design a text publish system with a generate URL like pastebin
* Upon text input persist data into a key, value store
* Key is a generated hash or id avoiding clashes that also serves as URL parameter
* values are the text itself along metadata
* How to avoid collisions?
* Hints: Account for high traffic on minimum percentage of values 