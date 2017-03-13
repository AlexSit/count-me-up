Dear Sir or Madam!

The task's formulation didn't seem clear IMHO. 
As I was short on time I implemented the simplest solution ever and left few TODOs.
My main programming language is C#, but C# wasn't on list, so I used Python, for the first time for this kind of tasks.
I would love to continue implementing this task if I had more time.

My comments and assumptions about the task:

1. Given 10000000 votes were received
    And votes were distributed against candidates as:
      | candidate          | percentage |
      | candidate-1        |      5     |
      | candidate-2        |      10    |
      | candidate-3        |      20    |
      | candidate-4        |      25    |
      | candidate-5        |      40    |

- We have no information about the way we receive votes. 
- Nothing said how to define which user voted for a particular candidate.

2. And no more than 3 votes per user are allowed
- How do we know if someone voted more than 3 times?

3. When CountMeUp is asked for the results
    Then it responds in under 1 seconds
    And the final counts are:
      | candidate          |    count     |
      | candidate-1        |    500000    |
      | candidate-2        |    1000000   |
      | candidate-3        |    2000000   |
      | candidate-4        |    2000000   |
      | candidate-5        |    3000000   |

•   The same user can vote multiple times, up to a maximum of 3 times for the same candidate or for different ones. Count Me Up should not count a vote if the same user already exceeded the maximum allowed number of votes (that is should not count user-1 vote for candidate-5 if user-1 already voted for candidate-1, candidate-2 and candidate-3). This is the reason why candidate-5 for example received "only" 3M votes instead of 4M.

- I couldn't read how we could get that info (user already exceeded the maximum allowed number of votes) only having a look taken at given percentages.

MY ASSUMPTIONS:

My assumption is we only can receive concrete votes from concrete customers in real-time in following format, e.g.:

{
    "userKey": "Tom Smith, Manchester, UK",
    "candidateId": 3    
}

or 
{
    "userKey": "Aaron Z., London, UK",
    "candidateId": 5       
}

So while competition goes we receive requests from users storing their votes and remembering who voted for whom and how many times.
Also we have method that exposes info about the current results, namely, votes count for each candidate and percents.

Like that:

[{
   "candidateId": 1,   
   "voteCount": 500000,   
   "percents" : 5
}, {
   "candidateId": 2,
   "voteCount": 1000000,   
   "percents" : 10
}, {
   "candidateId": 3,
   "voteCount": 2000000, 
   "percents" : 20  
}, {
   "candidateId": 4,
   "voteCount": 2000000,   
   "percents" : 25
}, {
   "candidateId": 5,
   "voteCount": 3000000,   
   "percents" : 40
}]

I find it useful because we have percentages that looks good, and to meet CountMeUp requirements we expose count
on demand.


HOW TO RUN SOLUTION IN WINDOWS

Download repository
Download and install Python
Install Flask
Run python ~/app/__init__.py

A. POST http://localhost:5000/vote HTTP/1.1
Host: localhost:5000
Content-Length: 40
Content-Type: application/json

{ "userKey": "Bob", "candidateId": 5   }

HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 64
Server: Werkzeug/0.12 Python/3.4.4
Date: Mon, 13 Mar 2017 01:48:38 GMT

{
  "vote": {
    "candidateId": 5, 
    "userKey": "Bob"
  }
}


B.
GET http://localhost:5000/votes HTTP/1.1
Host: localhost:5000
Content-Length: 0
Content-Type: application/json

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 108
Server: Werkzeug/0.12 Python/3.4.4
Date: Mon, 13 Mar 2017 01:48:45 GMT

{
  "Alice": 3, 
  "Bob": 3, 
  "Tom Smith, Manchester, UK": 3, 
  "Tom Smith22222222, Manchester, UK": 3
}


C. GET http://localhost:5000/candidates HTTP/1.1
Host: localhost:5000
Content-Length: 0
Content-Type: application/json

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 378
Server: Werkzeug/0.12 Python/3.4.4
Date: Mon, 13 Mar 2017 01:49:00 GMT

[
  {
    "candidateId": 1, 
    "percents": 25.0, 
    "voteCount": 3
  }, 
  {
    "candidateId": 2, 
    "percents": 16.67, 
    "voteCount": 2
  }, 
  {
    "candidateId": 3, 
    "percents": 25.0, 
    "voteCount": 3
  }, 
  {
    "candidateId": 4, 
    "percents": 25.0, 
    "voteCount": 3
  }, 
  {
    "candidateId": 5, 
    "percents": 8.33, 
    "voteCount": 1
  }
]
