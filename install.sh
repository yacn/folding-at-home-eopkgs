#!/bin/bash

for component in "client" "control" "viewer"; do
  sudo eopkg bi --ignore-safety  $component/fah${component}*.eopkg
  sudo eopkg it --ignore-safety $component/fah${component}*.eopkg
done
