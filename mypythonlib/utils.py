import os

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)  