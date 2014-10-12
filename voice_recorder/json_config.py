import json


# noinspection PyMethodMayBeStatic
class JsonConfig(object):
    def get(self, key, default_value=None):
        config = self.get_config()
        if key in config:
            return config[key]
        else:
            return default_value

    def get_config(self):
        try:
            f = open("config.json", "r")
            res = json.load(f)
            f.close()
        except IOError:
            res = {}
        except ValueError:
            res = {}
        return res

    def set(self, key, value):
        config = self.get_config()
        config[key] = value
        self.save_config(config)

    def save_config(self, config_dict):
        f = open("config.json", "w")
        res = json.dumps(config_dict, indent=4)
        f.write(res)
        f.close()