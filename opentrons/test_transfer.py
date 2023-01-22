from opentrons import protocol_api

metadata={'apiLevel': '2.0'}

def run(protocol: protocol_api.ProtocolContext):
    tips = protocol.load_labware('opentrons_96_tiprack_1000ul', 1)
    flask = protocol.load_labware('agilent_1_reservoir_290ml', 4)
    waste = protocol.load_labware('agilent_1_reservoir_290ml', 2)
    fresh = protocol.load_labware('agilent_1_reservoir_290ml', 5)

    p1000 = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tips])

    p1000.transfer(1000, flask.wells()[0], waste.wells()[0], new_tip='always')
    p1000.transfer(1000, flask.wells()[0], fresh.wells()[0], new_tip='always')
    