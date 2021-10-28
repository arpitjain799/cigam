cigam ![Maintenance](https://img.shields.io/maintenance/no/2021?style=for-the-badge)
===================

类型检测库，不再维护。

后续将使用：https://gitee.com/kin9-0rz/pyftype

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

