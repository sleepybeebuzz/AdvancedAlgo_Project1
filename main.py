from ShippingTwoItems import taskA, longTaskA
from TheIslandProblem import largestMass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # items = [(1000.0, "Item A"), (1500.0, "Item B"), (2000.0, "Item C")]
    # longTaskA_Answer = longTaskA(items, 2500.00)
    # TaskA_Answer = taskA(items, 2500.00)
    # print(longTaskA_Answer)
    # print(TaskA_Answer)

    items0 = [(1000.0, "Item A"), (1500.0, "Item B"), (2000.0, "Item C"), (1200.0, "Gadget X"), (1300.0, "Widget Y"),
             (800.0, "Tool Z"), (1700.0, "Device M"), (900.0, "Appliance N"), (1600.0, "Gizmo P"),
             (750.0, "Contraption Q"), (1750.0, "Apparatus R"), (1100.0, "Instrument S"), (1400.0, "Mechanism T"),
             (825.0, "Doohickey U"), (1675.0, "Thingamajig V"), (550.0, "Whatchamacallit W"), (1950.0, "Doodad X"),
             (1250.0, "Gizmo Y"), (1150.0, "Widget Z"), (1350.0, "Gadget A")]

    items1 = [(980.0, "Widget AA"), (1520.0, "Gadget BB"), (1730.0, "Tool CC"), (1270.0, "Device DD"),
              (890.0, "Contraption EE"), (1610.0, "Apparatus FF"), (1140.0, "Instrument GG"), (1380.0, "Mechanism HH"),
              (1790.0, "Doohickey II"), (820.0, "Thingamajig JJ"), (1570.0, "Whatchamacallit KK"), (680.0, "Doodad LL"),
              (1930.0, "Gizmo MM"), (1090.0, "Widget NN"), (1410.0, "Gadget OO"), (630.0, "Tool PP"),
              (1870.0, "Device QQ"), (1320.0, "Contraption RR"), (1180.0, "Apparatus SS"), (710.0, "Instrument TT")]

    items2 = [(1050.0, "Gizmo A"), (1450.0, "Widget B"), (1800.0, "Gadget C"), (1250.0, "Tool D"), (950.0, "Device E"),
              (1650.0, "Contraption F"), (1150.0, "Apparatus G"), (1350.0, "Instrument H"), (1750.0, "Mechanism I"),
              (850.0, "Doohickey J"), (1550.0, "Thingamajig K"), (700.0, "Whatchamacallit L"), (1900.0, "Doodad M"),
              (1100.0, "Gizmo N"), (1400.0, "Widget O"), (600.0, "Gadget P"), (2000.0, "Tool Q"), (1300.0, "Device R"),
              (1200.0, "Contraption S"), (500.0, "Apparatus T")]

    for i in range(3):
        print(taskA(locals()[f'items{i}'], 2500))

    SampleInput = [
        [0, 1, 1],
        [0, 0, 1],
        [1, 1, 0]
    ]

    sample2 = [[1, 0, 1, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 1, 1, 1, 1],
                [1, 0, 1, 0, 0]]

    print(largestMass(SampleInput))
    print(largestMass(sample2))


