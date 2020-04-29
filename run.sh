#!/bin/bash -i
conda activate ds-Flask && FLASK_APP=app FLASK_ENV=deployment flask run
