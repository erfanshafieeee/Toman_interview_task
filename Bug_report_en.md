## Hypothetical Bugs for Digikala Website

## Bug 1 — Payment Failed But Order is Marked as Completed 💳❌

**Page/Product:** Checkout / Payment Gateway
**Severity:** Critical 🔥
**Bug Type:** Functional
**Environment:** Web (Chrome 120 / Windows 10) — Production environment
**User Role:** Regular logged-in user

### Steps to Reproduce

1. Log into your account and add 1 item to the cart.
2. Go to the checkout page.
3. Enter valid bank card details.
4. Click on the "Pay" button.
5. After displaying the "Payment Failed" message, the user is redirected to the "Order Details" page, and the order is saved with the "Completed" status.

### Expected Result

If there’s an error in the transaction, the order should not be saved as "Completed." The user should receive a clear error message (e.g., "Payment failed, please try again") and the order should remain in an uncertain or canceled state.

### Actual Result

The system displays the "Payment Failed" message, but the order is still saved with the "Completed" status. The orders are later sent to logistics, and payment is not received from the user, causing account discrepancies.

### Possible Cause

The issue might be caused by improper handling of the payment gateway's `callback` response.

---

## Bug 2 — Price Filter in Category Page Works Incorrectly 💸🔧

**Page/Product:** Category Listing Page — Price Range Slider
**Severity:** Major ⚠️
**Bug Type:** UI/UX
**Environment:** Desktop (Firefox 119) — Production
**User Role:** Visitor (or logged-in user)

### Steps to Reproduce

1. Go to a category page (e.g., Home Appliances).
2. Select the price filter range from 500,000 to 1,000,000 Toman.
3. Click "Apply Filter" or let it apply automatically.
4. Check the displayed results.

### Expected Result

Only products priced between 500,000 to 1,000,000 Toman should be displayed.

### Actual Result

The results include products priced above 1,000,000 Toman or below 500,000 Toman, especially showing products with a price of 0 or incorrect price display.

### Possible Cause

This issue might be due to either the `frontend` sending incorrect queries or the `backend` not correctly handling the filter.

### Evidence/Logs

* Example of filtered URL (query string parameters).
* API output (payload) and filters sent to the backend.
* Screenshots before and after applying the filter.

---

## Bug 3 — Incorrect Similar Products Displayed on Product Details Page 📱🔄

**Page/Product:** Product Details Page — Similar Products Section
**Severity:** Major ⚠️
**Bug Type:** Functional
**Environment:** Mobile Web (Chrome Android 14) — Staging
**User Role:** Visitor or logged-in user

### Steps to Reproduce

1. Enter the details page of a product (e.g., an **IP camera**).
2. Scroll to the **Similar Products** section at the bottom of the page.
3. Check whether similar products are displayed correctly.

### Expected Result

The similar products should be relevant to the product being viewed. For example, if I’m on the product details page for an **IP camera**, only similar **IP cameras** should be displayed.

### Actual Result

If I’m on the product details page for an **IP camera**, unrelated products like **iPhones** are displayed as similar products, which is incorrect.

### Possible Cause

The issue is likely caused by the `backend` using the **Title** of the product to find similar products, rather than using the product's **Category**. This causes products with similar names to be mistakenly shown as similar products.

### Evidence/Logs

* Screenshot of the Similar Products section.
