FROM python:3.6
WORKDIR /dataintegratie
ENV FILE_TO_DB vcf_tp_mongodb.py
RUN apk add --no-cache gcc musl-dev linux-headers
COPY ./requirements.txt ./install_and_deploy_mongodb.sh
ENV PATH " $PATH:/media/carlijnfransen/HD_CarlijnFransen/BIN-1920/gnomad.exomes.r2.1.1.sites.13.vcf"
RUN pip install -r requirements.txt
RUN sh install_and_deploy_mongodb.sh
EXPOSE 5000
CMD ["flask","run"]

