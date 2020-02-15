from src.learn import MC, block

# rozruch
mc = MC(x=-1173, y=-3, z=325)
mc.say("Aktualizacja (wstaw swoje imie)")
mc.clean()

# zaczynamy budować
mc.put(0, 0, 0, block.GOLD_BLOCK)
mc.put(0, 1, 0)
mc.put(11, 0, 0) # to nie zadziała
