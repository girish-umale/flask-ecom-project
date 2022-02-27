from flask import Flask, render_template, request
from product_info import Product

app = Flask(__name__)
prod_list = []


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/product/save', methods=['POST', 'GET'])
def save_update_product():
    message = ""
    if request.method == 'POST':
        formdata = request.form                 # method type post
        pid = int(formdata.get('prid'))
        isDuplicate = False
        for prod in prod_list:
            if prod.productId == pid:
                prod.productName = formdata.get('prnm')
                prod.productQuantity = int(formdata.get('prqty'))
                prod.productVendor = formdata.get('prven')
                prod.productPrice = float(formdata.get('prprice'))

                isDuplicate = True
                break
        if isDuplicate:
            message = "Product Successfully Updated.."
        else:

            product = Product(pid=formdata.get('prid'), pnm=formdata.get('prnm'), pqty=formdata.get('prqty'),
                              pven=formdata.get('prven'), ppric=formdata.get('prprice'))
            prod_list.append(product)
            message = "Product Successfully Added..!"

    return render_template('add_product.html', result=message, product=Product())


@app.route('/product/delete/<int:pid>', methods=['GET'])
def delete_product(pid):
    for prod in prod_list:
        if prod.productId == pid:
            prod_list.remove(prod)
            break
    return render_template('list_products.html', prodList=prod_list)


@app.route('/product/edit/<int:pid>', methods=['GET'])
def edit_product(pid):
    product = None
    for prod in prod_list:
        if prod.productId == pid:
            product = prod
    return render_template('add_product.html', product=product)


@app.route('/product/list')
def get_all_product():
    return render_template('list_products.html', prodList=prod_list)


@app.route('/product/search', methods=['GET', 'POST'])
def search_product():
    if request.method == "POST":
        formdata = request.form
        pid = int(formdata.get('prid'))
        for prod in prod_list:
            if prod.productId == pid:
                return render_template('search_product.html', prod=prod)
    return render_template('search_product.html', product=None)


if __name__ == '__main__':
    app.run(debug=True)
