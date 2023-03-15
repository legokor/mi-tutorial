# Hydra
> *A framework for elegantly configuring complex applications*

Hydra's key features:
- Hierarchical configuration composable from multiple sources
- Configuration can be specified or overridden from the command line
- Run multiple jobs with different arguments with a single command
- YAML configuration files
- Atomatically sets up logging to consele and file, can be overridden


Override the config parameters with command line arguments:
```sh
python src\mypackage\mymodule.py sub_config.sub_variable=z
```

Use different sub-configuration:
```sh
python src\mypackage\mymodule.py sub_config=my_subconfig_y
```

For details and more features, see [Hydra's documentation](https://hydra.cc/docs/intro/).