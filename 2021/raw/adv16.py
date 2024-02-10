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

running_sum = 0

def consumepacket(pos):
  global running_sum
  version, pos = consumeint(pos, 3)
  running_sum += version
  typeid, pos = consumeint(pos, 3)
  if typeid == 4:
    literal, pos = consumeliteral(pos)
    return [literal], pos
  else:
    length_id, pos = consumeint(pos, 1)
    if length_id:
      subpackets, pos = consumeint(pos, 11)
      packets = []
      for i in range(subpackets):
        packet, pos = consumepacket(pos)
        packets.append(packet)
      return packets, pos
    else:
      length, pos = consumeint(pos, 15)
      packets = []
      start = pos
      while pos < start + length - 6:
        packet, pos = consumepacket(pos)
        packets.append(packet)
      return packets, pos 

while pos < len(raw) - 6:
  packet, pos = consumepacket(pos)
  print(packet)
  if all(c == "0" for c in raw[pos:]):
    break
print(running_sum)
