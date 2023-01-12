# rescuetime-to-sqlite

Save data from RescueTime to a SQLite database

## Install

```console
foo@bar:~$ pip install -e git+https://github.com/myles/rescuetime-to-sqlite.git#egg=rescuetime-to-sqlite
```

## Authentication

First you will need to create an application at Micro.blog.

```console
foo@bar:~$ poetry run rescuetime-to-sqlite auth
Create a new API key here: https://www.rescuetime.com/anapi/manage
Paste the API key in the following:

Key: xxx
```

## Retrieving RescueTime analytic data

The `analytic-data` command will retrieve all the analytic data from RescueTime.

```console
foo@bar:~$ rescuetime-to-sqlite analytic-data rescuetime.db
```

## Retrieving RescueTime daily summary feed

The `daily-summary-feed` command will retrieve all the daily summary feed 
from RescueTime.

```console
foo@bar:~$ rescuetime-to-sqlite daily-summary-feed rescuetime.db
```
