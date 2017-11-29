cigam
===================

Determine file type using magic numbers.



### Install

```
pip install cigam
```

### Usage

```python
from cigam import Magic

m = Magic('test.dex')
print(m.get_type())
print(m.get_extension())
print(m.get_mime())
```

