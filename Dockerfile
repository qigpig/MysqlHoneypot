FROM qzkc/python2.7:v2
COPY ./ /mysqlhoneypot/
WORKDIR /mysqlhoneypot
RUN pip install flask \
	&& pip install Flask-HTTPAuth
CMD ["python" , "main.py"]