import math

hexdigits = input().strip()
raw = "".join(("0000" + bin(int(d, 16))[2:])[-4:] for d in hexdigits)
pos = 0

def consumeint(pos, bits):
  return int(raw[pos: pos + bits], 2), pos + bits

def consumebits(pos, bits):
  return raw[pos: pos + bits], pos + bits

def consumeliteral(pos):
  literal = 0
  while True:
    block, pos = consumebits(pos, 5)
    literal = literal * 16 + int(block[1:], 2)
    if block[0] == "0":
      break
  return literal, pos

def consumepacket(pos):
  version, pos = consumeint(pos, 3)
  typeid, pos = consumeint(pos, 3)
  if typeid == 4:
    literal, pos = consumeliteral(pos)
    return literal, pos
  else:
    length_id, pos = consumeint(pos, 1)
    packets = []
    if length_id:
      subpackets, pos = consumeint(pos, 11)
      for i in range(subpackets):
        packet, pos = consumepacket(pos)
        packets.append(packet)
    else:
      length, pos = consumeint(pos, 15)
      packets = []
      start = pos
      while pos < start + length - 6:
        packet, pos = consumepacket(pos)
        packets.append(packet)
    if typeid == 0:
      return sum(packets), pos
    elif typeid == 1:
      return math.prod(packets), pos
    elif typeid == 2:
      return min(packets), pos
    elif typeid == 3:
      return max(packets), pos
    elif typeid == 5:
      return 1 if packets[0] > packets[1] else 0, pos
    elif typeid == 6:
      return 1 if packets[0] < packets[1] else 0, pos
    elif typeid == 7:
      return 1 if packets[0] == packets[1] else 0, pos

while pos < len(raw) - 6:
  packet, pos = consumepacket(pos)
  print(packet)
  if all(c == "0" for c in raw[pos:]):
    break
