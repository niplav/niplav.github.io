include config.mk

.SUFFIXES: .dot .png

all: $(IMG)

puttit: $(IMG)
	mv $(IMG) ../../img/turning

.dot.png:
	dot -Tpng $< >$@

incomplete.png: incomplete.dot
	dot -Tpng $< >$@

intransitive.png: intransitive.dot
	circo -Tpng $< >$@

unbalanced_cycle.png: unbalanced_cycle.dot
	dot -Tpng $< >$@

clean:
	rm -f $(IMG)

.PHONY: puttit clean
