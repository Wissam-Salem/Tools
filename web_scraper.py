from playwright.sync_api import sync_playwright
import json

result = []
with sync_playwright() as pr:
    for page_number in range(1, 5):
        browser = pr.chromium.launch(headless=True)

        page = browser.new_page()
        page.goto(f"https://ayoubcomputers.com/keyboard/?page={page_number}", timeout=20000)
        page.wait_for_selector(".productGrid", timeout=20000)

        products = page.query_selector_all(".product")
        for product in products:
            title = product.query_selector(".card-title").query_selector("a").inner_text()
            price = product.query_selector(".price--main").inner_text()
    
            if not any(word in title.lower() for word in ["wireless", "bluetooth"]) or not price or float(price.split("$")[1]) > 100:
                continue
            
            image = product.query_selector(".card-img-container").query_selector("img").get_attribute("src")
            brand = product.query_selector(".card-text--brand").inner_text()
            url = product.query_selector(".card-figure").query_selector("a").get_attribute("href")

            new_keyboard = {
                "image": image,
                "title": title,
                "brand": brand,
                "price": price,
                "url": url
            }

            result.append(new_keyboard)
    browser.close()

with open("wireless_keyboards.json", "r") as file:
    data = json.load(file)

data.extend(result)

with open("wireless_keyboards.json", "w") as file:
    json.dump(data, file, indent=4)
    
print(json.dumps(result, indent=4))