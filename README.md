# Platform Event Trap (PET) decoder
This utility translate PETs into human readable form as defined in Platform Event Trap Format Specification v1.0 [1].

## Installation
Before running the script, install all python libraries:
```bash
$ pip install -r requirements.txt
```

## CLI
Run:
```bash
$ PYTHONPATH=`pwd` python cli/pet_decoder.py --help
```

## Web
Using flask.

Run:
```
$ export FLASK_APP="web.main:app"
$ python -m flask run
```

Currently also deployed at heroku: https://pet-decoder.herokuapp.com/

---
[1] https://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/platform-event-trap.pdf