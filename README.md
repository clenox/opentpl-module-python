# opentpl-module-python

Python module to access the OpenTPL API for data from and control of TP-Link Smart Plugs

This python module uses the OpenTPL API hosted on RapidAPI:  https://rapidapi.com/clenox/api/opentpl1

You will need a RapidAPI account and key to utilize this module.  Complete documentation of the API is provided at the above link.

Import:

from opentpl import opentpl

Use:

opentpl("uuid", body, "rapidAPIKey")

-- "uuid" is the KasaSmart username of the account.  Note that multiple KasaSmart accounts can be associated with a single RapidAPI account (see below).

-- body is the command dictionary (see below).

-- "rapidAPIKey" is your unique alphanumeric key provided by RapidAPI.

It typically takes 2 - 3 seconds for the API to return.  Please do not attempt to send queries / commands to a given plug more frequently than once every 3 seconds.

Body:

The following are in order of the steps you'll need to follow to get started.

-- Associate A New KasaSmart Account

  This is how you register a KasaSmart account for the first time to get access to it.  This only needs to be done once.

  KasaSmart_password is the password associated with the uuid.  These credentials are securely stored and used only when needed (for access key rotation, which is performed        automatically).

  body = {"command": "create_account", "password": "KasaSmart_password"}

-- Get Plug Names

  All calls to OpenTPL use unique alphanumeric plug IDs to avoid any potential conflict.  However, generally the location and/or function of each plug is indicated by the user   defined name / alias.  This command provides the mapping needed to associate each plug name to it's unique ID.

  body = {"command": "plug_names"}

-- Plug commands & data

  The following call provides on/off control, status (online or offline) and reporting of current power data.

  Valid commands are "ON", "OFF", "status", and "data" (as in the below example).

  Important note: the status command is not usually needed because the OpenTPL API automatically validates connectivity. If there is no connectivity, OpenTPL attempts to re- establish before sending other commands.  If not possible, an error ("offline") will be returned.

  body = {"command": "data", "plugid": "unique_plug_id"}

-- Delete (un-associate) KasaSmart account from OpenTPL

  This deletes all information about the KasaSmart account associated with the uuid, including credentials, from OpenTPL.  Note this has no effect on the KasaSmart account itself.  if accidentally invoked this can be easily corrected by simply creating the account again.

  body = {"command": "del_account"}
  
  

  




