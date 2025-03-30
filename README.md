# micropython-localtime
<br>
Get real localtime with 'Summer' and 'Winter' time change<br>
<br>
This replaces the <code><strong>time.localtime()</strong></code> function by returning the actual value of the local time and date,<br>
with support for 'summer' and 'winter' time changes.<br>
<br>
Simply place the 'time.py' file in your project directory.<br>
<strong>It is imperative to keep the filename 'time.py'</strong>.<br>
<br>
In your source code, simply place:<br>
<code><strong>import time</strong></code><br>
or<br>
<code><strong>from time import localtime</strong></code><br>
<br>
All other '<strong>time</strong>' functions are also accessible, except that the '<strong>localtime</strong>' function is replaced by the new<br>
function in the '<strong>time.py</strong>' file.<br>
