#!/usr/bin/python
import re

class Option:
    def get_title(self, option):
        parts=option.split(':');
        self.title= parts[0];
        return self.title;
    
    def get_value(self, option):
        parts=option.split(':');
        self.title= parts[0];
        if (parts[1] == '\"Host\\'):
            self.title ='Host'
            self.value =parts[2].split('|')[0];
        else:
            self.value= parts[1];
        return self.value;

    def parse_optionobj_from_option(self,option):
        parts=option.split(':');
	if (parts[1]=='\"Host\\'):
		self.title = 'Host';
		self.value = parts[2].split('|')[0];
        else:
		self.title=parts[0];
            	self.value=parts[1];
        
    def print_title(self):
        print 'title=',self.title;
    
    def print_value(self):
        print 'value=',self.value;
    
    def print_optionobj(self):
        print self.title,'=',self.value;
            
            
