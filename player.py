from collections import Counter

nums = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, "A": 14, "Z": 15}


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.tuple_hand = []

    def new_deal(self):
        self.hand = []
        self.tuple_hand = []

    def set_cards(self, hand):
        self.hand.append(hand)
        if len(self.hand) == 7:
            for card in self.hand:
                self.tuple_hand.append((nums[card[0]], card[1]))

    @staticmethod
    def most_frequent(lst):
        data = Counter(lst)
        return data.most_common(1)[0]

    @staticmethod
    def second_most_frequent(lst):
        data = Counter(lst)
        return data.most_common(2)[-1]

    @staticmethod
    def get_suits(hand):
        rs = []
        for card in hand:
            rs.append(card[1])
        return rs

    @staticmethod
    def get_number(hand):
        rs = []
        for card in hand:
            rs.append(nums[card[0]])
        return rs

    def is_straight_flush_Z(self):
        if ([x[0] for x in self.tuple_hand if (15) in x]):
            list_without_15 = [item for item in self.tuple_hand if (15) not in item]
            sorted(self.tuple_hand, key=lambda card: card[0], reverse=True)
            p_sf = self.most_frequent(self.get_suits(self.tuple_hand))
            
            if p_sf[1] >= 4:
                p_sf_hand_set = [item for item in list_without_15 if (p_sf[0]) in item]
                p_sf_hand = sorted(set([x[0] for x in p_sf_hand_set]))

                rh = [] 
                es = [11, 12, 13, 14]
                bs = [2, 3, 4, 5, 14]


                if (all(x in (p_sf_hand) for x in es)) is True:
                    
                    for x in range (0, 4):
                        true_hand = [item for item in p_sf_hand_set if (es[x]) in item]
                        rh.append(true_hand)

                    rh = [val for sublist in rh for val in sublist]
                    rh = rh + [(15, '⦿')]
                    return True, rh, 0
                
                if (all(x in (p_sf_hand) for x in bs)) is True or sum(map(lambda x: x in p_sf_hand, bs)) == 4:

                    result = []
                    
                    for x in range (0, 5):
                        true_hand = [item for item in p_sf_hand_set if (bs[x]) in item]
                        result.append(true_hand)


                    last = [elem if elem else [('Z', '⦿')] for elem in result]
                    rh = [val for sublist in last for val in sublist]
                    return True, rh, 0             

                else:
                    missing_numbers = [item for item in set(range(1, 15)) if item not in p_sf_hand]
                    list_of_p_straights = []
                    list_of_p_straight_hands = []
                    list_of_straight_sets = []

                    for x in reversed(range(len(missing_numbers))):
                        missing_individual_numbers = [(missing_numbers[x])]
                        p_straights = list(sorted(missing_individual_numbers + p_sf_hand))
                        list_of_p_straights.append(p_straights)

                    for list_of_p_straights in list_of_p_straights:
                        for start_index in range(len(list_of_p_straights) - 4):
                            end_index = start_index + 5
                            sublist = list_of_p_straights[start_index:end_index]
                            list_of_p_straight_hands.append(sublist)
                    
                    for n in range(2, 11):
                        straight_set = list(set(range(n, n+5)))
                        list_of_straight_sets.append(straight_set)

                    straight_hands = [x for x in list_of_p_straight_hands if x in list_of_straight_sets]

                    if len(straight_hands) >= 1:
                        highest_hand = (max(map(lambda x: x, straight_hands)))

                        result = []
                        
                        for x in range (0, 5):
                            true_hand = [item for item in p_sf_hand_set if (highest_hand[x]) in item]
                            result.append(true_hand)

                        last = [elem if elem else [('Z', '⦿')] for elem in result]
                        rh = [val for sublist in last for val in sublist]
                        sh = sorted(highest_hand, reverse=True)
                        ranks = '%02d%02d%02d%02d%02d' % (tuple([x for x in sh]))
                        ranks = float(f'0.{ranks}')

                        return True, rh, ranks
                    return False, [], []
            else:
                return False, [], []          
        return False, [], []

    def is_straight_Z(self):
        if ([x[0] for x in self.tuple_hand if (15) in x]):
            list_without_15 = [item for item in self.tuple_hand if (15) not in item]
            pure_list = sorted(set([x[0] for x in list_without_15]))
            #because straight doesn't go up to 15
            rh = []

            # back_straight_check
            bs = [2, 3, 4, 5, 14]
            if (all(x in (pure_list) for x in bs)) is True or sum(map(lambda x: x in pure_list, bs)) == 4:
                seen = set()
                keep = []
                for num, suit in self.tuple_hand:
                    if num in seen:
                        continue
                    else:
                        seen.add(num)
                        keep.append((num, suit))

                self.tuple_hand = keep
                
                for x in range (0, 5):
                    true_hand = [item for item in self.tuple_hand if (bs[x]) in item]
                    rh.append(true_hand)
            
                rh = [elem if elem else [('Z', '⦿')] for elem in rh]
                rh = [val for sublist in rh for val in sublist]
                return True, rh, 0.1
            
##                suits = [x[-1] for x in rh]
##                data = Counter(suits)
##                p_sf = self.most_frequent(1)[0]
##
##                if p_sf[1] == 5:
##                    return True, rh
##                
##                if p_sf[1] == 4:
##                    sf_hand = [item for item in rh if (p_sf[0]) in item]
##                    rh = []
##                    for x in range (0, 5):
##                        true_hand = [item for item in sf_hand if (bs[x]) in item]
##                        rh.append(true_hand)
##
##                    rh = [elem if elem else [('Z', '⦿')] for elem in rh]
##                    rh = [val for sublist in rh for val in sublist]
    
            else:
                missing_numbers = [item for item in set(range(1, 15)) if item not in pure_list]
                list_of_p_straights = []
                result = []
                list_of_p_straight_hands = []
                list_of_straight_sets = []

                for x in reversed(range(len(missing_numbers))):
                    missing_individual_numbers = [(missing_numbers[x])]
                    p_straights = list(sorted(missing_individual_numbers + pure_list))
                    list_of_p_straights.append(p_straights)

                for list_of_p_straights in list_of_p_straights:
                    for start_index in range(len(list_of_p_straights) - 4):
                        end_index = start_index + 5
                        sublist = list_of_p_straights[start_index:end_index]
                        list_of_p_straight_hands.append(sublist)
                
                for n in range(2, 11):
                    straight_set = list(set(range(n, n+5)))
                    list_of_straight_sets.append(straight_set)

                straight_hands = [x for x in list_of_p_straight_hands if x in list_of_straight_sets]

                if len(straight_hands) >= 1:
                    highest_hand = (max(map(lambda x: x, straight_hands)))
                    seen = set()
                    keep = []
                    for num, suit in self.tuple_hand:
                        if num in seen:
                            continue
                        else:
                            seen.add(num)
                            keep.append((num, suit))
                            
                    self.tuple_hand = keep
                
                    for x in range (0, 5):
                        true_hand = [item for item in self.tuple_hand if (highest_hand[x]) in item]
                        rh.append(true_hand)

                    rh = [elem if elem else [('Z', '⦿')] for elem in rh]
                    rh = [val for sublist in rh for val in sublist]
                    sh = sorted(highest_hand, reverse=True)
                    ranks = '%02d%02d%02d%02d%02d' % (tuple([x for x in sh]))
                    ranks = float(f'0.{ranks}')
                    return True, rh, ranks
                return False, [], []
        return False, [], []


    def is_flush_Z(self):
    #Hand with 4 same suited cards will become "FLUSH"
        if ([x[0] for x in self.tuple_hand if (15) in x]):
            list_without_15 = [item for item in self.tuple_hand if (15) not in item]
            suit_counter = self.most_frequent(self.get_suits(list_without_15))
            
            if suit_counter[1] >= 4:
                is_f_hand_set = [item for item in self.tuple_hand if (suit_counter[0]) in item]
                is_f_hand_full_set = is_f_hand_set + [(15, '⦿')]
                is_f_hand = sorted(set([x[0] for x in is_f_hand_full_set]))
                flush_hands = []
                pure_list = sorted(set([x[0] for x in list_without_15]))
                missing_numbers = [item for item in set(range(1, 15)) if item not in pure_list]
                max_number = (max(missing_numbers))
                
                for start_index in range(len(is_f_hand) - 4):
                    end_index = start_index + 5
                    sublist = is_f_hand[start_index:end_index]
                    flush_hands.append(sublist)

                
                highest_hand = (max(map(lambda x: x, flush_hands)))

                rh = []

                for x in range (0, 5):
                    true_hand = [item for item in is_f_hand_set if (highest_hand[x]) in item]
                    rh.append(true_hand)

                
                rh = [elem if elem else [('Z', '⦿')] for elem in rh]
                rh = [val for sublist in rh for val in sublist]
                #accessing list
                sh = [x[0] for x in rh]
                sh[sh.index("Z")] = max_number
                sh = sorted(sh, reverse=True)
                ranks = '%02d%02d%02d%02d%02d' % (tuple([x for x in sh]))
                ranks = float(f'0.{ranks}')
                return True, rh, ranks
            return False, [], []              
        return False, [], []

    def is_4_kind_Z(self):
    #Four of a Kind with Z will become "FIVE OF A KIND"
        if ([x[0] for x in self.tuple_hand if (15) in x]):
            list_without_15 = [item for item in self.tuple_hand if (15) not in item]
            p_4 = self.most_frequent([a[:-1] for a in list_without_15])

            if p_4[1] == 4:
                quadriple = list(item for item in self.tuple_hand if p_4[0][0] in item)[:4]
                z = [('Z', '⦿')]
                rh = quadriple + z
                ranks = '%02d' % ([x[0] for x in rh][0])
                ranks = float(f'0.{ranks}')
                             
                return True, rh, ranks
            return False, [] , []
        return False, [], []
        
    def is_3_kind_Z(self):

    #Three of a Kind with Z will become "FOUR OF A KIND"
        if ([x[0] for x in self.tuple_hand if (15) in x]):
            list_without_15 = [item for item in self.tuple_hand if (15) not in item]
            p_3 = self.most_frequent([a[:-1] for a in list_without_15])

            if p_3[1] == 3:
                triple = list(item for item in self.tuple_hand if p_3[0][0] in item)[:3]
                r_nums = [item for item in list_without_15 if (triple[0][0]) not in item]
                h_num = sorted((r_nums), reverse=True)[:1]
                z = [('Z', '⦿')]
                rh = triple + z + h_num
                sh = (([x[0] for x in rh])[0:3])
                sh = ([(sh[0])] + sh + (([x[0] for x in rh])[4:5]))
                ranks = '%02d%02d%02d%02d%02d' % (tuple([x for x in sh]))
                ranks = float(f'0.{ranks}')
                
                return True, rh, ranks
            return False, [] , []
        return False, [], []

    def is_two_pair_Z(self):

    #Two Pair hand with Z will become "FULL HOUSE"

        if ([x[0] for x in self.tuple_hand if (15) in x]):
            pair1 = self.most_frequent([x[0] for x in self.tuple_hand])
            pair2 = self.second_most_frequent([x[0] for x in self.tuple_hand])

            if pair1[1] == 2 and pair2[1] == 2:

                rh = sorted(list(item for item in self.tuple_hand if (pair1[0]) in item or (pair2[0]) in item))[:5]
                rh = sorted(rh, reverse=True)
                pair1 = ((rh)[0:2])
                pair2 = ((rh)[2:4])
                z = [('Z', '⦿')]
                rh = pair1 + z + pair2
                sh = (([x[0] for x in rh])[0:2])
                sh = ([(sh[0])] + sh + (([x[0] for x in rh])[3:5]))
                ranks = '%02d%02d%02d%02d%02d' % (tuple([x for x in sh]))
                ranks = float(f'0.{ranks}')
                
                return True, rh , ranks          
            return False, [], []
        return False, [], []


    def is_pair_Z(self):

    #Pair hand with Z will become "THREE OF A KIND"
        if ([x[0] for x in self.tuple_hand if (15) in x]):
            pair = self.most_frequent([x[0] for x in self.tuple_hand])
            if pair[1] == 2:
                h = list(item for item in self.tuple_hand)
                find_Z = sorted((h), reverse=True)[:1]
                r_nums = [item for item in self.tuple_hand if (find_Z[0][0]) not in item]
                r_nums = [item for item in r_nums if (pair[0]) not in item]
                h_nums = sorted((r_nums), reverse=True)[:2]
                pair = list(item for item in self.tuple_hand if (pair[0]) in item)[:2]
                z = [('Z', '⦿')]
                rh = pair + z + h_nums
                sh = (([x[0] for x in rh])[0:2])
                sh = ([(sh[0])] + sh + (([x[0] for x in rh])[3:5]))
                ranks = '%02d%02d%02d%02d%02d' % (tuple([x for x in sh]))
                ranks = float(f'0.{ranks}')
                
                return True, rh, ranks
            return False, [], []
        return False, [], []


    def is_high_Z(self):

    #High hand with Z will become "ONE PAIR"
        if ([x[0] for x in self.tuple_hand if (15) in x]):
            h = list(item for item in self.tuple_hand)
            find_Z = sorted((h), reverse=True)[:1]
            r_nums = [item for item in self.tuple_hand if (find_Z[0][0]) not in item]
            h_nums = sorted((r_nums), reverse=True)[:4]
            z = [('Z', '⦿')]
            rh = z + h_nums
            sh = (([x[0] for x in rh])[1:5])
            sh = [sh[0]] + sh
            ranks = '%02d%02d%02d%02d%02d' % (tuple([x for x in sh]))
            ranks = float(f'0.{ranks}')
            
            return True, rh, ranks
        else:
            return False, [] , []         

    def is_straight_flush(self):

        sorted(self.tuple_hand, key=lambda card: card[0], reverse=True)
        is_sf = self.most_frequent(self.get_suits(self.tuple_hand))

        if is_sf[1] >= 5:
            is_sf_hand_set = [item for item in self.tuple_hand if (is_sf[0]) in item]
            is_sf_hand = sorted(set([x[0] for x in is_sf_hand_set]))

            rh = [] 
            bs = [2, 3, 4, 5, 14]
            
            if (all(x in (is_sf_hand) for x in bs)) is True:
                
                for x in range (0, 5):
                    true_hand = [item for item in is_sf_hand_set if (bs[x]) in item]
                    rh.append(true_hand)

                rh = [val for sublist in rh for val in sublist]
                ranks = 0
                return True, rh, ranks

            else:
                list_of_is_straight_hands = []
                list_of_straight_sets = []

                for start_index in range(len(is_sf_hand) - 4):
                        end_index = start_index + 5
                        sublist = is_sf_hand[start_index:end_index]
                        list_of_is_straight_hands.append(sublist)
                
                for n in range(2, 11):
                    straight_set = list(set(range(n, n+5)))
                    list_of_straight_sets.append(straight_set)

                straight_hands = [x for x in list_of_is_straight_hands if x in list_of_straight_sets]

                if len(straight_hands) >= 1:
                    
                    highest_hand = (max(map(lambda x: x, straight_hands)))
                    
                    for x in range (0, 5):
                        true_hand = [item for item in is_sf_hand_set if (highest_hand[x]) in item]
                        rh.append(true_hand)

                    rh = [val for sublist in rh for val in sublist]
                    sh = sorted(rh, reverse=True)
                    ranks = '%02d' % ([x[0] for x in sh][0])
                    ranks = float(f'0.{ranks}')

                    return True, rh, ranks
                return False, [], []
        return False, [], []          

    def is_straight(self):
        pure_list = sorted(set([x[0] for x in self.tuple_hand]))

        rh = []

        # back_straight_check
        bs = [2, 3, 4, 5, 14]
        if (all(x in (pure_list) for x in bs)) is True:
            seen = set()
            keep = []
            for num, suit in self.tuple_hand:
                if num in seen:
                    continue
                else:
                    seen.add(num)
                    keep.append((num, suit))
                
            self.tuple_hand = keep
            for x in range (0, 5):
                true_hand = [item for item in self.tuple_hand if (bs[x]) in item]
                rh.append(true_hand)

            rh = [val for sublist in rh for val in sublist]
            ranks = 0
            return True, rh, ranks
    
        else:
            list_of_is_straight_hands = []
            list_of_straight_sets = []

            for start_index in range(len(pure_list) - 4):
                    end_index = start_index + 5
                    sublist = pure_list[start_index:end_index]
                    list_of_is_straight_hands.append(sublist)
            
            for n in range(2, 11):
                straight_set = list(set(range(n, n+5)))
                list_of_straight_sets.append(straight_set)

            straight_hands = [x for x in list_of_is_straight_hands if x in list_of_straight_sets]

            if len(straight_hands) >= 1:
                seen = set()
                keep = []
                for num, suit in self.tuple_hand:
                    if num in seen:
                        continue
                    else:
                        seen.add(num)
                        keep.append((num, suit))
                    
                self.tuple_hand = keep
                
                highest_hand = (max(map(lambda x: x, straight_hands)))
                
                for x in range (0, 5):
                    true_hand = [item for item in self.tuple_hand if (highest_hand[x]) in item]
                    rh.append(true_hand)

                rh = [val for sublist in rh for val in sublist]
                sh = sorted(rh, reverse=True)
                ranks = '%02d' % ([x[0] for x in sh][0])
                ranks = float(f'0.{ranks}')

                return True, rh, ranks
            return False, [], []

    def is_flush(self):

        suit_counter = self.most_frequent(self.get_suits(self.tuple_hand))
        
        if suit_counter[1] >= 5:
            is_f_hand_set = [item for item in self.tuple_hand if (suit_counter[1]) in item]
            is_f_hand = sorted(set([x[0] for x in is_f_hand_set]))

            flush_hands = []
            
            for start_index in range(len(is_f_hand) - 4):
                end_index = start_index + 5
                sublist = is_f_hand[start_index:end_index]
                flush_hands.append(sublist)

            if len(flush_hands) >= 1:
                
                highest_hand = (max(map(lambda x: x, flush_hands)))
                seen = set()
                keep = []
                rh = []
                
                for num, suit in self.tuple_hand:
                    if num in seen:
                        continue
                    else:
                        seen.add(num)
                        keep.append((num, suit))
                        
                self.tuple_hand = keep

                for x in range (0, 5):
                    true_hand = [item for item in self.tuple_hand if (highest_hand[x]) in item]
                    rh.append(true_hand)
                    
                sh = sorted(rh, reverse=True)
                ranks = '%02d%02d%02d%02d%02d' % (tuple([x[0] for x in sh]))
                ranks = float(f'0.{ranks}')
                return True, rh, ranks
            return False, [], []
        
        else:
            return False, [], []

    def is_num_of_a_kind(self, num):
        kind_counter = self.most_frequent(self.get_number(self.hand))
        rh = list(item for item in self.tuple_hand if (kind_counter[0]) in item)[:5]
        
        r_nums = [item for item in self.tuple_hand if (rh[0][0]) not in item]
        h_num = sorted((r_nums), reverse=True)[:(5 - len(rh))]
        rh = rh + h_num
        
        if kind_counter[1] == num:
            ranks = '%02d%02d%02d%02d%02d' % (tuple([x[0] for x in rh]))
            ranks = float(f'0.{ranks}')
            return True, rh, ranks
        else:
            return False, [], []

    def is_house(self):
        values = self.get_number(self.hand)
        three_of_a_kind = self.most_frequent(values)
        pair = self.second_most_frequent(values)

        if three_of_a_kind[1] == 3 and pair[1] == 2:
            rh = [item for item in self.tuple_hand if (three_of_a_kind[0]) in item] + \
                 [item for item in self.tuple_hand if (pair[0]) in item]
            ranks = '%02d%02d%02d%02d%02d' % (tuple([x[0] for x in rh]))
            ranks = float(f'0.{ranks}')
            return True, rh, ranks
        return False, [], []

    def is_two_pair(self):
        self.tuple_hand = sorted(self.tuple_hand, reverse=True)
        values = self.get_number(self.hand)
        pair1 = self.most_frequent(values)
        pair2 = self.second_most_frequent(values)

        if pair1[1] == 2 and pair2[1] == 2:
            rh = list(item for item in self.tuple_hand if (pair1[0]) in item or (pair2[0]) in item)[:5]
            r_nums = [item for item in self.tuple_hand if (rh[0][0]) not in item and (rh[2][0]) not in item]
            h_num = sorted((r_nums), reverse=True)[:1]  
            rh = rh + h_num
            ranks = '%02d%02d%02d%02d%02d' % (tuple([x[0] for x in rh]))
            ranks = float(f'0.{ranks}')
  #          ranks = float('0.%s' % ranks)
            return True, rh, ranks
        return False, [], []

    def is_pair(self):
        pair = self.most_frequent(self.get_number(self.hand))
        if pair[1] == 2:
            r_nums = [item for item in self.tuple_hand if (pair[0]) not in item]
            h_num = sorted((r_nums), reverse=True)[:3]
            rh = list(item for item in self.tuple_hand if (pair[0]) in item)[:5]
            rh = rh + h_num
            ranks = '%02d%02d%02d%02d%02d' % (tuple([x[0] for x in rh]))
            ranks = float(f'0.{ranks}')
            return True, rh, ranks
        return False, [], []

    def is_high(self):

        r = list(item for item in self.tuple_hand)
        rh = sorted((r), reverse=True)[:5]
        ranks = '%02d%02d%02d%02d%02d' % (tuple([x[0] for x in rh]))
        ranks = float(f'0.{ranks}')       
        return True, rh, ranks

        
    def evaluate_hand(self):

        e_straight = [11, 12, 13, 14, 15]
        r_straight = [10, 11, 12, 13, 14]
        b_straight = [2, 3, 4, 5, 14]

        is_straight_flush_Z, straight_flush_Z, r = self.is_straight_flush_Z()
        if is_straight_flush_Z:
            if (list(x[0] for x in straight_flush_Z)) == e_straight:
                return "EMPEROR STRAIGHT FLUSH", straight_flush_Z, 16          
            if (list(x[0] for x in straight_flush_Z)) == r_straight or sum(map(lambda x: x in (list(x[0] for x in straight_flush_Z)), r_straight)) == 4:
                return "ROYAL STRAIGHT FLUSH", straight_flush_Z, 15
            if (list(x[0] for x in straight_flush_Z)) == b_straight or sum(map(lambda x: x in (list(x[0] for x in straight_flush_Z)), b_straight)) == 4:
                return "BACK STRAIGHT FLUSH", straight_flush_Z, 14
            else:
                return "STRAIGHT FLUSH", straight_flush_Z, r+12          

        is_4_kind_Z, four_of_a_kind_Z, r = self.is_4_kind_Z()
        if is_4_kind_Z:
            return "FIVE OF A KIND", four_of_a_kind_Z, r+13

        is_flush_Z, flush_hand, r = self.is_flush_Z()
        if is_flush_Z:
            return "FLUSH", flush_hand, r+11
        
        is_3_kind_Z, three_kind_Z, r = self.is_3_kind_Z()
        if is_3_kind_Z:
            return "FOUR OF A KIND", three_kind_Z, r+9
        
        is_two_pair_Z, two_pair_Z, r = self.is_two_pair_Z()
        if is_two_pair_Z:
            most_repeats = self.most_frequent([x[1] for x in two_pair_Z])[1]
            if most_repeats == 1:
                return "FULL HOUSE", two_pair_Z, r+10
            else:
                return "HOUSE", two_pair_Z, r+8
            
        is_straight_Z, straight_Z, r = self.is_straight_Z()
        if is_straight_Z:
            if (list(x[0] for x in  straight_Z)) == r_straight or sum(map(lambda x: x in (list(x[0] for x in  straight_Z)), r_straight)) == 4:
                return "ROYAL STRAIGHT", straight_Z, r+7
            if (list(x[0] for x in  straight_Z)) == b_straight or sum(map(lambda x: x in (list(x[0] for x in  straight_Z)), b_straight)) == 4:
                return "BACK STRAIGHT", straight_Z, 6
            else:
                return "STRAIGHT", straight_Z, r+5
            
        is_pair_Z, pair_Z, r = self.is_pair_Z()
        if is_pair_Z:
            return "THREE OF A KIND", pair_Z, r+4

        is_high_Z, high_Z, r = self.is_high_Z()
        if is_high_Z:
            return "ONE PAIR", high_Z, r+2

        is_straight_flush, straight_flush, r = self.is_straight_flush()
        if is_straight_flush:          
            if (list(x[0] for x in straight_flush)) == r_straight:
                return "ROYAL STRAIGHT FLUSH", straight_flush, 15
            if (list(x[0] for x in straight_flush)) == b_straight:
                return "BACK STRAIGHT FLUSH", straight_flush, 14
            else:
                return "STRAIGHT FLUSH", straight_flush, r+12
            
        is_five_of_a_kind, five_of_a_kind, r = self.is_num_of_a_kind(5)
        if is_five_of_a_kind:
            return "FIVE OF A KIND", five_of_a_kind, r+13

        is_flush, flush_hand, r = self.is_flush()
        if is_flush:
            return "FLUSH", flush_hand, r+11
        
        is_four_of_a_kind, four_of_a_kind, r = self.is_num_of_a_kind(4)
        if is_four_of_a_kind:
            return "FOUR OF A KIND", four_of_a_kind, r+9
        
        is_house, house_hand, r = self.is_house() 
        if is_house:
            most_repeats = self.most_frequent([x[1] for x in house_hand])[1]
            if most_repeats == 1:
                return "FULL HOUSE", house_hand, r+10
            else:
                return "HOUSE", house_hand, r+8
        
        is_straight, straight_hand, r = self.is_straight()
        if is_straight:
            if (list(x[0] for x in  straight_hand)) == r_straight:
                return "ROYAL STRAIGHT", straight_hand, r+7
            if (list(x[0] for x in  straight_hand)) == b_straight:
                return "BACK STRAIGHT", straight_hand, r+6
            else:
                return "STRAIGHT", straight_hand, r+5           

        is_three_of_a_kind, three_of_a_kind, r = self.is_num_of_a_kind(3)
        if is_three_of_a_kind:
            return "THREE OF A KIND", three_of_a_kind, r+4
        
        is_two_pair, two_pair, r = self.is_two_pair()
        if is_two_pair:
            return "TWO PAIR", two_pair, r+3 

        is_pair, pair, r = self.is_pair()
        if is_pair:
            return "ONE PAIR", pair, r+2

        else:
            _, high, r = self.is_high()
            return "HIGH CARD", high, r+1
