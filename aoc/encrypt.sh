mkdir -p encrypted_input
  for i in `seq -w 1 25` ; do
  echo $i
  gpg --symmetric --cipher-algo AES256 --batch --yes \
    --passphrase="$AOC_SECRET" --output encrypted_input/input.$i.txt.gpg input.$i.txt
  python3.13 adv$i-r.py < input.$i.txt > output.$i.txt
  gpg --symmetric --cipher-algo AES256 --batch --yes \
    --passphrase="$AOC_SECRET" --output encrypted_input/output.$i.txt.gpg output.$i.txt
done
