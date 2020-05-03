#!/bin/bash
celery -A currencyapp worker --beat -l info