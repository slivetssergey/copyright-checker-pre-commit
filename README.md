# pre-commit-hooks

## Requirements

Install and configure [pre-commt](https://pre-commit.com/#install).

## Check commit message

This pre-commit hook serve checking commit message.

### Dependencies
Required dependency installation [commit-msg](https://pre-commit.com/#pre-commit-for-commit-messages)


```bash
pre-commit install --hook-type commit-msg
```

### Usage

Add commit message checker to `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/slivetssergey/pre-commit-hooks
    rev: latest
    hooks:
      - id: commit-message
        name: check commit message
        args: [
            '--min_length', '10',
            '--max_length', '100',
        ]
```

Params:
- --pattern - optional. regex pattern for checking commit message
- --min_length - optional. Minimal message length
- --max_length - optional. Maximum message length

## Copyright checking

This pre-commit hook serve checking copyright in files.
Works with multiline copyright. Works with shebang and allow usage of python regular expressions.

### Usage

Add copyright checker to `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/slivetssergey/pre-commit-hooks
    rev: latest
    hooks:
    -   id: copyright
        name: copyright python
        types: [ python ]
        args: [ --copyright=copyright_py.txt ]
```

for checking your python files or

```yaml
-   repo: https://github.com/slivetssergey/pre-commit-hooks
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
