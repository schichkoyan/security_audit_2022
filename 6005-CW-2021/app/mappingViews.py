"""
Views for the mapping task
"""

import flask
import logging

from .meta import app


from .models import *



@app.route("/products", methods=["GET","POST"])
def products():
    """
    Single Page Application for Products
    """
    theItem = flask.request.args.get("item")
    if theItem:
        #We Do A Query for It
        itemQry = Item.query.filter_by(id=theItem).first()
        reviewQry = Review.query.filter_by(itemId=theItem)
        if itemQry is None:
            flask.abort(404, "No Such Item")

        #Add to Cart
        if flask.request.method == "POST":

            quantity = flask.request.form.get("quantity")
            try:
                quantity = int(quantity)
            except ValueError:
                flask.flash("Error Buying Item")
                return flask.render_template("showItem.html",
                                             item = itemQry,
                                             reviews=reviewQry)
            
            logging.warning("Buy Clicked %s items", quantity)
            #And we add something to the Session for the user to keep track
            basket = flask.session.get("basket", {})

            basket[theItem] = quantity
            flask.session["basket"] = basket
            flask.flash("Item Added to Cart")

            
        return flask.render_template("showItem.html",
                                     item = itemQry,
                                     reviews=reviewQry)
    else:
        #flask.abort(404, "No Args Specified")
        #return "No such product"

        books = Item.query.filter_by(category="book")
        books.filter_by(hidden=False)
        
        return flask.render_template("allItems.html",
                                     books = books)
    
    
