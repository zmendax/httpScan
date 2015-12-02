#!/bin/bash 

for i in {1000..8000..1}
do
    let t=70200000+$i
    echo $t >> `find . -name userpass`
done
