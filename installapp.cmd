@echo on

call python test_wsgi.py install --server Kotodo
call iisreset