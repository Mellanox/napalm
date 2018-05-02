# Simple Flask app to test getters


### Installation
Install the dev branch of Napalm, or whatever version you wish to test against

```bash
pip install -e .
cd test_getters
pip install -r requirements.txt
```

### Testing

Make sure you are located in the test_getters directory, start Flask:

```
flask run
```

Open 127.0.0.1:500 in a browser window

### Running

1. Click on the platform you want to test (currently only IOS)
2. Click on the getter you want to test
3. Paste the output from the requested command
4. Repeat step 3 as neccesary if there are more commands
5. Examine the data that Napalm returned or view the traceback

