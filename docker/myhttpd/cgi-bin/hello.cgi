#!/bin/bash
echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'

# PATH="/bin:/usr/bin:/usr/ucb:/usr/opt/bin"
# export $PATH

echo '<title>System Uptime</title>'
echo '</head>'
echo '<body>'

echo "<h3> host: $(hostname) </h3>"
echo "<h3> date: $(date) </h3>"
echo "<h3> uptime: $(uptime) </h3>"

echo '</body>'
echo '</html>'

exit 0
