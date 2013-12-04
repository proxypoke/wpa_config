.PHONY: man
man:
	a2x -f manpage -D man README.txt
	bzip2 -f man/wpa_config.8
