### API hacking
#
* APIs specify definitions and protocols for programs to communicate to each-other via a set of rules. Apps on the IPhone rely on the camera's API so that they can integrate camera functionality.
* More complex apps rely on APIs.
* An organization will use APIs to share data across different applications. 
* For example, if a developer wanted the contents of a tweet, they would use a GET request to api.twitter.com. The server would return data formated
  in JSON. APIs usually return data in JSON or XML formats.
* APIs usually require users to authenticate before using them. Users do this by providing access tokens
  in API requests. Other times, special headers or cookies are required.
* **REST API** - Commonly used structure. Returned in JSON or plaintext.
  These make it easier to find endpoints via queries. They use various HTTP methods: GET,POST,PUT,DELETE
* **SOAP API** - Less commonly used architecture. Also used by IoT devices. This usses XML and contains a header and a body.
  These also use WSDL as a service to describe the API's structure.
* **GraphQL API** - newer tech that allows developers to request specific fields and grab multiple resources with one call.
  Uses one endpoint and a different query language. "Queries" grab data, "Mutations" change data.
* **API Centric apps** - applications built with APIs. Instead of retrieving HTML documents, these have client components that 
  requests and renders data with API calls.
### Hunting for API vulnerabilities
#
* Very similar to web applications. Difficult part is understanding what the application expects and tailor payloads.
* Can have input validation vulnerabilities.
* For GraphQL, send introspection queries to figure out the structure.
* For SOAP, find the WSDL file.
* If its REST/SOAP, or if introspection is disabled on the GraphQL API, then enumerate
  as many endpoints as you can.
* Deduce endpoints from the ones you've already found.
* Look at intercepted packets for API calls.
* Generate errors for more info by providing different data types or malformed JSON.
* Study JavaScript source code for endpoints & GitHub repos.
* Look at how access cookies work for a given endpoint.
* Rate limiting issues.
