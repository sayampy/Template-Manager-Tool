# A cli Project
## Installation
```bash
$ pip install templater
```

## Usages
### Checking version
`tmt -V` | `tmt --version`
### creating template
`tmt new <template_name> <Dir Path| type:path; Default:current path>`
```bash
$ ls
main.py
module
requirements.txt

$ tmt new mymodule ./module
/usr/module successfully Init as Template, "mymodule"
```
### loading template
`tmt load <[project_name | type:non-existing path]> <template_name>`
```bash
$ ls myprojects

$ tmt load myprojects/new mymodule
template mymodule successfully loaded on myprojects/new dir
$ ls myprojects
new
```
### show current available templates
`tmt show`
```bash
$ tmt show
python
mymodule
```
### removing template
`tmt remove <template_name> [--confirm -c [yes|no] | required: False]`
```bash
$ tmt remove mymodule
Confirmation[yes/no]: yes
mymodule template successfully removed
```
## Visit Urls
+ **[Visit Github Repo](https://github.com/sayampy/Template-Manager-Tool/)**
+ **[tell your Issues](https://github.com/sayampy/Template-Manager-Tool/issues)**
