import time
import random
import asyncio
import pyperclip
from func import css_click_center,xpath_click_center,click_checkboxes,css_scroll_center,xpath_scroll_center







async def Facebook_MarketPlace_Bot(page,df):
    await page.bringToFront()
    await xpath_click_center(page, '//span[contains(text(), "Sell Something")]')
    await asyncio.sleep(2)
    await xpath_click_center(page, '//span[contains(text(), "Item for sale")]')
    await asyncio.sleep(2)

    img = [eval(x) for x in df['PRODUCT_PIC_URLS']][0]
    # Step 1: Find all image-type file inputs
    file_inputs = await page.querySelectorAll('input[type="file"][accept*="image"]')
    if not file_inputs:
        print("❌ No image file inputs found!")
    else:
        print(f"ℹ️ Found {len(file_inputs)} image file inputs. Filtering...")

        # Step 2: Choose the input with multiple upload enabled
        target_input = None
        for i, input_elem in enumerate(file_inputs):
            accept_attr = await page.evaluate('(el) => el.getAttribute("accept")', input_elem)
            multiple_attr = await page.evaluate('(el) => el.hasAttribute("multiple")', input_elem)
            if "image" in accept_attr and multiple_attr:
                target_input = input_elem
                print(f"✅ Picked file input #{i} (multiple upload enabled)")
                break

        # Step 3: Fallback if no multiple input found
        if not target_input:
            target_input = file_inputs[-1]
            print("ℹ️ No multiple-input found. Using last available input.")

        # Step 4: Make it visible
        await page.evaluate('el => el.style.display = "block"', target_input)

        # Step 5: Upload the file
        await target_input.uploadFile(*img)
        print("✅ File uploaded to input successfully")

        # Step 7: Disable the input after upload to stop re-triggers
        await page.evaluate('''el => {
            el.disabled = true;
            el.style.display = "none";
        }''', target_input)
        print("🧩 Input disabled to prevent multiple uploads")

    await asyncio.sleep(2)

    title_input = await page.waitForXPath('//span[text()="Title"]/following-sibling::input')
    await asyncio.sleep(2)
    title_input.click()
    await title_input.type(f"{df['NAME'][0].split(',')[0]}") #### ENTER NAME OF YOUR PRODUCT HERE (EXAMPLE : PS5 PRO)

    price_input = await page.waitForXPath('//span[contains(text(),"Price")]/following-sibling::input')
    await asyncio.sleep(2)
    price_input.click()
    await price_input.type(f"{df['PRODUCT_PRICE'][0]}")  #### ENTER PRICE OF YOUR PRODUCT HERE (EXAMPLE : 5000)
    await asyncio.sleep(2)

    await xpath_scroll_center(page,'//label[.//span[text()="Condition"]]')
    await xpath_click_center(page,'//label[.//span[text()="Condition"]]')
    await asyncio.sleep(2)
    await page.waitForFunction('''() => {
        return Array.from(document.querySelectorAll('div[role="option"]'))
            .some(e => e.innerText && e.innerText.trim() === "New");
    }''', {'timeout': 7000})

    await page.evaluate('''
    () => {
        const el = Array.from(document.querySelectorAll('div[role="option"]'))
            .find(e => e.innerText && e.innerText.trim() === "New");
        if (el) {
            el.scrollIntoView({ behavior: "smooth", block: "center" });
            el.click();
        }
    }
    ''')  ############ [ IF NOT NEW PRODUCT REPLACE ==='NEW' TO USED, FAILY NEW................ ETC]
    print("✅ Waited for and clicked on 'New'")


    await asyncio.sleep(2)
    more_details = await page.waitForXPath('//div[@role="button" and .//span[text()="More details"]]')
    expanded = await page.evaluate('(element) => element.getAttribute("aria-expanded")', more_details)
    if expanded == "false":
        await more_details.click()
        print("✅ Clicked to open the 'More details' section.")
    else:
        print("ℹ️ 'More details' section already open.")

    await xpath_click_center(page,'//label[.//span[text()="Description"]]//textarea')
    await asyncio.sleep(1)
    await xpath_click_center(page,'//label[.//span[text()="Description"]]//textarea')

 
    text_content = f"""

    ################ ENTER PRODUCT DESCRIPTIONS HERE ##########

    """
    pyperclip.copy(text_content)
    await asyncio.sleep(1)
    await xpath_click_center(page,'//label[.//span[text()="Description"]]//textarea')
    await page.keyboard.down('Control')
    await page.keyboard.press('V')
    await page.keyboard.up('Control')
    await asyncio.sleep(2)
    await css_scroll_center(page,'div[role="button"][aria-label="Next"]')
    await css_click_center(page, 'div[role="button"][aria-label="Next"]')
    await asyncio.sleep(2)
    await css_scroll_center(page,'div[role="button"]')
    marketplace_btn = await page.evaluateHandle('''() => {
        const btn = Array.from(document.querySelectorAll('div[role="button"]'))
            .find(el => el.innerText && el.innerText.trim().includes("Marketplace"));
        return btn || null;
    }''')
    await asyncio.sleep(1)
    if marketplace_btn:
        # Scroll it smoothly to the center of the viewport
        await page.evaluate('el => el.scrollIntoView({ behavior: "smooth", block: "center" })', marketplace_btn)
        await marketplace_btn.click()
        print("✅ 'Marketplace' button clicked successfully!")
    else:
        print("❌ 'Marketplace' button not found on this page.")

    await asyncio.sleep(2)
    await click_checkboxes(page, max_clicks=20, delay=0.5)

    await css_click_center(page, 'div[role="button"][aria-label="Post"]')


    await asyncio.sleep(3)
