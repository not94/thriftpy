# -*- coding:utf-8 -*-


class ThriftDocHelper(object):

    def __init__(self, service):
        self.service = service
        self.args_map = {}
        self.result_map = {}
        for func in service.thrift_services:
            self.args_map[func] = getattr(service, func + "_args")
            self.result_map[func] = getattr(service, func + "_result")

    def should_generate_doc(self):
        pass

    def generate_doc(self):
        pass
