# check-stock

## Automatically check the stock status of products

For now, this only works for <a href="https://www.chapters.indigo.ca/en-ca/">chapters.indigo.ca</a>.

NOTE: You need python3 and all modules used in `app.py` and `check_stock.py` installed on your machine to be able to run this program.

### To run on Mac:

1. Open Finder and navigate to the location of this folder (`check-stock`).
2. Double-click the file `app.command`. This will launch your terminal.<br>
   (a) If this gives you an "unidentified developer" error, right-click the file, choose Open > Open.
3. Displayed in your terminal will be a line similar to the following:
    ```shell
    * Running on http://111.0.0.1:1000/ (Press CTRL+C to quit)
    ```
    Copy this http link into your browser of choice.
4. To quit the program, press <kbd>⌃ control</kbd> + <kbd>C</kbd> in your terminal, and close the browser window.

If you get a permission error at step 2, do the following then continue above with step 3:

1. Open Terminal (<kbd>⌘ command</kbd> + <kbd>space</kbd>, type in 'Terminal', press <kbd>enter</kbd>).
2. Navigate to the `check_stock` folder.
3. Run the following command:
    ```shell
    chmod 111 app.command
    ```
    
### Statuses

Available for shipping:

-   Free shipping on orders over $35

Not available for shipping:

-   On re-order online
-   Out of stock online

<br><br>

## To-do

1. Add option to change "nickname" of product
2. Make compatible with other online stores
3. Automatically run this program every set amount of time and send notification
