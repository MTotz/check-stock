# check-stock

## Automatically check the stock status of products

For now this only works for <a href="https://www.chapters.indigo.ca/en-ca/">chapters.indigo.ca</a> because of the HTML of the website.

It will check all the links in the file 'links.txt' contained in this folder. To add/edit/remove a link, simply add/edit/remove the corresponding link in the text file.

### To run on Mac:

1. Open Finder and navigate to the location of this folder (`check-stock`).
2. Double-click the file `check_stock.command`.

If you get a permission error at step 2, then do the following:

1. Open Terminal (<kbd>⌘ Command</kbd> + <kbd>Space</kbd>, type in 'Terminal', press <kbd>Enter</kbd>).
2. Navigate to the `check_stock` folder.
3. Run the following command:
    ```shell
    chmod 111 check-stock.command
    ```
    Double-clicking `check_stock.command` should no longer give the error.

### Statuses

Available for shipping:

-   Free shipping on orders over $35

Not available for shipping:

-   On re-order online
-   Out of stock online

<br><br>

## To-do

1. Use SQL to store website links
2. Add options to delete and add products
3. Add option to change "nickname" of product
4. Make compatible with other online stores
5. Open up pages of products that are available
6. Automatically run this program every set amount of time and send notification
