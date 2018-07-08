#!/bin/bash

for component in "client" "control" "viewer"; do
  sudo eopkg bi --ignore-safety  $component/pspec.xml
  sudo eopkg it --ignore-safety fah${component}*.eopkg
done
