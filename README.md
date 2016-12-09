# bots-charsets
This repository contains some variations of edifact charsets. In a regular installation good default charactersets are installed in usersys/charsets. These defaults are the same as the unoa_regular and unob_regular.

If you want to use charactersets as provided in this repository, copy the files you want to use to usersys/charsets, and rename to eg unoa.py
* unoa_regular - edifact standard, plus some extra characters that are often used in real-world.
* unob_regular - edifact standard, plus some extra characters that are often used in real-world.
* unoa_strict - edifact standard
* unob_strict - edifact standard
* unoa_like_unoc - UNOA is handled as if it is UNOC; so eg é and ö are OK
* unob_like_unoc - UNOA is handled as if it is UNOC; so eg é and ö are OK

`unoa_like_unoc.py` has all 256 values for characters. This might be easy as a starting point for extended character conversion.
