Many times we need to search some emails in the Gmail, but instead of simply searching for a name or key word, there are many useful tricks in Gmail that can save you a lot of time. Here are some of the tricks I use all the time for search in my life. 

### Using different operators

* Finding emails with 'Barack Obama' in subject line

```
subject:Obama
```

* Finding the unread emails from Barack Obama with attachment that emails

```
is:unread from:Barack Obama has:attachment
```

* Finding emails larger than 10 MB in size: 

```
size:10MB
``` 

* Finding emails larger than 5 MB and smaller than 10 MB in size: 

```
larger_than:5m smaller_than:10M 
```
* Finding emails larger than 5 MB and older than 1 year  

```
larger:5m older_than:1y
```

* Finding emails with word document as the attachment

```
filename:.doc
```

* Finding all the emails with attachment in drafts

```
in:drafts has:attachment 
```

* Finding emails between two dates

```
after:2011/08/22 before:2011/08/31 
```

### Combining operators

By default, Gmail combines with multiple operators with 'AND', for example, the above one is finding the emails after 2011/08/22 AND 2011/08/31. But there are more options:

* Search exact phrase

```
"good day"
```
Note that, if you search only for good day, you will get results from emails contain both good and day in them, but they may not contain "good day" phrase. 

* Search emails containing either Iron man **OR** Spider man

```
"Iron man" OR "Spider man"
```

* Search emails not containing day but have good in it

```
good -day
```

* Search emails have dinner and movie in the subject line

```
subject:(dinner movie)
```
This will find emails have both dinner and movie in the subject line, but they are maybe not a phrase. 