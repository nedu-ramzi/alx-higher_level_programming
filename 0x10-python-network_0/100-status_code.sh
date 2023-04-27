#!/bin/bash
# script that sends a request to a URL passed as an argument, and displays only the status code of the response
# >/dev/null part redirects the response body to the null device, since we only care about the headers and not the body.
# -o option specifies the output file.
# -w option specifies the format for the output
# -s option suppresses the progress meter and other non-error messages
curl "$1" -w "%{http_code}" -so /dev/null
