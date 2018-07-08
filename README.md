# Folding @ Home Solus eopkg configs

eopkg configuration files for installing Folding @ Home Client, Control, and Viewer
on Solus.

## install:

```sh
./install.sh
# runs:
for component in "client" "control" "viewer"; do
  sudo eopkg bi --ignore-safety  $component/pspec.xml
  sudo eopkg it --ignore-safety $component/fah${component}*.eopkg
done
```

# uninstall:

```sh
./uninstall.sh
# runs:
for component in "client" "control" "viewer"; do
  sudo eopkg remove fah$component
done
```
