#flake8:noqa
import json
# -- read -- 


stats = {'players':[]}
stats_2 = {}

def new_player_list(identifier,name,wins,loses):
	global stats
	player = {'id':identifier, 'name':name, 'wins':wins, 'loses':loses}
	stats['players'].append(player)

def new_player(identifier,name,wins,loses):
	global stats_2
	new_player_dict = {'name':name, 'wins':wins, 'loses':loses}
	stats_2[identifier] = new_player_dict

#observe the behavior of adding 2 guys with same id using list and just dictionaries.

new_player_list(10030,'skyr',10,5)
new_player_list(10030,'nooblet',10,5)
new_player_list(10028,'zezima',10,5)
new_player_list(10027,'zenos',10,5)
new_player_list(10026,'pandasidi',10,5)

print "Using List in json:"
# print stats,"\n\n"
print json.dumps(stats),"\n\n"

new_player(10030,'skyr',10,5)
new_player(10030,'nooblet',10,5)
new_player(10028,'zezima',10,5)
new_player(10027,'zenos',10,5)
new_player(10026,'pandasidi',10,5)

print "Using just dictionaries:"
# print stats_2,"\n\n"
print json.dumps(stats_2)


