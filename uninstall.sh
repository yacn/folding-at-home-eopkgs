#!/bin/bash

for component in "client" "control" "viewer"; do
  sudo eopkg remove fah$component
done
