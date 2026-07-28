# `mk/ai.mk`
## creates project files dump for AI

```sh
cp -r ~/E/doc ./
find doc -type f -regex '.+\.md$' -exec cat {} > tmp/{APP}.ai.md \;
```

```Makefile
.PHONY: ai tmp/$(APP).ai.md
ai: tmp/$(APP).ai.md
tmp/$(APP).ai.md:
	find doc -type f -regex '.+\.md$$' -exec cat {} > $@ \;
	cat doc/ai.md >> $@
```
