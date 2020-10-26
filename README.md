# nasa-pushpin
A TrackerGG api example using Push-pin for streaming Realtime updates from the TrackerGG API.


## You will need a NASA Api Account
* Register Here: https://api.nasa.gov/


## Nasa Client Container
A simple python app which makes requests to the NASA API. https://api.nasa.gov/

* Add your API_KEY to the `creds.env` file

* Serves port `5000`

### Endpoints

* `/` - health check /heartbeat, responds if container is online and reachable.
* `/stats` - gives the last 5 days of Near Earth Orbit Object data from NASA.
* `/stream` - the pushpin stream (In progress)

## Pushpin Container
A pushpin implementation which streams results of the trackerGG api to any streams connected.

### Config
* The `pushpin/config` folder contains a routes file that is provided to the pushpin app when the container starts.  Add routes here. (default: Anything on Localhost goes to 5000 on nasaapi_client container)