"""

"""
import pymongo
import vcf


def main():
    con = create_db_connection()
    read_vcf(con)


def read_vcf(con):
    vcf_reader = vcf.Reader(open('D:/BIN-1920/gnomad.exomes.r2.1.1.sites.13.vcf'))
    for record in vcf_reader:
        chrom = record.CHROM
        pos = record.POS
        ref = record.REF
        alt = record.ALT
        try:
            non_cancer_af = record.INFO['non_cancer_AF'][0]
        except KeyError:
            pass
            #print (record.INFO)
        cancer_af = calculate_cancer_af(non_cancer_af)
        benign = filter_for_benign(cancer_af)
        if benign:
            document = create_document(chrom, pos, ref, alt, cancer_af)
            add_document(document, con)


def create_db_connection():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['cancer_api']
    col =  db['exome_data']
    return col

def read_vcf():
    # vcf_reader = vcf.Reader(open('D:\\BIN-1920\\gnomad.exomes.r2.1.1.sites.13.vcf'))
    vcf_reader = vcf.Reader(open('D:\\ZZhier\\gnomad.exomes.r2.1.1.sites.13.vcf'))
    for record in vcf_reader:
        for x in record.INFO:
            print(x)
            if x == 'non_cancer_AF':
                pass
        break


def create_db_connection():
    client = pymongo.MongoClient("localhost", 27017)
    db = client.cancer_api
    posts = db.posts
    return posts


def calculate_cancer_af(non_cancer_af):
    cancer_af = 1-non_cancer_af
    # calculates the cancer AF by doing a 1-non_cancer_AF
    return cancer_af


def filter_for_benign(cancer_af):
    # True =  Keep
    # False =  Discard
    if 0 < cancer_af < 0.01:
        return True
    else:
        return False
    # filters variants which have an cancer_AF>0.01


def create_document(chrom, pos, ref, alt, cancer_af):
    doc_dict = {}
    doc_dict["chromosome"] = chrom
    doc_dict["positon"] = pos
    doc_dict["ref"] = ref
    doc_dict["alt"] = alt
    doc_dict["cancer_af"] = cancer_af
    return doc_dict


def add_document(document, con):
    # adds document as json/dictionary style format to the MongoDB database
    con.insert_one(document)





main()
