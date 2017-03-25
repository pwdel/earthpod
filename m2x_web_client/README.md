# Sample App to Display Data from CleverFaucet
A small Python based Flask app that displays data from a [Raspberry Pi based faucet monitor](https://github.com/attm2x/m2x-sample-cleverfaucet/) and can be easily deployed on Heroku. This sample app pulls data from [AT&T's M2X](http://m2x.att.com).

An example running on Heroku can be found here: https://floating-beach-7934.herokuapp.com

## What you need
* A free [Heroku Account](https://signup.heroku.com/).
* A free AT&T [M2X Account](https://m2x.att.com/signup).
* An M2X Device set up to record water temperature and volume (for an example, see: https://github.com/attm2x/m2x-sample-cleverfaucet)
* Basic Python knowledge.
* [Pip](https://pypi.python.org/pypi/pip) to resolve dependencies
* Recommended:
  * Installed Python and Virtualenv in a unix-style environment. [See this guide for guidance.](http://docs.python-guide.org/en/latest/starting/install/osx/)


## Dependencies

* [m2x-python](https://github.com/attm2x/m2x-python) - v3.0.4
* [Flask](http://flask.pocoo.org) 
* [Gunicorn](http://gunicorn.org/)

## Instructions
1. Create your free Heroku Account 
2. Download and install the [Heroku Toolbelt](https://toolbelt.heroku.com)
3. Login to Heroku from the terminal

    ```bash
    $ heroku login
    ```
    
4. Clone this repository
 
    ```bash
    $ git clone https://github.com/attm2x/m2x-sample-cleverfaucet-web.git
    $ cd m2x-sample-faucet-web
    ```

5. Use pip to install dependencies (preferably inside a virtualenv):

  ```bash
  $ pip install Flask gunicorn
  ```
6. Now create a .env file inside your m2x-sample-faucet-web directory.
7. Add the following to your .env file, adding the API Key and Device ID from your M2X account (this is so you can run your app locally).

  ```
  MASTER_API_KEY=
  DEVICE_ID=
  ```
8. Make sure your data streams for this device are named 'temperature' and 'water_use'.
9. Create three charts for your device adding the appropriate data streams to each:
    1. temperature
    2. water_use
    3. temperature and water_use
10. You should now be able to run the app locally at http://localhost:5000:

  ```bash
  $ foreman start
  ```
11. In order to run the app on Heroku, first you need to create a heroku app.

  ```bash
  $ heroku create
  ```
12. Next we will set the environmental config variables on for the heroku app. Fill in the place after the equals sign with your M2X API Key and Device ID:

  ```bash
  $ heroku config:set MASTER_API_KEY= DEVICE_ID=
  ```
13. Finally push the repo to Heroku:

  ```bash
  $ git push heroku master
  ```
14. Your app should be up in running. Open it in your browser with:

  ```bash
  $ heroku open
  ```

##LICENSE

This sample application is released under the MIT license. See [`LICENSE`](LICENSE) for the terms.

