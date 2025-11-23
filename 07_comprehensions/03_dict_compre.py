tea_prices_inr = {
    "Masala Chai": 120,
    "Elaichi Chai": 150,
    "Spicy Chai": 200
}

tea_prices_usd = {tea:price/80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)
