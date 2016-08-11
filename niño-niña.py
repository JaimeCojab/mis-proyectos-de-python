# -*- coding: utf-8 -*-
mama = input ("si mama quiere niña pulse 0,si mama quiere niño ponga 1,")
papa = input ("si papa quiere niña pulse 0,si papa quiere niño ponga 1,")
if mama == 1 and papa == 1:
    print "es niño"
if mama == 0 and papa == 1:
    print "es niña"
if mama == 1 and papa == 0:
    print "es niña"
if mama == 0 and papa == 0:
    print "es niño"
# Los if sirven para que la computadora sepa bajo que
# circunstancias poder seguir ordenes, los "or" sirven al revez
# que los "if".
