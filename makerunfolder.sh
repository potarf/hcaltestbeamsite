#!/bin/bash
for run in $(ls hcaltestbeam/rawdata | sed 's/HTB_\(.*\)\.root/\1/'); do
  if [ ! -d "hcaltestbeam/runs/$run" ]; then
    mkdir hcaltestbeam/runs/$run
  fi
done

