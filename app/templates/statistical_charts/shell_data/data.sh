#!/bin/bash

mysql -N -u'root' -p'passwd' -h'192.168.0.160' <<EOF
use oj;
select solution_id from solution order by sub_time desc limit 1;
EOF
