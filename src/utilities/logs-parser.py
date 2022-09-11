import os


class LogParser:
    """
    Generic log parser class for log files
    """
    
    def __init__(self, config):
        """
        LogParser Class initializer.

        config [dict]: It contains LogParser configuration
        
        example:
        {
            source: zookeeper | file,
            file_path: /etc/lomo/config.json
            zk_hostL localhost
        }
        """
        pass

    def load_configuration(self, source):
        """
        It will load configuration using the provided source. Configuration can be loaded from following sources:

        1. Config file.
        2. Zookeeper.
        """
        pass 

