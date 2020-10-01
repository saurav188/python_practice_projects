#. represents that the domino is standing still
#L represents that the domino is falling to the left side
# represents that the domino is falling to the right side


class Solution(object):
    def pushDominoes(self, dominoes):
        initial_position=dominoes
        next_position=''
        final_position=False
        while not final_position:
            for i in range(len(initial_position)):
                this_unit=initial_position[i]
                if i<len(initial_position)-1:
                    next_unit=initial_position[i+1]
                else:
                    next_unit=None
                if i>0:
                    prev_unit=initial_position[i-1]
                else:
                    prev_unit=None
                
                if this_unit=='.':
                    if next_unit=='L':
                        if prev_unit!='R':
                            next_position+='L'
                        else:
                            next_position+='.'
                    elif prev_unit=='R':
                        next_position+='R'
                    else:
                        next_position+='.'
                elif this_unit=='R':
                    if next_unit=='L':
                        next_position+='.'
                    else:
                        next_position+='R'
                elif this_unit=='L':
                    if prev_unit=='R':
                        next_position+='.'
                    else:
                        next_position+='L'
                        
            if next_position==initial_position:
                final_position=True
            initial_position=next_position
            next_position=''
        return initial_position

print(Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR

#..R...L..R.
#..RR.LL..RR each domino moved once
#..RR.LL..RR each domino moved once but didn't change so this is the output