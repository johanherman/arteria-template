import arteria
import tornado.web
from arteria.web.handlers import BaseRestHandler
from template import __version__ as template_version


class BaseTemplateHandler(BaseRestHandler):
    """ Provides core logic for Template handlers
    """
    def initialize(self, config_svc):
        """ Stores the config service received from start() in app.py
        """
        self.config_svc = config_svc

    def append_status_link(self, wrapper):
        wrapper.info.link = self.create_status_link(wrapper.type_txt,
                                                    wrapper.info.pid)

    def create_status_link(self, wrapper, pid):
        return "%s/%s/status/%s" % (self.api_link(), wrapper, pid)


class EchoHandler(BaseTemplateHandler):
    """ Our handler for checking echoing the input plus a value
		from the config file. 
    """
    def get(self, echostring):
        """ Print out the echostring together with a string from the config file. 

                Args:
                    echostring: The string to echo back
                    Or empty if only the config string should be returned

                Returns:
                    JSON with fields containing the echostring and config string, 
					as well as current version of the service. 
        """
        try:
            conf = self.config_svc.get_app_config()
            txt = conf["example_echo_string"]

            if echostring:
                txt = "Conf says: " + txt + " And you said: " +  echostring

            self.write_object({'msg': txt})
        except RuntimeError, err:
            raise tornado.web.HTTPError(500, "An error occurred: {0}".format(str(err)))
