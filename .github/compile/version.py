import json
import os
import re
print(os.environ["MSG"])
rb = re.split("^[^\n]+\n\n", json.loads(os.environ["MSG"])[-1])