# Unofficial Python Caflou SDK

Unofficial Python development kit meant to streamline accessing and modifying data stored in Caflou. This is not the API documentation. [(Official API docs link)](https://documenter.getpostman.com/view/4786951/RWMFrTQC)

This project is developed and maintained by Robert Krása ([dev@robovo.cz](mailto:"dev@robovo.cz")). And is in very early stage of development.

## How does it work

Once initialized, you can use the usual HTTP methods to access and write the data to Caflou. All methods return Python dict with returned data. Watch out for the `{"results": <DATA>}` returned for requests without specific ID.
The methods are:
- GET
- POST
- PATCH
- DELETE

The POST and PATCH methods take a Python dict as payload. Formatting the dict is up to you for now. As well as figuring out the different caveats of the API. Good luck.


## Setup

1. Download a copy of the source code to your project folder.
2. import the caflou class
  ```python
  from caflou.caflou.caflou import Caflou # Sorry about that, hopefully it will change to a single  caflou soon
  ```
3. Get the credentials. Your credentials can be found in the Caflou app: Cog wheel > Account Settings > API  (URL ending in /settings/integration)
4. Initiate the Caflou object 
  ```python
  caflou = Caflou(accound_id, token)
  ```
5. Call the available methods to read/write data.
  ```python
  invoice = caflou.get("invoices/123")
  projects = caflou.get("projects", per=1000)
  item_response = caflou.post("products",{"name": "Test product"})
  del_response = caflou.delete(f"products/{item_response["id"]}")
  ```
6. Process the data I guess.


## Todo

In no particular order.
- [ ] Create a installable pip package
- [ ] Copy the whole object model to classes and allow for dot notation usage
- [ ] Support async
- [ ] Swith to httpx client
- [ ] Better network exception handling
- [ ] Setup HTTP session on init
- [ ] Add unit testing
- [ ] Support fetching variables from .env files
- [ ] Add typing
- [ ] Add proper logging
- [ ] Add support for downloading all objects of type
- [ ] Add local caching of data for batch manipulation
- [ ] Generate docs from code

----

This work is inspired by the [Notion API Client](https://github.com/ramnes/notion-sdk-py) and the [Fakturoid API Client]()
