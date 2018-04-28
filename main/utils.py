import main
import re


class RequestData(object):
    
    def request_data(self):
        """
        Returns a dictionary that can be passed to the `self.client` of
        `flask.ext.testing.TestCase` as the request data.
        """
        pass

def route_exists(route):
    return route in map(lambda r: r.rule, main.main.url_map.iter_rules())
