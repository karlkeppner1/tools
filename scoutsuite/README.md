parse_findings.py will output the findings to standard out in the following format for easy reference  
```
<service>
  <rule> : <level>
    <finding(s)>
```  

usage:  
./parse_findings.py <scoutsuite_results.js> [<severity_filter>]  
python3 parse_findings.py <scoutsuite_results.js> [<severity_filter>]  

ARGS:  
&nbsp;&nbsp;scoutsuite_results.js (required)  
&nbsp;&nbsp;&nbsp;&nbsp;relative or absolute path to .js output from scoutsuite, typically found in scoutsuite-results dirctory  
&nbsp;&nbsp;severity_filter (optional)  
&nbsp;&nbsp;&nbsp;&nbsp;danger  
&nbsp;&nbsp;&nbsp;&nbsp;warning  