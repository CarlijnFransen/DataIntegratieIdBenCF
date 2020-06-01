"""

"""
import pymongo
import vcf


def main():
    read_vcf()
    posts = create_db_connection()


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


def add_document():
    # adds document as json/dictionary style format to the MongoDB database
    pass


def create_db():
    pass


main()
