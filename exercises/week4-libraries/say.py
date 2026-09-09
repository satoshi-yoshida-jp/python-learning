import cowsay
import sys
# import from saying.py
from saying import hello

# use cowsay
# if len(sys.argv) == 2:
#     cowsay.trex("hello, " + sys.argv[1])


# use hello from saying.py
if len(sys.argv) == 2:
    hello(sys.argv[1])