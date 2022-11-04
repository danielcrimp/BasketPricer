import sys
import operator as op
import locale


# by having our Store information as a class, we can separate the context (i.e. price info, store info) of the basket from the basket class
# we can also build multiple different store environments, and the basket class will still function.
# this design is built based on the assumption there may be a multi-store arrangement in future with different prices and promotions.

class Store:
    def __init__(self,catalogue,promotions):

        # initialise our catalogue from a dict input.
        # we could use a custom class here (which would allow for extending information available on items, say, item weight)
        # however, using a dict allows much more generic promotions functionality - and our basket can contain a simple list
        # this means any methods interacting with basket contents will not require bespoke 'unpacking' functionality to extract prices or names
        # this also allows us to centralise price information and simplifies promotions logic

        self.catalogue = catalogue

        #initialise our promotions from a list (of functions) input
        self.promotions = promotions
    
    def apply_promotions(self,basketcontents):
        discount = 0.0
        discountspiel = []
        for promo in self.promotions:
            a, b = 0.0, ''
            a, b =  promo(basketcontents,self.catalogue)
            if a:
                discount += a
            if b:
                discountspiel.append(b)
        return discount, discountspiel

    def get_price(self,itemstring):
        return self.catalogue[itemstring]
    

class Basket:
    def __init__(self,Store):
        self.contents = []
        self.Store = Store

    def add_item(self, itemstring):
        
        # Lacking further scenario information, tolerating incorrect input case should suffice 
        if itemstring.capitalize() in self.Store.catalogue:
            self.contents.append(itemstring.capitalize())
        else:
            print('Item not recognised: {}'.format(itemstring))
            print('Please choose items from the catalogue below...')
            for i in list(self.Store.catalogue.keys()):
                print(i)
            exit()

    def checkout(self):
        cost = 0        
        for item in self.contents:
            cost += self.Store.get_price(item)

        discount, discountspiel = self.Store.apply_promotions(self.contents)

        if not discountspiel:
            print('Subtotal: {} (No offers available)'.format(locale.currency(cost,grouping = True)))
            print('Total price: {}\n'.format(locale.currency(cost-discount,grouping = True)))
        else:
            print('Subtotal: {}'.format(locale.currency(cost,grouping = True)))
            for i in discountspiel: print(i)
            print('Total price: {}\n'.format(locale.currency(cost-discount,grouping = True)))
        

def main():

    # set locale for currency formatting
    locale.setlocale(locale.LC_ALL, '')

    # initialise store information - catalogue and current promotion logic.
    # assume we want to be able to modify both of these and have our basket operate as expected

    mycatalogue = {
        'Soup':0.65,
        'Bread':0.8,
        'Milk':1.3,
        'Apples':1
    }

    # initialise promotions. These are functions which take in a basket's contents and the local store's catalogue, and return a tuple containing the discount provided and contextual information
    # this arrangement is a result of a focus on extensibility - we could easily add logic - say, BOGO for milk bottles, and add that to the promo list
    # to make this generic or data driven, we would have to standardise logic arrangements on the input data i.e. have multiple discount formats

    def apple_promo(basketcontents,catalogue):

        subdiscount = catalogue.get('Apples')*0.1
        discount = 0

        for i in basketcontents:
            if i == 'Apples':
                discount += subdiscount

        if discount > 0:
            discountspiel = 'Apples 10% off: {}'.format(locale.currency(discount,grouping = True))
        else:
            discountspiel = ''

        return discount, discountspiel

    def bread_promo(basketcontents,catalogue):

        subdiscount = catalogue['Bread']*0.5

        discount = 0

        countbread = op.countOf(basketcontents,'Bread')

        countsoup = op.countOf(basketcontents,'Soup')

        discount = subdiscount*min(countbread, int(countsoup/2))

        if discount > 0:
            discountspiel = '50% off one loaf of bread for two tins of soup: {}'.format(locale.currency(discount,grouping = True))
        else:
            discountspiel = ''

        return discount, discountspiel

    mypromotions = [
        apple_promo,
        bread_promo,
    ]

    mystore = Store(mycatalogue,mypromotions)

    mybasket = Basket(mystore)

    for i in sys.argv[1:]:
        mybasket.add_item(i)

    mybasket.checkout()


if __name__ == '__main__':
    main()