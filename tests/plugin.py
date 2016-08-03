import os
from tempest.test_discover import plugins


class NeutronStagingTempestPlugin(plugins.TempestPlugin):
    def load_tests(self):
        base_path = os.path.split(os.path.dirname(
            os.path.abspath(__file__)))[0]
        test_dir = "neutron-tempest-staging/tests/tempest/"
        full_test_dir = os.path.join(base_path, test_dir)
        return full_test_dir, base_path

    def register_opts(self, conf):
        pass

    def get_opt_lists(self):
        pass
