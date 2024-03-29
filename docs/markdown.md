# Markdown language

Markdown is the most commonly used language for documenting repositories. This readme.md is also written in Markdown. GitHub automatically generates a preview of the readme.md file from the currently selected folder. Embedded readme files are allowed.

We have collected the most common basic elements of this language.

## Common elements

| Markdown syntax  | Rendered result |
| ----------- | ----------- |
| Simple line | Simple line |
| Line #1\<br><br>Line #2 | Line #1<br>Line #2 |
| Line #1(double space)<br>Line #2 | Line #1<br>Line #2 |
| \# Heading 1 | <h1>Heading 1</h1> |
| \#\# Heading 2 | <h2>Heading 2</h2> |
| \#\#\#\#\#\# Heading 6 | <h6>Heading 6</h6> |
| \*\*bold option #1\*\* | **bold option #1** |
| \_\_bold option #2\_\_ | __bold option #2__ |
| \*itallic option #1\* | *italic option #1* |
| \_italic option #2\_ | _italic option #2_ |
| \\\*\\\*bold\\\*\\\* | \*\*bold\*\* |
| Items:<br>- Item #1<br>- Item #2 | Items <ul><li>Item #1</li><li>Item #2</li></ul>|
| HTML items <br>\<ul><br>\<li>Item #1\</li><br>\<li>Item #2\</li><br>\</ul> | HTML items <ul><li>Item #1</li><li>Item #2</li></ul>|
| \<hr /> | Page #1 <hr /> Page #2|
| \[link](https://legokor.hu/) | [link](https://legokor.hu/) |
| \!\[image_name](images/logo-small.jpg) | ![image_name](images/logo-small.jpg) |
| \<img src="images/logo.jpg" width="100"> | <img src="images/logo.jpg" width="100"> |
| \[link](legokor.hu) | [link](legokor.hu) |
| Inline \`code\` sample | Inline `code` sample |
| \`\`\`python <br>print()<br>\`\`\` | ```print() ``` |
| \`\`\`sh <br>ls<br>\`\`\` | `ls` |


## Others
Others which were hard to show in a table:

-   `Source`  
    \> Block quote  
    `Result`
    > Block quote

-   Code blocks  
    `Source`     
    \`\`\`python  
    print()  
    \`\`\`  
    `Result`
    ```python
    print()
    ```

-   Code blocks in another language  
    `Source`    
    \`\`\`sh  
    ls  
    \`\`\`  
    `Result`
    ```sh
    ls
    ```
-   Horizontal rules  
    `Source`  
    \-\-\-  
    `Result`  
--- 

Check out this more extensive [Syntax guide](https://www.markdownguide.org/basic-syntax/)!
