# BasketPricer :shopping_cart:
This is a simple tool for checking how much some groceries cost.

## Instructions to Run
to run this tool, pull the repo, open a terminal in the relevant directory and type:
>"python3 PriceBasket.py {what you want to buy}"

What you want to buy should be a list of grocery items, separated by spaces. If you put in an unrecognised item, you'll be prompted with a selection of valid items.

## Commentary
This system has been designed with extensibility in mind.
- New 'store contexts' can be rapidly developed with different catalogues and promotions
- Promotions can be easily added by initialising functions that process store and basket info and return discount information
- Custom classes used sparingly to ease developing promotions logic - no unpacking required.

## Future Improvements
This code was written fairly quickly and tailored to a brief. Therefore, there would be some improvements I might make if given more time.
- Testing. While the current code is quite robust to most user inputs by ignoring all but almost identical strings, more unit tests and assertions could be included. Potential catches include:
    - Detecting poor pricing information. If the code was edited such that prices were negative, huge or infinitesimal - or even the wrong dtype this would pass through to the output
    - Detecting poor discount information (negatives)
- Bespoke classes for grocery items. Currently grocery item information is kept as a standard dict for simplicity. However, additional functionality (such as processing item weights, nutritional information, et cetera) will require refactoring. An ORM could be used here as grocery item information is likely to be kept in a large database.
- Formatting. It's pretty readable in my opinion, but this can almost always be improved.
- Currency formatting. Strictly speaking, according to the given brief, we should be formatting currencies less than a pound, as 10p rather than £0.10. I used Locale to format currency, which takes a lot of the fiddly work out. If the pence formatting were absolutely necessary, I could switch to a more obscure library or develop my own string formatting methods. However, for this application, I think the simplicity afforded by the Locale library is a bigger win than the currency formatting being slightly neater.