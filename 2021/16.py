import math
import operator
from functools import reduce
from aocd import submit, data, lines


def process_packet(packet):
    version = int(packet[:3],2)
    type_id = int(packet[3:6],2)
    packet = packet[6:]
    if type_id == 4:
        value = ""
        while packet[0] == "1":
            value += packet[1:5]
            packet = packet[5:]
        value += packet[1:5]
        packet = packet[5:]
        if packet.rstrip('0') == '':
            return version
        else:
            return version + process_packet(packet)
    else:
        length_id = int(packet[0])
        packet = packet[1:]
        if length_id == 0:
            length_bits = 15
        else:
            length_bits = 11
        length = int(packet[:length_bits], 2)
        packet = packet[length_bits:]
        packet = packet[:]
        return version + process_packet(packet)


def part_one(packet):
    packet = packet.split()[0]
    binary_packet = f"{int(packet, 16):0{len(packet*4)}b}"
    return process_packet(binary_packet)


type_to_operator = {
    0: operator.add,
    1: operator.mul,
    2: min,
    3: max,
    5: operator.gt,
    6: operator.lt,
    7: operator.eq
}


def process_packet2(packet):
    version = int(packet[:3],2)
    type_id = int(packet[3:6],2)
    packet = packet[6:]
    if type_id == 4:
        value = ""
        while packet[0] == "1":
            value += packet[1:5]
            packet = packet[5:]
        value += packet[1:5]
        packet = packet[5:]
        value = int(value, 2)
        return value, packet
    else:
        length_id = int(packet[0])
        packet = packet[1:]
        if length_id == 0:
            length_bits = 15
            length = int(packet[:length_bits], 2)
            sub_packets = None
        else:
            length_bits = 11
            length = None
            sub_packets = int(packet[:length_bits], 2)
        packet = packet[length_bits:]
        if sub_packets:
            operands = []
            for _ in range(sub_packets):
                operand, packet = process_packet2(packet)
                operands.append(operand)
        else:
            bits_processed = 0
            length_packet = len(packet)
            operands = []
            i = 0
            while bits_processed < length:
                operand, packet = process_packet2(packet)
                operands.append(operand)
                bits_processed += length_packet - len(packet)
                length_packet = len(packet)
                i += 1
        return reduce(type_to_operator[type_id], operands), packet


def part_two(packet):
    binary_packet = f"{int(packet, 16):0{len(packet*4)}b}"
    return int(process_packet2(binary_packet)[0])


if __name__ == '__main__':
    #print(part_one(data))
    #print(part_two("C200B40A82"))
    #print(part_two("04005AC33890"))
    #print(part_two("D8005AC2A8F0"))
    #print(part_two("F600BC2D8F"))
    #print(part_two("9C005AC2F8F0"))
    print(part_two("9C0141080250320F1802104A08"))
    print(part_two(data))
    #submit(part_two(data))
