# BS4 - IMDB Upcoming Movies

A simple web scraping script which collates data for upcoming films for the current month from IMDB, and stores this into a .csv file.

This script is can be scheduled to run each month if scheduled (Windows Scheduler / Crontab). The url has been optimised to change each month based on current date.

Once this script has been executed, this will create a .csv file in the same directory the script has been exectuted. This will the data with the following headers:

``` imdb-upcoming-films-YYYY-MM ```

* Title
* Length
* Description
