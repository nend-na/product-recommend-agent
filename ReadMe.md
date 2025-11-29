PROD.AI – Product Recommendation Agent



\## 1. What this project is



PROD.AI is a small web app that helps people quickly find suitable products from a fixed list.  

You type a short message like “wireless earphones for gym” or “comfortable running shoes,” and the app shows three products that best match what you asked for.



The app runs in the browser using Streamlit and does not need any external APIs or databases.



-----------------------------------------------------------------------------------------------------------------------------------------



\## 2. What the agent does



\- Reads a short, natural‑language query from the user.

\- Looks for keywords such as \*\*watch\*\*, \*\*shoes\*\*, \*\*earphones\*\*, or \*\*laptop / work\*\*.

\- Decides which category the query belongs to (watch, shoes, earphones, or workspace items).

\- Searches a small, curated product list that lives in the code.

\- Picks three products that are the closest match and shows them as cards with:

&nbsp; - product name  

&nbsp; - short description  

&nbsp; - helpful tags (e.g. “Fitness”, “Work”, “Travel”).



------------------------------------------------------------------------------------------------------------------------------------------



\## 3. Features



\- Clean, minimal one‑screen interface with a search bar and a “Recommend” button.

\- Instant results because everything runs in memory and there are no heavy ML models.

\- Focused on a few everyday categories:

&nbsp; - Smartwatches / fitness bands  

&nbsp; - Running shoes  

&nbsp; - Earphones / headphones  

&nbsp; - Simple workspace accessories (laptop stand, keyboard, webcam, lamp, etc.)

\- Works on desktop and mobile via the Streamlit UI.



------------------------------------------------------------------------------------------------------------------------------------------



\## 4. Limitations



\- Uses a fixed, hard‑coded product catalog. It is \*\*not\*\* connected to a real e‑commerce store, live prices, or stock.

\- Uses simple keyword and rule‑based logic, not a trained recommendation model.

\- Does not store user history or learn from user behavior over time.

\- Handles common, straightforward product needs best; very complex or niche queries may not match well.



------------------------------------------------------------------------------------------------------------------------------------------



\## 5. Tech stack



\- \*\*Language:\*\* Python  

\- \*\*Web framework:\*\* Streamlit  

\- \*\*Hosting:\*\* Streamlit Community Cloud  

\- \*\*Logic:\*\* Simple keyword + category matching on an in‑memory list of products  

\- \*\*Main dependencies:\*\*  

&nbsp; - `streamlit`  

&nbsp; - `python-dotenv`



\_No external APIs or external ML services are used in this version.\_



------------------------------------------------------------------------------------------------------------------------------------------



\## 6. How to run the app locally



1\. \*\*Clone the repository\*\*

[git clone https://github.com/nend-na/product-recommend-agent.git](git clone https://github.com/nend-na/product-recommend-agent.git)



2\. \*\*(Optional) Create a virtual environment\*\*

python -m venv .venv



macOS / Linux

source .venv/bin/activate



Windows

.venv\\Scripts\\activate





3\. \*\*Install dependencies\*\*

pip install -r requirements.txt





4\. \*\*Start the app\*\*

streamlit run main.py





5\. Open the URL shown in the terminal (usually `http://localhost:8501`) in your browser.



------------------------------------------------------------------------------------------------------------------------------------------



\## 7. How to use it



1\. Type what you are looking for, for example:

\- “wireless earphones for office calls”

\- “running shoes for daily jogging”

\- “smartwatch for fitness tracking”

\- “laptop stand for work from home”

2\. Click \*\*Recommend\*\*.

3\. Scroll down to see three recommended products with descriptions and tags.

4\. Change your query and click \*\*Recommend\*\* again to explore different options.



------------------------------------------------------------------------------------------------------------------------------------------



\## 8. Possible future improvements



\- Connect to a real product API or database to use live products, prices and stock.

\- Replace keyword rules with a semantic search or embedding model for smarter matching.

\- Add user accounts and history so recommendations can become more personal over time.

\- Add filters for price range, brand, style, and other preferences.

\- Expand to many more product categories beyond the current few.



------------------------------------------------------------------------------------------------------------------------------------------



\## 9. Links



\- \*\*Live demo:\*\* [https://appuct-recommend-agent-gjmnmfhapenpqvvuuyc4pu.streamlit.app](https://appuct-recommend-agent-gjmnmfhapenpqvvuuyc4pu.streamlit.app/)-

&nbsp;\*\*GitHub repo:\*\* `[https://github.com/nend-na/product-recommend-agent`](https://github.com/nend-na/product-recommend-agent`)







