---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Cardano Transaction Tools ![PyPI - Python Version](https://img.shields.io/badge/python-%3E%3D3.8-blue)

<br />

**Table of contents**

- [Transaction Vizualisation](#Transaction-Vizualisation)

<br />


## Transaction Vizualisation

```python
from IPython.display import SVG
from cardano_tx import transaction as tx

TX_FILE="tests/test-files/tx-files/txMetadata.signed"
SAVE_TO="tests/flow-chart/txMetadata.svg"

# Create the transaction flow chart
tx.vizualisation(txFile=TX_FILE, saveTo=SAVE_TO)

# Show the transaction flow chart
SVG(SAVE_TO)
```

