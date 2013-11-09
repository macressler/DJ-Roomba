from collections import namedtuple

ROBOT = namedtuple('Robot', 'drive speed')

def noop(state, _):
    return ('foo',), state

def drive_straight(state, val):
    state = ROBOT('straight', -val*300)
    return ('drive_straight', state.speed), state

def turn(state, val):
    state = ROBOT('turn', -val*300)
    return ('drive', state.speed, 0), state

def control(state, val):
    if val == 0:
        return noop(state, val)
    return ('control',), ROBOT(0, 0)
