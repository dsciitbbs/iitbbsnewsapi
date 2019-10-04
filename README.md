
IIT Bhubaneswar News API
=====

[![Build Status](https://travis-ci.com/dsciitbbs/iitbbsnewsapi.svg?branch=master)](https://travis-ci.com/dsciitbbs/iitbbsnewsapi)

>A JSON API to scrap latest news, events details and notices from <http://www.iitbbs.ac.in>


## Features
* News and Updates
	* Return JSONified count, link text and URL for top 30 news and updates.
* Events
	* Return JSONified count, link text and URL of all upcoming events.
* Notices
	* Return JSONified count, link text and URL of all available notices.
* Bus Schedule
  * Get Latest links of PDF and XLS bus schedule files. 
* Time table
  * Get correct timetable of the day on passing your roll number.
* Tweets
  * Get the latest tweets from IIT Bhubaneswar's official handle via this endpoint.

## Schema
All API access is over `HTTPS`, and accessed from the `<https://iitbbs.herokuapp.com>`. All data is sent as JSON.

```bash
curl -i https://iitbbs.herokuapp.com

HTTP/1.1 200 OK
Connection: keep-alive
Server: gunicorn/19.7.1
Date: Wed, 12 Jul 2017 19:31:03 GMT
Content-Type: application/json
Content-Length: 200
Via: 1.1 vegur

{
  'author' : 'Aman Pratap Singh'
  'email' : 'amanprtpsingh@gmail.com',
  'endpoint' : 'https://iitbbs.herokuapp.com',
  'project_name' : 'IITBBSNewsAPI',
  'project_url' : 'https://nightawks.github.io/IITBBSNewsAPI/'
}
```

## Endpoints

### `GET: /news`  
Result:  
```json
{
  "count": 30, 
  "list": [
    {
      "text": "New Admission : 2017-18", 
      "url": "http://www.iitbbs.ac.in/admission-portal.php"
    }, 
    {
      "text": "Recruitment of Part-Time Coaches, Yoga Instructor & Yoga Assistant", 
      "url": "http://www.iitbbs.ac.in/notice/news_1499481442.pdf"
    }, 
    {
      "text": "Information to the provisionally selected candidates  for joining to M.Sc. Programme 2017-18", 
      "url": "http://www.iitbbs.ac.in/msc.php"
    }, 
  ]
}
```

### `GET: /events`  
Result:  
```json
{
  "count": 1, 
  "list": [
    {
      "text": "7th International Conference On Soft Computing for Problem Solving during December 23-24, 2017", 
      "url": "http://www.iitbbs.ac.in/notice/event_1488324349.pdf"
    }
  ]
}
```

### `GET: /notices`  
Result:  
```json
{
  "count": 39, 
  "list": [
    {
      "text": "Result of Physical Training Instructor", 
      "url": "http://www.iitbbs.ac.in/notice/resultofphysicaltraininginstructor_1498601014.pdf"
    }, 
    {
      "text": "Subjects to be offered for Summer Quarter 2016-17", 
      "url": "http://www.iitbbs.ac.in/notice/subjectstobeofferedforsummerquarter201617_1495022716.pdf"
    }, 
  ]
}
```

### `GET: /bus`  
Result:  
```json
{
  "pdf": "www.iitbbs.ac.in/transportation-fle/transport_1529956769.pdf",
  "xls": "www.iitbbs.ac.in/transportation-fle/transport_1529956769.xls"
}
```

### `GET: /timetable?roll={roll}`
Result for roll=16CS01017:
```json
{
  "status":"200",
  "data":[
  {
    "subject":"NSS",
    "time":"5:30-6:30"
  },
  {
    "subject":"Advanced Algorithms",
    "time":"2:30-4:30"}
  ],
}
```

### `GET: /tweets..`
Result:
```json
{
  "count": 30,
  "list": [
    {
      "text":"ISRO chief K Sivan Visit Lingaraj Temple In Bhubaneswar ",
      "url': 'https://youtu.be/SqmnzroBM6k"
    }, 
    {
      "text": "ISRO Chief K Sivan On Chandrayaan 2 Mission", 
      "url": "https://youtu.be/PcVqihrWd-c"
    },
    ]
}
```

## Contributing
Feel free to submit a pull request or an issue. Sugest new features on issue tracker.

## License

Built with ♥ by Developer Student Club, IIT Bhubaneswar under [MIT License](http://aps.mit-license.org/)  
Special Thanks to Aman Pratap Singh ([@apsknight](http://github.com/apsknight)) who originally came up with the idea.
