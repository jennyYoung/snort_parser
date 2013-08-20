#!/usr/bin/python

class Fields:
	def get_field_list_from_header(self,header):
		fields = header.split(' ');
		result['action'] = fields[0];
		result['protocol'] = fields[1];
		result['sourceIP'] = fields[2];
		result['sourcePort'] = fields[3];
	        result['direction'] = fields[4];
        	if direction=='->':
            		result['direction'] = 1
        	elif direction=='<->':
            		result['direction']=0
        	else:
            		result['direction']=-1;
        	result['destIP'] = fields[5];
		destPorts = fields[6].split('[');
		destPorts = destPorts[1].split(']');
		destPorts = destPorts[0];
		ports=destPorts.split(',');
		result['destPorts'] = ports;

	def print_fields(self):
		print "action=",self.action;
		print "protocol=",self.protocol;
		print "sourceIP=", self.sourceIP;
		print "sourcePort=",self.sourcePort;
		print "direction=", self.direction;
		print "destIP=", self.destIP;
		print "destPort=",self.destPorts;

		
