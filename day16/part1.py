# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

message = entries[0]
length = 4 * len(message)
message = bin(int(message, 16))[2:]
# add leading zeroes if necessary
while len(message) < length:
    message = '0' + message


def decode_packet(packet):
    i = 0
    version = int(packet[i:i + 3], 2)
    version_sum = version
    i += 3
    type_id = int(packet[i:i + 3], 2)
    i += 3
    if type_id == 4:
        literal = ""
        while True:
            # add the group to the literal value
            literal += packet[i + 1:i + 5]
            # check if we should keep reading
            if packet[i] == "0":
                i += 5
                break
            else:
                # move on to the next group
                i += 5
        literal = int(literal, 2)
    else:
        # operator packet
        length_type_id = int(packet[i], 2)
        i += 1
        if length_type_id == 0:
            total_length = int(packet[i:i + 15], 2)
            i += 15
            limit = i + total_length
            while i < limit:
                index, value = decode_packet(packet[i:])
                i += index
                version_sum += value
        elif length_type_id == 1:
            number_of_packets = int(packet[i:i + 11], 2)
            i += 11
            for x in range(number_of_packets):
                index, value = decode_packet(packet[i:])
                i += index
                version_sum += value
    return i, version_sum


print(decode_packet(message)[1])
