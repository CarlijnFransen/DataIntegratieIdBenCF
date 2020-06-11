from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/results")
def index():
    return render_template('results.html')


# @app.route('/request', methods=['GET'])
# def test():
#     chromosome = request.args.get('chrom')
#     print(chromosome)
#     position = request.args.get('pos')
#     print(position)
#     nucleotide = request.args.get('nt')
#     print(nucleotide)
#     return render_template('results.html', chrom_pos_1=chromosome, pos_pos_1=position, nucleo_pos_1=nucleotide)
#

if __name__ == "__main__":
    app.run()
