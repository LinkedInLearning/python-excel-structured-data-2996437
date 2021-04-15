
import os
import json
try:
    print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
        
except Exception as e:
    print(e)
