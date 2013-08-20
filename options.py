#!/usr/bin/python
from option import Option

class OptionList:

    def parse_options_to_obj_list(self, options):
        list=[];
        parts=options.split('; ');
        for itemOption in parts:
            option=Option();
            option.parse_optionobj_from_option(itemOption);
            list.append(option);
        self.optionlist=list;
        return self.optionlist;

    def print_option_list(self):
        for optionobj in self.optionlist:
            optionobj.print_optionobj();
            
            
