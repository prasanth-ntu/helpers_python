# Tensorflow Notes

## Useful Notes
### Disable Tensorflow debugging information

We can disable all debuggin logs using `os.environ`:
```
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
```

Tested on *tf 1.5*

In details,
```
0 = all messages are logged (default behavior)
1 = INFO messages are not printed
2 = INFO and WARNING messages are not printed
3 = INFO, WARNING, and ERROR messages are not printed
```
Reference:
[Stack Overflow - Disable Tensorflow debugging information](https://stackoverflow.com/questions/35911252/disable-tensorflow-debugging-information/42121886)
