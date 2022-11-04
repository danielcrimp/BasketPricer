# BasketPricer :shopping_cart:
This is a simple tool for checking how much some groceries cost.

## Instructions to Run
to run this tool, pull the repo, open a terminal in the relevant directory and type:
    >"python3 PriceBasket.py {what you want to buy}"

What you want to buy should be a list of grocery items, separated by spaces. If you put in an unrecognised item, you'll be prompted with a selection of valid items.

## Commentary
This system has been designed with extensibility in mind.
- New store contexts can be developed with different catalogues and promotions
- Promotions can be added by initialising functions that take in store and basket info and return discount information
- Custom classes used sparingly to allow exposure to develop promotion logic 