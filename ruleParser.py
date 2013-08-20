#!/usr/bin/python
from fields import Fields
from options import OptionList
from result import RuleFields

def get_header_options_from_line(s):
	parts = s.split('(');
	header = parts[0];
	options = parts[1].split(';)')[0];
	return header,options;

def get_fields_from_header(header):
	fields = header.split(' ');
	return fields;

def get_field_list_from_header(result,header):
	fields = header.split(' ');
	result['header_action'] = fields[0];
	result['header_protocol'] = fields[1];
	result['header_sourceIP'] = fields[2];
	result['header_sourcePort'] = fields[3];
	direction = fields[4];
	if direction=='->':
		result['header_direction'] = 1
	elif direction=='<->':
		result['header_direction']=0
	else:
		result['header_direction']=-1;
	result['header_destIP'] = fields[5];
	destPorts = fields[6];
	if '[' in destPorts:
		destPorts = fields[6].split('[');
		destPorts = destPorts[1].split(']');
		destPorts = destPorts[0];
		ports=destPorts.split(',');
		result['header_destPorts'] = ports;
	else:
		result['header_destPorts'] = destPorts;

def print_fields(result):
    print "header_action=",result['header_action'];
    print "header_protocol=",result['header_protocol'];
    print "header_sourceIP=", result['header_sourceIP'];
    print "header_sourcePort=",result['header_sourcePort'];
    print "header_direction=", result['header_direction'];
    print "header_destIP=", result['header_destIP'];
    print "header_destPort=",result['header_destPorts'];

def parse_optionobj_from_option(option):
	option=option.strip();
	print 'option=',option;
	parts=option.split(':');
	if (parts[1]=='\"Host\\'):
		title = 'Host';
		value = parts[2].split('|')[0];
	else:
		title=parts[0];
		value=parts[1];
	return title,value;

def parse_options_to_obj_list(result, options):
	parts=options.split('; ');
	contentList=[];
	for itemOption in parts:
		print "**************";
		print itemOption;
		print "**************";
		if (itemOption != ""):
			title, value=parse_optionobj_from_option(itemOption);
			if (title=='content'):
				contentList.append(value);
			else:
				result[title]=value;
	if (contentList !=[]):	
		result['content']=contentList;


def parse_options_to_key_value(result, options):
	parts=options.split('; ');
	optionMap={};
	for itemOption in parts:
		if (itmeOption != None):
			key, value=parse_key_value_pair_from_option(itemOption);
			print "key=",key;
			print "value=",value;
			if optionMap.has_key(key):
				val=optionMap[key];
			else:
				val=[];
			print val;
			val=val.append(value);
			print val;
			optionMap[key]=val;
	for key,value in optionMap.iteritems():
		result[key] = value;

def process_rule_file(filename):
	f = open(filename,'r');
	if f is None:
		print 'error: no such file: ', filename;
		return none;
	allresult={};
	for line in f:
		result={};
		header,options = get_header_options_from_line(line);
		print '------------rule---------';
		get_field_list_from_header(result,header);
		parse_options_to_obj_list(result,options);
		sid = result['sid'];
		allresult[sid]=result;
		print_rule(result);
	#print allresult;
	return allresult;

def print_rule(ruledic):
	for key, value in ruledic.iteritems():
		print key,"= ",value;

def get_rule_by_id(filename,id):
	res=process_rule_file(filename);
	if res is None:
		return None;
	r=res[id];
	if r is None:
		print 'error: id= ',id,' is not valid!';
		return None;
	print_rule(r);
	return r;

def get_field_by_id(filename,id,fieldname):
	res=get_rule_by_id(filename,id);
	if res is None:
		print 'error: id= ',id,'not exists';
		return None;
	else:
                print fieldname,"=",res[fieldname];
                return res[fieldname];

# example of parsing the rule file #
print '-----------------';
res=process_rule_file('snort_rules_example.rules');
#example of getting one rule obj#
print '------------------';
r= res['83626548'];
# example of getting one field of one rule from the rule file #
print '-------------------';
print res['83626548']['header_protocol'];
#example of print one rule#
print '--------------------';
print res['83626548'];
#example of getting one field from one rule obj resulting from rule file#
print '---------------------';
get_field_by_id('snort_rules_example.rules','83626548','header_action');


