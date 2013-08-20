#!/usr/bin/python

class RuleFields:
	def set_fields_from_header(self,action, protocol, sourceIp, sourcePort, direction, destIP, destPorts):
		self.action = action;
		self.protocol = protocol;
		self.sourceIP = sourceIp;
		self.sourcePort = sourcePort;
		self.direction = direction;
		self.destIP = destIP;
		self.destPorts = destPorts;

	def set(self,fieldName,fieldValue):
		if (fieldName == 'action'):
			self.action=fieldValue;
		elif (fieldName == 'protocol'):
			self.protocol=fieldValue;
		elif (fieldName =='sourceIP'):
			self.sourceIP=fieldValue;
		elif (fieldName == 'sourcePort'):
			self.sourcePort=fieldValue;
		elif (fieldName == 'direction'):
			self.direction=fieldValue;
		elif (fieldName =='destIP'):
			self.destIP=fieldValue;
		elif (fieldName == 'destPorts'):
			self.destPorts=fieldValue;
		elif (fieldName == 'sid'):
			self.sid=fieldValue;
		elif (fieldName == 'rev'):
			self.rev=fieldValue;
		elif (fieldName =='msg'):
			self.msg=fieldValue;
		elif (fieldName == 'contenthost'):
			self.contenthost=fieldValue;
		elif (fieldName == 'content'):
			self.content=fieldValue;
                else:
                    print 'error: no such field: ',fieldName;

	def get(self,fieldName):
		if (fieldName == 'action'):
			return self.action;
		elif (fieldName == 'protocol'):
			return self.protocol;
		elif (fieldName =='sourceIP'):
			return self.sourceIP;
		elif (fieldName == 'sourcePort'):
			return self.sourcePort;
		elif (fieldName == 'direction'):
			return self.direction;
		elif (fieldName =='destIP'):
			return self.destIP;
		elif (fieldName == 'destPorts'):
			return self.destPorts;
		elif (fieldName == 'sid'):
			return self.sid;
		elif (fieldName == 'rev'):
			return self.rev;
		elif (fieldName =='msg'):
			return self.msg;
		elif (fieldName == 'contenthost'):
			return self.contenthost;
		elif (fieldName == 'content'):
			return self.content;
		else:
			print 'error: no such field: ', fieldName;
			return None;
    
	def set_options(self, sid, rev, msg, host,content):
		self.sid = sid;
		self.rev = rev;
		self.msg = msg;
		self.contenthost = host;
		self.content = content;
            
	def set_action(self,action):
		self.action = action;

	def get_action(self):
		return self.action;

	def set_protocol(self,protocol):
		self.protocol=protocol;

	def get_protocol(self):
		return self.protocol;

	def set_sourceIP(self,sourceIP):
		self.sourceIP=sourceIP;

	def get_sourceIP(self):
		return self.sourceIP;

        def set_sourcePort(self, sourcePort):
		self.sourcePort=sourcePort;
	
	def get_sourcePort(self):
		return self.sourcePort;
        
	def set_direction(self, direction):
                self.direction = direction;

	def get_direction(self):
		return self.direction;

	def set_destIP(self,destIP):
                self.destIP = destIP;

	def get_destIP(self):
		return self.destIP;
	
	def set_destPorts(self, destPorts):
                self.destPorts = destPorts;

	def get_destPorts(self):
		return self.destPorts;

	def set_options(self, sid, rev, msg, host,content):
		self.sid = sid;
		self.rev = rev;
		self.msg = msg;
		self.contenthost = host;
		self.content = content;

	def set_sid(self,sid):
		self.sid = sid;

	def get_sid(self):
		return self.sid;

	def set_rev(self,rev):
		self.rev = rev;

	def get_rev(self):
		return self.rev;

	def set_msg(self,msg):
		self.msg = msg;

	def get_msg(self):
		return self.msg;
	
	def set_contenthost(self,host):
		self.contenthost = host;

	def get_contenthost(self):
		return self.contenthost;

	def set_content(self,content):	
		self.content = content;

	def get_content(self):
		return self.content;

	def print_fields(self):
		print "action=",self.action;
		print "protocol=",self.protocol;
		print "sourceIP=", self.sourceIP;
		print "sourcePort=",self.sourcePort;
		print "direction=", self.direction;
		print "destIP=", self.destIP;
		print "destPorts=",self.destPorts;

	def print_options(self):
		print "sid=",self.sid;
		print "rev=",self.rev;
		print "msg=", self.msg;
		print "host=",self.contenthost;
		print "content=", self.content;

	def print_rule(self):
		self.print_fields();
		self.print_options();


