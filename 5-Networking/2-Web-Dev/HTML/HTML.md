

# `Hypertext Markup Language`

[`mdn web docs_ HTML`](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)

<br>

___

<br>

Covered in this file:

1. [`HTML Defined`](#html-defined)
1. [`Comments`](#comments)
1. [`Elements`](#elements)
1. [`Tags`](#tags)
1. [`Attributes`](#attributes)
1. [`Organizing HTML`](#organizing-html)




<br>

___

[`Back To Top`](#hypertext-markup-language)

<br>

# `HTML Defined`
`HTML (Hypertext Markup Language)` is the standard language for creating and structuring web documents. It uses a system of tags and attributes to define the elements on a webpage, including headings, paragraphs, links, and more. HTML provides the basic structure for content on the World Wide Web and is essential for creating web pages. 

<br>

___

[`Back To Top`](#hypertext-markup-language)

<br>

# `Comments`
A `comment` in HTML is a way to add annotations or notes within the code. Comments are not displayed in the browser and are ignored during the rendering of the webpage. They serve as helpful explanations for developers and are crucial for code documentation. 

```html
<!--This is a single line HTML Comment -->
```

```html
<!--
This 
is 
a 
multi-line 
HTML 
Comment 
-->
```

<br>

___

[`Back To Top`](#hypertext-markup-language)

<br>

# `Elements`
`Elements` in HTML define the structure and content of a web page. They include tags like `<html>`, `<head>`, `<body>`, `<h1>,` `<p>`, etc., each serving a specific purpose in organizing and presenting information. 

HTML Elements are made of 3 parts:

* `Opening Tag`: This is the start of the element and is enclosed in angle brackets (`< >`). 
    * For example, `<p>` starts a paragraph.

* `Content`: This is the information or content that appears between the opening and closing tags. 
    * For example, in `<p>`Hello, world!`</p>`, the text "Hello, world!" is the content.

* `Closing Tag`: This marks the end of the element and is similar to the opening tag but with a forward slash before the element name (e.g., `</p>`).

<br>

syntax:
```html
<tag> content </tag>
```
OR
```html
<tag>

    content

</tag>
```




<br>

___

[`Back To Top`](#hypertext-markup-language)

<br>

# `Tags`
A `tag` in HTML is a fundamental building block that defines an element. 
It consists of an opening tag, content, and a closing tag. Tags are used 
to structure and format the content on a webpage, providing a standardized 
way to create and display various elements such as headings, paragraphs, 
links, etc. 

<br>

`Opening Tag`: This is the start of the element and is enclosed in angle brackets (`< >`). 
```html
<tag>
```

<br>


`Closing Tag`: This marks the end of the element and is similar to the opening tag but with a forward slash `/` before the element name.
```html
</tag>
```

<br>

___

[`Back To Top`](#hypertext-markup-language)

<br>

# `Attributes`
`Attributes` in HTML provide additional information or behavior to elements. 

* For example, the 'lang' attribute in the `<html>` tag specifies the language 
of the document, aiding in language-specific processing or styling. Attributes 
can be found in various HTML tags, enhancing the functionality and presentation 
of the content. 

syntax:
```html
<tag attribute = "value"> content </tag>
```

<br>

___

[`Back To Top`](#hypertext-markup-language)

<br>

# `Organizing HTML`
When you're writing HTML code, it's a good idea to organize it neatly. You can do this by adding spaces or tabs at the beginning of each line to create a consistent structure. For every child element (like a paragraph or heading) inside a parent element (like a section or body), you should indent them to show their relationship. 

This helps make your HTML code more readable and easier to understand. 


```html
<!DOCTYPE html> 
<html lang="en-us"> 

    <head>
        <title>Page Title</title> 
    </head> 
    <body> 

        <h1>This is a heading</h1> 

        <p>This is a paragraph.</p> 
        
        <a href="https://www.w3schools.com">This is a link</a> 

        <img src="image.png" alt="alt text here"> 

        <div>
            
            <!-- div content -->

        </div>

    </body> 
    
</html> 



```
```html
<!-- This is an HTML comment, it allows developers to make notes inside of their HTML -->

<!DOCTYPE html> 
<!-- This declaration defines the document to be HTML5 -->

<html lang="en-us"> 
<!-- This is the opening tag for the HTML document, specifying the language as English (United States) -->
  
    <head>
    <!--This is the opening tag for the head of the HTML document-->
        
        <title>Page Title</title> 
        <!-- This is the title of the HTML document, displayed in the browser's title bar or tab -->
    
    </head> 
    <!--This is the closing tag for the head of the HTML document-->

    <body> 
    <!-- This is the opening tag for the body of the HTML document, where the content is placed -->

        <h1>This is a heading</h1> 
        <!-- This is a level 1 heading, used to define the main heading of the document -->
        

        <p>This is a paragraph.</p> 
        <!-- This is a paragraph tag, used to define a block of text as a paragraph -->
        

        <a href="https://www.w3schools.com">This is a link</a> 
        <!-- This is an anchor tag to define hyperlinks and create clickable text/images-->


        <img src="image.png" alt="alt text here"> 
        <!--This is the HTML image element. It is used to embed images into a webpage -->


        <div>
        <!--
            The HTML <div> element is a generic container or a division 
            that is used to group and structure content on a webpage. 
            The term "div" stands for "division.
        -->
        </div>

    </body> 
    <!-- This is the closing tag for the body of the HTML document -->
</html> 
<!-- This is the closing tag for the HTML document -->
```

<br>

___

[`Back To Top`](#hypertext-markup-language)

<br>