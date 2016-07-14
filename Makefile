install:
	python lang.py -i

install-extra:
	python lang.py -i -l ${Lang}

check:
	python lang.py -c

check-extra:
	python lang.py -c -l ${Lang}

clean:
	test -f ${Lang}.wordlist || exit 2;
	cat ${Lang}.wordlist | sort -u > ${Lang}.tmp ; mv ${Lang}.tmp ${Lang}.wordlist

