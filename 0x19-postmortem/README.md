Title: Service CRYPTOGATEWAY failed, affecting all customers
Incident date: 2022-06-09
Owner: Andrés Henderson
Peer-review committee: Andrés Henderson & Andrés Henderson
Tags: API CRYPTOGATEWAY service failure
Summary: The CRYPTOGATEWAY service has failed to provide a JSON response to clients between 2020-06-09 at 13:00 UTC and 2022-06-09 16:00 UTC.
Supporting data:
Customer Impact: Customers were unable to retrieve sales data. Databases were not accessible, sales logging was unaffected.
Incident Response Analysis: The incident was aknowledged within 30 minutes of begining due to traffic monitoring using datadog. Customers called for support whilst we were working on solution. 
Escalation was early and appropriate.
Issue originated at small number of file descriptors allowed for the service.
Solution was tested using postman and the service was operational.
Post-Incident Analysis: Further and more thorough tests should be performed on the API. 
Request load should be tested against the service.
Timeline: 2020-06-09 at 13:00 UTC, no connections were made to the service.
Contributing factors: Due to short deply and testing time, no complete tests were performed on the service. 
Lessons Learned: Every service should be tested in as many scenarios as possible. 
Action items: Testing of high volume of requests to be performed by Andrés Henderson on 2020-06-10 from 13:00 to 15:00 UTC, report will be sent to Andrés Henderson for further evaluation. Corrective measures will be reviewed by an all hands meeting of the team. 