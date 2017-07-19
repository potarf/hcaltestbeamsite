#!/bin/bash
for run in $(ls hcaltestbeam/rawdata/ | sed -n 's/HTB_//' | sed -n 's/.root//'); do
    echo $run
done

