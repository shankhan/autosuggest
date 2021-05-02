# REST Web Service - Autosuggest

## Before You Begin
- Install Docker
- MySQL is installed and you have the necessary credentials.


## Setting up the application
### Development Environment:
- After cloning the repo run `docker-compose up`
- To access the api call the url with `http://localhost:5000/api/gene_suggest?query={query}&species={species}&limit={limit}`