integresql-client-python
========================

[![integresql-client-python version](https://img.shields.io/pypi/v/integresql-client-python.svg)](https://pypi.python.org/pypi/integresql-client-python)
[![integresql-client-python license](https://img.shields.io/pypi/l/integresql-client-python.svg)](https://pypi.python.org/pypi/integresql-client-python)
[![integresql-client-python python compatibility](https://img.shields.io/pypi/pyversions/integresql-client-python.svg)](https://pypi.python.org/pypi/integresql-client-python)
[![Downloads](https://static.pepy.tech/personalized-badge/integresql-client-python?period=total&units=international_system&left_color=grey&right_color=yellow&left_text=Downloads)](https://pepy.tech/project/integresql-client-python)
[![say thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/marcin%40urzenia.net)

Python client for [IntegreSQL](https://github.com/allaboutapps/integresql).


Current stable version
----------------------

0.9.0

Python version
--------------

`integresql-client-python` is tested against Python 3.8+. Older Python versions may work, or may not.

How to use
----------

```python
from integresql_client_python import IntegreSQL

integresql = IntegreSQL('template_directory')

# integresql.debug = True

with integresql as tpl:
    with tpl.initialize() as dbinfo:
        # dbinfo is None if template is already initialized
        if dbinfo:
            # connect and import fixtures
            print("initialize db with fixtures with db data:", dbinfo)

    db = tpl.get_database()
    with db as dbinfo:
        # connect and do whatever you want
        print("Do your tests with db data:", dbinfo)

    # or manually, you can use as many databases as you need or IntegreSQL will allow
    dbinfo1 = db.open()
    print("Do your tests", dbinfo1)
    dbinfo2 = db.open()
    print("Do your tests", dbinfo2)
    dbinfo3 = db.open()
    print("Do your tests", dbinfo3)
    # connect and do whatever you want

    # do not forget about closing resources:
    db.close(dbinfo1)
    db.close(dbinfo2)
    db.close(dbinfo3)
```

Authors
-------

* Marcin Sztolcman ([marcin@urzenia.net](mailto:marcin@urzenia.net))

Contact
-------

If you like or dislike this software, please do not hesitate to tell me about
it via email ([marcin@urzenia.net](mailto:marcin@urzenia.net)).

If you find a bug or have an idea to enhance this tool, please use GitHub's
[issues](https://github.com/msztolcman/integresql-client-python/issues).

ChangeLog
---------

### v0.9.0

* first public version
