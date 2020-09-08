# python-rdrsegmenter

A Python wrapper for [RdrSegmenter](https://github.com/datquocnguyen/RDRsegmenter) using Pyjnius

## Table Of Contents

  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Example](#example)

## Prerequisites

- Java 1.8+ ([JRE](http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html) or [JDK](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html))

## Installation

You can install this package from PyPI using [pip](http://www.pip-installer.org):

```
$ pip install python-rdrsegmenter
```

## Example

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
from python_rdrsegmenter import load_segmenter
segmenter = load_segmenter()
segmenter.tokenize("Tôi là chàng sinh viên Bách Khoa")
```
