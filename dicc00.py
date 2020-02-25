tickets={'4105505664': ['g_battlefield', 'c_isp'],
 '4097533527': ['g_nba', 'c_crash'],
 '4097528257': ['g_fifa', 'c_crash'],
 '4098283140': ['g_fifa', 'c_network'],
 '4098273356': ['g_madden', 'c_network'],
 '4097123527': ['g_fifa', 'c_crash'],
 '4197528257': ['g_fifa', 'c_isp'],
 '4094283140': ['g_fifa', 'c_network'],
 '4098863356': ['g_madden', 'c_network'],
        }

games_list=['g_fifa','g_nba','g_madden','g_skate','g_battlefield','g_ncaa','g_pvz','g_battlefron']
cause_list=['c_crash','c_isp','c_network','c_external','c_bd','c_unknown']


#x = { list(tickets.values())[0][1] : list(tickets.keys())[0]}

#x = { list(tickets.values())[0][1] : list(tickets.keys())[6]}
x = {}

for i in range(len(list(tickets))):
    if 'c_crash' == list(tickets.values())[i][1]:
        x["c_crash"].append(list(tickets.keys())[i])

