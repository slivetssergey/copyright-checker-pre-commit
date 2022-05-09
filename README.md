# pre-commit-hooks

## Requirements

Install and configure [pre-commt](https://pre-commit.com/#install).

## Check commit message

## Copyright checking

This pre-commit hook serve checking copyright in files.
Works with multiline copyright. Works with shebang and allow usage of python regular expressions.

### Usage

Add copyright checker to `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/slivetssergey/copyright-checker-pre-commit
    rev: latest
    hooks:
    -   id: copyright
        name: copyright python
        types: [ python ]
        args: [ --copyright=copyright_py.txt ]
```

for checking your python files or

```yaml
-   repo: https://github.com/slivetssergey/copyright-checker-pre-commit
    rev: latest
    hooks:
    -   id: copyright
        name: copyright javascript
        types: [ javascript ]
        args: [ --copyright=copyright_js.txt ]
```

for checking js scripts.

See more params on [configure hooks](https://pre-commit.com/#pre-commit-configyaml---hooks).

Add a file with copyright text content. You can use multiline text with python regular expressions.
```text
# Copyright (C) 202[0-9]
```
