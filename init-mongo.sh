#!/bin/bash
mongorestore -d ${MONGO_INITDB_DATABASE} /dump/sample_collection.bson
